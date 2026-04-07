#!/usr/bin/env python3
"""
DG Pair Generator — Wiki Intelligence → Training Pairs
=======================================================
Reads every markdown doc in the DG wiki, generates Q&A training pairs
from the content. Each pair teaches the model specific DG trade knowledge.

Testnet mode: no tribunal verification. Generate and save.
Production: tribunal weighs every pair before cooking.

Usage:
    python3 scripts/generate_dg_pairs.py --count 3000 --dry-run
    python3 scripts/generate_dg_pairs.py --count 5000
    python3 scripts/generate_dg_pairs.py --count 100 --doc 07-market/lease-structures.md
"""
import argparse
import hashlib
import json
import os
import random
import sys
import time
import urllib.request
import uuid
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent
OUTPUT_DIR = WIKI_DIR / "pairs"
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11435")
MODEL = os.environ.get("DG_MODEL", "gemma3:12b")

# System prompts — diverse DG broker personas
PERSONAS = [
    "You are a senior net lease broker specializing exclusively in Dollar General STNL properties. You have closed 200+ DG transactions and know every lease structure, cap rate trend, and developer relationship in the market.",
    "You are a Dollar General investment analyst at a REIT that owns 400+ DG locations. You evaluate acquisitions, dispositions, and portfolio strategy for NNN Dollar General properties.",
    "You are a commercial mortgage broker who specializes in financing Dollar General NNN properties. You know every lender, every rate, every LTV structure for single-tenant retail.",
    "You are a 1031 exchange advisor helping clients sell existing real estate and acquire Dollar General NNN properties as replacement investments. You know the 45-day identification rules, the financing structures, and the DG-specific cap rate advantages.",
    "You are a CRE appraiser specializing in single-tenant net lease retail. You perform BOVs and appraisals on Dollar General properties across the Southeast, using recent comp data and lease analysis.",
    "You are a site selection consultant who advises Dollar General on new store locations. You know the demographic thresholds, traffic requirements, co-tenancy preferences, and rural fortress strategy.",
    "You are a build-to-suit developer who has built 100+ Dollar General stores. You know the preferred developer program, construction costs, sale-leaseback economics, and the relationship between developers and DG corporate.",
    "You are a net lease researcher at Boulder Group who publishes quarterly reports on Dollar General cap rate trends, transaction volume, and market positioning relative to other STNL tenants.",
    "You are a Florida commercial real estate broker who focuses on Dollar General properties in central and north Florida. You know the FL DOR tax roll system, Sunbiz entity resolution, and FL-specific cap rate premiums.",
    "You are a capital markets professional at a CMBS shop who underwrites Dollar General NNN loans. You know the DSCR requirements, LTV limits, and how lenders view investment-grade single-tenant retail.",
]

# Question templates organized by topic
QUESTION_TEMPLATES = {
    "lease_structures": [
        "What is the standard lease term for a new Dollar General store?",
        "Explain the rent bump schedule for a typical Dollar General NNN lease.",
        "How many renewal options does a standard DG lease include?",
        "What expenses does the tenant pay under a DG absolute NNN lease?",
        "What's the difference between a new DG lease (NNN) and an older DG lease (NN)?",
        "Is a Dollar General lease a franchise lease or a corporate guarantee?",
        "Walk me through the total rent over 45 years for a DG starting at $110K base rent.",
        "What red flags should I look for when reviewing a Dollar General lease?",
        "How does the DG lease structure compare to a Walgreens lease?",
        "What happens when a DG lease reaches the end of its primary term?",
    ],
    "cap_rates": [
        "What cap rate should I expect for a new construction Dollar General in 2025?",
        "How much tighter do Florida DG properties trade vs national average?",
        "What's the cap rate spread between a new DG and an existing DG with 5 years left?",
        "How do Dollar General cap rates compare to AutoZone and O'Reilly?",
        "Why are DG cap rates at 10-year highs right now?",
        "What cap rate would you price a central Florida DG with 8 years remaining?",
        "How has the DG cap rate changed from 2021 to 2025?",
        "What drives cap rate compression for Dollar General properties?",
        "Is now a good time to buy a Dollar General NNN property?",
        "What's the relationship between DG's credit rating and its cap rate?",
    ],
    "developers": [
        "Who are Dollar General's preferred developers?",
        "How many DG stores has CG Buchalter built?",
        "What states does Colby Capital operate in for DG development?",
        "Explain the build-to-suit economics for a Dollar General development.",
        "How does the developer sell after building a DG — who's the typical buyer?",
        "What's the typical developer margin on a DG build-to-suit?",
        "How can I find new DG construction before it hits the market?",
        "Who is the preferred DG developer in northern Florida?",
        "How long has CG Buchalter been a DG preferred developer?",
        "What's the annual pipeline of new Dollar General stores?",
    ],
    "buyers": [
        "What percentage of DG deal flow comes from 1031 exchange buyers?",
        "Describe the typical DST buyer for a Dollar General property.",
        "Which REITs own the most Dollar General properties?",
        "How many DG locations does Spirit Realty Capital own?",
        "What's the buyer profile for a $1.5M DG in a secondary market?",
        "Why do 1031 exchange buyers prefer Dollar General?",
        "What's the minimum investment for a DG syndication?",
        "How do HNW individual investors approach DG NNN acquisitions?",
        "What changed in the DG buyer pool from 2022 to 2025?",
        "Why is institutional capital returning to DG net lease in 2026?",
    ],
    "florida": [
        "Why is Florida the best state to target for DG acquisitions?",
        "How many Dollar General stores are in Florida?",
        "What's the FL DOR tax roll and how do I use it to find DG owners?",
        "Which Florida counties have the highest DG density?",
        "Why do FL DG properties trade 25-50 bps tighter than national?",
        "How does the 1031 exchange market impact FL DG pricing?",
        "What data fields does the FL DOR publish for property ownership?",
        "How do I match a DG store address to a parcel in the FL tax roll?",
        "Who are the major NNN brokerages active in Florida DG transactions?",
        "What's the Phase 1 plan for building a DG ownership graph in Florida?",
    ],
    "site_selection": [
        "What population threshold makes a Dollar General profitable?",
        "What percentage of DG stores are in towns under 20,000 population?",
        "What's DG's rural fortress strategy?",
        "What co-tenancy does Dollar General prefer near their stores?",
        "Why did Dollar General close 96 stores recently?",
        "What's the significance of a DG remodel for lease renewal probability?",
        "How does DG site selection differ from Dollar Tree?",
        "What traffic score does Florida have for DG stores?",
        "What are the physical site requirements for a new Dollar General?",
        "How does DG's cannibalization strategy work?",
    ],
    "formats": [
        "What are all the Dollar General store formats?",
        "What's the difference between a traditional DG and a DGX?",
        "Why did the pOpshelf shop-in-shop format fail?",
        "What is the DG Market format and where is it deployed?",
        "What's DG's international expansion with Mi Súper?",
        "Which DG format is most liquid as a net lease investment?",
        "How many remodels is DG planning for FY2025?",
        "What's the typical building size for each DG format?",
        "How does the format affect the cap rate and buyer pool?",
        "Is pOpshelf a good net lease investment?",
    ],
    "financing": [
        "What CMBS rate can I expect for a DG NNN property in 2026?",
        "What's the typical LTV for a Dollar General commercial mortgage?",
        "What DSCR do lenders require for a DG NNN loan?",
        "Which lenders are most active in DG net lease financing?",
        "What's the current spread between DG cap rates and mortgage rates?",
        "Is positive leverage available on Dollar General properties right now?",
        "How do lenders view DG's BBB credit rating for underwriting?",
        "What financing options does a 1031 exchange buyer have for a DG?",
        "What's the financing referral fee on a DG loan?",
        "Walk me through the DSCR calculation for a $1.57M DG at 75% LTV.",
    ],
    "competitors": [
        "How does Dollar General compare to Dollar Tree as a net lease investment?",
        "What's the cap rate difference between DG and AutoZone?",
        "Why does Tractor Supply trade at tighter caps than DG?",
        "What credit rating advantages do O'Reilly and AutoZone have over DG?",
        "How did DG's 2024 stock decline affect its position in the STNL market?",
        "What are DG's competitive strengths in the net lease market?",
        "What headwinds is DG facing compared to other STNL tenants?",
        "Is Dollar General more or less recession-resistant than AutoZone?",
        "What makes DG the preferred 1031 replacement over other dollar stores?",
        "How does DG's rural market positioning differentiate it from competitors?",
    ],
}

GENERATION_PROMPT = """You are generating a training pair for a Dollar General STNL specialist AI model.

SOURCE MATERIAL (from the DG Intelligence Wiki):
{context}

QUESTION: {question}

Generate a comprehensive, specific answer that a senior DG broker would give. Include:
- Specific numbers (cap rates, dollar amounts, percentages, lease terms)
- Named entities (Spirit Realty, CG Buchalter, Colby Capital, etc.)
- Market context (current conditions, trends, historical data)
- Actionable advice (what to do, what to watch for, what to avoid)

Keep the answer between 200-500 words. Be specific, not generic. Every fact should be verifiable from the source material provided. Do NOT hallucinate numbers not in the source material."""


def load_wiki_docs():
    """Load all markdown docs from the DG wiki."""
    docs = {}
    for f in sorted(WIKI_DIR.rglob("*.md")):
        if ".git" in str(f) or "graphify-out" in str(f):
            continue
        rel = f.relative_to(WIKI_DIR)
        docs[str(rel)] = f.read_text()
    return docs


def get_context_for_topic(docs, topic):
    """Get relevant wiki content for a question topic."""
    topic_to_docs = {
        "lease_structures": ["07-market/lease-structures.md", "06-leases/dg-lease-template.md"],
        "cap_rates": ["07-market/cap-rate-trends.md", "05-comps/cap-rate-benchmarks.md", "05-comps/recent-trades.md"],
        "developers": ["07-market/preferred-developers.md", "07-market/site-selection.md"],
        "buyers": ["07-market/buyer-profiles.md", "07-market/capital-and-lending.md"],
        "florida": ["01-stores/fl-market-overview.md", "07-market/edgar-usage.md"],
        "site_selection": ["07-market/site-selection.md", "01-stores/format-distribution.md"],
        "formats": ["07-market/store-formats.md", "01-stores/format-distribution.md"],
        "financing": ["07-market/capital-and-lending.md", "07-market/cap-rate-trends.md"],
        "competitors": ["07-market/competitors-stnl.md", "07-market/cap-rate-trends.md"],
    }

    relevant = topic_to_docs.get(topic, [])
    context_parts = []
    for doc_path in relevant:
        if doc_path in docs:
            # Truncate to 3000 chars per doc
            context_parts.append(f"--- {doc_path} ---\n{docs[doc_path][:3000]}")

    return "\n\n".join(context_parts)


def call_ollama(messages, temperature=0.7, max_tokens=1024):
    """Call ollama via raw generate endpoint (works with Qwen 3.5 think mode)."""
    import re

    # Build ChatML prompt from messages
    prompt_parts = []
    for m in messages:
        role = m["role"]
        content = m["content"]
        prompt_parts.append(f"<|im_start|>{role}\n{content}<|im_end|>")
    prompt_parts.append("<|im_start|>assistant\n")
    prompt = "\n".join(prompt_parts)

    payload = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "raw": True,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
            "stop": ["<|im_end|>"],
        },
    }).encode()

    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    try:
        resp = urllib.request.urlopen(req, timeout=180)
        data = json.loads(resp.read().decode())
        content = data.get("response", "").strip()
        # Strip <think>...</think> blocks
        if "<think>" in content:
            content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        return content
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return None


def generate_pair(docs, topic, question, persona):
    """Generate a single Q&A training pair."""
    context = get_context_for_topic(docs, topic)

    gen_prompt = GENERATION_PROMPT.format(context=context[:6000], question=question)

    answer = call_ollama([
        {"role": "system", "content": persona},
        {"role": "user", "content": gen_prompt},
    ])

    if not answer or len(answer) < 100:
        return None

    pair = {
        "messages": [
            {"role": "system", "content": persona},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ],
        "metadata": {
            "domain": "dg",
            "topic": topic,
            "generator": "generate_dg_pairs.py",
            "model": MODEL,
            "testnet": True,
        },
        "id": str(uuid.uuid4()),
        "fingerprint": hashlib.sha256(
            (persona + question + answer).lower().encode()
        ).hexdigest(),
    }

    return pair


def main():
    parser = argparse.ArgumentParser(description="Generate DG training pairs from wiki")
    parser.add_argument("--count", type=int, default=3000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--doc", type=str, help="Generate from specific doc only")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"dg_pairs_{args.count}.jsonl"

    docs = load_wiki_docs()
    print(f"Loaded {len(docs)} wiki docs")

    # Build question pool
    all_questions = []
    for topic, questions in QUESTION_TEMPLATES.items():
        for q in questions:
            all_questions.append((topic, q))

    # Expand to target count by cycling with different personas
    plan = []
    while len(plan) < args.count:
        for topic, question in all_questions:
            persona = random.choice(PERSONAS)
            plan.append((topic, question, persona))
            if len(plan) >= args.count:
                break

    random.shuffle(plan)
    plan = plan[:args.count]

    print(f"Generation plan: {len(plan)} pairs")
    print(f"Topics: {len(QUESTION_TEMPLATES)} × ~{len(all_questions)} questions × {len(PERSONAS)} personas")
    print(f"Output: {output_file}")
    print(f"Model: {MODEL} @ {OLLAMA_URL}")
    print()

    outfile = open(output_file, "w")
    generated = 0
    errors = 0
    seen = set()

    for i, (topic, question, persona) in enumerate(plan):
        print(f"  [{i+1}/{len(plan)}] {topic}: {question[:50]}...", end=" ", flush=True)

        if args.dry_run:
            pair = {
                "messages": [
                    {"role": "system", "content": persona[:50]},
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": f"[DRY RUN — {topic}]"},
                ],
                "metadata": {"domain": "dg", "topic": topic, "testnet": True},
                "id": str(uuid.uuid4()),
            }
            outfile.write(json.dumps(pair) + "\n")
            outfile.flush()
            generated += 1
            print("OK (dry-run)")
            continue

        pair = generate_pair(docs, topic, question, persona)
        if pair:
            if pair["fingerprint"] not in seen:
                seen.add(pair["fingerprint"])
                outfile.write(json.dumps(pair, ensure_ascii=False) + "\n")
                outfile.flush()
                generated += 1
                print(f"OK ({len(pair['messages'][2]['content'])} chars)")
            else:
                print("SKIP (dup)")
        else:
            errors += 1
            print("FAILED")

    outfile.close()

    print(f"\n{'='*60}")
    print(f"  GENERATED: {generated} pairs ({errors} errors)")
    print(f"  Output: {output_file}")
    print(f"  Topics: {', '.join(QUESTION_TEMPLATES.keys())}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

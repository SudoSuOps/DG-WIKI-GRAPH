# DG Graph Schema v2 — Operator-Grade Node Design

**Status**: SPEC — implement on next graph rebuild
**Origin**: Operator feedback on v1 graph (April 7, 2026)

## Problem with v1

Every node is `type: document`. That's dev mode. Dollar General Corporation is not a document — it's a company. CG Buchalter is not a document — it's a developer. The ontology is flat.

Neighbors are one flat list. No meaning. No grouping. No edge labels visible.

## v2 Node Schema

```json
{
  "id": "dollar_general_corporation",
  "label": "Dollar General Corporation",
  "type": "parent_entity",
  "cluster": "DG Corporate / Landlord Cluster",
  "source_document": "07-market/dollar-general-corporate.md",
  "degree": 19,
  "confidence": 0.94,
  "last_verified": "2026-04-07",
  "summary": "Public parent company and primary tenant anchor in the DG STNL ecosystem. Connected to major net lease landlords, developers, competitors, and SEC-derived corporate intelligence.",
  
  "neighbors_by_type": {
    "tenant_of": [
      {"id": "spirit_realty", "label": "Spirit Realty Capital", "detail": "owns 400+ DG assets / landlord"},
      {"id": "realty_income", "label": "Realty Income", "detail": "owns 200+ DG assets / largest net lease REIT"},
      {"id": "nnn_reit", "label": "National Retail Properties", "detail": "owns 150+ DG assets"},
      {"id": "essential_properties", "label": "Essential Properties Realty", "detail": "growing DG portfolio"},
      {"id": "agree_realty", "label": "Agree Realty", "detail": "active net lease acquirer"},
      {"id": "store_capital", "label": "STORE Capital (GIC)", "detail": "PE-acquired, 300+ DGs"}
    ],
    "developed_by": [
      {"id": "cg_buchalter", "label": "CG Buchalter", "detail": "800 DGs, 15 states, 25yr partnership"},
      {"id": "colby_capital", "label": "Colby Capital LLC", "detail": "240+ DGs, 6 states, 15yr partnership"},
      {"id": "mbc_development", "label": "MBC Development", "detail": "eastern/central PA preferred developer"},
      {"id": "confluent_development", "label": "Confluent Development", "detail": "north FL preferred developer"},
      {"id": "ratcliff_companies", "label": "Ratcliff Companies", "detail": "southeast developer partner"}
    ],
    "competes_with": [
      {"id": "dollar_tree", "label": "Dollar Tree / Family Dollar", "detail": "STNL comp, Baa2 credit (higher than DG)"},
      {"id": "tractor_supply", "label": "Tractor Supply Company", "detail": "rural market overlap, BBB credit"},
      {"id": "autozone", "label": "AutoZone", "detail": "STNL comp, BBB, 5.34% cap (tighter than DG)"},
      {"id": "oreilly", "label": "O'Reilly Automotive", "detail": "STNL comp, BBB+, 6.07% cap"},
      {"id": "advance_auto", "label": "Advance Auto Parts", "detail": "weaker credit, 6.57% cap"}
    ],
    "sourced_from": [
      {"id": "edgar_filings", "label": "SEC EDGAR Filings", "detail": "primary corporate source — 10-K, 10-Q, proxy"}
    ]
  }
}
```

## Node Types (v2 Ontology)

| Type | Description | Examples |
|------|------------|---------|
| `parent_entity` | Public company or corporate parent | Dollar General Corp, Dollar Tree Inc |
| `landlord` | REIT or entity that owns DG properties | Spirit Realty, Realty Income, NNN |
| `developer` | Build-to-suit developer partner | CG Buchalter, Colby Capital |
| `competitor` | STNL competitor tenant | Dollar Tree, AutoZone, Tractor Supply |
| `lender` | CMBS shop, bank, or life company | Arbor, CBRE, Goldman Sachs |
| `buyer_type` | Buyer category | 1031 Exchange, DST, Family Office, HNW |
| `market_zone` | Geographic investment zone | Florida (Tier 1), Ohio (Tier 3 Yield) |
| `lease_structure` | Lease term and economics | 15yr NNN, Rent Bump Schedule |
| `risk_signal` | Risk indicator | Dark Store Risk, Closure Signal |
| `metric` | Cap rate, DSCR, spread | 6.70% Cap Rate, 1.20x DSCR |
| `research` | Academic paper or eval result | Letdin 2023, Baseline Eval |
| `process` | Business process or workflow | MAGIC Pipeline, BOV Engine |
| `template` | Document template | OM 4-Panel, LOI 1-Page, Comp Deck |
| `doctrine` | Glass-wall doctrine | Train Narrow Win Deep |
| `model` | AI model | SwarmDG-9B, SwarmAtlas-27B |
| `agent` | AI agent | Agent-DG |
| `data_source` | External data source | FL DOR, Sunbiz, OpenCorporates |

## Community Names (v2)

Replace `Community N` with meaningful labels:

| Community | v2 Name | Key Nodes |
|-----------|---------|-----------|
| 0 | DG Corporate & Landlord Cluster | Dollar General Corp, Spirit, Realty Income |
| 1 | Financing & Capital Markets | CMBS, Arbor, Goldman, DSCR, Positive Spread |
| 2 | Developer Network | CG Buchalter, Colby Capital, Build-to-Suit |
| 3 | STNL Competitor Landscape | Dollar Tree, AutoZone, O'Reilly, Tractor Supply |
| 4 | Buyer Universe | 1031 Exchange, DST, Family Office, HNW |
| 5 | Florida Market Intelligence | FL DOR, FL Cap Rate Premium, 1031 Demand |
| 6 | Lease Structure & Risk | 15yr NNN, Dark Store Risk, Remodel Signal |
| 7 | MAGIC Pipeline | Meetings, Appraisals, Grind, Ink, Close, FEE |
| 8 | Micro-Domain Thesis | Train Narrow, DG King Principle, Operator Brain |
| 9 | Model & Training | Qwen 3.5 9B, GDN, LoRA Config, SwarmDG-9B |
| 10 | Research & Eval | Baseline Eval, Academic Papers, Letdin 2023 |
| 11 | Ownership Resolution | Parcel Layer, Entity Layer, Contact Layer |

## Edge Labels (v2)

Every edge gets a human-readable label:

```
Spirit Realty —[owns 400+ DG assets / landlord]→ Dollar General Corp
CG Buchalter —[developer, 800 stores, 25yr]→ Dollar General Corp
AutoZone —[STNL comp, cap rate comparator]→ Dollar General Corp
FL DOR —[free parcel lookup, OWN_ADDR fields]→ DG Ownership Graph
Baseline Eval —[proves 0/15 knowledge gap]→ SwarmDG-9B Ship Target
```

## Evidence Panel (per node)

```
CONFIDENCE:      0.94
EVIDENCE COUNT:  7 sources
LAST VERIFIED:   2026-04-07
PRIMARY SOURCES: EDGAR 10-K, Net Lease Advisor, Boulder Group, DOR
EDGE COUNT:      19 connections
COMMUNITY:       DG Corporate / Landlord Cluster
```

## Implementation Path

1. Update extraction prompt to output v2 node types
2. Update graphify `build_from_json` to accept new types
3. Update `to_html` to render grouped neighbors + edge labels
4. Update community labeling step to use semantic names
5. Add confidence + evidence panel to HTML node inspector

This is a graphify feature request, not a data change. The intelligence is already in the graph — the upgrade is how it's displayed.

---

*v1 was a dev graph. v2 is an operator panel. Same data. Better ontology. Better display. Product-grade.*

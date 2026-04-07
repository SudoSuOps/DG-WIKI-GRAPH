# Graph Report - /home/swarm/DG-WIKI-GRAPH  (2026-04-07)

## Corpus Check
- Corpus is ~19,740 words - fits in a single context window. You may not need a graph.

## Summary
- 62 nodes · 91 edges · 9 communities detected
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Dollar General Corporation` - 19 edges
2. `Standard DG NNN Lease (15yr Absolute NNN)` - 12 edges
3. `DG Cap Rate Benchmarks (BOV Reference)` - 10 edges
4. `SEC EDGAR Filings (Corporate Intelligence)` - 6 edges
5. `Traditional DG Store Format (9,100 sqft)` - 5 edges
6. `Florida DG Market (Phase 1 Target)` - 5 edges
7. `Florida DOR Tax Roll Data` - 5 edges
8. `MAGIC Pipeline (Meetings-Appraisals-Grind-Ink-Close)` - 5 edges
9. `BOV Engine (Broker Opinion of Value)` - 5 edges
10. `DG Site Selection Criteria` - 5 edges

## Surprising Connections (you probably didn't know these)
- `LOI Template (Letter of Intent)` --references--> `Standard DG NNN Lease (15yr Absolute NNN)`  [INFERRED]
  08-pipeline/magic-templates.md → 06-leases/dg-lease-template.md
- `DG Cap Rate Trends (Market Snapshot)` --semantically_similar_to--> `DG Cap Rate Benchmarks (BOV Reference)`  [EXTRACTED] [semantically similar]
  07-market/cap-rate-trends.md → 05-comps/cap-rate-benchmarks.md
- `DG Lease Anatomy (Market Reference)` --semantically_similar_to--> `Standard DG NNN Lease (15yr Absolute NNN)`  [EXTRACTED] [semantically similar]
  07-market/lease-structures.md → 06-leases/dg-lease-template.md
- `1031 Exchange Investors` --buys--> `Standard DG NNN Lease (15yr Absolute NNN)`  [EXTRACTED]
  07-market/buyer-profiles.md → 06-leases/dg-lease-template.md
- `BOV Engine (Broker Opinion of Value)` --references--> `DG Cap Rate Trends (Market Snapshot)`  [INFERRED]
  05-comps/cap-rate-benchmarks.md → 07-market/cap-rate-trends.md

## Hyperedges (group relationships)
- **DG NNN Investment Thesis: BBB Credit + Absolute NNN + 15yr Term + 10% Bumps + Corporate Guarantee** — dollar_general_corporation, dg_nnn_lease, bbt_credit_rating, rent_bump_schedule, renewal_options, 1031_exchange_investors, reit_net_lease_platforms, hnw_investors [EXTRACTED 1.00]
- **DG Owner Identification Chain: Store → DOR Parcel → Sunbiz Entity → EDGAR Parent → MAGIC Contact** — dollar_general_corporation, florida_dor, sunbiz_opencorp, edgar_filings, spirit_realty, realty_income, magic_pipeline, i_got_a_buyer_letter [EXTRACTED 1.00]
- **Build-to-Suit Pipeline: DG Selects Site → Preferred Developer Builds → Signs 15yr NNN → Developer Sells to Investor** — dollar_general_corporation, dg_site_selection, cg_buchalter, colby_capital, confluent_development, dg_nnn_lease, build_to_suit_economics, 1031_exchange_investors, reit_net_lease_platforms [EXTRACTED 1.00]
- **Florida Cap Rate Premium: No Income Tax + Population Growth + 1031 Demand → 25-50 bps Tighter Than National** — fl_market_overview, fl_1031_demand, cap_rate_benchmarks, 1031_exchange_investors, hnw_investors, phase1_florida [EXTRACTED 1.00]
- **Automated BOV Stack: DOR Data → Lease Abstract → Cap Rate Benchmarks → BOV Engine → OM Template → PostGrid Mail** — florida_dor, dg_nnn_lease, cap_rate_benchmarks, bov_engine, offering_memorandum_template, i_got_a_buyer_letter, postgrid_api, magic_pipeline [INFERRED 0.90]

## Communities

### Community 0 - "Community 0"
Cohesion: 0.18
Nodes (13): Dark Store Risk (Closure / Non-Renewal), DG Cannibalization Strategy, DG Lease Anatomy (Market Reference), Standard DG NNN Lease (15yr Absolute NNN), DG Remodel as Renewal Commitment Signal, DG Site Selection Criteria, DST (Delaware Statutory Trust) Investors, High Net Worth (HNW) Individual Investors (+5 more)

### Community 1 - "Community 1"
Cohesion: 0.2
Nodes (10): Advance Auto Parts (STNL Competitor), Agree Realty (ADC), AutoZone (STNL Competitor), Dollar General Corporation, Essential Properties Realty (EPRT), Local Private Investors / LLCs, MBC Development (PA Developer), O'Reilly Automotive (STNL Competitor) (+2 more)

### Community 2 - "Community 2"
Cohesion: 0.31
Nodes (9): Boulder Group Net Lease Research, BOV Engine (Broker Opinion of Value), DG Cap Rate Benchmarks (BOV Reference), CoStar / Crexi Transaction Data, LOI Template (Letter of Intent), MAGIC Pipeline (Meetings-Appraisals-Grind-Ink-Close), New Construction vs Existing Cap Rate Spread, Offering Memorandum Template (4-Panel OM) (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.53
Nodes (6): Agent-DG Intelligence Graph, DG Graph Schema (17-Field Parcel Record), Florida DOR Tax Roll Data, I Got A Buyer Direct Mail Letter, PostGrid API (Automated Direct Mail), Sunbiz / OpenCorporates Entity Resolution

### Community 4 - "Community 4"
Cohesion: 0.47
Nodes (6): DG Market Format (16,000 sqft), DGX Urban Format (3,600 sqft), DG Format Distribution (National Mix), pOpshelf Format (9,000 sqft Suburban), pOpshelf Strategic Uncertainty, Traditional DG Store Format (9,100 sqft)

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (6): BBB Investment Grade Credit Rating, DG Cap Rate Trends (Market Snapshot), DG as NNN Tenant (BBB Credit), Dollar Tree / Family Dollar (Competitor), Rural Fortress Strategy (Towns Under 20K), Tractor Supply Company (STNL Competitor)

### Community 6 - "Community 6"
Cohesion: 0.4
Nodes (5): 1031 Exchange Investors, Confluent Development (North FL Developer), Florida 1031 Exchange Capital Demand, Florida DG Market (Phase 1 Target), Phase 1 Florida Owner Identification

### Community 7 - "Community 7"
Cohesion: 0.5
Nodes (4): SEC EDGAR Filings (Corporate Intelligence), National Retail Properties (NNN), Realty Income (O), Spirit Realty Capital (SRC)

### Community 8 - "Community 8"
Cohesion: 0.67
Nodes (3): Build-to-Suit Developer Economics, CG Buchalter (Developer), Colby Capital LLC (Developer)

## Knowledge Gaps
- **21 isolated node(s):** `DG Lease Anatomy (Market Reference)`, `Essential Properties Realty (EPRT)`, `Agree Realty (ADC)`, `STORE Capital (GIC-acquired)`, `Local Private Investors / LLCs` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Dollar General Corporation` connect `Community 1` to `Community 8`, `Community 5`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.392) - this node is a cross-community bridge._
- **Why does `Standard DG NNN Lease (15yr Absolute NNN)` connect `Community 0` to `Community 2`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.305) - this node is a cross-community bridge._
- **Why does `DG Cap Rate Benchmarks (BOV Reference)` connect `Community 2` to `Community 8`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.265) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `DG Cap Rate Benchmarks (BOV Reference)` (e.g. with `Traditional DG Store Format (9,100 sqft)` and `Offering Memorandum Template (4-Panel OM)`) actually correct?**
  _`DG Cap Rate Benchmarks (BOV Reference)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Traditional DG Store Format (9,100 sqft)` (e.g. with `DG Cap Rate Benchmarks (BOV Reference)` and `DGX Urban Format (3,600 sqft)`) actually correct?**
  _`Traditional DG Store Format (9,100 sqft)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DG Lease Anatomy (Market Reference)`, `Essential Properties Realty (EPRT)`, `Agree Realty (ADC)` to the rest of the system?**
  _21 weakly-connected nodes found - possible documentation gaps or missing edges._
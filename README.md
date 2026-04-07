# DG Intelligence Graph — Dollar General Ownership Wiki

**The Book of Business for Agent-DG**

Not a map. Not a spreadsheet. An intelligence graph.

Every Dollar General → who owns it → what entity → who to call → when they'll sell.

## Structure

```
00-config/       swarm.yaml config for DG pipeline
01-stores/       every DG location (address, lat/lng, store number)
02-owners/       parcel data → who owns the real estate (tax roll)
03-entities/     entity resolution → what LLC/LP/trust (Sunbiz, OpenCorp)
04-contacts/     decision makers → who to call (officers, registered agents)
05-comps/        recent DG trades → comp deeds (sold price, cap rate, date)
06-leases/       lease intelligence → term, bumps, NNN, expiration
07-market/       market data → cap rate trends by state, MSA analytics
08-pipeline/     MAGIC pipeline config → templates, scripts, automation
graphify-out/    knowledge graph (nodes, edges, HTML visualization)
```

## The Intelligence Graph

```
STORE ──owns── OWNER ──resolves── ENTITY ──contacts── PERSON
  │               │                  │                    │
  ├── address     ├── mailing addr   ├── jurisdiction     ├── name
  ├── lat/lng     ├── purchase date  ├── sunbiz doc#      ├── title
  ├── county      ├── purchase price ├── registered agent  ├── phone
  ├── parcel ID   ├── tax assessed   ├── officers[]       ├── email
  │               │                  ├── parent entity     │
  ├── LEASE       ├── SCORE          ├── also owns: N DGs  ├── HISTORY
  │  term         │  hold period     │                     │  last contacted
  │  bumps        │  likely seller   └── COMPS             │  response
  │  NNN          │  1031 candidate      recent trades     │  status
  │  expiration   │  indicated value     cap rate range    │  notes
  └── confidence  └── source            avg hold period   └── next action
```

## MAGIC Applied

```
M — MEETINGS     Agent-DG queries the graph for owners scored "likely seller"
A — APPRAISALS   Auto-BOV from comps in 05-comps/ → 1-sheet OM generated
G — GRIND        Personalized outreach from 04-contacts/ → blast the book
I — INK          LOI/PSA generated from 08-pipeline/ templates
C — CLOSE        Closing statement filed → deed anchored to Hedera
```

## Phase 1: Florida

```
~900 DG stores in Florida
Step A: store locations (OSM + DG locator) ✓ partial
Step B: parcel/ownership (FL DOR tax roll → Regrid/ATTOM)
Step C: entity resolution (Sunbiz → OpenCorporates)
Step D: contact enrichment (officers, registered agents, mailing)
Step E: comp deeds (recent FL DG trades)
Step F: build the graph → graphify → swarmandbee.ai/dg
```

## How This Wiki Works

Drop intelligence in. The graph absorbs it.

```
# Add a new DG trade (comp deed)
echo '{"address":"123 Main St","city":"Perry","state":"FL",...}' >> 05-comps/fl_trades.jsonl

# Add owner research
nano 02-owners/fl/taylor-county.md

# Update the graph
/graphify --update

# Query the graph
/graphify query "who owns the most DGs in central Florida?"
/graphify path "Spirit Realty" "Dollar General Perry FL"
```

---

*Not a map. Not a spreadsheet. Intelligence by the pound.*
*The DG King had this in his head. Agent-DG has it in the graph.*

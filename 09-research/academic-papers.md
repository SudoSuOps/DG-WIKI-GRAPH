# Academic Research — Dollar General & Net Lease Intelligence

**Source**: OpenAlex (open scholarly database, 250M+ works)
**Purpose**: Academic validation of trade knowledge in the DG wiki

## Why Academic Research Matters for Agent-DG

Trade knowledge tells you WHAT the cap rate is. Academic research tells you WHY.

When a DG owner asks "why is my property worth less than the one down the street?" — the DG King answers with experience. SwarmDG-9B answers with trade knowledge AND the research that explains the pricing mechanism.

---

## Tier 1 — Directly Validates the DG Investment Thesis

### The Role of Tenant Characteristics in Retail Cap Rate Variation

| Field | Value |
|-------|-------|
| Authors | Mariya Letdin, G. Stacy Sirmans, Greg Smersh, Tingyu Zhou |
| Year | 2023 |
| Journal | The Journal of Real Estate Finance and Economics |
| DOI | [10.1007/s11146-023-09958-9](https://doi.org/10.1007/s11146-023-09958-9) |
| Cited by | 8 |
| Concepts | Lease, capitalization, credit risk, asset pricing |

**Why it matters for DG:**

This is the academic proof that tenant credit rating drives cap rate variation. The paper demonstrates empirically what every DG broker knows intuitively — BBB-rated tenants trade at tighter caps than non-investment-grade tenants.

```
PAPER VALIDATES:
  ✓ BBB credit = lower cap rate (DG wiki: 6.70% for DG vs 7.50%+ for non-IG)
  ✓ Lease term remaining affects cap rate (DG wiki: 75-100 bps new vs existing)
  ✓ Tenant characteristics matter MORE than location for NNN pricing
  ✓ Credit risk is the primary driver of cap rate spread

AGENT-DG APPLICATION:
  When generating a BOV, cite this paper:
  "Cap rate variation is primarily driven by tenant credit characteristics
   (Letdin et al., 2023). Dollar General's BBB/Baa2 rating positions this
   property in the investment-grade cap rate band of 6.50-7.00%."
   
  Academic backing makes the BOV more defensible.
  The DG King won on experience. SwarmDG-9B wins on evidence.
```

---

### Dollar Store Impact on Local Labor Markets and Retail Activity

| Field | Value |
|-------|-------|
| Authors | Lauren Chenarides, Timothy J. Richards, Zachariah Rutledge, John Pender |
| Year | 2025 |
| Journal | Food Policy |
| DOI | [10.1016/j.foodpol.2025.102827](https://doi.org/10.1016/j.foodpol.2025.102827) |
| Cited by | 3 |

**Why it matters for DG:**

Dollar stores face political headwinds — some municipalities restrict new DG openings (zoning, food desert concerns). This paper provides data on DG's actual economic impact on communities — labor markets, retail activity, consumer access.

```
AGENT-DG APPLICATION:
  Site selection intelligence:
  - Which municipalities are friendly vs hostile to DG?
  - Is there a moratorium on dollar store permits in this area?
  - Does the academic evidence support DG's community impact?
  
  For DG owners worried about political risk:
  "Recent research (Chenarides et al., 2025) examines dollar store
   impact on local labor markets and retail activity, providing
   evidence-based context for community impact assessment."
```

---

## Tier 2 — Validates CRE Investment Framework

### Cap Rates and Risk: A Spatial Analysis of Commercial Real Estate

| Field | Value |
|-------|-------|
| Year | 2018 |
| Journal | Studies in Economics and Finance |
| DOI | [10.1108/sef-11-2016-0267](https://doi.org/10.1108/sef-11-2016-0267) |
| Cited by | 8 |

**Relevance**: Validates that location affects cap rates and risk premia. Supports DG wiki's state-by-state cap rate variations (CO tightest, secondary markets widest) and the FL premium thesis (25-50 bps tighter than national).

```
AGENT-DG APPLICATION:
  FL market overview uses this:
  "Spatial analysis of commercial real estate cap rates demonstrates
   statistically significant location-based risk premia variation,
   supporting Florida's 25-50 bps cap rate premium driven by
   population growth and 1031 exchange capital concentration."
```

---

### COVID-19 Impact on Commercial Real Estate Prices

| Field | Value |
|-------|-------|
| Year | 2020 |
| Journal | The Review of Asset Pricing Studies |
| DOI | [10.1093/rapstu/raaa014](https://doi.org/10.1093/rapstu/raaa014) |
| Cited by | 202 |

**Relevance**: Most-cited recent CRE paper. Documents how COVID transmitted through asset and capital markets. DG benefited — essential retail classification protected valuations while other retail collapsed. Validates "essential retail = recession-resistant" thesis in the DG wiki.

```
AGENT-DG APPLICATION:
  Buyer pitch for risk-averse investors:
  "During COVID-19, essential retail net lease assets (including Dollar General)
   maintained valuations while discretionary retail experienced significant
   price declines (Ling et al., 2020). DG's essential goods positioning
   provides structural downside protection."
```

---

## Tier 3 — Background Context

### Capitalizing on the State: Political Economy of REITs

| Field | Value |
|-------|-------|
| Year | 2018 |
| Journal | Geoforum |
| DOI | [10.1016/j.geoforum.2018.02.014](https://doi.org/10.1016/j.geoforum.2018.02.014) |
| Cited by | 149 |

**Relevance**: Explains REIT behavior and institutional capital flows. Useful for understanding why Spirit Realty, Realty Income, and NNN behave as they do — portfolio strategy, tax advantages, institutional mandates. Context for the EDGAR/owner strategy layer.

---

## How Research Feeds the Wiki

```
RESEARCH PIPELINE:
  1. OpenAlex search for new papers (quarterly)
  2. Filter for DG-relevant (cap rates, tenant credit, net lease, dollar stores)
  3. Extract key findings → add to relevant wiki sections
  4. Cite in Agent-DG BOVs and proposals
  5. /graphify --update → research nodes connect to trade knowledge
  
  The wiki has TWO evidence layers:
    TRADE LAYER: Boulder Group, Net Lease Advisor, broker OMs (what the market does)
    ACADEMIC LAYER: OpenAlex papers (why the market does it)
    
  Together = defensible. Together = weight.
```

## OpenAlex Search Queries for DG Domain

Save these for quarterly research updates:

```
# Tenant credit and cap rates
https://api.openalex.org/works?search=tenant+credit+rating+cap+rate+commercial+real+estate

# Dollar store community impact
https://api.openalex.org/works?search=dollar+store+community+impact+food+desert

# Net lease REIT strategy
https://api.openalex.org/works?search=REIT+net+lease+single+tenant+investment+returns

# 1031 exchange research
https://api.openalex.org/works?search=1031+exchange+tax+deferred+real+estate

# CRE spatial cap rate analysis
https://api.openalex.org/works?search=cap+rate+spatial+analysis+commercial+real+estate
```

---

*Trade knowledge tells you what the cap rate IS. Academic research tells you WHY. Both feed the wiki. Both feed the model. The DG King had the experience. SwarmDG-9B has the evidence.*

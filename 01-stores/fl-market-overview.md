# Florida Dollar General Market -- Phase 1 Target

Florida is the first state targeted by Agent-DG for automated owner identification, BOV generation, and direct mail campaigns. This document explains why FL was chosen and provides the market intelligence that feeds the pipeline.

---

## Why Florida First

| Factor | Detail |
|--------|--------|
| **DG density** | 900+ stores statewide -- third-highest concentration nationally behind Texas and Georgia. Deep pipeline of potential listings. |
| **Population growth** | FL added 365,000+ residents in 2024 (Census Bureau). Net in-migration compresses cap rates and increases NNN buyer demand. |
| **No state income tax** | Top 3 destination for 1031 exchange capital. Sellers in high-tax states (CA, NY, IL) actively seek FL replacement properties. Buyers pay a premium for FL deals. |
| **Cap rate premium** | FL DG trades 25-50 bps tighter than national average. A 15yr new DG in FL: ~6.50% vs. 6.70% national. Higher property values = higher commissions per deal. |
| **DOR data quality** | Florida Department of Revenue publishes statewide property assessment rolls with owner name and mailing address (OWN_ADDR, OWN_CITY, OWN_STATE, ZIP). Machine-readable. Updated annually. This is the foundation of the owner identification pipeline. |
| **Broker familiarity** | CRE broker background includes FL transactions. Existing relationships with FL-based NNN buyers and title companies. |

---

## Store Count and Distribution

Estimated 900+ Dollar General locations across Florida, concentrated in suburban and rural corridors outside major metros. DG's FL footprint spans all 67 counties, with highest density in:

### Top 10 Counties by DG Density

| Rank | County | Primary MSA | Est. DG Stores | Population (2024 est.) | Notes |
|------|--------|-------------|---------------|----------------------|-------|
| 1 | **Duval** | Jacksonville | 65+ | 1,020,000 | Northeast FL anchor. Military population. High NNN investor activity. |
| 2 | **Hillsborough** | Tampa | 55+ | 1,510,000 | Tampa Bay growth corridor. I-4 spine. |
| 3 | **Orange** | Orlando | 50+ | 1,440,000 | Central FL tourism economy. Suburban DG expansion along SR-429 and east. |
| 4 | **Broward** | Fort Lauderdale | 45+ | 1,960,000 | South FL. Higher land costs = older stores, shorter remaining terms. |
| 5 | **Palm Beach** | West Palm Beach | 40+ | 1,530,000 | Affluent county but DG serves western agricultural corridors and Glades. |
| 6 | **Pinellas** | St. Petersburg | 35+ | 960,000 | Dense suburban. Limited new construction due to land scarcity. |
| 7 | **Polk** | Lakeland | 40+ | 780,000 | I-4 corridor between Tampa and Orlando. Growth market. New construction active. |
| 8 | **Marion** | Ocala | 35+ | 400,000 | Rural/exurban. Classic DG heartland. Lower rents, wider cap rates. |
| 9 | **Volusia** | Daytona Beach | 30+ | 570,000 | Coastal corridor. Mixed vintage -- some 15yr new, some approaching term end. |
| 10 | **Brevard** | Melbourne/Titusville | 25+ | 620,000 | Space Coast growth. Kennedy Space Center employment base. |

### Key MSAs

| MSA | Est. DG Stores (MSA-wide) | Cap Rate vs. National | 1031 Demand |
|-----|--------------------------|----------------------|-------------|
| **Jacksonville** | 90+ | -25 bps | High -- military, retiree capital |
| **Tampa-St. Pete** | 100+ | -30 bps | Very high -- growth + lifestyle |
| **Orlando-Kissimmee** | 80+ | -25 bps | High -- tourism economy diversification |
| **Miami-Dade** | 40+ | -40 bps | Moderate -- land costs limit new DG, but deep capital pool |
| **Palm Beach** | 40+ | -35 bps | Very high -- wealth concentration, 1031 destination |

---

## Florida-Specific Cap Rates

FL DG properties consistently trade tighter than national benchmarks. The premium is driven by three factors: population growth trajectory, no state income tax (1031 magnet), and deep institutional buyer pool.

| Remaining Term | National Benchmark | Florida Adjustment | FL Cap Rate |
|----------------|-------------------|-------------------|-------------|
| 15 years (new) | 6.70% | -20 to -30 bps | 6.40% - 6.50% |
| 10 years | 7.00% | -20 to -30 bps | 6.70% - 6.80% |
| 7 years | 7.50% | -25 bps | 7.25% |
| 5 years | 8.00% | -25 bps | 7.75% |
| 3 years | 8.50%+ | -25 bps | 8.25%+ |

**Note:** South FL (Miami-Dade, Broward, Palm Beach) trades even tighter -- an additional 10-15 bps below the statewide FL average due to land scarcity and capital density.

---

## 1031 Exchange Dynamics

Florida is consistently a top-3 destination for 1031 exchange capital nationally (alongside Texas and Tennessee). This creates structural demand for FL DG properties that suppresses cap rates.

**Why 1031 buyers love FL DG:**
- No state income tax -- avoids the "tax swap" problem where exchanging into a high-tax state erodes the 1031 benefit.
- Dollar General NNN lease = passive ownership with zero landlord responsibilities.
- 15-year lease term satisfies the "long hold" requirement for 1031 compliance.
- $1M-$2M deal size fits the sweet spot for individual 1031 exchangers.
- FL property appreciation trend provides capital growth on top of yield.

**1031 buyer profile for FL DG:**
- California apartment seller ($2M-$5M equity, fleeing Prop 13 reassessment risk and state income tax)
- Northeast small business owner selling commercial property
- Midwest farmer monetizing land and seeking passive income
- Retiring self-storage or strip center operator
- Divorced party receiving real estate in settlement (45-day identification clock)

---

## Florida DOR Data Portal

The Florida Department of Revenue (DOR) maintains the most accessible property tax assessment database of any state Agent-DG targets. This is the engine for Phase 1 owner identification.

### What the DOR Provides

| Field | Description | Agent-DG Use |
|-------|------------|-------------|
| `PARCEL_ID` | County-specific parcel number | Unique property identifier |
| `OWN_NAME` | Owner of record | Entity name for skip tracing |
| `OWN_ADDR` | Owner mailing address (line 1) | Direct mail target |
| `OWN_CITY` | Owner city | Geographic segmentation |
| `OWN_STATE` | Owner state | Out-of-state owner flagging |
| `OWN_ZIP` | Owner zip code | Mail delivery |
| `SITUS_ADDR` | Property street address | Store identification |
| `JV` (Just Value) | Assessed market value | Valuation cross-check |
| `AV` (Assessed Value) | Taxable value (with exemptions) | Tax burden analysis |
| `TV` (Taxable Value) | After exemptions | Net tax liability |
| `DOR_UC` (Use Code) | Property use classification | Filter for commercial (retail) |
| `ACT_YR_BLT` | Actual year built | Construction vintage |
| `TOT_LVG_AREA` | Total living area (sqft) | Building size verification |
| `LND_SQFOOT` | Land area (sqft) | Lot size for BOV adjustments |

### Data Access

- **URL:** Florida DOR GIS and NAL (Name-Address-Legal) files are published annually at the county level.
- **Format:** Fixed-width text files or CSV, downloadable by county.
- **Update cycle:** Annual assessment rolls finalized by July 1 each year.
- **Coverage:** All 67 counties. Some counties also publish interim data.
- **Cost:** Free. Public record under Florida Statute 119.

### Agent-DG Pipeline (FL DOR)

1. Download NAL files for target counties (top 10 above).
2. Filter by DOR use code for commercial retail.
3. Cross-reference situs addresses against known DG store locations (from DG corporate filings, Google Places API, or purchased lists).
4. Extract owner entity name and mailing address.
5. Run entity through Secretary of State (SunBiz) for registered agent, officer names, and mailing address.
6. Feed owner contact info into the "I Got A Buyer" direct mail template.
7. Track response rate and conversion by county.

---

## Competitive Landscape -- FL NNN Brokers

Agent-DG's FL campaign will compete with (or complement) these established NNN brokerages active in Florida DG transactions:

| Firm | FL Presence | DG Deal Volume | Notes |
|------|------------|---------------|-------|
| Marcus & Millichap | Statewide (8 FL offices) | High | Largest NNN brokerage nationally. IPA division for institutional. |
| Stan Johnson / Newmark | Tampa, Orlando, Miami | High | STNL specialist. Recently merged. |
| Boulder Group | Remote (Chicago HQ) | Moderate | Advisory/research. Referral-based. |
| SRS Real Estate Partners | Tampa, Orlando, Miami | Moderate | Growing NNN practice. |
| Capstone Advisors | Jacksonville | Moderate | Regional specialist, strong DG track record. |
| Local independents | County-level | Low-Moderate | Relationship-based. Often list on behalf of long-term holders. |

**Agent-DG advantage:** Speed. Automated BOV generation and direct mail within 48 hours of DOR data refresh vs. weeks of manual research by traditional brokers. The agent does not replace broker judgment -- it generates the first draft and the first touch.

---

## Phase 1 Milestones

| Milestone | Target | Status |
|-----------|--------|--------|
| FL DOR data ingestion (top 10 counties) | Q2 2026 | PLANNED |
| DG store location matching | Q2 2026 | PLANNED |
| Owner entity resolution (SunBiz cross-ref) | Q2 2026 | PLANNED |
| First "I Got A Buyer" mail drop (100 letters) | Q3 2026 | PLANNED |
| First listing appointment from DG owner | Q3 2026 | PLANNED |
| First closed DG transaction (FL) | Q4 2026 | PLANNED |

---

*Last updated: 2026-04-06. Store counts are estimates based on DG corporate filings (FY2025 10-K) and third-party location data. Actual counts will be confirmed during DOR data ingestion.*

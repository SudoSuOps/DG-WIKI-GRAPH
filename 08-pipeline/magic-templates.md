# MAGIC Templates -- Stock Materials for Agent-DG

MAGIC = **M**ail, **A**nalysis, **G**eneration, **I**ntelligence, **C**losure. Five template categories that cover the full DG listing lifecycle from first contact to closing. Every template uses `{{VARIABLE}}` placeholders that Agent-DG populates automatically from the knowledge graph (store data, owner data, lease data, comps, BOV output).

---

## 1. The "I Got A Buyer" Letter (PostGrid Direct Mail)

**Format:** 1 page, printed on letterhead, mailed via USPS First Class in a #10 envelope.
**Delivery:** PostGrid API (automated print + mail).
**Cost:** $1.50/letter (print + postage + envelope).
**API endpoint:** `POST https://api.postgrid.com/print-mail/v1/letters`
**Turnaround:** 3-5 business days from API call to mailbox.

### Letter Text

```
{{BROKER_NAME}}
{{FIRM}}
{{FIRM_ADDRESS}}
{{PHONE}} | {{EMAIL}}
{{FIRM_WEBSITE}}

{{DATE}}

{{OWNER_NAME}}
{{OWNER_ADDRESS}}
{{OWNER_CITY}}, {{OWNER_STATE}} {{OWNER_ZIP}}

RE: Your Dollar General Property at {{PROPERTY_ADDRESS}}

Dear {{OWNER_NAME}},

I am writing because I represent a qualified buyer actively seeking Dollar General
net lease investments in {{PROPERTY_STATE}}, and your property at
{{PROPERTY_ADDRESS}} matches their acquisition criteria.

Here is what I know about your asset:

    Tenant:              Dollar General Corporation (NYSE: DG)
    Property Address:    {{PROPERTY_ADDRESS}}
    Lease Type:          Absolute NNN
    Remaining Term:      {{LEASE_TERM}} years (approx.)
    Indicated Cap Rate:  {{CAP_RATE}}%
    Indicated Value:     ${{INDICATED_VALUE}}

My buyer is prepared to close within 45 days with no financing contingency. This is
not a mass mailing -- I have specifically identified your property based on its
lease profile, location, and market conditions.

If you have considered selling, or if you would simply like a confidential opinion
of value at no cost and no obligation, I would welcome a conversation.

I have closed ${{TRACK_RECORD_VOLUME}} in net lease transactions and specialize
exclusively in Dollar General properties. I understand the asset, the lease, and
the buyer pool.

Please call or text me directly at {{PHONE}}, or reply to {{EMAIL}}.

Respectfully,

{{BROKER_NAME}}
{{TITLE}}
{{FIRM}}
License #{{LICENSE_NUMBER}} | {{LICENSE_STATE}}
```

### PostGrid API Integration

```json
{
  "to": {
    "firstName": "{{OWNER_FIRST}}",
    "lastName": "{{OWNER_LAST}}",
    "companyName": "{{OWNER_ENTITY}}",
    "addressLine1": "{{OWNER_ADDRESS}}",
    "city": "{{OWNER_CITY}}",
    "provinceOrState": "{{OWNER_STATE}}",
    "postalOrZip": "{{OWNER_ZIP}}",
    "country": "US"
  },
  "from": {
    "firstName": "{{BROKER_FIRST}}",
    "lastName": "{{BROKER_LAST}}",
    "companyName": "{{FIRM}}",
    "addressLine1": "{{FIRM_ADDRESS}}",
    "city": "{{FIRM_CITY}}",
    "provinceOrState": "{{FIRM_STATE}}",
    "postalOrZip": "{{FIRM_ZIP}}",
    "country": "US"
  },
  "template": "{{POSTGRID_TEMPLATE_ID}}",
  "mergeVariables": {
    "PROPERTY_ADDRESS": "...",
    "LEASE_TERM": "...",
    "CAP_RATE": "...",
    "INDICATED_VALUE": "...",
    "TRACK_RECORD_VOLUME": "..."
  }
}
```

### Variables Required

| Variable | Source | Example |
|----------|--------|---------|
| `{{OWNER_NAME}}` | DOR data / skip trace | "Magnolia Holdings LLC" |
| `{{OWNER_ADDRESS}}` | DOR OWN_ADDR field | "1234 Oak Street" |
| `{{PROPERTY_ADDRESS}}` | DOR SITUS_ADDR field | "5678 Highway 90, Pensacola, FL 32506" |
| `{{LEASE_TERM}}` | Lease abstract (06-leases) | "12" |
| `{{CAP_RATE}}` | BOV engine (cap-rate-benchmarks.md) | "6.70" |
| `{{INDICATED_VALUE}}` | NOI / cap rate | "1,567,000" |
| `{{BROKER_NAME}}` | Config (00-config) | "John Smith" |
| `{{TRACK_RECORD_VOLUME}}` | Config | "45M" |

---

## 2. The OM -- Offering Memorandum (1 Sheet, Folded, 4 Panels)

**Format:** 1 sheet of 11x17 paper, folded in half to create a 4-panel 8.5x11 booklet. Printed full color, glossy stock.
**Use:** Hand to prospective buyers at meetings, attach to email blasts, include in listing packets.
**Generation:** Agent-DG populates all `{{variables}}` and renders to PDF via template engine.

### Panel 1: Cover (Front)

```
+--------------------------------------------------+
|                                                  |
|              {{PHOTO}}                           |
|     (Street-level exterior photo of store)       |
|                                                  |
|--------------------------------------------------+
|                                                  |
|  DOLLAR GENERAL                                  |
|  {{ADDRESS_LINE_1}}                              |
|  {{CITY}}, {{STATE}} {{ZIP}}                     |
|                                                  |
|  EXCLUSIVELY LISTED AT                           |
|  ${{PRICE}}                                      |
|  {{CAP_RATE}}% CAP RATE                          |
|                                                  |
|  NNN INVESTMENT | CORPORATE GUARANTEE            |
|                                                  |
|  {{FIRM_LOGO}}                                   |
|  {{BROKER_NAME}} | {{PHONE}}                     |
|                                                  |
+--------------------------------------------------+
```

**Variables:**

| Variable | Source | Notes |
|----------|--------|-------|
| `{{PHOTO}}` | Google Street View API or broker-supplied | 1200x800px minimum |
| `{{ADDRESS_LINE_1}}` | Store address | Street address only |
| `{{CITY}}`, `{{STATE}}`, `{{ZIP}}` | Store address | |
| `{{PRICE}}` | BOV output or listing price | Formatted with commas |
| `{{CAP_RATE}}` | BOV engine | To 2 decimal places |

### Panel 2: Inside Left -- Property Details

```
+--------------------------------------------------+
|                                                  |
|  PROPERTY OVERVIEW                               |
|                                                  |
|  {{AERIAL}}                                      |
|  (Aerial/satellite photo with parcel outline)    |
|                                                  |
|  Parcel ID:       {{PARCEL_ID}}                  |
|  Lot Size:        {{LOT_SIZE}} acres             |
|  Building Size:   {{BUILDING_SIZE}} sqft         |
|  Year Built:      {{YEAR_BUILT}}                 |
|  Construction:    {{CONSTRUCTION_TYPE}}          |
|  Parking:         {{PARKING_SPACES}} spaces      |
|  Zoning:          {{ZONING}}                     |
|                                                  |
|  LEASE SUMMARY                                   |
|                                                  |
|  Tenant:          Dollar General Corporation     |
|  Lease Type:      Absolute NNN                   |
|  Lease Start:     {{LEASE_START}}                |
|  Lease End:       {{LEASE_END}}                  |
|  Remaining Term:  {{REMAINING_TERM}} years       |
|  Options:         {{OPTIONS}} (x {{OPTION_YRS}}) |
|  Rent Bumps:      {{BUMPS}}                      |
|  Annual Rent:     ${{ANNUAL_RENT}}               |
|                                                  |
+--------------------------------------------------+
```

**Variables:**

| Variable | Source | Notes |
|----------|--------|-------|
| `{{AERIAL}}` | Google Maps Static API or county GIS | Parcel overlay preferred |
| `{{PARCEL_ID}}` | DOR data | County assessor number |
| `{{LOT_SIZE}}` | DOR LND_SQFOOT / 43,560 | Convert sqft to acres |
| `{{BUILDING_SIZE}}` | DOR TOT_LVG_AREA | Verify against lease |
| `{{LEASE_START}}` | Lease abstract | MM/YYYY format |
| `{{LEASE_END}}` | Lease abstract | MM/YYYY format |
| `{{BUMPS}}` | Lease abstract | e.g., "10% every 5 years" |

### Panel 3: Inside Right -- Financials & Tenant

```
+--------------------------------------------------+
|                                                  |
|  TENANT PROFILE                                  |
|                                                  |
|  {{TENANT_PROFILE}}                              |
|                                                  |
|  Company:         Dollar General Corporation     |
|  Ticker:          NYSE: DG                       |
|  Revenue:         ${{DG_REVENUE}} (FY{{FY}})     |
|  Net Income:      ${{DG_NET_INCOME}}             |
|  Credit Rating:   {{CREDIT_RATING}} (S&P)        |
|  Store Count:     {{DG_STORE_COUNT}}+            |
|  Founded:         1939                            |
|  Headquarters:    Goodlettsville, TN             |
|                                                  |
|  FINANCIAL SUMMARY                               |
|                                                  |
|  Net Operating Income (NOI):                     |
|                                                  |
|  {{RENT_SCHEDULE}}                               |
|                                                  |
|  Year 1-5:    ${{RENT_YR1}}/yr   (${{PSF_1}}/sf)|
|  Year 6-10:   ${{RENT_YR6}}/yr   (${{PSF_6}}/sf)|
|  Year 11-15:  ${{RENT_YR11}}/yr  (${{PSF_11}}/sf)|
|                                                  |
|  Current NOI:     ${{NOI}}/year                  |
|  Cap Rate:        {{CAP_RATE}}%                  |
|  Price:           ${{PRICE}}                     |
|  Price/SF:        ${{PRICE_PSF}}                 |
|                                                  |
+--------------------------------------------------+
```

**Variables:**

| Variable | Source | Notes |
|----------|--------|-------|
| `{{TENANT_PROFILE}}` | Standard DG boilerplate (2-3 sentences) | Updated annually from 10-K |
| `{{CREDIT_RATING}}` | S&P / Moody's | Currently BBB- (S&P) |
| `{{NOI}}` | Annual rent (NNN = rent is NOI) | |
| `{{RENT_SCHEDULE}}` | Lease abstract with bump schedule | Tabular format |
| `{{DG_REVENUE}}` | DG 10-K | e.g., "$38.7B" |
| `{{PRICE_PSF}}` | Price / building sqft | |

### Panel 4: Back Cover -- Broker Contact

```
+--------------------------------------------------+
|                                                  |
|  EXCLUSIVELY LISTED BY                           |
|                                                  |
|  {{BROKER_PHOTO}}                                |
|                                                  |
|  {{BROKER_NAME}}                                 |
|  {{TITLE}}                                       |
|  {{FIRM}}                                        |
|                                                  |
|  {{PHONE}}                                       |
|  {{EMAIL}}                                       |
|  {{FIRM_WEBSITE}}                                |
|                                                  |
|  License #{{LICENSE_NUMBER}}                     |
|  {{LICENSE_STATE}}                               |
|                                                  |
|  TRACK RECORD                                    |
|                                                  |
|  {{TRACK_RECORD}}                                |
|                                                  |
|  Total NNN Volume:    ${{TOTAL_VOLUME}}          |
|  DG Transactions:     {{DG_COUNT}}               |
|  Avg Days on Market:  {{AVG_DOM}} days           |
|  Client Retention:    {{RETENTION}}%             |
|                                                  |
|  {{FIRM_LOGO}}                                   |
|                                                  |
|  This offering is made subject to errors,        |
|  omissions, change of price, prior sale, or      |
|  withdrawal without notice.                      |
|                                                  |
+--------------------------------------------------+
```

**Variables:**

| Variable | Source | Notes |
|----------|--------|-------|
| `{{BROKER_NAME}}` | Config (00-config) | Full legal name |
| `{{FIRM}}` | Config | Brokerage name |
| `{{PHONE}}` | Config | Direct line, not office |
| `{{EMAIL}}` | Config | Professional email |
| `{{TRACK_RECORD}}` | Config | 2-3 sentence summary |
| `{{TOTAL_VOLUME}}` | Config | Lifetime NNN dollar volume |
| `{{DG_COUNT}}` | Config | Number of DG deals closed |

---

## 3. The LOI -- Letter of Intent (1 Page)

**Format:** 1 page. PDF generated from template. Non-binding expression of intent to purchase.
**Use:** Buyer submits to seller/listing broker to initiate negotiation. Agent-DG pre-fills from BOV data so the buyer just reviews and signs.

### LOI Template

```
LETTER OF INTENT

Date:          {{LOI_DATE}}

To:            {{SELLER_NAME}}
               {{SELLER_ADDRESS}}

From:          {{BUYER_NAME}}
               {{BUYER_ADDRESS}}

RE:            {{PROPERTY}}
               {{PROPERTY_ADDRESS}}


Dear {{SELLER_NAME}},

This Letter of Intent sets forth the basic terms under which {{BUYER_NAME}}
("Buyer") proposes to acquire the property described below from {{SELLER_NAME}}
("Seller"). This LOI is non-binding and is intended solely as a basis for
further negotiation and the preparation of a definitive Purchase and Sale
Agreement.


1. PROPERTY:
   {{PROPERTY}}
   {{PROPERTY_ADDRESS}}
   Parcel ID: {{PARCEL_ID}}

2. PURCHASE PRICE:
   ${{PRICE}} ({{PRICE_WORDS}} Dollars)

3. EARNEST MONEY:
   ${{EARNEST_MONEY}} ({{EARNEST_PCT}}% of Purchase Price), deposited with
   {{ESCROW_AGENT}} within {{EARNEST_DAYS}} business days of mutual execution
   of the Purchase and Sale Agreement.

4. DUE DILIGENCE PERIOD:
   {{DUE_DILIGENCE_DAYS}} calendar days from the Effective Date of the PSA.
   Buyer may terminate for any reason during this period and receive a full
   refund of Earnest Money.

5. CLOSING DATE:
   On or before {{CLOSING_DATE}}, or {{CLOSING_DAYS}} calendar days from
   the Effective Date, whichever is later.

6. FINANCING:
   {{FINANCING_TYPE}}
   [ ] All Cash — No Financing Contingency
   [ ] Conventional Financing — {{LTV}}% LTV, {{FINANCING_DAYS}}-day
       contingency period

7. CONTINGENCIES:
   {{CONTINGENCIES}}
   - Satisfactory review of lease and all amendments
   - Satisfactory review of title commitment and survey
   - Satisfactory environmental assessment (Phase I ESA)
   - Estoppel certificate from tenant
   {{ADDITIONAL_CONTINGENCIES}}

8. TITLE AND SURVEY:
   Seller to provide title commitment and existing survey within
   {{TITLE_DAYS}} business days. Buyer to have {{OBJECTION_DAYS}} days
   to review and object.

9. PRORATIONS:
   Rents, taxes, and assessments prorated as of the Closing Date.

10. BROKER:
    {{BROKER_NAME}}, {{FIRM}}
    Commission: Per separate agreement.

11. CONFIDENTIALITY:
    Both parties agree to keep the terms of this LOI confidential.

12. EXPIRATION:
    This LOI expires if not accepted by {{LOI_EXPIRATION_DATE}}.

This Letter of Intent is non-binding and does not create any obligation
on either party. A binding agreement will exist only upon execution of a
mutually acceptable Purchase and Sale Agreement.


_________________________          _________________________
{{BUYER_NAME}}                     {{SELLER_NAME}}
Buyer                              Seller
Date: _______________              Date: _______________
```

### Standard Defaults (Agent-DG Pre-Fill)

| Field | Default Value | Notes |
|-------|--------------|-------|
| `{{EARNEST_MONEY}}` | 1% of purchase price | Industry standard for STNL |
| `{{DUE_DILIGENCE_DAYS}}` | 30 | Standard. Some buyers request 45. |
| `{{CLOSING_DATE}}` | 45 days from PSA execution | Cash buyers. Finance = 60-75 days. |
| `{{FINANCING_TYPE}}` | All Cash | Default for 1031 exchangers. Toggle for financed deals. |
| `{{TITLE_DAYS}}` | 10 | Business days |
| `{{OBJECTION_DAYS}}` | 5 | Business days after receipt |
| `{{LOI_EXPIRATION_DATE}}` | 5 business days from LOI date | Creates urgency |
| `{{CONTINGENCIES}}` | Lease, title, survey, Phase I, estoppel | Standard NNN contingencies |

---

## 4. The Comp Deck Card (Single Comp)

**Format:** 1 card per comparable sale. 5 cards assembled into a comp deck. Sized for screen (16:9) and print (half-letter landscape).
**Use:** Attached to BOVs, OMs, and listing presentations. Tribunal-verified comps only (sourced from 05-comps database).

### Card Layout

```
+--------------------------------------------------+
|                                                  |
|  {{PHOTO}}              COMPARABLE SALE           |
|  (Street view           SOLD {{DATE}}            |
|   of comp)                                       |
|                         {{ADDRESS}}              |
|                         {{CITY}}, {{STATE}} {{ZIP}}|
|                                                  |
|--------------------------------------------------+
|                                                  |
|  SALE PRICE     CAP RATE     NOI                 |
|  ${{PRICE}}     {{CAP}}%     ${{NOI}}/yr         |
|                                                  |
|  BUILDING       LOT          LEASE REMAINING     |
|  {{SQFT}} sqft  {{LOT}} ac   {{LEASE_REMAINING}} yrs |
|                                                  |
|  PRICE/SF       YEAR BUILT   RENT BUMPS          |
|  ${{PSF}}       {{YR_BUILT}} {{BUMPS}}           |
|                                                  |
|--------------------------------------------------+
|                                                  |
|  Buyer:  {{BUYER}}                               |
|  Seller: {{SELLER}}                              |
|  Broker: {{COMP_BROKER}}                         |
|  Source: {{SOURCE}} | Verified: {{VERIFY_DATE}}  |
|                                                  |
+--------------------------------------------------+
```

### Variables

| Variable | Source | Notes |
|----------|--------|-------|
| `{{PHOTO}}` | Google Street View or broker photo | Comp property exterior |
| `{{ADDRESS}}` | Comp database (05-comps) | Full street address |
| `{{DATE}}` | Closing date from deed records | MM/DD/YYYY |
| `{{PRICE}}` | Recorded sale price | Formatted with commas |
| `{{CAP}}` | NOI / sale price | 2 decimal places |
| `{{NOI}}` | Annual rent at time of sale | From lease abstract or listing data |
| `{{LEASE_REMAINING}}` | Years remaining at sale date | Rounded to nearest integer |
| `{{BUYER}}` | Deed records / CoStar | Entity name |
| `{{SELLER}}` | Deed records / CoStar | Entity name |
| `{{SOURCE}}` | Data source | CoStar, Crexi, county records, or broker-confirmed |
| `{{VERIFY_DATE}}` | Date comp was verified | Agent-DG verification timestamp |

### Comp Deck Assembly (5 Cards)

Agent-DG selects 5 comps using this priority:

1. **Same state, same remaining term bracket** (+/- 2 years)
2. **Most recent close date** (last 12 months preferred, 24 months maximum)
3. **Similar building size** (+/- 1,500 sqft)
4. **Diversity of cap rates** (don't cherry-pick -- show the range)
5. **At least 1 new construction and 1 existing** (if available)

The comp deck is rendered as a single PDF with a cover page summarizing the 5 comps in a comparison table, followed by 5 individual cards.

---

## 5. The Proposal Booklet (5 Pages)

**Format:** 5 pages, 8.5x11, portrait. Full color. Saddle-stitched or digital PDF.
**Use:** Delivered to property owner at the listing appointment or mailed after initial phone call. The "pitch book" to win the listing.
**Tone:** Professional, data-driven, confident. No fluff. Show the owner you know their property better than they do.

### Page 1: Cover

```
+--------------------------------------------------+
|                                                  |
|              {{PROPERTY_PHOTO}}                  |
|                                                  |
|  CONFIDENTIAL OFFERING ANALYSIS                  |
|                                                  |
|  DOLLAR GENERAL                                  |
|  {{PROPERTY_ADDRESS}}                            |
|  {{CITY}}, {{STATE}} {{ZIP}}                     |
|                                                  |
|  Prepared Exclusively For:                       |
|  {{OWNER_NAME}}                                  |
|                                                  |
|  {{DATE}}                                        |
|                                                  |
|  {{FIRM_LOGO}}                                   |
|  {{BROKER_NAME}} | {{PHONE}} | {{EMAIL}}         |
|                                                  |
+--------------------------------------------------+
```

### Page 2: Your Property

A one-page summary of everything Agent-DG knows about the owner's property. The goal is to demonstrate expertise and accuracy. If the owner reads this and says "that's exactly right," you win the listing.

```
+--------------------------------------------------+
|                                                  |
|  YOUR PROPERTY AT A GLANCE                       |
|                                                  |
|  {{AERIAL_PHOTO}}                                |
|                                                  |
|  Address:         {{PROPERTY_ADDRESS}}           |
|  Parcel ID:       {{PARCEL_ID}}                  |
|  Lot Size:        {{LOT_SIZE}} acres             |
|  Building Size:   {{BUILDING_SIZE}} sqft         |
|  Year Built:      {{YEAR_BUILT}}                 |
|  Assessed Value:  ${{ASSESSED_VALUE}} ({{TAX_YEAR}})|
|  Annual Taxes:    ${{ANNUAL_TAXES}}              |
|                                                  |
|  LEASE DETAILS                                   |
|                                                  |
|  Tenant:          Dollar General Corporation     |
|  Lease Start:     {{LEASE_START}}                |
|  Lease End:       {{LEASE_END}}                  |
|  Remaining Term:  {{REMAINING_TERM}} years       |
|  Annual Rent:     ${{ANNUAL_RENT}}               |
|  Rent Bumps:      {{BUMPS}}                      |
|  Options:         {{OPTIONS}}                    |
|  Lease Type:      Absolute NNN                   |
|                                                  |
|  YOUR NET OPERATING INCOME                       |
|                                                  |
|  Annual Rent:     ${{ANNUAL_RENT}}               |
|  Taxes:           ($0 — tenant pays)             |
|  Insurance:       ($0 — tenant pays)             |
|  Maintenance:     ($0 — tenant pays)             |
|  ───────────────────────────────                 |
|  NOI:             ${{NOI}}/year                  |
|                                                  |
+--------------------------------------------------+
```

### Page 3: Our Valuation

The BOV. Show the math. Three approaches to value to build credibility.

```
+--------------------------------------------------+
|                                                  |
|  BROKER OPINION OF VALUE                         |
|                                                  |
|  APPROACH 1: INCOME (CAP RATE)                   |
|                                                  |
|  NOI:                    ${{NOI}}                |
|  Market Cap Rate:        {{CAP_RATE}}%           |
|  Indicated Value:        ${{VALUE_INCOME}}       |
|                                                  |
|  Cap rate derived from {{CAP_RATE_SOURCE}}       |
|  ({{REMAINING_TERM}} yr remaining, {{STATE}})    |
|                                                  |
|  APPROACH 2: COMPARABLE SALES                    |
|                                                  |
|  {{COMP_1_ADDRESS}} — ${{COMP_1_PRICE}} ({{COMP_1_CAP}}%) |
|  {{COMP_2_ADDRESS}} — ${{COMP_2_PRICE}} ({{COMP_2_CAP}}%) |
|  {{COMP_3_ADDRESS}} — ${{COMP_3_PRICE}} ({{COMP_3_CAP}}%) |
|  {{COMP_4_ADDRESS}} — ${{COMP_4_PRICE}} ({{COMP_4_CAP}}%) |
|  {{COMP_5_ADDRESS}} — ${{COMP_5_PRICE}} ({{COMP_5_CAP}}%) |
|                                                  |
|  Avg Comp Cap Rate:      {{AVG_COMP_CAP}}%       |
|  Indicated Value:        ${{VALUE_COMPS}}        |
|                                                  |
|  APPROACH 3: PRICE PER SQUARE FOOT               |
|                                                  |
|  Building Size:          {{BUILDING_SIZE}} sqft  |
|  Market PSF Range:       ${{PSF_LOW}}-${{PSF_HIGH}}|
|  Applied PSF:            ${{APPLIED_PSF}}        |
|  Indicated Value:        ${{VALUE_PSF}}          |
|                                                  |
|  ═══════════════════════════════                 |
|  RECONCILED VALUE:       ${{RECONCILED_VALUE}}   |
|  RECOMMENDED LIST PRICE: ${{LIST_PRICE}}         |
|  ═══════════════════════════════                 |
|                                                  |
+--------------------------------------------------+
```

### Page 4: Market Comps

Full comp deck (condensed). 5 comparable sales with photos, cap rates, and sale prices. Draws from the Comp Deck cards (template #4 above) but formatted as a single page with a comparison table.

```
+--------------------------------------------------+
|                                                  |
|  COMPARABLE SALES — DOLLAR GENERAL               |
|  {{STATE}} | Last 24 Months                      |
|                                                  |
|  # | Address        | Sold    | Price     | Cap  | NOI      | Term |
|  1 | {{C1_ADDR}}    | {{C1_D}}| ${{C1_P}} | {{C1_C}}% | ${{C1_N}}| {{C1_T}} |
|  2 | {{C2_ADDR}}    | {{C2_D}}| ${{C2_P}} | {{C2_C}}% | ${{C2_N}}| {{C2_T}} |
|  3 | {{C3_ADDR}}    | {{C3_D}}| ${{C3_P}} | {{C3_C}}% | ${{C3_N}}| {{C3_T}} |
|  4 | {{C4_ADDR}}    | {{C4_D}}| ${{C4_P}} | {{C4_C}}% | ${{C4_N}}| {{C4_T}} |
|  5 | {{C5_ADDR}}    | {{C5_D}}| ${{C5_P}} | {{C5_C}}% | ${{C5_N}}| {{C5_T}} |
|                                                  |
|  Avg Sale Price:     ${{AVG_PRICE}}              |
|  Avg Cap Rate:       {{AVG_CAP}}%                |
|  Avg Price/SF:       ${{AVG_PSF}}                |
|                                                  |
|  Source: County deed records, CoStar, broker     |
|  network. All comps verified.                    |
|                                                  |
+--------------------------------------------------+
```

### Page 5: Marketing Plan & About Us

Explain what the broker will do to sell the property. Then close with credentials.

```
+--------------------------------------------------+
|                                                  |
|  OUR MARKETING PLAN FOR YOUR PROPERTY            |
|                                                  |
|  WEEK 1-2: PREPARATION                           |
|  - Professional photography and drone aerial     |
|  - Full offering memorandum (4-panel OM)         |
|  - Title and lease review                        |
|  - Estoppel certificate request to DG            |
|                                                  |
|  WEEK 2-4: MARKET LAUNCH                         |
|  - Listed on CoStar, Crexi, LoopNet, CREXi      |
|  - Direct email blast to {{BUYER_DB_COUNT}}+     |
|    pre-qualified NNN buyers                      |
|  - Targeted outreach to 1031 exchange            |
|    accommodators and estate planners             |
|  - Featured in weekly NNN investment digest      |
|                                                  |
|  WEEK 4-8: OFFERS & NEGOTIATION                  |
|  - Best-and-final offer process (if multiple)    |
|  - LOI negotiation and PSA execution             |
|  - Buyer qualification and proof of funds        |
|                                                  |
|  WEEK 8-12: DUE DILIGENCE & CLOSING             |
|  - Coordinate estoppel, SNDA, title, survey      |
|  - Manage due diligence timeline                 |
|  - Close with {{TITLE_COMPANY}}                  |
|                                                  |
|  Target: Under contract in 30 days.              |
|  Target: Closed in 60-90 days.                   |
|                                                  |
|  ─────────────────────────────────               |
|                                                  |
|  ABOUT {{BROKER_NAME}}                           |
|                                                  |
|  {{BROKER_BIO}}                                  |
|                                                  |
|  {{BROKER_PHOTO}}                                |
|                                                  |
|  Specialization: Dollar General NNN              |
|  Total Volume:   ${{TOTAL_VOLUME}}               |
|  DG Deals:       {{DG_COUNT}} closed             |
|  Markets:        {{MARKETS}}                     |
|                                                  |
|  {{FIRM}}                                        |
|  {{FIRM_ADDRESS}}                                |
|  {{PHONE}} | {{EMAIL}}                           |
|  {{FIRM_WEBSITE}}                                |
|                                                  |
|  {{FIRM_LOGO}}                                   |
|                                                  |
+--------------------------------------------------+
```

---

## Template Rendering Pipeline

All 5 templates follow the same rendering flow inside Agent-DG:

```
Knowledge Graph (stores, owners, leases, comps)
        │
        ▼
    BOV Engine (cap-rate-benchmarks.md lookups)
        │
        ▼
    Variable Assembly (merge all {{variables}} into dict)
        │
        ▼
    Template Engine (Jinja2 or equivalent)
        │
        ▼
    PDF Renderer (WeasyPrint or Puppeteer)
        │
        ▼
    Output: PDF file per template
        │
        ├──▶ PostGrid API (letters only)
        ├──▶ Email attachment (OM, LOI, comp deck, proposal)
        └──▶ Print queue (proposal booklet)
```

---

## Variable Master List

Complete list of all unique variables across all 5 templates:

| Category | Variables |
|----------|----------|
| **Property** | `PROPERTY_ADDRESS`, `ADDRESS_LINE_1`, `CITY`, `STATE`, `ZIP`, `PARCEL_ID`, `LOT_SIZE`, `BUILDING_SIZE`, `YEAR_BUILT`, `CONSTRUCTION_TYPE`, `PARKING_SPACES`, `ZONING`, `ASSESSED_VALUE`, `ANNUAL_TAXES`, `TAX_YEAR` |
| **Lease** | `LEASE_START`, `LEASE_END`, `REMAINING_TERM`, `LEASE_TERM`, `ANNUAL_RENT`, `BUMPS`, `OPTIONS`, `OPTION_YRS`, `RENT_YR1`, `RENT_YR6`, `RENT_YR11`, `PSF_1`, `PSF_6`, `PSF_11` |
| **Financials** | `NOI`, `CAP_RATE`, `PRICE`, `INDICATED_VALUE`, `LIST_PRICE`, `RECONCILED_VALUE`, `VALUE_INCOME`, `VALUE_COMPS`, `VALUE_PSF`, `PRICE_PSF`, `APPLIED_PSF`, `PSF_LOW`, `PSF_HIGH`, `EARNEST_MONEY`, `EARNEST_PCT` |
| **Owner** | `OWNER_NAME`, `OWNER_FIRST`, `OWNER_LAST`, `OWNER_ENTITY`, `OWNER_ADDRESS`, `OWNER_CITY`, `OWNER_STATE`, `OWNER_ZIP` |
| **Tenant** | `TENANT_PROFILE`, `CREDIT_RATING`, `DG_REVENUE`, `DG_NET_INCOME`, `DG_STORE_COUNT`, `FY` |
| **Broker** | `BROKER_NAME`, `BROKER_FIRST`, `BROKER_LAST`, `BROKER_PHOTO`, `BROKER_BIO`, `TITLE`, `FIRM`, `FIRM_LOGO`, `FIRM_ADDRESS`, `FIRM_CITY`, `FIRM_STATE`, `FIRM_ZIP`, `FIRM_WEBSITE`, `PHONE`, `EMAIL`, `LICENSE_NUMBER`, `LICENSE_STATE`, `TRACK_RECORD`, `TRACK_RECORD_VOLUME`, `TOTAL_VOLUME`, `DG_COUNT`, `AVG_DOM`, `RETENTION`, `MARKETS`, `BUYER_DB_COUNT`, `TITLE_COMPANY` |
| **Comps** | `COMP_[1-5]_ADDRESS`, `COMP_[1-5]_PRICE`, `COMP_[1-5]_CAP`, `BUYER`, `SELLER`, `COMP_BROKER`, `SOURCE`, `VERIFY_DATE`, `AVG_COMP_CAP`, `AVG_PRICE`, `AVG_CAP`, `AVG_PSF` |
| **LOI** | `LOI_DATE`, `BUYER_NAME`, `BUYER_ADDRESS`, `SELLER_NAME`, `SELLER_ADDRESS`, `ESCROW_AGENT`, `CLOSING_DATE`, `CLOSING_DAYS`, `DUE_DILIGENCE_DAYS`, `EARNEST_DAYS`, `FINANCING_TYPE`, `LTV`, `FINANCING_DAYS`, `CONTINGENCIES`, `ADDITIONAL_CONTINGENCIES`, `TITLE_DAYS`, `OBJECTION_DAYS`, `LOI_EXPIRATION_DATE`, `PRICE_WORDS` |
| **Media** | `PHOTO`, `AERIAL`, `PROPERTY_PHOTO`, `AERIAL_PHOTO` |
| **PostGrid** | `POSTGRID_TEMPLATE_ID`, `DATE` |

---

*Last updated: 2026-04-06. Templates are living documents -- update variable lists as the knowledge graph schema evolves.*

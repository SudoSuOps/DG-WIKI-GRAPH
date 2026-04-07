# DG Graph Schema — 17 Fields Per Parcel

| Field | Source | Notes |
|-------|--------|-------|
| store_address | DG locator / OSM | physical location |
| lat | geocode | spatial match to parcel |
| lon | geocode | spatial match to parcel |
| parcel_id | FL DOR / Regrid | ties to tax roll |
| county | FL DOR / Regrid | 67 FL counties |
| owner_name_raw | tax roll / ATTOM | as-filed owner name |
| owner_mailing_address | tax roll / ATTOM | where tax bills go |
| ownership_source | pipeline | "FL_DOR" / "ATTOM" / "Regrid" |
| entity_match_name | Sunbiz | normalized entity name |
| entity_jurisdiction | Sunbiz / OpenCorp | FL, DE, etc. |
| sunbiz_doc_number | Sunbiz | unique FL filing ID |
| registered_agent | Sunbiz | legal contact |
| registered_agent_address | Sunbiz | agent office |
| officers_managers | Sunbiz | decision makers (JSON array) |
| parent_entity | OpenCorp / SEC EDGAR | ultimate parent |
| confidence_score | pipeline | 0.0-1.0 match quality |
| last_verified_at | pipeline | timestamp |

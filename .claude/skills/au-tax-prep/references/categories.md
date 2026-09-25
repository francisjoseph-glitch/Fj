# Category field checklists

For each in-scope category, capture these fields per ledger line. A missing field = blank cell + entry in Questions & Flags. Each category also lists its **Expected documents** — used by the completeness check (Workflow step 3): report anything expected-but-absent to the user before building. Categories not listed here can be added following the same pattern (date, description, amount, source ID, flags).

## Residential / investment property (per property — one section or tab per property)

**Expected documents**: property manager annual summary (or 12 monthly statements), loan interest statement per loan, council rates notices, water bills, insurance policy/renewal, body corporate levies (if strata), land tax assessment (if applicable), depreciation/quantity surveyor schedule, repair & maintenance invoices, loan documents for any new borrowing.

**Income**: rent received (per statement period), other income (e.g. insurance payouts, bond retained).
Fields: period, source (agent statement / bank), gross rent, agent fees deducted on statement, net received, Source ID.

**Expenses** — itemise under standard ATO rental schedule headings so the accountant can map directly:
advertising, body corporate, borrowing expenses, cleaning, council rates, capital works/depreciation (from quantity surveyor schedule — transcribe the schedule's annual figures, do not derive your own), gardening, insurance, interest on loan, land tax, legal expenses, pest control, property agent fees, repairs & maintenance, stationery/phone/postage, travel (note: generally not deductible for residential rental since 2017 — flag if present), water charges, sundry.
Fields per line: date, supplier, description, amount (GST-inclusive), category heading, Source ID.

**Apportionment triggers**: private-use periods, part-year rental, below-market rent to relatives, mixed-purpose or redrawn loans — collect the income-use percentage and basis via the apportionment gate; record in Apportionment Summary.

**Flags to raise**: repairs vs capital improvement ambiguity (e.g. "replaced entire fence" vs "fixed fence panel"), expenses dated during personal use periods, borrowing costs >$100 (spread over 5 years — Carry-forward tab, accountant to handle), interest statements mixing multiple loan purposes.

## Shares / ETFs

**Expected documents**: dividend statements for every holding (incl. DRP notices), annual tax statement (AMMA/AMIT) for every ETF/trust, buy and sell contract notes for every disposal, margin/investment loan interest statement if geared, prior-year capital loss figure (from prior-year pack).

**Dividends & distributions**: payment date, holding, unfranked amount, franked amount, franking credits, TFN withholding if any, DRP participation (note shares issued in lieu), Source ID. For ETF/trust annual tax statements (AMMA/AMIT), transcribe each labelled component exactly as printed (e.g. 13U, 13C, 18A capital gains components, foreign income, AMIT cost base net amounts) — these labels are what the accountant keys in.

**CGT events (disposals)**: holding, quantity sold, sale date, gross proceeds, brokerage on sale, acquisition date(s), acquisition cost incl. brokerage, whether held >12 months (list the dates; do not apply the discount yourself), parcel-matching method if broker report states one, Source ID. If acquisition records are missing, flag it — cost base gaps are a top accountant question. Maintain acquisitions still held in the cost-base register (Carry-forward tab) for future years.

## Digital assets (crypto)

**Expected documents**: transaction history export per exchange/wallet or a crypto tax tool report, records of AUD valuations used, prior-year capital loss figure.

Each disposal is a CGT event — including crypto-to-crypto swaps, spending crypto, and converting to fiat. Fields: asset, quantity, disposal date, AUD value at disposal (state the source of the AUD valuation), acquisition date, AUD cost base, exchange/wallet, fees, Source ID. Staking/airdrop/interest receipts: date, asset, quantity, AUD value at receipt, Source ID (these are ordinary income at receipt — list them separately from CGT events). If the user provides a tax report from a crypto tax tool (Koinly, CryptoTaxCalculator etc.), transcribe its summary figures and attach the detail as a source rather than re-deriving thousands of rows.

## Commodities (gold, silver, etc.)

**Expected documents**: dealer invoices for both purchase and sale of every item disposed of; storage/insurance invoices if held for investment.

Treated as CGT assets. Same fields as share disposals: item, purchase date/cost, sale date/proceeds, dealer invoices as sources. Flag personal-use-asset questions (<$10,000 acquisitions) for the accountant rather than deciding.

## PAYG income

**Expected documents**: income statement (myGov) or payment summary per employer, bank interest summary per account.

Per employer: employer name, ABN if shown, gross payments, tax withheld, reportable fringe benefits, reportable super contributions, lump sums, from the income statement (myGov) or payment summary. Also list: bank interest per account (bank, gross interest, TFN withholding), other income. Note that income statements are usually pre-filled at the ATO — the ledger is for cross-checking, say so in the notes.

## Work-related expenses

**Expected documents**: receipts/invoices for claimed items, WFH hours record (diary/timesheet) if claiming WFH, car logbook or km record if claiming car, notice-of-intent acknowledgment if claiming personal super contributions.

Fields: date, supplier, description, amount, work-use percentage **as stated by the user via the apportionment gate** (never assume one; record the basis), category (D1–D5 style: car, travel, clothing/laundry, self-education, other), Source ID.
- **Car**: method (cents-per-km or logbook) as chosen by user; for cents-per-km record the km claimed and the trip purpose basis; for logbook, transcribe the logbook percentage and itemised costs.
- **Working from home**: method (fixed rate per hour or actual cost) as chosen by user. Fixed rate: total hours from the user's record (diary/timesheet — note what the record is), multiplied by the current ATO rate (verified per Workflow step 2); list separately any depreciating assets claimed on top. Actual cost: itemised running expenses with work-use basis. If the user has no hours record, flag it — do not estimate hours.
- Items over $300 (depreciating assets): list cost, date, expected work percentage; flag for depreciation treatment rather than expensing.

## Travel-related deductions

Date, destination, purpose, connection to income-earning (as stated by user), transport/accommodation/meals amounts, whether an employer allowance was received (flag if yes — affects substantiation), travel diary existence for trips ≥6 nights (flag if absent), work-related percentage for mixed business/private trips (via apportionment gate), Source ID.

## Sole trader (business schedule — part of the individual return, kept as its own tab group)

**Expected documents**: invoices issued (or sales report), business bank/card statements, expense receipts, asset purchase invoices, vehicle logbook if used for business, prior-year depreciation schedule, insurance policies, super contribution receipts + notice of intent.

**Income**: invoice/sale date, customer (or "various" for point-of-sale summaries), description, amount, GST component if registered, Source ID. Note the user's ABN and whether GST-registered — if registered, record amounts GST-exclusive and note that BAS figures are the accountant's cross-check; if not registered, GST-inclusive.

**Expenses** — itemise under plain business headings: advertising, accounting/bookkeeping, bank fees, contractor/subcontractor payments (note ABNs), home office running costs (business-use % via apportionment gate; occupancy costs raise CGT questions — flag), insurance (public liability, professional indemnity, income protection), materials/stock, motor vehicle (method + business % via apportionment gate), phone/internet (business % via apportionment gate), rent of business premises, software/subscriptions, travel, sundry.
Fields per line: date, supplier, description, amount, heading, business-use %, Source ID.

**Depreciating assets**: cost, purchase date, description, expected business-use % — flag instant-asset-write-off eligibility against the threshold verified in Workflow step 2; the accountant decides treatment.

**Flags to raise, never decide**: PSI (personal services income) indicators — e.g. most income from one client for personal effort/skills; cash vs accruals basis; unpaid invoices at 30 June; stock on hand valuation; private use of business assets.

## Carry-forward items (feeds the Carry-forward tab)

Collect from the prior-year pack/return and current-year documents:

- **Capital losses carried forward**: amount, origin FY, asset class if stated, source (prior return label). Do not net against current-year gains — the accountant applies losses.
- **Borrowing expenses being spread** (5-year): loan, original amount, start date, amount previously claimed if shown, Source ID.
- **Depreciation schedules**: transcribe this year's figures; note the schedule's remaining life so next year's pack picks it up.
- **CGT cost-base register**: for share/crypto/commodity parcels still held — asset, quantity, acquisition date, cost incl. fees, Source ID. This is what prevents next year's "missing cost base" flags.
- Anything else the prior return shows as carried forward (e.g. non-commercial business losses) — transcribe and flag for the accountant.

## SMSF (fund-level pack — separate workbook)

**Expected documents**: fund bank statements, member contribution statements, dividend/distribution statements, rental statements if fund holds property, insurance policy documents, 30 June asset valuations, actuarial certificate if part-pension, prior-year financials, accounting/audit/ASIC invoices.

Income: contributions per member (concessional/non-concessional as labelled by source documents — flag unlabelled ones), rent, interest, dividends with franking credits, distributions, CGT events (same fields as above).
Expenses: accounting/audit fees, ASIC/supervisory levy, insurance premiums (note policy type), investment expenses, property expenses if fund holds property, bank fees.
Records: member statements, bank statements, actuarial certificate if in pension phase (flag if fund is part-pension and no certificate provided), asset valuations at 30 June (flag missing valuations).
Flag, never decide: contribution cap questions, related-party transactions, in-house assets, non-arm's-length income indicators.

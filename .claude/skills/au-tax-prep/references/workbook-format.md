# Workbook format specification

One workbook per entity per financial year. Filename: `FY<YYYY-YY>_<Individual|SMSF>_TaxPack_<Name>.xlsx`. Build with the xlsx skill. Professional, restrained formatting: bold headers, frozen header rows, currency formatting ($#,##0.00), autofilter on ledger tabs, column widths sized to content. No decorative colour beyond a single header fill. Never include a Tax File Number anywhere in the workbook or brief.

## Tab order

### 1. Summary
- Header block: taxpayer/fund name, entity type, financial year, date prepared, preparer note ("Prepared with AI assistance for review by registered tax agent — not tax advice, not a tax calculation").
- Category totals table: one row per in-scope category → total income items ($), total expense/deduction items ($), item count, open questions count. Totals link by formula to the category tabs (use SUM references, not hard-coded numbers, so accountant edits flow through).
- Prominent pointer line: "Work/income-use percentages for mixed-use items are listed on the Apportionment Summary tab — to be applied by the tax agent in the final calculation."
- Notes: ATO rates verified (with rate, source URL, date checked), ATO compliance focus areas relevant to this pack, method choices the user made (e.g. WFH fixed rate, car method), expected documents not provided, anything excluded and why.

### 2. Apportionment Summary
The single place the accountant looks to see every percentage that must be applied in the final calculation. One row per mixed-use item or item group:

Columns: Ref #, Category, Item / description, Full amount ($, as transcribed), Work/income-use % (user-stated; blank if unresolved), Basis of % (e.g. "4-week diary", "12-week logbook", "user estimate — no record"), Substantiation record held (Y/N + type), Affected ledger lines (tab + line refs), Flag.

Rules:
- Percentages appear here exactly as the user stated them via the apportionment gate — never derived or defaulted. A blank % row must carry a flag and a matching Questions & Flags entry.
- Do not compute the apportioned amount — the accountant applies the percentage. (A reference-only column "Indicative amount at stated %" may be included if the user asks, clearly labelled indicative.)
- Header note on the tab: "Percentages below were stated by the taxpayer. To be reviewed and applied by the registered tax agent in the final tax calculation."

### 3..n Category tabs (one per in-scope category)
- Standard ledger columns: Line #, Date, Payer/Supplier, Description, Amount, Sub-category, Work/Income-use %, Source ID, Flag.
- Adapt columns per category using references/categories.md (e.g. dividends tab has franked/unfranked/franking-credit columns; CGT tab has acquisition and disposal column groups; sole trader income tab has a GST column if registered).
- Sort by date within tab. Subtotal rows per sub-category where useful, grand total row at bottom (formulas).
- Property: one tab per property if multiple, or one tab with a Property column if the user prefers.
- Sole trader: separate Income and Expenses tabs (or sections) so business items never mingle with employee work-related expenses.
- Flag column values: blank, `DUPLICATE?`, `OUT-OF-PERIOD`, `MISSING-DATA`, `APPORTION?` (mixed use, percentage unresolved), `ACCOUNTANT-Q` — each flagged row must have a matching entry in Questions & Flags.

### n+1. Carry-forward (include when any such items exist)
Items that span financial years, collected per references/categories.md:

Columns: Ref #, Type (capital loss c/f, borrowing expense spread, depreciation schedule, CGT cost base — parcel held, other), Asset/loan/item, Origin FY, Amount / opening balance ($), Detail (e.g. remaining years of spread, quantity held), Source ID, Flag.

Note on tab: "Transcribed from prior-year return/pack and current-year documents. The tax agent applies these; next year's pack should start from this tab."

### n+2. Questions & Flags
Columns: Ref #, Category, Ledger line ref, Issue description, What's needed to resolve, Status (Open/Resolved), Resolution note. This is the accountant's punch list — write issues in plain language ("Invoice S014 dated 28 June but paid 3 July — confirm which FY basis to use"). Include unresolved apportionment percentages and expected documents not provided. Deduction-discovery groups the user answered "none" to are NOT listed here (they go in Summary notes) — only genuine open items.

### n+3. Source Register
Columns: Source ID, Filename, Document type, Issuer, Document date, Category fed, Duplicate-of (if applicable), Notes. Every input file appears here exactly once, including unreadable or unclassified files (noted as such).

## Cover brief

Alongside the workbook, produce a one-page brief (markdown or docx per user preference) the user can email their accountant: entity and FY, categories covered with item counts and totals, **the apportionment summary table (or its headline items) with the note that percentages are taxpayer-stated and to be applied by the agent**, carry-forward items included, expected documents not provided, list of open questions, list of source documents provided, and the preparer disclaimer.

---
name: au-tax-prep
description: Prepare Australian tax return support packs (organised ledgers, summaries, and an accountant-ready Excel workbook) for individual, sole trader, and SMSF tax returns. Use whenever the user mentions preparing for their Australian tax return, EOFY / end of financial year prep, organising tax documents, ATO deductions, tax ledgers, an "accountant pack", work-use or private-use percentages / apportionment of expenses, sole trader or ABN income, carry-forward capital losses, or asks to summarise property, shares/ETF, dividend, crypto, commodity, PAYG income, work-from-home, or work-related expense records for a financial year — even if they only mention one category (e.g. "summarise my property expenses for FY26"), and even if they just ask HOW to get started organising documents for their Australian tax return. Also use for SMSF annual return preparation support.
---

# Australian Tax Return Preparation Assistant

You act as an experienced Australian senior tax accountant's preparer. Your job is to take a user's raw tax documents (invoices, statements, schedules, logs) and produce an organised, traceable, accountant-ready summary pack for one Australian financial year (1 July – 30 June). The pack is given to a human registered tax agent who validates and lodges the return.

**You are a preparer, not an adviser or lodger.** You itemise, categorise, total, and flag. You do not calculate tax payable, apply marginal rates or SMSF tax rates, determine deductibility in contested cases, or give tax advice. Where deductibility or treatment is uncertain, list the item and flag it as a question for the accountant.

## Workflow

Follow these steps in order. Do not skip the scoping, apportionment, and planning steps.

### 0. Onboard first-time users

If the user hasn't yet provided documents, or asks how to use this / how to get started, show them the short guide in `references/quick-start.md` (reproduce its user-facing section verbatim) before doing anything else. It tells them how to organise documents into category folders, connect them, and what to type. Skip this step when the user has clearly already set up — files attached or a folder connected, and scope stated.

### 1. Scope the engagement

Before touching any documents, confirm with the user:

1. **Entity**: individual tax return, sole trader (part of the individual return but a distinct schedule — see `references/categories.md`), SMSF annual return, or a combination (individual and SMSF kept strictly separate — never mix them in one ledger).
2. **Financial year**: e.g. FY2025–26 = 1 July 2025 – 30 June 2026. All items must fall in this window; anything outside it gets flagged, not silently included or excluded.
3. **Categories in scope**: full pack, or a subset (property only, shares only, etc.).
4. **Occupation / investor profile**: what they do for work (e.g. engineer, manager) and what they invest in. This drives the deduction-discovery step below.
5. **Prior-year pack**: ask whether they have last year's accountant pack or return — it supplies carry-forward items (capital losses, borrowing-expense spreads, depreciation schedules, CGT cost bases). If provided, treat it as a source document.
6. **Where the inputs are**: attached files, a folder, or both.

If the user has already stated some of these in their request, don't re-ask — confirm only what's missing.

### 2. Verify current-year ATO settings

Use web search to confirm the ATO figures that change year to year and are relevant to the categories in scope, e.g. the fixed-rate work-from-home cents-per-hour rate, the cents-per-km motor vehicle rate, the instant asset write-off threshold (sole traders), and any record-keeping requirements that apply. Also check the ATO's published compliance focus areas for the year (e.g. rental interest apportionment, WFH records, crypto disposals) so relevant items can be flagged as likely to attract scrutiny. Cite the ATO source in the workbook's Notes. Never rely on memorised rates — they change most years.

### 3. Inventory and read the inputs

- List every file provided. Read each one (see the file-reading skill for formats).
- Build a **source register**: assign each document a Source ID (S001, S002 …) recording filename, document type, issuer, date, and which category it feeds.
- **Duplicate check**: compare documents by issuer + date + amount + invoice number. Where two files appear to be the same document (e.g. an emailed PDF and a scanned copy), include it once and note the duplicate in the register. If unsure whether two similar items are duplicates or genuinely separate transactions, ask the user — never guess.
- **Date check**: flag any item dated outside the confirmed financial year.
- **Completeness check**: compare what was provided against the "Expected documents" list for each in-scope category in `references/categories.md`. Report missing documents to the user before building — a rental pack without a loan interest statement, or a share pack without buy contract notes, is a common and costly gap.

### 4. Deduction discovery

Using the occupation/investor profile from step 1, run the short checklist interview in `references/deduction-checklists.md` for the matching personas. The purpose is to surface documents the user forgot they had (professional memberships, income protection insurance, donations, subscriptions, financial advice fees, etc.) — not to advise on deductibility, which stays with the accountant. Ask once, as a compact grouped list; note "user confirmed none" for empty groups so the accountant knows the question was asked.

### 5. Apportionment clarification gate — do not build without this

Many expenses have mixed personal and work/income use: phone and internet, home-office running costs, car, travel, self-education, devices and equipment, a rental property with private-use periods, a loan drawn for mixed purposes. Percentages materially change the return, so they must come from the user, never from you.

- After inventorying, list every item or group with potential mixed use.
- For each, check whether the user has **already** stated a percentage (in this conversation, in their files — e.g. a logbook or diary — or in the prior-year pack as a reference point). Don't re-ask what's already answered.
- For everything unresolved, **stop and ask in one consolidated set of questions** — not item-by-item drip. For each percentage collected, also record the **basis** ("4-week diary", "12-week logbook", "estimate — no record") and whether a substantiation record exists.
- If the user cannot or will not give a percentage, record the full amount, leave the percentage blank, and raise a flag — never assume, default, or copy a "typical" percentage.

Every percentage collected here flows to the **Apportionment Summary** tab of the workbook (see `references/workbook-format.md`), so the accountant can see and apply them in the final calculation.

### 6. Present the plan, then wait

Before producing anything, tell the user in plain terms: which categories you found data for, roughly how many items per category, what the workbook will contain, any documents you couldn't read or classify, any expected documents missing, any duplicates or out-of-period items found, and the apportionment percentages you'll be recording. Ask them to confirm or correct before you build the workbook. If discrepancies or ambiguities exist, stop and resolve them with the user first.

### 7. Build the workbook

Read `references/workbook-format.md` for the exact Excel structure, and `references/categories.md` for the fields required per category. Use the xlsx skill to build the file. Key principles:

- One workbook per entity per financial year, named like `FY2025-26_Individual_TaxPack_<Name>.xlsx`.
- Summary tab first, then Apportionment Summary, then one tab per in-scope category, then Carry-forward (if any such items exist), then Questions & Flags, then Source Register.
- Every ledger line carries its Source ID so the accountant can trace it to a document.
- Totals per category are simple sums of listed amounts — no tax computation.
- Never invent, estimate, or "reasonably assume" a figure. Missing data becomes a blank cell plus a row in Questions & Flags.

### 8. Validate before delivering

Before presenting the workbook, self-check: every source document appears in the register; every ledger line traces to a source; category totals recompute correctly; no item appears twice; all flagged items appear in Questions & Flags; dates all fall in the FY (or are flagged); every mixed-use item appears in the Apportionment Summary with either a user-stated percentage or an open flag; no TFN appears anywhere in the workbook. Tell the user what you checked. Then deliver the workbook and a short cover brief the user can forward to their accountant (entity, FY, categories covered, item counts, apportionment summary, missing documents, open questions).

## Guardrails (always apply)

- Never mix individual and SMSF records in one ledger or workbook.
- Never alter, round, or "correct" an amount from a source document. Transcribe exactly.
- Never assume, default, or estimate a work-use / income-use percentage. Percentages come from the user with a stated basis, or the item is flagged (step 5).
- Never decide contested deductibility — flag it. E.g. repairs vs capital improvement, personal-use-asset questions, PSI classification for sole traders.
- Never transcribe a Tax File Number into the workbook or brief. If a source document shows a TFN, record the document normally but mask the number (e.g. `TFN on file — not transcribed`).
- If the user asks you to calculate their tax refund/payable, decline that part: explain it's for their registered tax agent, and offer the organised ledger instead.
- Deduction discovery (step 4) surfaces documents; it never asserts that an item *is* deductible.
- SMSF work is compliance-sensitive: for SMSF packs, keep to organising fund income, expenses, contributions, and member/asset records; flag anything touching contribution caps, pension standards, or in-house asset questions for the accountant/auditor.
- Escalate every ambiguity to the user and wait for instructions before proceeding.

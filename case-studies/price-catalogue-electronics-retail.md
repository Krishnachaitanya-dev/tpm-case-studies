# From one client meeting to a 3,104-product price catalogue

How I turned a recorded conversation with an electronics retailer into a tested, live pricing system.

| 3,104 | 37 | 22 | 237 |
|---|---|---|---|
| products | brands | live acceptance checks | automated tests |

- **Client:** an electronics retail chain in Odisha
- **My role:** Technical Project Manager and developer (freelance)
- **Timeline:** August to November 2026

## The problem, and how the brief changed

**The original brief (August 2026).** The head office received distributor price sheets by email, one brand at a time and in different formats: Excel, binary Excel, and sometimes a table pasted into the email itself. Prices were updated by hand. The first version of the system read these emails automatically and extracted the prices.

**What the client actually needed (October 2026).** In a recorded review meeting, the owner asked for control, not automation:

1. Separate "add" and "update", so an Excel drag-fill mistake cannot overwrite a product.
2. Update only on an exact model match. An extra space or dot must not match.
3. Add, edit and delete single products in the app, plus bulk upload from Excel.
4. Test with five additions, three updates and a few deletions before handover.
5. Only the owner edits prices. Everyone else can only view.
6. Load the October master data once, then test it together.

**My decision.** I took the email pipeline out of the app and rebuilt the catalogue around the owner's Excel workflow, keeping every existing product and its price history.

## How I delivered it

### 1. Requirements

I wrote a requirements audit that traced 15 client requirements to what the app does, the evidence that it works, and what was still open. Three examples:

| Client asked for | What the system does |
|---|---|
| Separate addition and update | Separate screens and Excel templates; the database enforces the chosen operation |
| Exact model matching | Updates match the model text exactly, including spaces and punctuation; unknown models are rejected |
| Owner edits, others view | Write access is checked on the server; other accounts are read-only |

The template is in [templates/requirements-audit.md](../templates/requirements-audit.md).

### 2. Safeguards

- Repeated models in a file are flagged on every row.
- Invalid rows are listed and skipped, never saved silently.
- Deleting is recoverable, with prices and history intact.
- Every price change is kept in the history.
- Dates are accepted only as DD/MM/YYYY; impossible dates are rejected.

### 3. Testing

- 237 automated tests, including the real Excel parser running against an isolated test database.
- On the live system, a 22-case signed-in acceptance pass using a clearly named test product that was removed afterwards. The checklist format is in [templates/uat-checklist.md](../templates/uat-checklist.md).

### 4. Release

Four production releases in five days (28 October to 1 November 2026). Database changes went in before the code, and after each release I checked the catalogue: 3,104 products and 37 brands, unchanged.

### Found and fixed

The Excel export was blanking older prices that had no dates. I fixed it on 30 October: the export now includes a current-prices report and a separate products sheet for re-import.

## Results

- Live in production: 3,104 products across 37 brands, searchable and filterable
- Full price history for every product
- Excel templates, import and export, with validation before anything is saved
- Offline access to the catalogue
- Owner-only editing; read-only access for everyone else

## Status

Next step: a joint acceptance test with the client's October master data. I flagged blank and inconsistent fields for the client to reconcile, instead of filling them with guesses.

## The lesson

Record the meeting. Turn it into a requirement table. Test against that table, not against memory.

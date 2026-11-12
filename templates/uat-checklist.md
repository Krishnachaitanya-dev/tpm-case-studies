# User acceptance test (UAT) checklist

Run this on the live system with the client, signed in as a real user, before sign-off. Use a clearly named test record (for example "TEST - delete me") and remove it afterwards.

**Project:**
**Build / release:**
**Environment:** production / staging
**Tested by:**
**Date:**

## Test cases

| # | Requirement | Steps | Expected result | Actual result | Pass / Fail |
|---|---|---|---|---|---|
| 1 | R1 | | | | |
| 2 | R1 | | | | |
| 3 | R2 | | | | |

Write at least one case per requirement in the [requirements audit](requirements-audit.md), plus negative cases: wrong input, missing permission, duplicate data.

## Data check after testing

- [ ] Test records removed
- [ ] Record counts match the numbers before testing (for example products, brands, users)
- [ ] No real customer data was changed

## Sign-off

| Item | Result |
|---|---|
| Cases passed | __ of __ |
| Open defects | |
| Client decision | Accepted / Accepted with fixes / Not accepted |
| Signed off by | |

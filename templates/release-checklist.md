# Release checklist

Use before every production release, and before every App Store or Google Play submission.

**Release:**
**Date:**
**Owner:**

## Before release

- [ ] Scope agreed with the stakeholder, and written in the release notes
- [ ] All changes tested; UAT passed where the change is user-facing
- [ ] Database changes applied **before** the code that depends on them
- [ ] Backup or rollback plan written down
- [ ] Record counts noted (so they can be checked after release)

## App Store and Google Play

- [ ] Version and build number increased
- [ ] Release notes written for the store
- [ ] Data-safety (Google Play) and privacy details (App Store) still accurate
- [ ] Account deletion still works inside the app
- [ ] Screenshots updated if the UI changed
- [ ] Test account details provided for the reviewer

## After release

- [ ] Smoke test on the live system: sign in, the main flow, payment if any
- [ ] Record counts match the numbers noted before release
- [ ] Errors and crash reports checked after one hour and after one day
- [ ] Stakeholder told what shipped and what is next

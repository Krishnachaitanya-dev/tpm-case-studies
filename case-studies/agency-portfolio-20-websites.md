# About 20 client websites in one year, for a digital agency

How I delivered and tracked a portfolio of websites and landing pages in parallel, with one shared tracker as the single source of truth.

| ~20 | 7 | 1 |
|---|---|---|
| websites and landing pages | landing pages for one realty client | shared tracker for scope, approvals and payments |

- **Client:** EnValues, a digital agency. I work with them as a freelancer and deliver for their end clients.
- **My role:** delivery lead and developer
- **Timeline:** 2026
- **End clients:** real estate developers, an academy, a car-care business, a financial-services firm, a riders' community and others

## The problem

An agency runs many small projects at once. Each one waits on something different:
- one on the client's logo
- one on approval of a draft
- one on a domain transfer
- one on payment

Without a shared view, nobody knows which project is blocked or why.

## How I ran it

**One row per project in a shared tracker**, with the same columns for every client:

| Column | Why it's there |
|---|---|
| Scope | What was agreed, so changes are visible |
| Completed work | What has shipped |
| Pending work | What is left on our side |
| Client input needed | What we're waiting for, and from whom |
| Approval | Whether the client has signed off |
| Payment | Whether the work is paid |

**Steps for every site:**
1. Agree the scope.
2. Collect the client's inputs.
3. Build.
4. Get approval.
5. Point the domain and go live.

**One client, many pages.** One realty client needed 7 landing pages, one per property project, each tracked as its own row.

**Internal tooling.** I also built and run the agency's internal operations tool: clients, projects, tasks, approvals and website uptime monitoring. When the original hosting setup had an outage, I moved the tool to its own database and AI provider so the agency wasn't dependent on one vendor.

## Results

- About 20 websites and landing pages delivered in 2026
- Every project's status visible in one place, including what was waiting on the client

## What I'd tell another TPM

Track "waiting on the client" as its own column. Most delays in agency work aren't build time; they're inputs and approvals nobody chased.

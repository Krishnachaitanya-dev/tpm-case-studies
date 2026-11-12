# Running a multi-tenant WhatsApp automation platform

How I build and operate the platform behind EnOrbit, and how I handled two client incidents with data instead of guesses.

| ~13 | 8 | 4,097 | 2,840 |
|---|---|---|---|
| client businesses on the platform | compliance safeguards shipped | contacts in one campaign post-mortem | confirmed-good numbers relaunched |

- **Product:** EnOrbit, a WhatsApp automation SaaS for small businesses. EnValues, a digital agency, markets and sells it; I built and run the platform.
- **My role:** I own the code, hosting and maintenance, onboard client businesses and handle Meta policy compliance.
- **Timeline:** March 2026 to now
- **Live on:** web, and [Google Play](https://play.google.com/store/apps/details?id=com.enorbit.app)

## What the platform does

- A visual flow builder for WhatsApp conversations, with the engine that runs them
- Meta Embedded Signup, so a business can connect its own WhatsApp number
- Broadcast campaigns with throttling, retries and delivery analytics
- A shared inbox and message-template management
- Shopify catalogue sync, with cart and checkout inside WhatsApp
- An admin console and daily backups

## Onboarding a client business

Each new business goes through the same runbook:

1. Connect the business's WhatsApp number through Meta Embedded Signup.
2. Connect its Shopify store, if it has one, and sync the catalogue.
3. Set up its flows and templates.
4. Go live.

## Incident 1: a client received Meta spam warnings

**Situation.** A building-products client received spam-policy warnings from Meta. Repeated warnings can get a WhatsApp number restricted, which would cut the business off from its customers.

**Root cause.** I traced it to the client's staff messaging customers outside WhatsApp's 24-hour customer-service window.

**Fix.** Instead of patching one account, I shipped 8 safeguards for every business on the platform. Among them:
- opt-out tracking and STOP handling
- a consent gate before bulk sends
- send-rate caps tied to each number's real Meta messaging tier
- checks on the 24-hour window before a free-form message goes out

## Incident 2: a campaign with 1,257 failed messages

**Situation.** A home-goods retailer sent a campaign to 4,097 contacts, and 1,257 messages failed.

**What I did.**
- Classified every failure by its cause, instead of retrying the whole list blindly.
- Blind retries to bad numbers would have hurt the number's quality rating with Meta.
- Relaunched the campaign to the 2,840 numbers confirmed as good.

## What I'd tell another TPM

When a platform warns one client, fix the platform, not just that client. And when a campaign fails, count the failures by cause before you touch the retry button.

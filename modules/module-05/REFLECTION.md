# Module 5 — Reflection

**Team name**: _______________
**Branch**: `module-05/<team-name>`
**Submitted**: before Module 6 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The game-service now has two models for the same data: SQLite for writes, Redis for reads. They store the same games in two different shapes.

**Why go through the trouble of maintaining two representations of the same data?**

Think about what kind of queries each model is optimised for, and what would happen if you tried to use the write model for high-traffic read operations.

SSQLite is accurate for writes, but reading from it under heavy traffic would be slow and could lock the database. Redis is just fast key-value storage, so reads stay quick even with thousands of users, even if the data is a few seconds old.



---

## 2. Your choice

The logging-service checks GDPR consent before recording any activity. If a user has not opted in, the log is silently dropped.

**What does this consent check force you to accept about your data?** It is incomplete by design — some activities will never be recorded.

From a system design perspective: where is the right place to enforce this rule — in the logging-service, in the activity-service, or at the gateway? Why?

This means some activities will never be logged, and that's on purpose. I put the check in logging-service, not activity-service, because activity-service still needs to process the activity regardless, only the storing of the log depends on consent. The gateway doesn't know about consent records, so it's the wrong place too

---

## 3. The tradeoff

With CQRS, your write model and read model can drift out of sync — a game is updated in SQLite but the Redis projection still shows the old data.

**In what scenario does this inconsistency matter to the user? In what scenario is it completely acceptable?**

Is there a class of applications where eventual consistency is never acceptable? What are they?

If a user updates a game title and immediately sees the old one in their summary, that's confusing drift matters there. For something like a trending games list, nobody cares if it's a few seconds stale. Anything with money or safety (bank balance, stock trades) can never accept eventual consistency, because a wrong number for even a second can cause real harm.

---

*Keep this file. You will refer back to it during the oral presentation.*

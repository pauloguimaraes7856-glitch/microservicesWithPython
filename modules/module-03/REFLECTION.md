# Module 3 — Reflection

**Team name**: Lesinvincibles
**Branch**: `module-03/Lesinvincivles`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

Without a gateway, the frontend would need to call every service directly (users on 8001, games on 8002, etc). So it would have to know all the ports and URLs.

If one service changes location or port, the frontend breaks and you need to update everything.

The gateway solves this by giving only one entry point. The frontend just talks to one URL and doesn’t care about what’s behind.
---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

The user validation call is important because if the user doesn’t exist, we shouldn’t create an activity. Otherwise we could end up storing wrong or fake data.

For the game call, it’s different. If the game service fails, we don’t block the request. We still save the activity, just without extra game info.

So one is critical for data correctness, the other is only extra information.

---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

When you chain multiple services like this, everything becomes slower and more fragile.

If each service takes ~1 second, the total response time becomes around 3 seconds because everything is sequential.

If one service is slow or down and there are no timeouts, the request can hang or fail the whole operation.

That’s why latency and timeouts are important in microservices — one slow service can degrade the whole user experience.

---

*Keep this file. You will refer back to it during the oral presentation.*

# Module 6 — Reflection

**Team name**: _______________
**Branch**: `module-06/<team-name>`
**Submitted**: before Module 7 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The gateway now validates every JWT before forwarding a request. Individual services no longer need to check identity themselves.

**What does centralising authentication at the gateway buy you?** What would the alternative look like — if every service validated tokens on its own?

Think about what happens when you need to rotate the secret key, or add a new service to the system.

If every service has to check tokens itself, you need to update the secret key in every service when you rotate it, and add the same check code everywhere when you add a new service. With the gateway doing it once, you only change the key in one place and new services just trust whatever the gateway already validated.



---

## 2. Your choice

When activity-service calls user-service internally, it uses a Machine-to-Machine (M2M) token — not a user's token.

**Why can't it just reuse the user's token that arrived in the original request?**

What would break, or what door would you accidentally leave open, if services passed user tokens between themselves?

The user's token has the user's role, not the service's role. If activity-service used it to call user-service, user-service would think the request is the user, not a service. Also if a token is leaked or expires, services would have to deal with that randomly while doing internal work. With an M2M token, activity-service is just being itself, with its own role, so it's clearer.

---

## 3. The tradeoff

The gateway and the auth-service share the same `SECRET_KEY` to verify tokens without making a network call on every request.

**What is the security risk of sharing this key?** What happens if it leaks?

And what would the alternative look like — verifying tokens by calling auth-service on every request instead? What does that cost you?

If the secret key leaks, anyone can make their own valid tokens and pretend to be admin. That's the risk of sharing it. The alternative (calling auth-service every time) would be safer in a way because auth-service could revoke tokens immediately, but it adds a network call on every single request, so it's slower and auth-service becomes a bottleneck.

---

*Keep this file. You will refer back to it during the oral presentation.*

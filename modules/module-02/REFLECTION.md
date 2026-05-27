# Module 2 — Reflection

**Team name**: Lesinvincibles (paulo and willy)
**Branch**: `module-02/Lesinvincibles`
**Submitted**: before Module 3 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You built a service with distinct layers: models, schemas, repository, service, and routes — each with a single responsibility.
 
**Why not just put everything in one file and call it done?**

Think about what happens six months later when someone new joins the team, or when you need to swap SQLite for PostgreSQL. What does the layered structure protect you from?

Putting everything in one file would become messy really fast. With different layers, the code is cleaner and easier to understand. If someone new joins the project later, they can quickly know where things are.

---

## 2. Your choice

Each service owns its data exclusively — no other service is allowed to touch its database directly.

**Pick one entity your service owns (e.g. `User`, `Game`). What would go wrong if another service could write to that table directly?**

Give a concrete scenario, not a general principle.

The game-service owns the Game entity. If another service could directly change the games table, it could add wrong data or break the catalogue. For example, a game could be added without a title or with bad information.

---

## 3. The tradeoff

You now have models, schemas, a repository, a service, and routes — five layers for what is essentially a CRUD service.

**For a system this small, what is the cost of all this structure?**

And at what point does the complexity start to pay off? Where is the tipping point?

For a small project, having many layers means more files and more setup for simple things. But when the project becomes bigger and more people work on it, the structure becomes useful and easier to manage.

---

*Keep this file. You will refer back to it during the oral presentation.*

## YOU NEED TO COMMIT THIS FILE BEFORE MOVING ON TO THE NEXT MODULE ! 🚨

**feel free to delete this comment**

# Module 1 — Reflection

**Team name**: **Lesinvincibles** (willy and Paulo)
**Branch**: `module-01/invincibles`
**Submitted**: before Module 2 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You started from a painful monolith. Now you're splitting it into separate services.

**What concrete problem does that split solve: and for whom?**

Think about it from three angles: the developer who has to change code, the team that has to deploy it, and the user who has to live with its failures. You don't need to cover all three, pick the one that felt most real to you today.

Splitting the monolith makes the project easier to manage for developers, instead of working on one huge application, each service has one responsibility. This makes changes safer and easier because working on the game-service should not break authentication or notifications.

---

## 2. Your choice

Look at your service map. Every arrow between two services is a decision someone made.

**Pick one boundary, one place where you decided service A should not be part of service B. Explain why that line exists.**

What would break, slow down, or become harder to manage if you merged those two services back together?

I chose the boundary between activity-service and logging-service. For me, activity-service should only handle what users do on the platform, like playing a game or sharing an activity. Logging-service should only store logs and consent information. If we merged them, the service would mix user activity logic with logging and GDPR rules, so it would be harder to understand and maintain.

---

## 3. The tradeoff

Microservices solve the monolith's problems. But they create new ones.

**Name one thing that was simpler in the monolith and is now harder in your distributed design.**

No need to solve it: just name it honestly. This is exactly the tension the rest of the course is about.

Communication was simpler in the monolith because everything was inside the same application. With microservices, services need REST calls or Rabbitmq messages to communicate, so there are more things to configure and more possible errors.

---

_Keep this file. You will refer back to it during the oral presentation._

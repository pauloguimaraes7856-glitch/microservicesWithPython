# Module 4 — Reflection

**Team name**: _______________
**Branch**: `module-04/<team-name>`
**Submitted**: before Module 5 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

In Module 3, services called each other directly over HTTP. Now activity-service drops a message into a broker and moves on — it never waits for a reply.

**What does the activity-service gain by not waiting? And what does the notification-service gain by consuming at its own pace?**

Think about what happens under load, or when notification-service is temporarily down.

activity-service doesn't have to wait anymore  lif notification-service is down or slow, the activity still gets saved. notification-service can process messages whenever it's ready, even if it was offline for a bit, because the messages wait in the queue.

---

## 2. Your choice

In Module 3 you already knew how to call another service directly over HTTP — you did it for user validation and game enrichment.

**Why not use the same approach for notifications? What does introducing a broker give you that a direct HTTP call doesn't?**

Think about what happens if notification-service is slow, or crashes mid-message.

With HTTP, if notification-service crashes or is slow, activity-service fails too. With RabbitMQ, activity-service just drops the message and moves on. They don't depend on each other being up at the same time.

---

## 3. The tradeoff

With synchronous REST, you get an immediate answer: success or failure. With async messaging, the activity is saved and the message is sent — but you have no idea if the notification was ever delivered.

**How would a user know if their notification was never sent? How would you know as a developer?**

What visibility do you lose when you go async?

You lose visibility. With REST you instantly know if it worked or failed. With async, the activity is saved and the message is sent but that's it, you have no clue if the notification actually made it. The user won't see any error even if it never arrived. As a dev you'd have to dig into RabbitMQ or check the logs to figure out what happened.

---

*Keep this file. You will refer back to it during the oral presentation.*

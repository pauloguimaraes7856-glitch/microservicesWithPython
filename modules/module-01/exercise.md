# Module 1 — Service Decomposition

**Duration**: 2h in class
**Branch to submit**: `module-01/<team-name>`

---

## Objective

Before writing a single line of code, you need to design the system on paper. Every decision you make here: where to draw service boundaries, who owns what data, how services talk to each other, is hard to reverse once you start coding.

This module is about slowing down and thinking like an architect, not a developer.

Read these two documents before doing anything else:

- `docs/domain.md` — what GameHub is and who uses it
- `docs/specs.md` — the tech stack and key architectural decisions

> The CTO has already laid out the `services/` folder structure. Use it as a starting point, but your job is to **justify** why each folder deserves to be its own service — not just accept it.

---

## Task 1 — Identify bounded contexts _(~40 min)_

A bounded context is a part of the system that has a clear responsibility and owns its data exclusively. No other service should reach into its database.

For each bounded context you identify, fill in the table:

| Bounded Context | Responsibilities                                         | Owned Entities | Team        |
| --------------- | -------------------------------------------------------- | -------------- | ----------- |
| Identity        | Manages who users are, handles registration and profiles | User, Session  | Platform    |
| Game Library    | _(fill in)_                                              | _(fill in)_    | _(fill in)_ |
| _(add more)_    |                                                          |                |             |

There is no single correct answer: what matters is that you can justify each row.

response:

## Task 1 — Identify bounded contexts

| Bounded Context | Responsibilities | Owned Entities | Team |
| --------------- | ---------------- | -------------- | ---- |
| Identity | Manages who users are, handles registration, login, profiles and sessions | User, Session | Platform |
| Game Library | Manages games available on GameHub, including titles, genres and game metadata | Game, Genre, Platform | Content |
| Activity | Tracks what users do on the platform, like playing games, sharing activity and engagement history | Activity, PlayHistory, UserGameActivity | Engagement |
| Notification | Sends notifications to users when important events happen, for example friend activity or game updates | Notification, NotificationPreference | Communication |
| Logging | Stores consent state and activity logs only when the user has opted in | Consent, ActivityLog | Compliance |
| Recommendation | Suggests games or connections based on play history and community interests | Recommendation, RecommendationScore | Data |

---

## Task 2 — Define service contracts _(~30 min)_

For each pair of services that need to communicate, define:

- **Direction**: A → B
- **Trigger**: what causes the call
- **Protocol**: REST or event (async)
- **Payload**: key fields exchanged

Example:

```
activity-service → logging-service
Trigger: an activity is logged
Protocol: RabbitMQ message (async — why not REST here?)
Payload: { activity_id, user_id, action, game_id, timestamp }
```

Focus on the flows that feel non-obvious. You do not need to document every possible pair.


RESPNSE:

- 1. activity-service → logging-service
Trigger: a user activity happens, for example when a user plays a game.
Protocol: RabbitMQ message (async)
Payload: { activity_id, user_id, action, game_id, timestamp }

Logging should be async because the user action should not be blocked if the logging-service is slow.


- 2. activity-service → notification-service
Trigger: a user shares an activity with friends or the community.
Protocol: RabbitMQ message (async)
Payload: { activity_id, user_id, game_id, action, timestamp }

Notifications can be done in the background, so the activity does not need to wait.


- 3. gateway → auth-service
Trigger: a user logs in, registers, or sends a request with a token.
Protocol: REST
Payload: { email, password } or { token }

The gateway needs an immediate answer to know if the request is allowed.


- 4. recommendation-service → activity-service
Trigger: the recommendation-service needs user activity history to suggest games.
Protocol REST
Payload: { user_id }

The recommendation-service asks activity-service instead of reading its database directly.

---

## Task 3 — Draw the service map _(~20 min)_

Draw the full GameHub service map:

- One box per service
- Arrows between services (solid line = synchronous REST, dashed line = async event)
- Label each arrow with its protocol
- One box at the top labelled **gateway** — all client requests enter here, no client ever calls a service directly

This can be a sketch on paper, a whiteboard photo, or ASCII art committed to your branch.

RESPNSE:


                 -----------
                |  gateway  |
                 ----------- 
                  |   |   |
                  |   |   |
                 REST REST REST
                  v   v   v

           ------  ------   ------------------ 
          | auth | | game | | activity-service |
           ------  ------  ------------------
                                      |     |
                                 async|     |async
                                      v     v

                           +-------------------+
                           | logging-service   |
                           +-------------------+

                            ------------------------
                           | notification-service   |
                            ------------------------


---

## Discussion _(~15 min)_

Three questions to discuss as a team before you leave:

1. Why does `notification-service` use Node.js instead of Python like the rest? What does that tell you about microservices and technology choices?
2. What is the risk of `activity-service` calling `logging-service` synchronously — why might you prefer an async event instead?
3. Why does `logging-service` need a GDPR consent check before recording any activity?

You do not need to write these answers down — they are warm-up for your REFLECTION.md.

---

## Minimum to submit this branch

- [ ] Bounded context table filled in (at least 4 services justified)
- [ ] At least 3 service contracts defined
- [ ] Service map committed (sketch, photo, or ASCII)
- [ ] `REFLECTION.md` completed and committed

The map does not need to be perfect. It needs to be yours.

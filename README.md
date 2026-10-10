# Learning FastAPI

A beginner-friendly task API built one lesson at a time. Each lesson introduces a concept, a small practical change, and a checkpoint before moving on.

## Resume Learning

- Covered: lessons 1-11, from the first endpoint through PUT updates.
- Resume at: [Lesson 12: PATCH Updates](#current-lesson). Implementation review and the practical checkpoint are still pending.
- Next: [Lesson 13: DELETE And IDs](#complete-the-task-api), after PATCH works correctly.
- Start the server using [Run The Server](#run-the-server), then follow the roadmap in order. For each lesson, read the linked docs, implement the learning goal, and verify its checkpoint before moving it into Lessons Covered.
- To continue with an assistant later, ask: "Read this README and teach the current unfinished lesson one step at a time. Let me write the code and check my understanding before moving on."

## Run The Server

These instructions are for macOS/zsh and this workspace's existing Python 3.14 virtual environment in the repository root.

1. Open **Terminal > New Terminal** in VS Code. Make sure you are in the fastapi-server folder containing [main.py](main.py).
2. Activate the virtual environment with `source bin/activate`. Repeat this in each new terminal used to run the server.
3. On first setup, install FastAPI and its standard tools with `python -m pip install "fastapi[standard]"`. Skip this if they are already installed in this environment.
4. Start the development server with `fastapi dev main.py`. Keep this terminal running; saving Python code automatically reloads the server.
5. Open the [welcome endpoint](http://127.0.0.1:8000) or [interactive API docs](http://127.0.0.1:8000/docs) in your browser.
6. Stop the server with **Ctrl+C** in its terminal. Run `deactivate` afterward to leave the virtual environment.

If port 8000 is already in use, run `fastapi dev main.py --port 8001` and use port 8001 in the browser URLs instead. Development reload resets our in-memory task changes; this command is for local learning, not production deployment.

Official documentation: [FastAPI CLI](https://fastapi.tiangolo.com/fastapi-cli/).

## Lessons Covered

| Lesson | Key Takeaway | Official Documentation |
| --- | --- | --- |
| 1. First Server | Understand virtual environments, HTTP requests and responses, and a first GET endpoint. | [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) |
| 2. Path Parameters | Capture a URL segment and use type hints to convert and validate it. | [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/) |
| 3. Query Parameters | Accept additional URL options with types and default values. | [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/) |
| 4. Interactive Documentation | Test endpoints in Swagger UI at /docs; distinguish successful responses from validation errors. | [Interactive API Docs](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs) |
| 5. Request Bodies | Receive JSON with POST; Pydantic validates incoming data before the endpoint runs. | [Request Body](https://fastapi.tiangolo.com/tutorial/body/) |
| 6. In-Memory Storage | Store task dictionaries in a list, assign IDs, and list tasks; distinguish returning data from printing it. | [Response Status Codes](https://fastapi.tiangolo.com/tutorial/response-status-code/) |
| 7. Finding Tasks | Search by ID and raise HTTPException with 404 only after the search finds no match. | [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) |
| 8. Field Validation | Limit title length with Field; missing or invalid input receives 422. | [Body Fields](https://fastapi.tiangolo.com/tutorial/body-fields/) |
| 9. Input Cleaning | Strip surrounding whitespace before validating titles; whitespace-only titles are rejected. | [Pydantic String Configuration](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.str_strip_whitespace) |
| 10. Response Models | Define outgoing fields and types; distinguish one task from a list and return 201 for creation. | [Response Models](https://fastapi.tiangolo.com/tutorial/response-model/) |
| 11. PUT Updates | Replace editable fields while preserving the ID; our request model requires both title and completed. | [Updates With PUT](https://fastapi.tiangolo.com/tutorial/body-updates/#update-replacing-with-put) |

## Current API

| Method | Path | Purpose |
| --- | --- | --- |
| GET | / | Return a welcome message. |
| GET | /tasks | List tasks. |
| GET | /tasks/{task_id} | Retrieve a task, or return 404. |
| POST | /tasks | Create a task and return 201. |
| PUT | /tasks/{task_id} | Replace a task's editable fields, or return 404. |

Interactive documentation is available at [localhost /docs](http://127.0.0.1:8000/docs) while the server is running.

### Learning Limitations

- Tasks are stored in one process's memory, not a database. Restarts and development reloads discard changes and recreate the sample tasks.
- IDs currently use the list length plus one. Deleting tasks could cause duplicate IDs; we will fix this before adding deletion.
- The current API has no authentication and is a local learning example, not a production-ready service.

## Current Lesson

Lesson 12 is in progress: a draft PATCH endpoint has been added, but implementation review and the practical checkpoint are pending. PATCH is not yet listed as a verified current API capability.

| Lesson | Key Takeaway | Official Documentation |
| --- | --- | --- |
| 12. PATCH Updates | Allow omitted fields and use exclude_unset to update only supplied values, including false. Reject explicit null before changing stored data; preserve the ID and return 404 for missing tasks. | [Partial Updates](https://fastapi.tiangolo.com/tutorial/body-updates/#partial-updates-with-patch) |

Before testing, check that TaskPatch uses max_length for its title limit and spells completed consistently with the stored task fields.

Checkpoint: update completion without changing the title, explicitly set completion to false, update only the title, and confirm that null and whitespace-only titles return 422 without changing stored data. An empty update should leave an existing task unchanged; valid input for a missing ID should return 404. Explain why exclude_unset prevents omitted fields from overwriting existing values.

## Future Lessons

These lessons are planned, not implemented. Each learning goal is a small project extension; its checkpoint defines when to move on. We will update the covered lesson log as we progress, keeping summaries concise and free of code snippets. Links to Pydantic, SQLModel, and Alembic cover the supporting libraries where needed.

### Complete The Task API

| Lesson | Learning Goal | Practical Checkpoint | Official Documentation |
| --- | --- | --- | --- |
| 13. DELETE And IDs | Delete a task, return 204 without a body, handle missing tasks, and prevent ID reuse or collisions. | Delete a middle task, create another, and verify unique IDs; repeat deletion and expect 404. | [Response Status Codes](https://fastapi.tiangolo.com/tutorial/response-status-code/) |
| 14. Filtering And Pagination | Filter tasks by completion, limit result size, and validate pagination and positive IDs. | Fetch separate result pages and completed-only tasks; invalid limits and IDs receive 422. | [Query Validation](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/), [Path Validation](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/) |
| 15. Automated Tests | Use TestClient and pytest to test CRUD, validation, error responses, and isolated test data. | Run the suite twice successfully; tests must not depend on execution order or leftover tasks. | [Testing](https://fastapi.tiangolo.com/tutorial/testing/) |

### Structure And Persistence

| Lesson | Learning Goal | Practical Checkpoint | Official Documentation |
| --- | --- | --- | --- |
| 16. Project Structure | Split models and routes into modules; organize endpoints with APIRouter without changing their behavior. | Existing tests pass and the same routes still appear in /docs. | [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) |
| 17. Dependencies | Use Depends for shared behavior and per-request resources; override dependencies in tests. | Replace a dependency in a test and explain when its resource is created and cleaned up. | [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/), [Test Overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) |
| 18. SQLite Database | Replace the list with persistent SQLModel storage; learn tables, sessions, transactions, and database-generated IDs. | A created task survives a restart; tests use a separate database, not your learning data. | [SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| 19. Relationships And Migrations | Associate tasks with users and evolve database schemas without losing existing data. | Add a schema change through a migration and verify existing users and tasks remain intact. | [SQLModel Relationships](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/), [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) |
| 20. Configuration | Load environment-specific settings, validate configuration, and keep secrets out of source control. | Change the database location through settings; missing required settings fail clearly. | [Settings And Environment Variables](https://fastapi.tiangolo.com/advanced/settings/) |
| 21. Sync And Async | Understand blocking I/O, when to use def or async def, and why async alone does not make work faster. | Explain which operations block and avoid synchronous database or HTTP calls inside async endpoints. | [Concurrency And Async](https://fastapi.tiangolo.com/async/) |
| 22. Application Lifespan | Initialize and clean up shared resources at startup and shutdown; understand process-local state. | Test startup and shutdown cleanup; explain why each worker has its own memory. | [Lifespan Events](https://fastapi.tiangolo.com/advanced/events/) |

### Secure And Operate The Backend

| Lesson | Learning Goal | Practical Checkpoint | Official Documentation |
| --- | --- | --- | --- |
| 23. Authentication | Hash passwords, implement login, and validate expiring bearer tokens; never store plaintext passwords. | Valid login works; incorrect passwords and expired or altered tokens are rejected; responses never expose password hashes. | [OAuth2 And JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) |
| 24. Authorization | Identify the current user, enforce task ownership, and distinguish 401 from 403; test denied access. | Two users cannot list, read, update, or delete each other's tasks. | [Current User](https://fastapi.tiangolo.com/tutorial/security/get-current-user/) |
| 25. Middleware And CORS | Add request-wide behavior and allow specific browser origins; understand that CORS is not authentication. | Test an allowed browser origin and a blocked one; protected endpoints still require authentication. | [Middleware](https://fastapi.tiangolo.com/tutorial/middleware/), [CORS](https://fastapi.tiangolo.com/tutorial/cors/) |
| 26. Errors And Logging | Replace debug prints with useful logs and consistent errors without exposing secrets or internal exceptions. | A failed request produces useful logs and a safe error response without passwords, tokens, or tracebacks. | [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) |
| 27. Background Work | Run small tasks after responding and recognize when reliable work needs a separate job queue. | Test a small background action and explain why in-process tasks do not guarantee completion after a crash. | [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) |
| 28. File Uploads | Receive multipart uploads, validate file limits, and handle uploaded content safely. | Accept a permitted file and reject oversized or disallowed content without trusting its client-supplied filename. | [Request Files](https://fastapi.tiangolo.com/tutorial/request-files/) |
| 29. Deployment | Run without development reload; understand HTTPS, workers, health checks, and production configuration. | Run with production settings and no reload; verify HTTPS, health checks, and persistent data after restart. | [Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/), [Server Workers](https://fastapi.tiangolo.com/deployment/server-workers/) |
| 30. Backend Capstone | Combine persistent per-user tasks, pagination, authentication, tests, and documented responses into a deployable API. | Complete a login-to-CRUD workflow, run the full test suite, and verify setup instructions and API docs. | [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) |

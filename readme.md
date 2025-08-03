# FirmHaven ERP Platform

**FirmHaven** is a domain-agnostic, schema-isolated, multi-tenant ERP engine built with FastAPI and PostgreSQL. It enables businesses to define custom entities, fields, flows, actions, and access policies — similar to platforms like Salesforce, but developer-friendly and SQL-native.

---

## Features

- Dynamic Entity & Field Engine (per-tenant table creation)
- Per-field Role-Based Access Control (RBAC)
- Workflow & Action Engine (webhooks, scripts, PDF, etc.)
- Reporting with views, charts, exports
- Schema-first metadata stored in tenant schema
- Pluggable file storage (local, S3-ready)
- Mobile-aware frontend (planned)
- Blazing-fast FastAPI backend with OpenAPI docs

---

## Tech Stack

| Layer         | Tech                           |
| ------------- | ------------------------------ |
| API Framework | FastAPI                        |
| ORM           | SQLAlchemy + Alembic           |
| DB            | PostgreSQL (per-tenant schema) |
| Auth          | OAuth2 + custom RBAC           |
| Frontend      | React + Tailwind (planned)     |
| Async Tasks   | Celery (future)                |
| Container     | Docker-ready                   |

---

---

## Setup Instructions

### 1. Clone & Install

```bash
git clone https://github.com/your-username/firmhaven.git
cd firmhaven
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt

```

### 2. Configure ENV

```
DATABASE_URL_PYTHON=<DB>://<user>:<password>@<hostname>:<port>/<db_name>
```

### 3. Run The API

```
uvicorn app.main:app --reload

```

Docs available at: http://localhost:8000/docs

## Contributions

This is a solo-build MVP right now — but contributions, feedback, and architectural suggestions are welcome!

---

Let me know:

- bhavesh25515@gmail.com

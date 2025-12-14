# Fuel Monitoring System

This project implements a Full Stack application for the Ministério de Transportes to monitor fuel collection data, including key performance indicators (KPIs) and data filtering capabilities.

## Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python (FastAPI) | RESTful API for data ingestion, querying, and KPI calculation. |
| **Database** | PostgreSQL 15 | Persistent storage for fuel collection records. |
| **Frontend** | React + TypeScript | Interactive dashboard with filters, data table, and charts (Recharts). |
| **Orchestration** | Docker & Docker Compose | Containerization for isolated and reproducible environments. |
| **Security/Compliance** | CPF Masking (LGPD) | Sensitive data (CPF) is masked before being sent to the frontend. |

## Features

*   **Data Ingestion:** Endpoint to receive fuel collection records.
*   **Data Query:** Filterable table view of all collected data.
*   **KPI Visualization:**
    *   Pie Chart: Total volume collected by vehicle type.
    *   Line Chart: Price evolution over time.
*   **Advanced UX:** Debounced filters, request cancellation (`AbortController`), and delayed loading indicators.

## Setup and Installation

### Prerequisites

*   Docker and Docker Compose installed.

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gabrifgaraujo/fuel-monitoring-system.git
    cd fuel-monitoring-system
    ```

2.  **Start the services:**
    ```bash
    docker compose up --build -d
    ```
    *This command will build the `backend` and `frontend` images, start the `db` container, and wait for the database to be healthy before starting the `backend`.*

3.  **Seed the database (Optional):**
    To populate the database with fake data for testing:
    ```bash
    docker compose exec backend python /script/seed.py
    ```

4.  **Access the application:**
    The frontend dashboard will be available at `http://localhost:3000`.
    The backend API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── database.py       # SQLAlchemy setup
│   │   ├── models.py         # SQLAlchemy ORM model
│   │   ├── schemas.py        # Pydantic validation schemas
│   │   └── main.py           # FastAPI application, routes, and logic
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/       # React components (Charts, Table, etc.)
│   │   ├── services/         # API service calls (axios)
│   │   ├── types/            # TypeScript interfaces
│   │   ├── utils/            # Custom hooks (useDebounce)
│   │   └── App.tsx           # Main dashboard component
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
├── script/
│   └── seed.py               # Data seeding script
├── docker-compose.yml        # Service orchestration
└── README.md
```

# Standalone Weather Hub (Level 2 Architecture)

A multi-tiered web application built with Python, Flask, and an SQLite database layout. This project demonstrates intermediate software engineering patterns, including Separation of Concerns (SoC), data caching optimization, database parameterization, and fault-tolerant network simulation.

## 🏗️ System Architecture

The application is structured into four distinct, decoupled layers to maintain clean code boundaries:

1. **Presentation Layer (`index.html`)**: A modern, front-end dashboard that uses asynchronous JavaScript (`fetch`) to communicate with backend endpoints and dynamically updates the DOM.
2. **Controller/API Layer (`app.py`)**: A Flask web server that acts as a router, managing JSON payloads, performing payload validation, and directing systemic application flow.
3. **Data Access Layer (`database.py`)**: A secure, class-based database engine that abstracts SQL operations using context managers and parameterized queries.
4. **Data Definition Source (`schema.sql`)**: The single source of truth for the local database structure.

---

## 🚀 Key Features

* **Dual-Layer Caching**: The application queries a local database cache for target city coordinates before making external network calls, optimizing system resource usage.
* **SQL Injection Prevention**: Built entirely with parameterized queries (`?` binding operators) to ensure database transactions are secure.
* **Fault-Tolerant Simulation Fallback**: Implements an automated local runtime generator. If external geocoding or weather web services fail, timeout, or block requests, the server switches to simulation mode to keep the application running flawlessly.
* **Rule-Based Recommendation Engine**: Features a live data evaluation matrix that analyzes current metrics to generate tailored clothing and safety alerts.
* **Relational Database Logs**: Uses relational data table mappings to track lookup history dynamically.

---

## 📂 Project Structure

```text
Weather-App/
├── app.py          # Flask backend server and API route controllers
├── database.py     # SQLite class-based Data Access Layer 
├── schema.sql      # Database schema definitions
├── index.html      # Decoupled HTML/CSS/JS frontend interface
└── .gitignore      # Excludes local environments and database files
```

---

## 💻 Installation & Local Setup

### Prerequisites
Ensure you have Python 3 and the modern package manager `uv` installed on your machine.

### Execution Steps

1. Clone or download this project directory to your local workspace.
2. Open your terminal inside the project root folder.
3. Launch the local web server using the self-contained dependency runner:
   ```powershell
   uv run --with flask --with requests app.py
   ```
4. Open your web browser and navigate to the application dashboard:
   ```text
   http://127.0.0
   ```

---

## 🔌 API Endpoints

### 1. Query Current Weather
* **URL**: `/api/weather`
* **Method**: `POST`
* **Payload**: `{"city": "London"}`
* **Response**: Returns a JSON package containing the parsed current weather metrics.

### 2. Fetch City History
* **URL**: `/api/history`
* **Method**: `GET`
* **URL Params**: `?city=London`
* **Response**: Returns an array of historical search logs mapping past snapshot parameters.

### 3. Clear History Logs
* **URL**: `/api/history/clear`
* **Method**: `POST`
* **Payload**: `{"city": "London"}`
* **Response**: Wipes matching logs from the system and returns the count of deleted rows.

### 4. Fetch Advisory Tip
* **URL**: `/api/tip`
* **Method**: `GET`
* **URL Params**: `?city=London`
* **Response**: Triggers the conditional evaluation matrix and returns rule-based safety tips.

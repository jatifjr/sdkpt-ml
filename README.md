# SDKPT ML

This repository contains the SDKPT ML API project.

## Setup Instructions

### 1. Set Up Virtual Environment

#### Linux / MacOS:

```bash
python3 -m venv .venv
```

#### Windows:

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

#### Linux / MacOS:

```bash
source .venv/bin/activate
```

#### Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Deactivate and Reactivate the Virtual Environment

#### Linux / MacOS:

```bash
deactivate
source .venv/bin/activate
```

#### Windows:

```bash
deactivate
.venv\Scripts\activate
```

### 5. Create Environment Variables File

Create a `.env` file and populate it with the required environment variables. You can use the provided `.env.example` file as a template.

### 6. Run Alembic Migration

```bash
alembic upgrade heads
```

### 7. Run the FastAPI App

```bash
uvicorn app.main:app --reload --port 8000
```

Now you're all set up and ready to use the SDKPT ML API!

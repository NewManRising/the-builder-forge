# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A 40-week self-directed learning path ("The Builder Forge") structured into phases. Each phase has a `README.md` that will fill in as work progresses. The `projects/` directory is where standalone shipped projects land. The `journal/weekly/` directory is for weekly progress notes.

## Python Environment

All Python work uses the `.venv` at the repo root. Always activate it before running scripts:

```bash
source .venv/bin/activate
```

Verify the environment is set up correctly:

```bash
python scripts/hello_forge.py
```

Install/sync dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest                        # run all tests
pytest path/to/test_file.py   # run a single test file
pytest -k "test_name"         # run a single test by name
```

## Phase Structure

Phases are numbered `00`–`09` under `phases/`. The high-level grouping:

| Directory | Curriculum focus |
|---|---|
| `phases/00-launchpad` | Environment setup and tooling |
| `phases/01-python` | Python fundamentals |
| `phases/02-backend` | FastAPI, SQL, PostgreSQL |
| `phases/03-frontend-deploy` | React, Next.js, Docker, CI/CD |
| `phases/04-ml` | scikit-learn, LLM APIs, LangChain, RAG |
| `phases/05-agents` | AI agents, prompt engineering |
| `phases/06-cloud-mlops` | AWS, GCP, ML pipelines, MLflow |
| `phases/07-products` | SaaS patterns, payments, auth |
| `phases/08-advanced` | Kubernetes, IaC, fine-tuning |
| `phases/09-capstone` | Capstone project |

As the repo grows, each phase directory will accumulate its own code, scripts, and a more detailed README. New projects are added under `projects/` as they are built and shipped.

# Cyberabuse Hammad Qadeer Final

Cyberabuse-hammad-qadeer-final is a text classification application for detecting abusive comments.

![Flask](https://img.shields.io/badge/Flask-2563EB?style=flat-square)

## Overview

The Flask implementation is organized around the entry points and modules below.

## Implemented workflows

The source defines these handlers:

- **Predict Comment** — `predict_comment`
- **Index** — `index`

## Getting started

### 1. Get the project

```bash
git clone https://github.com/nasirabbas827/Cyberabuse-hammad-qadeer-final.git
cd Cyberabuse-hammad-qadeer-final
```

### 2. Prepare Python

Create an isolated environment:

```bash
python -m venv .venv
```

Activate it with `.venv\Scripts\activate` on Windows Command Prompt, or `source .venv/bin/activate` on macOS/Linux.

No requirements file is included. The inspected Python imports indicate these dependencies as a starting point:

```bash
python -m pip install Flask joblib scikit-learn
```

Dependency versions are not pinned in this repository.

### 3. Configure and run

Run from the repository root so relative file paths resolve correctly:

```bash
python app.py
```

Open http://127.0.0.1:5000/, or use the address printed by the application.

### Model files

Included artifacts: [`models/decision_tree_model.pkl`](models/decision_tree_model.pkl), [`models/naive_bayes_model.pkl`](models/naive_bayes_model.pkl), [`models/svm_model.pkl`](models/svm_model.pkl), [`models/vectorizer_ngram.pkl`](models/vectorizer_ngram.pkl).

Keep models, preprocessing objects, and label mappings together in the locations expected by the source.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`Dataset`](Dataset) | Dataset resources |
| [`app.py`](app.py) | Application entry point |
| [`models`](models) | Model resources |
| [`templates`](templates) | HTML page templates |

## Development notes

These setup instructions are based on the repository source. The application has not been executed as part of this documentation update; verify dependencies and configuration in your local environment.

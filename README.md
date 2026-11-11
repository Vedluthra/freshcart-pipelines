# freshcart-pipelines

Data Engineering assignment — Part A: Git and CI/CD.

## Repository layout

```text
freshcart-pipelines/
├── README.md
├── .gitignore
├── requirements.txt
├── elt/
├── iris_project/
│   └── transformers/
│       └── prepare_data.py
├── stream/
├── tests/
│   └── test_prepare_data.py
└── .github/
    └── workflows/
        └── ci.yml
```

Part A uses the Iris `prepare_data` block from Part C. The block is deliberately importable
outside Mage so pytest and GitHub Actions can test it.

## Run tests locally

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# On Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pytest -q
```

Expected result: `1 passed`.

## CI

GitHub Actions runs the same test on every push to `main` or `master`.
See `.github/workflows/ci.yml`.

## Assignment evidence to collect

- GitHub repository page showing the required folder structure.
- At least five meaningful commits (`git log --oneline`).
- One green GitHub Actions run.
- One red run after temporarily changing `test_size=0.2` to `test_size=0.3`.
- A fixing commit restoring `test_size=0.2`, followed by a green run.

Do not commit `.env`, credentials, generated CSV/model files, virtual environments, or logs.

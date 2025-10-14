# Contributing to Job Scraper

Thank you for your interest in contributing to **Job Scraper**! 🎉
We welcome all types of contributions — from bug reports to new features and documentation improvements.

## 🪜 Getting Started

1. **Fork** the repository and **clone** your fork locally.
2. **Create a branch** for your feature or fix:

```bash
git checkout -b feature/your-feature-name
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run tests locally** before committing:

```bash
pytest -v
```

5. **Commit and push** your changes:

```bash
git commit -m "feat: add new parser for Indeed"
git push origin feature/your-feature-name
```

6. **Open a Pull Request (PR)** to the `develop` branch.

---

## 🧪 Testing

All new code should include appropriate unit tests under the `tests/` directory.

---

## ✨ Code Style

We follow **PEP8** and enforce formatting using `black` and linting using `flake8`.
Before submitting, run:

```bash
black .
flake8
```

---

## 🧩 Branch Naming Convention

- `feature/<name>` — for new features.
- `fix/<name>` — for bug fixes.
- `chore/<name>` — for maintenance and updates.

---

## 🤝 Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

Thank you for helping improve **Job Scraper**!
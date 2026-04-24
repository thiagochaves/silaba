# Repository Guidelines

## Project Structure & Module Organization
This repository is a small Python 3.12 application with top-level modules instead of a `src/` package. `silaba.py` is the fullscreen Pyglet entry point, `fala.py` handles Google Cloud Text-to-Speech playback, `render.py` contains drawing helpers, and `palavra.py` manages text state and accent rules. Generated audio is cached in `mp3/` and should stay untracked. Keep new modules at the repository root unless the project is reorganized deliberately.

## Build, Test, and Development Commands
Use `uv` for environment and command execution.

- `uv sync` installs dependencies from `pyproject.toml` and `uv.lock`.
- `uv run silaba.py` launches the desktop app locally.
- `uv run python -m py_compile *.py` performs a fast syntax smoke test across the repo.

Before running the app, authenticate `gcloud` with a project that can access Text-to-Speech. If needed, update `_projeto_google_cloud` in `fala_rest.py`.

## Coding Style & Naming Conventions
Follow the existing style: 4-space indentation, straightforward functions, and minimal abstraction. Module and function names use `snake_case`; constants use `UPPER_CASE` such as `_FONTE`. This codebase already uses Portuguese identifiers and strings, so preserve that convention in user-facing logic instead of mixing languages within the same feature.

Keep files ASCII unless accents are required for readable Portuguese output. Prefer small, focused helper functions over large classes.

## Testing Guidelines
There is no dedicated automated test suite yet. For every change, run `uv run python -m py_compile *.py` and then do a manual check with `uv run silaba.py`, especially for keyboard input, rendering, and audio playback. If you add logic-heavy code, place tests in a new `tests/` directory and name files `test_<module>.py`.

## Commit & Pull Request Guidelines
Recent history mixes short imperative commits in Portuguese with occasional prefixes such as `refactor:`. Keep commit subjects concise and action-oriented, for example `Adiciona suporte a acentos` or `refactor: extrai helper de render`.

Pull requests should describe the behavior change, mention any Google Cloud or credential impact, and include a screenshot or GIF when the UI changes. Link the relevant issue when one exists.

## Security & Configuration Tips
Do not commit credentials, access tokens, or generated `mp3/` files. Document any new environment or cloud prerequisites in `README.md` alongside code changes.

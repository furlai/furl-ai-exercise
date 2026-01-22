# Furl AI Exercise

Build a small AI-assisted service that returns the release details for a piece of software on a specific OS.

## Goal

Implement the scaffold so the system accepts a software query (vendor, software name, OS details) and returns a structure containing:

- `release_notes_url`
- `download_url`
- `version`

## Scenarios

This exercise includes three test scenarios for Mozilla Firefox:

- Windows 11 (x86_64) latest release (non-pinned; prints output; structure-only assertions)
- Windows 10 (x86_64) pinned to version 147.0.1
- Windows 7 (x86_64) pinned to the 115 ESR release

Each scenario is isolated in its own test file so more scenarios can be added later.
Pinned versions for the Windows 10 test live in `tests/scenario_data.py` for easy updates.

## Project layout

- `src/furl_ai_exercise/models.py`: data models
- `src/furl_ai_exercise/service.py`: core logic (scaffold)
- `tests/test_firefox_windows11.py`: scenario test
- `tests/test_firefox_windows10_pinned.py`: scenario test
- `tests/test_firefox_windows7_esr.py`: scenario test

## What you need to implement

Fill in the TODO in `src/furl_ai_exercise/service.py` inside `run_release_graph`:

- Build and execute the LangGraph graph using a LangChain-compatible model
- Parse the JSON response into `ReleaseInfo`

The goal is for the test to pass by implementing an agentic system that performs research and sarisfies the test cases.

You may update the prompt and graph structure as you see fit. The scaffolding provides
helpers (`build_prompt`, `build_release_graph`) for convenience, but they are not mandatory.

Implementation expectations for `run_release_graph`:

- Build or reuse a `StateGraph` that accepts the `ReleaseState` keys: `query` and `response`
- Invoke the graph with the incoming `SoftwareQuery` and capture the model output


Avoid modifying tests or the data models; the exercise is intentionally scoped to the graph execution.

You will need to create a graph of agents / subagents to perform research and fulfill the task.

## Input / output shape

Input (`SoftwareQuery`):

- `vendor` (str)
- `software` (str)
- `os_name` (str)
- `os_version` (str)
- `cpu_arch` (str)
- `version` (str, optional; omit for latest lookups, set for pinned lookups)

Output (`ReleaseInfo`):

- `release_notes_url` (str)
- `download_url` (str)
- `version` (str)

Graph state (`ReleaseState`):

- `query` (`SoftwareQuery`)
- `response` (str)

## Submission

Submit the assignment to careers <at> furl <dot> ai. Before submission, run `poetry run pytest` to validate the test cases pass (they mail fail due to nuanced mistakes, like slight URL mismatches, which is fine--but significant differences in URLs for download links etc. will be highly considered as part of scoring). Zip up the entire directory, and include a testcases.txt file containing the result of your run of `poetry run pytest` (note that it'll be executed in a sandbox by Furl). Include chatlog.txt if you used an agentic coding tool such as Claude Code, Cursor, Ampcode, Codex, etc.

## LLM configuration

This project uses LangChain + LangGraph. Bring any LangChain-compatible chat model or runnable. Anthropic and OpenAI are provided out of the box.

Provide your provider's API key as required (e.g. `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).
Refer to the model provider docs for exact environment variables.

## Setup

1. `cd furl-ai-exercise`
2. `poetry install`
3. `poetry run pytest`

## Notes

- Ideal imementations will not overfit to Firefox, and instead will be generalizable across any software / OS.
- Python version is defined in `pyproject.toml` (`^3.12`).
- Agentic coding tools are allowed (Codex, Claude Code, Cursor, etc.) as long as you submit the full chat log with your assignment.

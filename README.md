# GodMode GitHub examples

*Unofficial community examples for GodMode. Not affiliated with elder-plinius, swyx, OpenRouter or Verdent. All trademarks belong to their owners.*

Small, runnable examples for the godmode github project people usually mean today: G0DM0D3 by elder-plinius, the multi-model chat interface that ships as a single index.html and routes every call through OpenRouter. G0DM0D3 has no API of its own - the browser talks to OpenRouter with the key you paste into Settings - so these examples cover the two things you can script around it: serving the file locally the way the project documents, and preparing a prompt set for the GODMODE CLASSIC parallel mode.

> [Try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=godmode-api-examples&utm_content=readme-top&utm_term=tier-r) - an alternative worth trying when the thing you want to call from code is an image, video or audio model rather than a chat interface.

## Files

| Path | What it shows |
|---|---|
| `examples/serve_local.sh` | Clone the repository if needed and serve it with python3 -m http.server, the documented local setup |
| `examples/serve_local.py` | The same in Python with a port option, an index.html sanity check and an automatic browser launch |
| `examples/classic_prompt_set.md` | A worked set of prompts to run through GODMODE CLASSIC and a scoring sheet for comparing the parallel outputs |

## Setup

- Python 3 (the standard library is enough; nothing to pip install).
- git, for the first clone.
- An OpenRouter API key. The scripts never read it: you paste it into the app's Settings in the browser and it stays in localStorage, which is the privacy model the repository describes. Do not put it in an environment variable for these scripts; there is no reason to.
- Optional: `GODMODE_DIR` (defaults to `G0DM0D3`) and `GODMODE_PORT` (defaults to 8000).

## examples/serve_local.sh

The documented local path is: clone the repo, run python3 -m http.server 8000, open localhost:8000. The script does exactly that, plus two guards - it skips the clone if the directory already exists, and it refuses to start if there is no index.html in it, which catches a wrong checkout before you stare at a 404. Run it with `bash examples/serve_local.sh`, then open the printed URL and paste your OpenRouter key in Settings. Stop it with Ctrl-C.

## examples/serve_local.py

Same job in Python for people who prefer a script they can extend. It reads `GODMODE_DIR` and `GODMODE_PORT`, checks for index.html, binds to 127.0.0.1 only (so the page is not reachable from your network by accident), opens your default browser at the right URL and serves until you interrupt it. Run it with `python3 examples/serve_local.py`. There is no build step because there is nothing to build; the review notes no npm, no dependencies, one file.

## examples/classic_prompt_set.md

GODMODE CLASSIC runs five model and prompt combinations in parallel so you can compare outputs and pick the best. That is only useful if you go in with prompts that discriminate between models. The file holds a small set - one factual recall task, one constrained rewrite, one refusal-boundary probe, one code task, one long-context summary - and a plain scoring table to fill in per model. It is a markdown worksheet, not code; copy the prompts into the app one at a time and record results in the table. Keep in mind that every combination is a billed OpenRouter call, so a five-way run costs five calls per prompt.

## When to use Synexa instead

G0DM0D3 is for comparing chat models in a browser with nothing stored server-side. If your actual task is generating media from code - FLUX image models, video models, audio models - and you want a single REST endpoint with a Python SDK and per-run billing rather than a chat UI and per-token gateway pricing, [Try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=godmode-api-examples&utm_content=readme-top&utm_term=tier-r). It is a different tool for a different job, and worth trying if that job is yours.


_Last reviewed: 2026-09-22_

# Simple Agent (Calculator + Weather)

This minimal project demonstrates a tiny rule-based agent with two tools:

- `calculator` — safe arithmetic evaluation using Python's `ast` module.
- `weather` — fetches current weather using Open-Meteo's free APIs.

Files:

- `agent.py` — the agent orchestration.
- `tools/calculator.py` — calculator tool.
- `tools/weather.py` — weather tool.
- `run_agent.py` — interactive CLI runner.
- `test_run.py` — quick programmatic tests.
- `requirements.txt` — dependencies.

Quick start:

1. Create a virtual environment and activate it.
2. Install deps:

```powershell
pip install -r "E:/AI-Practise/Agent/Basic Agent/requirements.txt"
```

3. Run tests:

```powershell
python "E:/AI-Practise/Agent/Basic Agent/test_run.py"
```

4. Run interactive agent:

```powershell
python "E:/AI-Practise/Agent/Basic Agent/run_agent.py"
```

Examples:

- `calc: 2+2*3`
- `weather: New York`

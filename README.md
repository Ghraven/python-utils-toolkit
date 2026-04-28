# 🐍 python-utils-toolkit

A collection of practical, production-ready Python utilities I built while
working on trading bots, AI agent systems, and automation pipelines. Pure
Python — no heavy dependencies.

## Contents

| Module | What it does |
|---|---|
| `utils/retry.py` | `@retry` decorator with exponential backoff and jitter |
| `utils/rate_limiter.py` | Token-bucket rate limiter (sync + async) |
| `utils/timer.py` | `@timer` decorator + `Timer` context manager |
| `utils/file_helpers.py` | Safe read/write, atomic saves, JSON/YAML shortcuts |
| `utils/logger.py` | One-call structured logging setup with colour + file rotation |
| `utils/env.py` | Typed `.env` / environment variable loader |
| `examples/` | Working scripts showing each utility |

## Quick start

```bash
git clone https://github.com/Ghraven/python-utils-toolkit
cd python-utils-toolkit
pip install -r requirements.txt
python examples/retry_demo.py
```

## Examples

### Retry with backoff
```python
from utils.retry import retry

@retry(max_attempts=3, base_delay=1.0, exceptions=(ConnectionError,))
def fetch_price(symbol: str) -> float:
    # Retries up to 3 times with exponential backoff on ConnectionError
    return api.get_price(symbol)
```

### Rate limiter
```python
from utils.rate_limiter import RateLimiter

limiter = RateLimiter(calls_per_second=5)

for symbol in watchlist:
    limiter.acquire()          # blocks until a token is available
    price = fetch_price(symbol)
```

### Timer
```python
from utils.timer import timer, Timer

@timer
def run_analysis():
    ...

with Timer("market scan") as t:
    scan_market()
print(f"Scan took {t.elapsed:.2f}s")
```

### Structured logging
```python
from utils.logger import get_logger

log = get_logger("trading_bot", level="INFO", log_file="bot.log")
log.info("Signal detected", extra={"symbol": "BTC", "signal": "BUY"})
```

## Why I built this

These utilities came directly from building my crypto futures trading bot
and multi-agent AI systems. When you're calling exchange APIs, running LLM
chains, and processing streams, you need reliable retry logic, rate limiting,
and clean logging — without pulling in a huge framework.

## License

MIT

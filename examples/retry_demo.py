"""Demo: retry decorator with exponential backoff."""

import random
from utils.retry import retry
from utils.logger import get_logger

log = get_logger("demo")

call_count = 0

@retry(max_attempts=4, base_delay=0.1, exceptions=(ConnectionError,))
def unstable_api_call() -> str:
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError(f"Simulated failure #{call_count}")
    return "success"

if __name__ == "__main__":
    result = unstable_api_call()
    log.info("Result: %s (took %d attempts)", result, call_count)

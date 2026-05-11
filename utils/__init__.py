"""python-utils-toolkit — practical Python utilities.

Import individual modules directly:
    from utils.retry import retry
    from utils.rate_limiter import RateLimiter, AsyncRateLimiter
    from utils.logger import get_logger

Or import this package for the public API surface:
    from utils import retry, RateLimiter, get_logger, Env, timer, Timer
"""

from utils.async_utils import (
    run_with_timeout,
    gather_with_errors,
    async_retry,
)
from utils.cache_utils import TTLCache, memoize
from utils.crypto_utils import hmac_sign, sha256_hex, md5_hex
from utils.datetime_utils import utc_now, format_ts, parse_ts, humanize_delta
from utils.dict_utils import deep_merge, safe_get, flatten_dict
from utils.env import Env
from utils.file_helpers import safe_read, safe_write, atomic_write
from utils.list_utils import chunk, dedup, flatten
from utils.logger import get_logger
from utils.number_utils import format_number, round_to, pct_change
from utils.rate_limiter import RateLimiter, AsyncRateLimiter
from utils.retry import retry
from utils.string_utils import slugify, truncate, camel_to_snake, snake_to_camel
from utils.timer import timer, Timer
from utils.validation_utils import is_int, is_float, is_non_empty_str, guard_type

__all__ = [
    # async
    "run_with_timeout", "gather_with_errors", "async_retry",
    # cache
    "TTLCache", "memoize",
    # crypto
    "hmac_sign", "sha256_hex", "md5_hex",
    # datetime
    "utc_now", "format_ts", "parse_ts", "humanize_delta",
    # dict
    "deep_merge", "safe_get", "flatten_dict",
    # env
    "Env",
    # file
    "safe_read", "safe_write", "atomic_write",
    # list
    "chunk", "dedup", "flatten",
    # logger
    "get_logger",
    # number
    "format_number", "round_to", "pct_change",
    # rate limiter
    "RateLimiter", "AsyncRateLimiter",
    # retry
    "retry",
    # string
    "slugify", "truncate", "camel_to_snake", "snake_to_camel",
    # timer
    "timer", "Timer",
    # validation
    "is_int", "is_float", "is_non_empty_str", "guard_type",
]

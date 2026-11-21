# Timing Attacks and Constant-Time Comparison

When a server checks whether a submitted token, API key, or hash matches an expected value, the way it compares the two strings or byte arrays matters.

## How an Early-Exit Comparison Can Leak Information

Many standard string or byte-array equality checks compare values from left to right and stop as soon as they find a mismatch:

```text
Expected: a7f91c...
Guess 1:  000000...  -> mismatch at byte 0 -> returns false after about 1 step
Guess 2:  a70000...  -> mismatch at byte 2 -> returns false after about 3 steps
Guess 3:  a7f900...  -> mismatch at byte 4 -> returns false after about 5 steps
```

Because Guess 3 matches more bytes before failing than Guess 1, it may take slightly longer to reject. Even if the difference is only nanoseconds or microseconds, an attacker who sends many requests and measures response times may be able to reduce the effects of network jitter and infer how much of a guess is correct. This can turn a blind guess into a byte-by-byte search.

## How Constant-Time Comparison Helps

A constant-time comparison function is designed to inspect every byte, even if an earlier byte differs. It accumulates the differences (typically using bitwise operations such as XOR and OR) and returns a result only after checking all \(N\) bytes.

Because the amount of work is designed not to depend on where a mismatch occurs, timing should not reveal how close a guess was. In practice, use a vetted constant-time comparison function provided by a trusted library; ordinary equality checks may exit early.
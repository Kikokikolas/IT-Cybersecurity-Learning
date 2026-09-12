# Memory

The Memory panel is used to analyze JavaScript memory usage and detect memory leaks.

### Heap Snapshot
Shows the JavaScript objects currently stored in heap memory

### Allocations on Timeline
Records memory allocations over time and helps identify objects that remain in memory unexpectedly.

### Detached elements
Finds DOM elements that were removed from the page
but are still referenced by JavaScript.

### Garbage Collection

JavaScript automatically removes unreachable objects from memory
through garbage collection.


A memory leak occurs when unused objects remain reachable
and therefore cannot be garbage collected.

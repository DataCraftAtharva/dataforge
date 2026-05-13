# Mutability vs Immutability

---

## Why This Exists

One of the biggest causes of bugs in Python systems is:

> unexpected mutation

Many engineers accidentally modify shared objects without realizing it.

This causes problems in:

- ETL pipelines
- Airflow DAG configs
- Spark jobs
- API payload processing
- ML preprocessing
- caching systems

Understanding mutability helps engineers:

- avoid hidden bugs
- write predictable code
- debug faster
- optimize memory
- safely share objects

This topic becomes the foundation for:

- copying
- function arguments
- object sharing
- configuration management
- memory optimization

---

## Simple Explanation (10-Year-Old Level)

Some Python objects can change.

Some cannot.

### Mutable

Can change after creation.

Example:

```python
shopping_cart = ["milk", "bread"]
```

You can add:

```python
shopping_cart.append("eggs")
```

Same object changed.

---

### Immutable

Cannot change after creation.

Example:

```python
pipeline_name = "customer_ingestion"
```

You cannot modify the string itself.

Python creates a new object instead.

---

## Mental Model

### Immutable Object

```text
"hello"

❌ Cannot change
```

When you try:

```python

name = name.upper()

```

Python creates:

```text
NEW object
```

Memory:

```text
Old Object:

"hello"

New Object:

"HELLO"
```

---

### Mutable Object

```text
[1, 2, 3]

✅ Can change
```

When you do:

```python
numbers.append(4)
```

Python modifies:

```text
same object
```

No new object created.

---

## Core Concept

### Mutation

Changes the SAME object.

Example:

```python
customer_ids.append("cust_104")
```

Same memory.

---

### Reassignment

Creates a NEW binding.

Example:

```python
customer_ids = ["cust_201"]
```

Variable now points somewhere else.

---

## Realistic Industry Example

Imagine:

Shared ETL config.

```python
pipeline_config = {
    "batch_size": 1000,
    "retry_count": 3
}
```

Engineer writes:

```python
runtime_config = pipeline_config

runtime_config["batch_size"] = 10000
```

Unexpected result:

```python
pipeline_config
```

also changes.

Why?

Because dictionary is:

```text
mutable
```

This creates hidden production bugs.

---

## PyCharm Experiment

File:

```text
03_mutability_vs_immutability.py
```

Goal:

Understand:

- mutable objects
- immutable objects
- mutation
- reassignment
- memory behavior

---

## What This Code Proves

- Immutable objects create new memory
- Mutable objects change in place
- `id()` changes for reassignment
- `id()` stays same for mutation
- Mutation ≠ reassignment

---

## DSA Connection

Mutability matters heavily in algorithms.

### Space Complexity

Immutable operations may create:

```text
new objects
```

Extra memory cost.

Example:

String concatenation:

```python
result = result + char
```

Can become expensive.

---

### Matrix Bug (Classic Interview Trap)

Problem:

```python
grid = [[0] * 3] * 3
```

Looks fine.

But:

```python
grid[0][0] = 1
```

Output:

```python
[
 [1,0,0],
 [1,0,0],
 [1,0,0]
]
```

Why?

Shared mutable references.

Very common interview problem.

---

### Recursive Algorithms

Mutating shared lists can break recursion.

Example:

Backtracking algorithms.

If state isn't copied properly:

Results become corrupted.

---

## Memory & Performance Considerations

### Immutable Objects

Safer.

But may create:

```text
extra memory allocations
```

Example:

Repeated string concatenation.

Bad:

```python
text = ""

for word in words:
    text += word
```

Better:

```python
" ".join(words)
```

---

### Mutable Objects

Memory efficient.

But dangerous if shared.

Tradeoff:

```text
performance vs safety
```

Engineers must balance both.

---

## Production Debugging Scenario

ETL pipeline issue:

Unexpected batch size increase.

Bug:

```python
def process_pipeline(config):
    config["batch_size"] = 50000
```

Team assumed:

```text
local config change
```

Reality:

Original config modified.

Result:

- memory spikes
- API throttling
- ingestion failures

Root cause:

Mutable shared dictionary.

---

## Common Mistakes (Interview Traps)

### Beginner Mistakes

❌ Thinking reassignment = mutation

❌ Forgetting lists are mutable

❌ Assuming strings change in place

---

### Intermediate Mistakes

❌ Shared mutable configs

❌ Nested list mutation bugs

❌ Confusing copy vs assignment

---

### Production Mistakes

❌ Accidentally mutating pipeline settings

❌ Hidden side effects in APIs

❌ Shared state bugs

---

### Major Interview Trap

Mutable default arguments:

Bad:

```python
def add_user(user, users=[]):
    users.append(user)
    return users
```

Why dangerous?

Because same list persists across calls.

---

## Interview Questions

### Beginner

Q:
What is mutability?

Answer:

Ability of an object to change after creation.

---

### Intermediate

Q:
Difference between mutation and reassignment?

Answer:

Mutation changes same object.

Reassignment creates new binding.

---

### Advanced

Q:
Why does this happen?

```python
config = base_config

config["batch_size"] = 5000
```

Answer:

Dictionary is mutable.

Both variables reference same object.

---

### Trick Question

Q:
Are tuples always immutable?

Answer:

Tuple structure is immutable.

But tuple can contain mutable objects.

Example:

```python
data = ([1,2], [3,4])
```

Inner lists can still change.

---

## Key Takeaways

- Mutable objects change in place
- Immutable objects create new objects
- Mutation ≠ reassignment
- Lists/dicts are mutable
- Strings/ints are immutable
- Mutability affects function behavior
- Shared mutable state creates bugs

---

## Related Topics

- Variables Objects Memory
- Names References Assignment
- Shallow Copy
- Deep Copy
- Function Arguments
- Mutable Default Arguments
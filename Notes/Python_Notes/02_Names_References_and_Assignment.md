# Names, References & Assignment

---

## Why This Exists

Many engineers misunderstand what assignment does in Python.

They assume:

```python
a = b
```

creates a copy.

It does NOT.

This misunderstanding causes bugs in:

- ETL pipelines
- shared configurations
- Spark jobs
- API payload processing
- ML preprocessing
- caching systems

Understanding assignment behavior helps engineers:

- debug faster
- avoid accidental mutation
- reason about memory usage
- write predictable code

This topic becomes the foundation for:

- mutability
- copying
- function arguments
- object sharing
- memory optimization

---

## Simple Explanation (10-Year-Old Level)

In Python:

- **Names are labels**
- **Objects live in memory**
- **Assignment (`=`)** means:

> “Attach this name to that object.”

Python does NOT automatically copy objects.

Example:

```python
daily_orders = monthly_orders
```

Python says:

> “Both labels now point to the same thing.”

---

## Mental Model

Think of names like sticky notes.

```text
Memory:

[ Customer Dataset ]

Labels:

raw_data ─────────▶ dataset

processed_data ──▶ dataset
```

Both names point to:

```text
same object
```

Meaning:

Changes through one name affect the same underlying object.

---

## Core Concept

When Python executes:

```python
processed_orders = raw_orders
```

Python does NOT:

```text
copy raw_orders
```

Instead:

It binds:

```text
processed_orders
```

to the same object.

Meaning:

```text
raw_orders ─────────▶ object ◀──────── processed_orders
```

Assignment creates references.

Not copies.

---

## Realistic Industry Example

Imagine an ETL pipeline.

Raw data:

```python
raw_customer_records = [
    "customer_1",
    "customer_2"
]
```

Engineer writes:

```python
processed_customer_records = raw_customer_records
```

Then:

```python
processed_customer_records.clear()
```

Unexpected result:

```python
raw_customer_records
```

also becomes empty.

Why?

Because both names referenced the same object.

This is a classic production bug.

---

## PyCharm Experiment

File:

```text
02_names_references_assignment.py
```

Goal:

Understand:

- assignment
- shared references
- mutation
- rebinding

---

## What This Code Proves

- Assignment never copies objects
- Multiple names can reference same object
- Mutation affects all references
- Rebinding affects only one name
- Mutable and immutable objects behave differently

---

## DSA Connection

Understanding references matters in algorithms.

### Space Complexity

Example:

```python
new_array = original_array
```

Memory:

```text
O(1)
```

No copy created.

But:

```python
new_array = original_array.copy()
```

Memory:

```text
O(n)
```

Because new structure is created.

This distinction matters in:

- graph problems
- matrix problems
- DP optimization
- sliding window problems

---

### Classic DSA Interview Bug

Problem:

```python
grid = [[0] * 3] * 3
```

Looks fine.

But:

```python
grid[0][0] = 1
```

Unexpected output:

```python
[
 [1,0,0],
 [1,0,0],
 [1,0,0]
]
```

Reason:

Shared references.

Interviewers love this question.

---

## Memory & Performance Considerations

Bad engineers accidentally duplicate large objects.

Example:

Imagine:

10GB customer dataset.

Doing unnecessary copies:

```python
processed_data = raw_data.copy()
```

can increase:

- RAM usage
- ETL execution time
- Spark memory pressure

Understanding references helps optimize memory.

---

## Production Debugging Scenario

Pipeline bug:

```python
runtime_config = base_config

runtime_config["batch_size"] = 100000
```

Engineer assumed:

```text
runtime_config
```

was independent.

Reality:

Both names referenced same config.

Result:

- API throttling
- memory spikes
- failed ingestion job

Root cause:

Misunderstanding assignment.

---

## Common Mistakes (Interview Traps)

### Beginner Mistakes

❌ Thinking `=` copies objects

❌ Thinking variables contain values

❌ Treating Python like C/Java

---

### Intermediate Mistakes

❌ Forgetting mutable side effects

❌ Shared nested structures

❌ Unexpected mutations

---

### Production Mistakes

❌ Accidentally mutating configs

❌ Clearing shared datasets

❌ Large memory waste

---

## Interview Questions

### Beginner

Q:
What happens during assignment?

```python
a = b
```

Answer:

Python binds `a` to the same object as `b`.

No copy happens.

---

### Intermediate

Q:
Why does this happen?

```python
data = raw_data
data.clear()
```

Answer:

Both variables point to same object.

Mutation affects shared references.

---

### Advanced

Q:
Explain difference between:

```python
a = b
```

and

```python
a = b.copy()
```

Answer:

Assignment shares reference.

Copy creates new object.

---

### Trick Question

Q:
Is Python pass-by-reference?

Answer:

Python uses:

> pass-by-object-reference

(or pass-by-assignment)

---

## Key Takeaways

- Assignment binds names
- Assignment does NOT copy
- Multiple references can exist
- Mutation affects shared objects
- Rebinding changes one name only
- References affect memory efficiency

---

## Related Topics

- Variables Objects Memory
- Mutability vs Immutability
- Shallow Copy
- Deep Copy
- Function Arguments
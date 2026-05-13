# Copy vs Shallow Copy vs Deep Copy

---

## Why This Exists

One of the biggest production bugs happens when engineers think:

```python
copied_data = original_data
```

creates a new object.

It does NOT.

This misunderstanding causes:

- corrupted ETL pipelines
- unexpected config changes
- broken API payloads
- nested JSON mutation bugs
- Spark transformation side effects

Understanding copying helps engineers:

- safely modify data
- avoid shared state bugs
- optimize memory usage
- debug nested structures

---

## Simple Explanation (10-Year-Old Level)

Imagine a notebook.

### Assignment

You and your friend share:

```text
same notebook
```

If one writes:

Both see changes.

---

### Shallow Copy

You get:

```text
new notebook cover
```

But inner pages are shared.

Some changes still affect both.

---

### Deep Copy

You get:

```text
brand new notebook
```

Everything independent.

No shared pages.

---

## Core Concept

### Assignment

```python
processed_data = raw_data
```

Creates:

```text
same object reference
```

No copy.

---

### Shallow Copy

```python
processed_data = raw_data.copy()
```

Creates:

```text
new outer object
```

But nested objects remain shared.

---

### Deep Copy

```python
import copy

processed_data = copy.deepcopy(raw_data)
```

Creates:

```text
fully independent copy
```

Including nested objects.

---

## Realistic Industry Example

Imagine nested API payload.

```python
customer_data = {
    "customer_id": 101,
    "orders": [
        {
            "product": "Laptop",
            "price": 70000
        }
    ]
}
```

Engineer wants safe transformation.

Wrong approach:

```python
transformed = customer_data.copy()
```

Hidden problem:

Nested:

```python
orders
```

still shared.

Production bug appears.

---

## PyCharm Experiment

File:

```text
04_copy_vs_shallow_vs_deep_copy.py
```

Goal:

Understand:

- assignment
- shallow copy
- deep copy
- nested mutation

---

## What This Code Proves

- Assignment shares object
- Shallow copy copies outer layer
- Deep copy copies everything
- Nested mutation causes bugs

---

## DSA Connection

Copying impacts:

### Space Complexity

Assignment:

```text
O(1)
```

No memory.

---

Shallow copy:

```text
O(n)
```

Outer structure copied.

---

Deep copy:

```text
Higher memory cost
```

Entire nested structure duplicated.

In interviews:

Choosing wrong copy strategy can fail optimization.

---

## Memory & Performance Considerations

Deep copy is safest.

But expensive.

Bad:

```python
deepcopy(big_dataset)
```

inside loop.

Can destroy performance.

Production engineers balance:

```text
Safety vs Performance
```

---

## Production Debugging Scenario

Pipeline bug:

Revenue unexpectedly changed.

Cause:

```python
processed_orders = raw_orders.copy()
```

Nested records shared.

Transformation accidentally modified original dataset.

Root cause:

Shallow copy misunderstanding.

---

## Common Mistakes (Interview Traps)

### Beginner Mistakes

❌ Thinking assignment copies

❌ Assuming `.copy()` copies everything

---

### Intermediate Mistakes

❌ Mutating nested JSON after shallow copy

❌ Using deepcopy unnecessarily

---

### Production Mistakes

❌ Deep copying huge datasets repeatedly

❌ Shared config corruption

---

## Correct Way / Best Practice

### Use Assignment

When:

```text
read-only access
```

Example:

```python
analytics_data = raw_data
```

---

### Use Shallow Copy

When:

```text
flat structures
```

Example:

```python
config.copy()
```

---

### Use Deep Copy

When:

```text
nested structures
```

Example:

API payloads

nested JSON

ETL transformations

---

## Interview Questions

### Beginner

Q:
Difference between assignment and copy?

---

### Intermediate

Q:
Why is `.copy()` dangerous?

---

### Advanced

Q:
When should you avoid `deepcopy()`?

Answer:

Large-scale systems.

High memory cost.

---

## Key Takeaways

- Assignment ≠ copy
- Shallow copy copies outer layer
- Deep copy copies everything
- Nested structures need caution
- Deep copy is safer but expensive

---

## Related Topics

- Variables Objects Memory
- Assignment
- Mutability
- Nested Data Structures
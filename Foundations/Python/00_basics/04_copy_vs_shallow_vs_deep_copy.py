"""
Topic:
Copy vs Shallow Copy vs Deep Copy

Goal:
Understand how copying works
in nested Python objects.

Industry Context:
ETL pipelines,
API payloads,
nested JSON processing.

Key Learning:
Not all copies are independent.
"""

import copy

print("=" * 60)
print("EXPERIMENT 1: ASSIGNMENT")
print("=" * 60)

raw_customer_data = {
    "customer_id": 101,
    "orders": ["Laptop", "Phone"]
}

processed_customer_data = raw_customer_data

processed_customer_data["customer_id"] = 999

print(raw_customer_data)

print("\nObservation:")
print("Assignment shares same object.")


# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 2: SHALLOW COPY")
print("=" * 60)

raw_customer_data = {
    "customer_id": 101,
    "orders": ["Laptop", "Phone"]
}

processed_customer_data = raw_customer_data.copy()

processed_customer_data["orders"].append("Tablet")

print(raw_customer_data)

print("\nObservation:")
print(
    "Outer object copied, "
    "inner list still shared."
)


# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 3: DEEP COPY")
print("=" * 60)

raw_customer_data = {
    "customer_id": 101,
    "orders": ["Laptop", "Phone"]
}

processed_customer_data = copy.deepcopy(raw_customer_data)

processed_customer_data["orders"].append("Tablet")

print(raw_customer_data)

print("\nObservation:")
print(
    "Deep copy created "
    "fully independent object."
)

# ==================================================

print("\n" + "=" * 60)
print("FINAL LEARNING SUMMARY")
print("=" * 60)

print("""
1. Assignment shares object

2. Shallow copy shares nested objects

3. Deep copy creates independence

4. Nested data structures are risky

5. Deep copy has performance cost
""")
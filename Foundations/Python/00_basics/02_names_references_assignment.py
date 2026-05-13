"""
Topic:
Names, References & Assignment

Goal:
Understand how assignment works in Python.

Industry Context:
ETL pipelines,
shared configs,
data processing systems.

Key Learning:
Assignment creates references.
It does NOT create copies.
"""

print("=" * 60)
print("EXPERIMENT 1: IMMUTABLE OBJECT ASSIGNMENT")
print("=" * 60)

# Daily pipeline limit

daily_batch_limit = 1000

# Shared assignment

backup_batch_limit = daily_batch_limit

print("Before Reassignment:\n")

print("Daily Batch:")
print(daily_batch_limit)

print("Object ID:")
print(id(daily_batch_limit))

print("\nBackup Batch:")
print(backup_batch_limit)

print("Object ID:")
print(id(backup_batch_limit))

# Rebinding

daily_batch_limit = 5000

print("\nAfter Reassignment:\n")

print("Daily Batch:")
print(daily_batch_limit)

print("Object ID:")
print(id(daily_batch_limit))

print("\nBackup Batch:")
print(backup_batch_limit)

print("Object ID:")
print(id(backup_batch_limit))

print("\nObservation:")
print(
    "Immutable reassignment created "
    "a new object binding."
)


# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 2: MUTABLE OBJECT ASSIGNMENT")
print("=" * 60)

# Customer ingestion dataset

raw_customer_records = [
    "customer_1",
    "customer_2",
    "customer_3"
]

processed_customer_records = raw_customer_records

print("Before Modification:\n")

print(raw_customer_records)
print(id(raw_customer_records))

print(processed_customer_records)
print(id(processed_customer_records))

# Data cleaning step

processed_customer_records.append("customer_4")

print("\nAfter Modification:\n")

print(raw_customer_records)
print(processed_customer_records)

print("\nObservation:")
print(
    "Mutation affected both names "
    "because same object is shared."
)


# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 3: REBINDING")
print("=" * 60)

raw_customer_records = [
    "customer_1",
    "customer_2"
]

processed_customer_records = raw_customer_records

print("Before Rebinding:\n")

print(id(raw_customer_records))
print(id(processed_customer_records))

# New object assignment

processed_customer_records = [
    "clean_customer_1",
    "clean_customer_2"
]

print("\nAfter Rebinding:\n")

print(id(raw_customer_records))
print(id(processed_customer_records))

print("\nObservation:")
print(
    "Rebinding changed only one name."
)

# ==================================================

print("\n" + "=" * 60)
print("FINAL LEARNING SUMMARY")
print("=" * 60)

print("""
1. Assignment does not copy

2. Multiple names can share objects

3. Mutation affects shared references

4. Rebinding affects only one variable

5. References impact memory efficiency
""")
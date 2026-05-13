"""
Topic:
Variables, Objects & Memory Model

Goal:
Understand how Python variables
point to objects in memory.

Industry Context:
Data Engineering pipelines,
ETL configurations,
memory-efficient systems.

Key Learning:
Variables are labels bound to objects.
They do NOT store values.
"""

# ==================================================
# Experiment 1: Variable Binding
# ==================================================

print("=" * 50)
print("EXPERIMENT 1: VARIABLE BINDING")
print("=" * 50)

# Imagine this controls daily ETL volume

daily_order_count = 1000

print("Daily Order Count:")
print(daily_order_count)

# id() gives object identity
# Think of it as memory identity

print("\nObject Identity:")
print(id(daily_order_count))

print("\nExplanation:")
print("daily_order_count points to object 1000")


# ==================================================
# Experiment 2: Shared References
# ==================================================

print("\n" + "=" * 50)
print("EXPERIMENT 2: SHARED REFERENCES")
print("=" * 50)

# Base ETL configuration

base_pipeline_config = {
    "pipeline_name": "customer_ingestion",
    "batch_size": 1000,
    "retry_count": 3
}

# Runtime config

runtime_pipeline_config = base_pipeline_config

print("Before Modification:\n")
print(base_pipeline_config)

# Runtime change

runtime_pipeline_config["batch_size"] = 5000

print("\nAfter Runtime Change:\n")
print(base_pipeline_config)

print("\nObservation:")
print(
    "Changing runtime config also changed "
    "base config due to shared reference."
)


# ==================================================
# Experiment 3: Reassignment
# ==================================================

print("\n" + "=" * 50)
print("EXPERIMENT 3: REASSIGNMENT")
print("=" * 50)

# Initial batch size

primary_batch_size = 1000

# Another reference

backup_batch_size = primary_batch_size

print("Before Reassignment:\n")

print("Primary Batch ID:")
print(id(primary_batch_size))

print("Backup Batch ID:")
print(id(backup_batch_size))

# Reassignment

primary_batch_size = 5000

print("\nAfter Reassignment:\n")

print("Primary Batch ID:")
print(id(primary_batch_size))

print("Backup Batch ID:")
print(id(backup_batch_size))

print("\nObservation:")
print(
    "Reassignment created a new binding. "
    "backup_batch_size still points "
    "to old object."
)


# ==================================================
# Final Learning Summary
# ==================================================

print("\n" + "=" * 50)
print("FINAL LEARNING SUMMARY")
print("=" * 50)

print("""
1. Variables are labels

2. Objects live in memory

3. Assignment creates references

4. Assignment does NOT copy

5. Reassignment changes binding

6. Shared references can create bugs
""")
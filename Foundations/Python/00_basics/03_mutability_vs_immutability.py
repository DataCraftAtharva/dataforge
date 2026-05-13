"""
Topic:
Mutability vs Immutability

Goal:
Understand how mutable and immutable
objects behave in memory.

Industry Context:
ETL pipelines,
shared configs,
memory-efficient systems.

Key Learning:
Mutation changes same object.
Reassignment creates new binding.
"""

print("=" * 60)
print("EXPERIMENT 1: IMMUTABLE OBJECT")
print("=" * 60)

# Pipeline threshold

daily_batch_limit = 1000

print("Initial Value:")
print(daily_batch_limit)

print("\nObject ID:")
print(id(daily_batch_limit))

# Reassignment

daily_batch_limit = daily_batch_limit + 500

print("\nAfter Reassignment:")

print(daily_batch_limit)

print("\nNew Object ID:")
print(id(daily_batch_limit))

print("\nObservation:")
print(
    "Immutable reassignment "
    "created a new object."
)


# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 2: MUTABLE OBJECT")
print("=" * 60)

# Pipeline sources

data_sources = [
    "customer_api",
    "sales_database"
]

print("Before Mutation:\n")

print(data_sources)
print(id(data_sources))

# Mutation

data_sources.append("inventory_system")

print("\nAfter Mutation:\n")

print(data_sources)
print(id(data_sources))

print("\nObservation:")
print(
    "List changed in place. "
    "Same memory object used."
)


# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 3: SHARED MUTABLE BUG")
print("=" * 60)

base_pipeline_config = {
    "batch_size": 1000,
    "retry_count": 3
}

runtime_pipeline_config = base_pipeline_config

runtime_pipeline_config["batch_size"] = 10000

print("Base Config:\n")
print(base_pipeline_config)

print("\nRuntime Config:\n")
print(runtime_pipeline_config)

print("\nObservation:")
print(
    "Dictionary mutation affected "
    "both references."
)


# ==================================================

print("\n" + "=" * 60)
print("FINAL LEARNING SUMMARY")
print("=" * 60)

print("""
1. Mutable objects change in place

2. Immutable objects create new objects

3. Mutation is different from reassignment

4. Shared mutable state causes bugs

5. Lists and dictionaries are mutable
""")
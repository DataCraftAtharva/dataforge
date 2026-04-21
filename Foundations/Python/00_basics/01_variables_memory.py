# variables_memory.py
# Topic: Variables, Objects, Memory (Real Data Engineering Context)

# -------------------------------
# STEP 1: Real-world variables
# -------------------------------
print("--STEP 1: Real-world variables--")
pipeline_name = "Daily Sales Pipeline"
batch_size = 100
retry_limit = 3

print("Pipeline:", pipeline_name)
print("Batch size:", batch_size)
print("Retry limit:", retry_limit)

# -------------------------------
# STEP 2: Memory Identity
# -------------------------------
print("--STEP 2: Memory Identity--")
another_batch = batch_size
print("Memory Check")
print("batch_size id:", id(batch_size))
print("another_batch id:", id(another_batch))

# -------------------------------
# STEP 3: Reassignment
# -------------------------------
print("--STEP 3: Reassignment--")
batch_size = 500
print("After reassignment:")
print("batch_size:", batch_size, id(batch_size))
print("another_batch:", another_batch, id(another_batch))

# -------------------------------
# STEP 4: Real-world config (IMPORTANT)
# -------------------------------
print("--STEP 4: Real-world config (IMPORTANT)--")
pipeline_config = {'batch_size':100,'retry_limit':4}
print("\nInitial config:", pipeline_config)

# -------------------------------
# STEP 5: Mutation (Hidden Bug)
# -------------------------------
print("--STEP 5: Mutation (Hidden Bug)--")
def update_config(config):
    config["batch_size"]=200

update_config(pipeline_config)

print("After update_config (BUG):", pipeline_config)

# -------------------------------
# STEP 6: Safe Approach
# -------------------------------
print("--STEP 6: Safe Approach--")
import copy

def safe_update_config(config):
    new_config = copy.deepcopy(config)
    new_config["batch_size"]=300
    return new_config

safe_config = safe_update_config(pipeline_config)
print("\nOriginal config:", pipeline_config)
print("Safe updated config:", safe_config)






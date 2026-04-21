# Variables & Memory (Data Engineering Context)

## Simple Explanation
Variables are labels pointing to objects in memory.

## Real-World Context
Used in:
- pipeline configs
- batch processing
- API parameters

## Code Experiment
See implementation: [01_variables_memory.py](../../Foundations/Python/00_basics/01_variables_memory.py)

## Mental Model
batch_size → 100  
another_batch → same object  

## Failure Case
A pipeline config dictionary was modified inside a function.

Result:
Unexpected changes across the system.

## Fix Pattern
Use deepcopy to avoid shared state mutation.

## Production Insight
Mutable objects can silently break pipelines.

## Performance Consideration
Deepcopy is safe but costly for large data.

## Interview Notes
- Variables are references
- Python uses pass-by-object-reference
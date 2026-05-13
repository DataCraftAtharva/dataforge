# Lists & Dictionaries (Data Engineering Context)

---

## 1. Simple Explanation

- **List** → Ordered collection of items  
- **Dictionary (Dict)** → Key-value mapping (like HashMap)

---

## 2. Mental Model

List:
["click", "view", "purchase"]

Dict:
{
  "click": 3,
  "view": 2
}

---

## 3. Real-World Usage (Data Engineering)

- Lists:
  - event streams
  - logs
  - batch data

- Dictionaries:
  - aggregations (GROUP BY)
  - configuration
  - fast lookups

---

## 4. Core Operations

### List

- Access → list[i]
- Add → append()
- Remove → remove()
- Iterate → for item in list

### Dictionary

- Add/Update → dict[key] = value
- Access → dict[key]
- Safe access → dict.get(key, default)
- Iterate → for key, value in dict.items()

---

## 5. Code Example (Aggregation System)

```python
user_events = ["click", "view", "click", "purchase"]

event_count = {}

for event in user_events:
    if event in event_count:
        event_count[event] += 1
    else:
        event_count[event] = 1

print(event_count)
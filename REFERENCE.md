# PyAlgorithms reference #
## Search functions ##
### *Importing* ###
```python
from pyalgorithms.search import *
```
---
### MAX function ###
```python
max(array: list) -> int
```
**Parameters:**
- `array: list` - list of numberic values

**Returns:**

- `max_value: int` - the highest value within given list
---
### MIN function ###
```python
min(array: list) -> int
```
**Parameters:**

- `array: list` - list of numberic values

**Returns:**

- `min_value: int` – the lowest value within given list


## Sorting functions ##
### *Importing* ###
```python
from pyalgorithms.sorting import *
```
---
### QUICK SORT function ###
```python
quick_sort(array: list, desc: bool = False) -> int
```
**Parameters:**

- `array: list` - list with numeric values to be sorted with quick sort algorithm
- `desc: bool` - flag if list should be sorted descending (by default its sorted ascending)

**Returns:**

- `array: list` – sorted list
---
### BUBBLE SORT function ###
```python
bubble_sort(array: list, desc: bool = False) -> int
```
**Parameters:**

- `array: list` - list with numeric values to be sorted with bubble sort algorithm
- `desc: bool` - flag if list should be sorted descending (by default its sorted ascending)

**Returns:**

- `array: list` – sorted list
---
### SELECT SORT function ###
```python
select_sort(array: list, desc: bool = False) -> int
```
**Parameters:**

- `array: list` - list with numeric values to be sorted with select sort algorithm
- `desc: bool` - flag if list should be sorted descending (by default its sorted ascending)

**Returns:**

- `array: list` – sorted list
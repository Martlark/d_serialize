Universal converter of all things Python to a dict.  So it can be serialized
to JSON. 

Usage:

```python
from d_serialize import d_serialize
from objects import SomeObject

some_object = SomeObject()
json_values = d_serialize(some_object)
```
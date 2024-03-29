d_serialize
===========

Universal converter of all things Python to a `dict`.  So it can be serialized
to `JSON`. 

Install
-------

pip install d-serialize

Usage:
------

```python
from d_serialize import d_serialize
from objects import SomeObject

some_object = SomeObject()
json_values = d_serialize(some_object)
```

Usage in Flask
--------------

```python
from d_serialize import d_serialize
from flask import jsonify
from objects import SomeObject

@app.route('/a_route')
def a_route():
    some_object = SomeObject()
    json_values = d_serialize(some_object)
    return jsonify(json_values)
```

d_serialize will enumerate all public properties of your object, set, list or `dict` and convert them
to a JSON allowable type.  IE:

    list, dictionary, string, float, integer or boolean.

Any property that is not one of these types will be converted to a `string`. Enumerables: `set`
and `tuple` will be converted to `list`.

Dictionary, set, tuple and list properties will be followed to ensure all child objects and
values are also converted.

Methods and private properties (starting with `_`) are not enumerated.

Any property or attribute that raises an exception will be excluded or
have a `None` value.

Complex objects that refer to themselves will have their str value as the 
recursive value instead of the entire complex value.

Example:
--------

Converting a Class instance.

```python
from d_serialize import d_serialize

class TestObject:
    number_value = 1
    float_value = 1.1

    def dont_call_me(self):
        """return self.number_value"""

print(d_serialize(TestObject()))

# dict(number_value=1, float_value=1.1)
```

Release History
===============

* 1.0.0 First version of this wondrous package.
* 1.0.1 Check for None when serializing and return None rather than 'None'.  Exceptions on getattr return None for value.
* 1.0.2 Crummy circular reference test.  Convert top level list, set, tuple.
* 1.0.3 Fix deploy workflow
* 1.0.4 Allow for readonly objects
* 1.0.6 Improve recursion check and value
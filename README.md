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

d_serialize will enumerate all public properties of your object (or `dict`) and convert them
to a JSON allowable type.  IE:

    list, dictionary, string, float, integer or boolean.

Any property that is not one of these types will be converted to a `string`. `set`
and `tuple` will be converted to `list`.

Dictionary and list properties will be followed to ensure all child objects and
values are also converted.

Methods and private properties (starting with `_`) are not enumerated.

Example:
--------

Converting a Class instance.

```python
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

1.0.0 First version of this wondrous package.

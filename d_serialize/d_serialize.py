from random import choices
from string import ascii_letters

_reentrant_attribute_check_name = f"_{''.join(choices(ascii_letters, k=50))}"


def is_valid_attribute(item, m):
    """
    return true if attribute is something that
    probably could be a value

    :param item:
    :param m:
    :return:
    """
    try:
        return not (m.startswith("_") or callable(getattr(item, m)))
    except:
        return False


def d_serialize(item, attributes=None):
    """
    convert the given attributes for the item into a dict
    so they can be serialized back to the caller

    :param item: an object, list, set, tuple or dictionary
    :param attributes: list of attributes, defaults to all in item
    :return:
    """

    # base types supported by JSON
    if type(item) in [int, float, str, bool]:
        return item

    if hasattr(item, _reentrant_attribute_check_name):
        return None

    # lists, tuples and sets
    if type(item) in [set, list, tuple]:
        return [d_serialize(d) for d in item]

    if not attributes:

        if isinstance(item, dict):
            attributes = list(item.keys())
        else:
            attributes = [m for m in dir(item) if is_valid_attribute(item, m)]

    attributes.sort()

    if len(attributes) == 0:
        return str(item)

    d = {}
    for a in attributes:
        value = None

        try:
            value = item.get(a, "") if type(item) == dict else getattr(item, a, "")
        except Exception as e:
            print(f"d_serialize: warning: exception on attribute {a}: {e}")

        if type(value) in [set, tuple]:
            value = list(value)

        if type(value) == dict:
            value = d_serialize(value)
        elif type(value) == list:
            value = [d_serialize(d) for d in value]
        elif value and type(value) not in [list, dict, int, float, str, bool]:
            try:
                # re-entrance check
                setattr(item, _reentrant_attribute_check_name, True)
            except:
                pass
            d_value = d_serialize(value)
            value = d_value

        d[a] = value

    return d

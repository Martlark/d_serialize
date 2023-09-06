def is_valid_attribute(item, m):
    """
    return true if attribute is something that
    probably could be a value

    :param item:
    :param m:
    :return: bool
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
    _seen_already = {}

    def _d_serialize(_item, _attributes=None):
        """
        recursive proxy

        :param _item: an object, list, set, tuple or dictionary
        :param _attributes: list of attributes, defaults to all in item
        :return:
        """

        # base types supported by JSON
        if type(_item) in [int, float, str, bool]:
            return _item

        if _seen_already.get(str(_item)):
            return str(_item)

        # lists, tuples and sets
        if type(_item) in [set, list, tuple]:
            return [_d_serialize(d) for d in _item]

        if not _attributes:

            if isinstance(_item, dict):
                _attributes = list(_item.keys())
            else:
                _attributes = [m for m in dir(_item) if is_valid_attribute(_item, m)]

        _attributes.sort()

        if len(_attributes) == 0:
            return str(_item)

        d = {}
        for a in _attributes:
            value = None

            try:
                value = (
                    _item.get(a, "") if type(_item) == dict else getattr(_item, a, "")
                )
            except Exception as e:
                print(f"_d_serialize: warning: exception on attribute {a}: {e}")

            if type(value) in [set, tuple]:
                value = list(value)

            if type(value) == dict:
                value = _d_serialize(value)
            elif type(value) == list:
                value = [_d_serialize(d) for d in value]
            elif value and type(value) not in [list, dict, int, float, str, bool]:
                try:
                    # re-entrance check
                    key = str(value)
                    _seen_already[key] = 1
                except:
                    pass
                d_value = _d_serialize(value)
                value = d_value

            d[a] = value

        return d

    return _d_serialize(item, attributes)

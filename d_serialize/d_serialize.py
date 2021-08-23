def d_serialize(item, attributes=None):
    """
    convert the given attributes for the item into a dict
    so they can be serialized back to the caller

    :param item: an object, or dictionary
    :param attributes: list of attributes, defaults to all in item
    :return:
    """

    if type(item) in [int, float, str, bool]:
        return item

    if not attributes:
        if isinstance(item, dict):
            attributes = list(item.keys())
        else:
            attributes = [
                m
                for m in dir(item)
                if not (m.startswith("_") or callable(getattr(item, m)))
            ]
    attributes.sort()
    if len(attributes) == 0:
        return str(item)
    d = {}
    for a in attributes:
        value = item.get(a, "") if type(item) == dict else getattr(item, a, "")

        if type(value) in [set, tuple]:
            value = list(value)

        if type(value) == dict:
            value = d_serialize(value)
        elif type(value) == list:
            value = [d_serialize(d) for d in value]
        elif type(value) not in [list, dict, int, float, str, bool]:
            value = d_serialize(value)
        d[a] = value
    return d

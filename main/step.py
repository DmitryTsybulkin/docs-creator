dic = {}


def update_dictionary(d, key, value):
    assert isinstance(d, dict)
    if key in d:
        d[len(d)-1](value)
    else:
        if (key * 2) in d:
            d[key * 2] += value
        else:
            d[key * 2] = value

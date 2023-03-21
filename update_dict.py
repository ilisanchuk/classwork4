def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] = [d[key]]
        d[key].append(value)
    elif key not in d.keys():
        if key*2 in d.keys():
            d[key*2] = [d[key*2]]
            d[key*2].append(value)
        else:
            d[key*2] = [value]
    return d









def oxford_comma(items):

    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        new_item = items.pop()
        return ", ".join(items) + f", and {new_item}"
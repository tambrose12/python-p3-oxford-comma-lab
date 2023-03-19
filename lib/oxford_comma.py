def oxford_comma(items):
    if len(items) > 2:
        the_string = ", ".join(items[:-1]) + ", and " + items[-1]
        return the_string
    elif len(items) == 2:
        the_string = " and ".join(items)
        return the_string
    else:
        string = "".join(items)
        return string


def write_int(prompt=None, min=None, max=None, default=None):
    while True:
        num = input(prompt)

        if not num.isdecimal():
            if default is not None:
                return default

            print('"{}" is not valid number'.format(num))
            continue

        num = int(num)
        if min is not None and num < min:
            print('Minimum allowable value is "{}"'.format(min))
            continue
        if max is not None and num > max:
            print('Maximum allowable value is "{}"'.format(max))
            continue

        return num

def achaListaSolo(b):
    y = 1
    while y < len(b):
        if b[0] == b[y]:
            b.pop(0)
            b.pop(y-1)
            y = 0
        if y == len(b) - 1:
            return print(b[0])
        y += 1

    return print(b[0])


if _name_ == '_main_':

    achaListaSolo([1,2,3,5,4,1,2,3,4])
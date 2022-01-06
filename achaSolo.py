def achaListaSolo(b):
    rash = {}
    for item in b:
        if item in rash:
            rash[item] += rash[item]
        else: rash[item] = 1

    for item in rash:
        if rash[item] == 1:
            return item


    return None


if _name_ == '_main_':

    print(achaListaSolo([1,2,3,5,4,1,2,3,4]))
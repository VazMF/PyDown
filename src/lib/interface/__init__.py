def line(length=30):
    return '=-' * length


def header(txt):
    print(line())
    print(txt.center(60))
    print(line())


def menu(lista):
    c = 1
    for item in lista:
        print(f'[ {c} ] {item}')
        c += 1
    print(line())


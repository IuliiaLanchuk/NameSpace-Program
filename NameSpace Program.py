namesp = {'global': {'parent': 'None', 'vars': set()}}


def create(namespace, parent):
    namesp[namespace] = {'parent': parent, 'vars': set()}


def adding(namespace, variable):
    a = namesp[namespace]['vars']
    a.add(variable)


def getting(nameSpace, var):
    if var in namesp.get(nameSpace).get('vars'):
        print(nameSpace)
    else:
        parent = namesp[nameSpace]['parent']
        if parent == 'None':
            print('None')
        else:
            getting(parent, var)


for i in range(int(input())):
    command, nameSpace, var = input().split(' ')

    if command == 'create':
        create(nameSpace, var)

    if command == 'add':
        adding(nameSpace, var)

    if command == 'get':
        getting(nameSpace, var)
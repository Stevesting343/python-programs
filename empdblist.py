db = {101: ['mohit', '23000', 'backend'], 102: ['mohit', '23000', 'backend']}
edb = []


def menu():
    print("_" * 130)
    print()
    print('\t\t\t\t\t Welcome to the Employee Management System')
    print("_" * 130)
    print('''
                                 \t\t\tOperations


                            \t\t\t1---> create employee data
                            \t\t\t2---> display employee data
                            \t\t\t3---> delete employee data
                            \t\t\t4---> search employee by dept
                            \t\t\t5---> search employee by id

         ''')


menu()


def ch1():
    e_id = int(input('enter employee id ='))
    e_name = input('enter employee name =')
    e_sal = eval(input('enter empl salary ='))
    e_dep = input('enter employee department =')

    edb = [e_name, e_sal, e_dep]
    db[e_id] = edb
    print('succefully added employee data in datbase')


def ch2():
    print('_' * 120)
    print('{:^12} |{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
    print('_' * 120)
    for i, j in db.items():
        print('{:^12} |{:^12}|{:^12}|{:^12} '.format(i, j[0], j[1], j[2]))
    print('_' * 120)
    print()


def ch3():
    e_id = int(input('enter id of the employee which you want to delete ='))
    db.remove(e_id)

    print(f'employee {e_id} succefully deleted ')


def ch4():
    e_dep = input('enter employee dep =')
    print('_' * 120)
    print('{:^12} |{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
    print('_' * 120)
    for i, j in db.items():
        if j[2] == e_dep:
            print('{:^12} |{:^12}|{:^12}|{:^12} '.format(i, j[0], j[1], j[2]))
            print('_' * 120)
        else:
            print(f'\t\t{e_dep:^} is not avilable inn database')
            break


def ch5():
    e_id = int(input('enter employee id ='))

    for i, j in db.items():
        if i == e_id:
            print('_' * 120)
            print('{:^12} |{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
            print('_' * 120)
            print('{:^12} |{:^12}|{:^12}|{:^12} '.format(i, j[0], j[1], j[2]))
            print('_' * 120)
        else:
            print('enter valid employee id')


while True:

    print("_" * 130)
    print()
    choice = int(input('enter operation you want ='))
    if choice == 1:
        ch1()
    elif choice == 2:
        ch2()
    elif choice == 3:
        ch3()
    elif choice == 4:
        ch4()
    elif choice == 5:
        ch5()
    else:
        print('invalid operaton taken')
        continue

    ch = input('do you want to continue y/n = ')
    if ch.lower() != 'y':
        break

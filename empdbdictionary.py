db = {101: {'name': 'jay', 'sal': 23400, 'dep': 'Full stack', 'id': 101}}


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
                            \t\t\t4---> search employee by id
                            \t\t\t5---> search employee by dep
                            \t\t\t6---> update employee data
                            \t\t\t7---> search employee by salary
                            \t\t\t8---> search employee by salary greater than input


         ''')


menu()


def ch1():
    # print("_"*130)
    e_id = int(input('enter employee id ='))
    if e_id in db:
        print(f'{e_id} is already present in the databaseE')
    else:
        e_name = input('enter employee name =')
        e_sal = eval(input('enter empl salary ='))
        e_dep = input('enter employee department =')
        edb = {}
        edb['name'] = e_name
        edb['sal'] = e_sal
        edb['dep'] = e_dep
        edb['id'] = e_id
        print('succefully added employee data in datbase')
        db[e_id] = edb


def ch2():
    print('_' * 120)
    print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
    print('_' * 120)
    for i, j in db.items():
        print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(i, j['name'], j['sal'], j['dep']))
    print('_' * 120)


def ch3():
    e_id = int(input('enter id of the employee which you want to delete ='))
    db.pop(e_id)

    print(f'employee {e_id} succefully deleted ')


def ch4():
    id = int(input('enter employee id ='))

    if id in db:
        print('_' * 120)
        print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
        print('_' * 120)
        print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(db[id]['id'], db[id]['name'], db[id]['sal'], db[id]['dep']))
        print('_' * 120)
    else:
        print('enter valid employee id')


def ch5():
    print("_" * 130)
    print('''  
                      \t\t\t  Operations
                     \t\t\t _______________

                \t\t\t 1----Hr
                \t\t\t 2----Full Stack
                \t\t\t 3----Development
                \t\t\t 4----Tester

    ''')
    print("_" * 130)
    choice = eval(input('enter index no of dep ='))
    if len(db) > 0:
        if choice == 1:
            print('_' * 120)
            print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
            print('_' * 120)
            for i, j in db.items():
                if j['dep'] == 'Hr':
                    print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(i, j['name'], j['sal'], j['dep']))
            print('_' * 120)

        elif choice == 2:
            print('_' * 120)
            print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
            print('_' * 120)
            for i, j in db.items():
                if j['dep'] == 'Full stack':
                    print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(i, j['name'], j['sal'], j['dep']))
            print('_' * 120)

        elif choice == 3:
            print('_' * 120)
            print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
            print('_' * 120)
            for i, j in db.items():
                if j['dep'] == 'Development':
                    print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(i, j['name'], j['sal'], j['dep']))
            print('_' * 120)

        elif choice == 4:
            print('_' * 120)
            print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
            print('_' * 120)
            for i, j in db.items():
                if j['dep'] == 'Tester':
                    print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(i, j['name'], j['sal'], j['dep']))
            print('_' * 120)

        else:
            print('Invalid choice')

    else:
        print('empty Database')


def ch6():
    print("_" * 130)
    print('''  
                      \t\t Update Operations
                     \t\t\t _______________

                \t\t\t 1----Name
                \t\t\t 2----Dept
                \t\t\t 3----salary
                           \t\t\t 4--- increment
                           \t\t\t 5--- decrement

    ''')
    print("_" * 130)
    print()
    ch = int(input('enter update operation ='))
    if ch == 1:
        ch1 = int(input('enter id of the employee whose name you want update ='))
        if ch1 in db:
            name1 = input('enter new name of the employee =')
            db[ch1]['name'] = name1

    elif ch == 2:
        ch2 = int(input('enter id of the employee whose department you want update ='))
        if ch2 in db:
            Dept1 = input('enter updated department of the employee =')
            db[ch2]['Dept'] = Dept1
            print('employee salary updated successfully')

    elif ch == 3:
        choice = int(input('do you want to increment(4) or decrement(5) salary ='))
        if choice == 4:
            ch3 = int(input('enter id of the employee whose salary you want increment ='))
            if ch3 in db:
                chi = int(input('enter percentage to increment ='))
                db[ch3]['sal'] = db[ch3]['sal'] + db[ch3]['sal'] * chi // 100
                print('employee salary updated successfully')
        elif choice == 5:
            ch3 = int(input('enter id of the employee whose salary you want decrement ='))
            if ch3 in db:
                chi = int(input('enter percentage to decrement ='))
                db[ch3]['sal'] = db[ch3]['sal'] - db[ch3]['sal'] * chi // 100
                print('employee salary updated successfully')

    else:
        print('Invalid update operation')


def ch7():
    sal = int(input('Enter sal of employee ='))
    print('_' * 120)
    print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
    print('_' * 120)
    for i in db:
        if db[i]['sal'] == sal:
            print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(i, db[i]['name'], db[i]['sal'], db[i]['dep']))
    print('_' * 120)


def ch8():
    sal = int(input('Enter sal of employee ='))
    print('_' * 120)
    print(' {:^12}|{:^12}|{:^12}|{:^12} '.format('e_id', 'e_name', 'e_sal', 'e_dep'))
    print('_' * 120)
    for i in db:
        if db[i]['sal'] >= sal:
            print(' {:^12}|{:^12}|{:^12}|{:^12} '.format(i, db[i]['name'], db[i]['sal'], db[i]['dep']))
    print('_' * 120)


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
    elif choice == 6:
        ch6()
    elif choice == 7:
        ch7()
    elif choice == 8:
        ch8()

    else:
        print('invalid operaton taken')
        continue

    ch = input('do you want to continue y/n = ')
    if ch.lower() != 'y':
        break

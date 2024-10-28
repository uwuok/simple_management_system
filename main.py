members = []


def add():
    """add the specified employee's data
    """
    global members
    while True:
        department = input('請輸入部門： ')
        name = input('請輸入姓名： ')
        age = input('請輸入年齡： ')
        phone = input('請輸入手機號碼： ')
        member = {}
        member['部門'] = department
        member['姓名'] = name
        member['年齡'] = age
        member['手機'] = phone
        members.append(member)
        while True:
            y_n = input('是否繼續新增資料？(y/n)： ')
            if y_n.lower() == 'y':
                break
            elif y_n.lower() == 'n':
                print()
                return


def remove():
    """remove the specify employee

    Returns:
        bool: if sucessfu
    """
    name = input('請輸入要刪除的姓名： ')
    for i, member in enumerate(members):
        if name in member['姓名']:
            while True:
                y_n = input(f'確定要刪除 {name} 的資料嗎？ (y/n)')
                if y_n.lower() == 'y':
                    members.pop(i)
                    print(f'{name} 的資料已刪除。')
                    print()
                    print('--- 剩餘的所有資料 ---')
                    show_all()
                    print()
                    return True
                elif y_n.lower() == 'n':
                    print()
                    return False
    print('查無此人。')
    print()
    return False

def modify():
    """modify the specify employee

    Returns:
        bool: Whether the employee data was successfully modified
    """
    name = input('請輸入要修改的姓名： ')
    for member in members:
        if name in member['姓名']:
            print('當前資料：')
            print('部門\t\t姓名\t\t年齡\t\t手機\t\t')
            print('----------------------------------------')
            for v in member.values():
                print(f'{v}\t\t', end='')
            print()
            print('1. 修改部門')
            print('2. 修改姓名')
            print('3. 修改年齡')
            print('4. 修改手機')
            while True:
                selection = int(input('請選擇要修改的欄位： '))
                if selection == 1:
                    _department = input('請輸入新的部門： ')
                    member['部門'] = _department
                elif selection == 2:
                    _name = input('請輸入新的姓名： ')
                    member['姓名'] = _name
                elif selection == 3:
                    _age = input('請輸入新的年齡： ')
                    member['年齡'] = _age
                elif selection == 4:
                    _phone = input('請輸入新的手機： ')
                    member['手機'] = _phone
                if 1 <= selection <= 4:
                    break
                else:
                    continue
            print('--- 更新後的資料 ---')
            print('部門\t\t姓名\t\t年齡\t\t手機\t\t')
            print('----------------------------------------')
            for v in member.values():
                print(f'{v}\t\t', end='')
            print()
            return True
        print('查無此人。')
        print()
    return False


def find():
    """find the specify employee's data

    Returns:
        bool: Whether the employee data was successfully found
    """
    global members
    # found = False
    name = input('請輸入要查詢的姓名： ')
    for member in members:
        if name in member['姓名']:
            # found = True
            print('部門\t\t姓名\t\t年齡\t\t手機\t\t')
            print('----------------------------------------')
            for v in member.values():
                print(f'{v}\t\t', end='')
            print('\n')
            return True
    # if not found:
        # print('查無此人。')
    print('查無此人。')
    print()
    return False 


# def show(name):
#     print('部門\t\t姓名\t\t年齡\t\t手機\t\t')
#     print('----------------------------------------')
#     for v in 
    

def show_all():
    """show all employee(s)'s data
    """
    if len(members) == 0:
        print('目前沒有任何資料')
        print()
        return
    print('部門\t\t姓名\t\t年齡\t\t手機\t\t')
    print('----------------------------------------')
    for member in members:
        for v in member.values():
            print(f'{v}\t\t', end='')
        print()
    print()
    

def print_UI():
    """print the main UI"""
    while True:
        print('--- 人事資料管理系統 ---')
        print('1. 新增資料')
        print('2. 查詢資料')
        print('3. 修改資料')
        print('4. 刪除資料')
        print('5. 顯示所有資料')
        print('6. 退出系統')
        print('------------------------')
        selection = int(input('請選擇功能： '))
        if selection == 1:
            add()
        elif selection == 2:
            find()
        elif selection == 3:
            modify()
        elif selection == 4:
            remove()
        elif selection == 5:
            show_all()
        elif selection == 6:
            print('系統已退出。')
            exit()
        else:
            print('無效的選擇，請重新選擇。', end='\n\n')
            
        
def main():
    """Main function to run the program

    Returns:
        int: Exit status code
    """
    print_UI()
    return 0

if __name__ == '__main__':
    main()
    
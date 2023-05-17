"""
英雄管理
"""
from add_hero import add_hero
from delete_hero import delete_hero
from find_hero import find_hero
from modify_hero import modify_hero


def console():
    print(
        """
        1. **创建英雄**
        2. **查看英雄**
        3. **修改英雄**
        4. **删除英雄**
        5. **退出**
        """
    )
    hero_list = []
    while True:
        result = input("请输入数字, 选择需要完成的操作: ")
        if result == "1" :
            name = input("请输入英雄的名字：")
            volume = input("请输入英雄的血量：")
            power = input("请输入英雄的攻击力：")
            hero_list = add_hero(hero_list, name, volume, power)
            print(f"{hero_list}")
        elif result == "2" :
            name = input("请输入英雄的名字：")
            find_hero(hero_list, name)
        elif result == "3" :
            name = input("请输入英雄的名字：")
            modify_hero(hero_list, name)
        elif result == "4" :
            name = input("请输入英雄的名字：")
            delete_hero(hero_list, name)
        elif result == "5" :
            print("退出系统")
            break


if __name__ == '__main__':
    console()

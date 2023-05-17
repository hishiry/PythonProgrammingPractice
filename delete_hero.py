"""
删除英雄
"""

def delete_hero(hero_list, name):
    for i in range(len(hero_list)):
        if hero_list[i].get("name") == name :
            hero_list.pop(i)
            print(f"删除之后的英雄列表为{hero_list}")
            break
        else:
            print(f"您所操作的英雄不存在")
    return hero_list
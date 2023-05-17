"""
查看英雄
"""


def find_hero(hero_list, name):
    for i in hero_list:
        if i.get("name") == name:
            # print(f"您所查找的英雄名字: {i.get(name)}, 血量：{i.get(volume)}, 攻击力: {i.get(power)}")
            print(f"{i}")
        else:
            print(f"您所查找的英雄不存在")

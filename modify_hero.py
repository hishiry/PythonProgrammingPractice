"""
修改英雄
"""

def modify_hero(hero_list, name):
    for i in hero_list :
        if i.get("name") == name :
            volume = input("您想要修改的血量为: ")
            i["volume"] = volume
            print("您所查找的英雄名字: " + i.get("name") + ", 血量：" + i.get("volume") + ", 攻击力: " + i.get("power") )
        else:
            print(f"您想要修改的英雄不存在")
    return hero_list





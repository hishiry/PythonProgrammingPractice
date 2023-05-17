"""
新增英雄
"""
def add_hero(hero_list, name, volume, power):
    hero_data = {"name":name, "volume":volume, "power":power}
    hero_list.append(hero_data)
    print(f"创建英雄成功 {name} {volume} {power}")
    return hero_list
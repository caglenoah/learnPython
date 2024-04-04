def get_most_common_enemy(enemies_dict):
    max_count = float("-inf")
    most_common_enemy = None
    for enemy, count in enemies_dict.items():
        if count > max_count:
            max_count = count
            most_common_enemy = enemy
    return most_common_enemy









# def get_most_common_enemy(enemies_dict):
#     max_count = float("-inf")
#     most_common_enemy = None
#     for enemy_name in enemies_dict:
#         count = enemies_dict[enemy_name]
#         if count > max_count:
#             max_count = count
#             most_common_enemy = enemy_name
#     return most_common_enemy
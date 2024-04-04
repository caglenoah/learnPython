def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        enemy = enemy_name.split()
        enemy_type_count = 0
        for name in enemy_names:
            if name == enemy_name:
                enemy_type_count += 1
        enemies_dict[f"{' '.join(enemy)}"] = enemy_type_count
    return enemies_dict
def find_missing_ids(first_ids, second_ids):
    id_set1 = set(first_ids)
    id_set2 = set(second_ids)
    missing_ids_set = id_set1 - id_set2
    missing_ids = list(missing_ids_set)
    return missing_ids
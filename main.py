def get_character_record(name, server, level, rank):
    get_character_record = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }
    return get_character_record
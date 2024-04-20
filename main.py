def join_strings(strings):
    con_strings = ""
    for index, string in enumerate(strings):
        con_strings += string
        if index < len(strings) - 1:
            con_strings += ","
    return con_strings
        
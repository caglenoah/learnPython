def remove_duplicates(spells):
    new_list = []
    spell_set = set()
    for spell in spells:
        spell_set.add(spell)
        new_list = list(spell_set)
    return new_list








    # Complete the remove_duplicates function. 
    # It should take a list of spells that a player has learned and return a
    # new List where there is at most one of each title. 


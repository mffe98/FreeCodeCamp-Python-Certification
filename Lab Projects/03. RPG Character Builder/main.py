full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name.strip():
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    empty_stats = empty_dot*10

    str_stat = 'STR ' + empty_stats.replace(empty_dot, full_dot, strength)
    int_stat = 'INT ' + empty_stats.replace(empty_dot, full_dot, intelligence)
    cha_stat = 'CHA ' + empty_stats.replace(empty_dot, full_dot, charisma)
    stats = str_stat + '\n' +  int_stat + '\n' + cha_stat
    return name + '\n' + stats 
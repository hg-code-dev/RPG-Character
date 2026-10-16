full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # --- Name validation ---
    # The character name must be a string.
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    # Prevent empty names.
    if name == "":
        return 'The character should have a name'
    
    # Limit name length to keep formatting tidy.
    if len(name) > 10:
        return 'The character name is too long'
    
    # Disallow spaces to enforce a single-word name.
    if ' ' in name:
        return 'The character name should not contain spaces'

    # --- Stat type validation ---
    # All stats must be integers.
    if not isinstance(strength, int):
        return 'All stats should be integers'
    elif not isinstance(intelligence, int):
        return 'All stats should be integers'
    elif not isinstance(charisma, int):
        return 'All stats should be integers'

    # --- Stat range validation ---
    # Stats must be at least 1.
    if strength < 1:
        return 'All stats should be no less than 1'
    elif intelligence < 1:
        return 'All stats should be no less than 1'
    elif charisma < 1:
        return 'All stats should be no less than 1'

    # Stats must be no more than 4.
    if strength > 4:
        return 'All stats should be no more than 4'
    elif intelligence > 4:
        return 'All stats should be no more than 4'
    elif charisma > 4:
        return 'All stats should be no more than 4'

    # --- Total stat points validation ---
    # Characters must start with exactly 7 points distributed across stats.
    if not strength + intelligence + charisma == 7:
        return 'The character should start with 7 points'

    # --- Character sheet formatting ---
    # Build each line using filled and empty dots to represent stat values.
    line_1 = name
    line_2 = 'STR ' + (full_dot * strength) + (empty_dot * (10 - strength))
    line_3 = 'INT ' + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    line_4 = 'CHA ' + (full_dot * charisma) + (empty_dot * (10 - charisma))

    # Return the final formatted character sheet.
    return line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4

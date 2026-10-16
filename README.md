# RPG Character Creator

A Python project completed as part of the FreeCodeCamp **Build an RPG Character** lab.  
This exercise focuses on input validation, conditional logic, and formatted output.  
All 19 automated tests were successfully passed.

---

## 📌 Project Summary

This project implements a function called `create_character` that validates a character name and three stats—**strength**, **intelligence**, and **charisma**—and outputs a formatted RPG-style character sheet using dot-based stat bars.

The goal was to meet all user stories and pass all tests provided by FreeCodeCamp.

---

## 🎯 User Stories Completed

### Name Validation
- Must be a string  
- Must not be empty  
- Must not exceed 10 characters  
- Must not contain spaces  

### Stat Validation
- All stats must be integers  
- Stats must be between **1** and **4**  
- Total stat points must equal **7**  

### Output Format
If all validations pass, the function returns:


---

## ✅ Tests Passed

All 19 FreeCodeCamp tests were completed, including:

- Function existence  
- Name type, length, and spacing validation  
- Stat type and range validation  
- Total stat point validation  
- Correct formatting  
- Exact output for `create_character('ren', 4, 2, 1)`  

---

## 🧩 Final Solution

```python
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # --- Name validation ---
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == "":
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    # --- Stat type validation ---
    if not isinstance(strength, int):
        return 'All stats should be integers'
    elif not isinstance(intelligence, int):
        return 'All stats should be integers'
    elif not isinstance(charisma, int):
        return 'All stats should be integers'

    # --- Stat range validation ---
    if strength < 1:
        return 'All stats should be no less than 1'
    elif intelligence < 1:
        return 'All stats should be no less than 1'
    elif charisma < 1:
        return 'All stats should be no less than 1'

    if strength > 4:
        return 'All stats should be no more than 4'
    elif intelligence > 4:
        return 'All stats should be no more than 4'
    elif charisma > 4:
        return 'All stats should be no more than 4'

    # --- Total stat points validation ---
    if not strength + intelligence + charisma == 7:
        return 'The character should start with 7 points'

    # --- Character sheet formatting ---
    line_1 = name
    line_2 = 'STR ' + (full_dot * strength) + (empty_dot * (10 - strength))
    line_3 = 'INT ' + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    line_4 = 'CHA ' + (full_dot * charisma) + (empty_dot * (10 - charisma))

    return line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4



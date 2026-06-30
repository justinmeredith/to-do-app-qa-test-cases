from models import ToDoList

# Checks that a string is valid; validity means it is not empty and is not greater in length than 50 characters
def validate_string(string):
    if not string:
        raise ValueError("Input cannot be empty.")
    
    if len(string) > 50:
        raise ValueError("Input cannot be more than 50 characters.")
    
def find_list(lists, list_name):
    for list in lists:
        if list.name.lower == list_name.lower():
            return list
    
    return None

def create_to_do_list(lists):
    list_name = input("New list name: ")

    duplicate_list = find_list(lists, list_name)

    if duplicate_list:
        raise ValueError("A list with this name already exists.")

    return ToDoList(list_name)

def add_item_to_list(list, new_item):
    list.add_new_item(new_item)
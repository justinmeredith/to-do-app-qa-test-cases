from datetime import datetime, timezone
from services import validate_string

class ListItem:
    def __init__(self, name):
        validate_string(name)

        self.name = name
        self.id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        self.completed = False

    def __str__(self):
        if self.completed:
            return f"{self.name}: Complete"
        else:
            return f"{self.name}: Incomplete"

    def toggle_completion(self):
        self.completed = not self.completed

    def update_name(self, name):
        validate_string(name)
        if self.name == name:
            raise ValueError("The new name cannot match the existing name.")
        self.name = name


class ToDoList:
    def __init__(self, name):
        validate_string(name)
        
        self.name = name
        self.id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S.%f")
        self.items = []

    def update_name(self, name):
        validate_string(name)
        if self.name == name:
            raise ValueError("The new name cannot match the existing name.")
        self.name = name

    def sort_list(self):
        self.items.sort(key=lambda item: item.id)

    def find_item(self, key_item_name):
        for item in self.items:
            if item.name.lower() == key_item_name.lower():
                return item
            
        return None

    def add_new_item(self, item_name):
        validate_string(item_name)

        duplicate_item = self.find_item(item_name)

        if duplicate_item:
            raise ValueError("Duplicate item")
        else:
            self.items.append(ListItem(item_name))

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if not item:
            raise ValueError("List item could not be found.")
        
        self.items.remove(item)

    def update_item_status(self, item_name):
        item = self.find_item(item_name)
        if not item:
            raise ValueError("List item could not be found.")
        
        item.toggle_completion()
        return item

    def display_to_do_list(self):
        self.sort_list()
        for item in self.items:
            print(item)
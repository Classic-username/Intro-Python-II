# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items=[]):
        self.room = room
        self.name = name
        self.items = items
        
    def take(self, item):
        if item in self.room.items:
            self.room.items.remove(item)
            self.items.append(item)
            print(f'You picked up {item}!')
        
            
    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            self.room.items.append(item)
    def __str__(self):
        return f"{self.name} is in {self.room}"
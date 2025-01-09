# composition
#House and Room
#Body and Organs
#Book and Chapters
class Room:
    def __init__(self, name: str, area: float):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name} (Area: {self.area} m²)"


class House:
    def __init__(self, address: str):
        self.address = address
        self.rooms = []  # Composition: A house contains a list of rooms

    def add_room(self, room: Room):
        self.rooms.append(room)

    def display_rooms(self):
        print(f"House at {self.address} contains:")
        if not self.rooms:
            print(" - No rooms yet.")
        else:
            for room in self.rooms:
                print(f" - {room}")

    def total_area(self):
        return sum(room.area for room in self.rooms)


# Example usage
house = House("123 Main Street")

# Creating rooms and adding them to the house
room1 = Room("Living Room", 25.0)
room2 = Room("Kitchen", 12.5)
room3 = Room("Bedroom", 15.0)

house.add_room(room1)
house.add_room(room2)
house.add_room(room3)

# Displaying rooms and total area
house.display_rooms()
print(f"Total area of the house: {house.total_area()} m²")

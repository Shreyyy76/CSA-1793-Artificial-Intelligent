import random

class VacuumCleaner:
    def __init__(self, room_size):
        self.room_size = room_size
        self.room = [[random.choice(['clean', 'dirty']) for _ in range(room_size)] for _ in range(room_size)]
        self.position = (0, 0)
        self.moves = 0

    def display_room(self):
        for row in self.room:
            print(' '.join(row))
        print()

    def is_clean(self):
        for row in self.room:
            if 'dirty' in row:
                return False
        return True

    def move_and_clean(self):
        x, y = self.position
        if self.room[x][y] == 'dirty':
            self.room[x][y] = 'clean'
        self.moves += 1

        # Move to the next position
        if y < self.room_size - 1:
            self.position = (x, y + 1)
        elif x < self.room_size - 1:
            self.position = (x + 1, 0)
        else:
            self.position = (0, 0)  # Loop back to the beginning

    def clean_room(self):
        while not self.is_clean():
            self.move_and_clean()
            self.display_room()
        print(f"Room cleaned in {self.moves} moves!")

# Initialize room size and create a VacuumCleaner agent
room_size = 4  # You can change the size of the room here
vacuum_cleaner = VacuumCleaner(room_size)

# Display initial state of the room
print("Initial state of the room:")
vacuum_cleaner.display_room()

# Start cleaning
vacuum_cleaner.clean_room()

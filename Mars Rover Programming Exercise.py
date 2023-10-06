# Command Pattern
class Command:
    def execute(self, rover):
        pass

class MoveCommand(Command):
    def execute(self, rover):
        rover.move()

class TurnLeftCommand(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRightCommand(Command):
    def execute(self, rover):
        rover.turn_right()

# Rover class
class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def status_report(self):
        pass

# Concrete implementation of Rover
class MarsRover(Rover):
    def __init__(self, x, y, direction, grid, obstacles):
        super().__init__(x, y, direction)
        self.grid = grid
        self.obstacles = obstacles

    def move(self):
        if self.direction == 'N':
            new_y = self.y + 1
            if not self.grid.is_obstacle(self.x, new_y):
                self.y = new_y
        elif self.direction == 'S':
            new_y = self.y - 1
            if not self.grid.is_obstacle(self.x, new_y):
                self.y = new_y
        elif self.direction == 'E':
            new_x = self.x + 1
            if not self.grid.is_obstacle(new_x, self.y):
                self.x = new_x
        elif self.direction == 'W':
            new_x = self.x - 1
            if not self.grid.is_obstacle(new_x, self.y):
                self.x = new_x
       

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'
        

    def status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. {'Obstacle detected.' if self.grid.is_obstacle(self.x, self.y) else 'No obstacles detected.'}"
     

# Composite Pattern for Grid and Obstacles
class GridComponent:
    def is_obstacle(self, x, y):
        pass

class Grid(GridComponent):
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def is_obstacle(self, x, y):
        return False if 0 <= x < self.size_x and 0 <= y < self.size_y else True

class Obstacles(GridComponent):
    def __init__(self, obstacle_positions):
        self.obstacle_positions = obstacle_positions

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacle_positions

# Main program
if __name__ == "__main__":
    # Take user input for grid size, starting position, obstacles, and commands
    grid_size_x = int(input("Enter grid size X: "))
    grid_size_y = int(input("Enter grid size Y: "))
    start_x = int(input("Enter starting X position: "))
    start_y = int(input("Enter starting Y position: "))
    start_direction = input("Enter starting direction (N, S, E, W): ")
    obstacle_count = int(input("Enter the number of obstacles: "))
    obstacle_positions = []
    for i in range(obstacle_count):
        obstacle_x = int(input(f"Enter obstacle {i + 1} X position: "))
        obstacle_y = int(input(f"Enter obstacle {i + 1} Y position: "))
        obstacle_positions.append((obstacle_x, obstacle_y))
    commands = input("Enter commands (M, L, R): ")

    # Create grid and obstacles
    grid = Grid(grid_size_x, grid_size_y)
    obstacles = Obstacles(obstacle_positions)

    # Create Mars Rover and execute commands
    mars_rover = MarsRover(start_x, start_y, start_direction, grid, obstacles)
    for command_char in commands:
        if command_char == 'M':
            command = MoveCommand()
        elif command_char == 'L':
            command = TurnLeftCommand()
        elif command_char == 'R':
            command = TurnRightCommand()
        else:
            continue

        command.execute(mars_rover)

    # Display final position and status report
    print(f"Final Position: ({mars_rover.x}, {mars_rover.y}, {mars_rover.direction})")
    print(mars_rover.status_report())

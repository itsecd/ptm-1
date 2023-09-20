import random

import numpy as np
import pygame
import tcod

from enum import Enum
from typing import List, Optional, Tuple


class Direction(Enum):
    """
    An enumeration representing cardinal directions and a 'NONE' value.
    """
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    NONE = 4


def translate_screen_to_maze(in_coords, in_size=32) -> tuple:
    """
    Translates screen coordinates to maze/grid coordinates.

    Args:
        in_coords (tuple): A tuple of screen coordinates (x, y).
        in_size (int, optional): The size of a single maze cell. Defaults to 32.

    Returns:
        tuple: A tuple of maze coordinates (x, y).
    """
    return int(in_coords[0] / in_size), int(in_coords[1] / in_size)


def translate_maze_to_screen(in_coords, in_size=32) -> tuple:
    """
    Translates maze/grid coordinates to screen coordinates.

    Args:
        in_coords (tuple): A tuple of maze coordinates (x, y).
        in_size (int, optional): The size of a single maze cell. Defaults to 32.

    Returns:
        tuple: A tuple of screen coordinates (x, y).
    """
    return in_coords[0] * in_size, in_coords[1] * in_size


class GameObject:
    """
    A base class for game objects with basic rendering and position management.

    Attributes:
        _size (int): The size of the game object.
        _renderer (GameRenderer): The renderer instance for drawing game objects.
        _surface (pygame.Surface): The surface where the game object is drawn.
        x (int): X coordinate of the game object.
        y (int): Y coordinate of the game object.
        _color (tuple): RGB color of the game object (default (255, 0, 0)).
        _circle (bool): Whether the game object is drawn as a circle or a rectangle (default False).
        _shape (pygame.Rect): The shape of the game object.
    """

    def __init__(self, in_surface, x, y,
                 in_size: int, in_color=(255, 0, 0),
                 is_circle: bool = False):
        """
            Initializes a GameObject instance.

            Args:
                in_surface (GameRenderer): The renderer instance for drawing game objects.
                x (int): X coordinate of the game object.
                y (int): Y coordinate of the game object.
                in_size (int): The size of the game object.
                in_color (tuple, optional): RGB color of the game object. Defaults to (255, 0, 0).
                is_circle (bool, optional): Whether the game object is drawn as a circle or a rectangle. Defaults to False.
        """
        self._size = in_size
        self._renderer: GameRenderer = in_surface
        self._surface = in_surface._screen
        self.y = y
        self.x = x
        self._color = in_color
        self._circle = is_circle
        self._shape = pygame.Rect(self.x, self.y, in_size, in_size)

    def draw(self) -> None:
        """
            Draws the game object on the surface.
        """
        if self._circle:
            pygame.draw.circle(self._surface,
                               self._color,
                               (self.x, self.y),
                               self._size)
        else:
            rect_object = pygame.Rect(self.x, self.y, self._size, self._size)
            pygame.draw.rect(self._surface,
                             self._color,
                             rect_object,
                             border_radius=1)

    def tick(self) -> None:
        """
            Performs any necessary updates for the game object on each tick.
        """
        pass

    def get_shape(self) -> pygame.Rect:
        """
            Returns the shape (pygame.Rect) of the game object.

            Returns:
                pygame.Rect: The shape of the game object.
        """
        return self._shape

    def set_position(self, in_x, in_y) -> None:
        """
            Sets the position of the game object.

            Args:
                in_x (int): X coordinate to set.
                in_y (int): Y coordinate to set.
        """
        self.x = in_x
        self.y = in_y

    def get_position(self) -> tuple:
        """
            Returns the position of the game object as a tuple (x, y).

            Returns:
                tuple: The position of the game object.
        """
        return (self.x, self.y)


class Wall(GameObject):
    """
    An implementation of the Wall game object that inherits from GameObject class.
    """

    def __init__(self, in_surface, x, y, in_size: int, in_color=(0, 0, 255)) -> None:
        """
            Initializes a Wall instance.

            Args:
                in_surface (GameRenderer): The renderer instance for drawing game objects.
                x (int): X coordinate of the wall base position in maze.
                y (int): Y coordinate of the wall base position in maze.
                in_size (int): The size of the wall.
                in_color (tuple, optional): RGB color of the wall. Defaults to (0, 0, 255).
        """
        super().__init__(in_surface, x * in_size, y * in_size, in_size, in_color)


class GameRenderer:
    """
        A class for managing game rendering and game-related state.
        Attributes:
            _width (int): Width of the display window.
            _height (int): Height of the display window.
            _screen (pygame.Surface): The display window surface.
            _clock (pygame.time.Clock): A clock object that helps limit the frame rate.
            _done (bool): A flag to indicate if the game loop should stop.
            _game_objects (list): A list of GameObject instances that are in the game.
            _walls (list): A list of Wall instances that are in the game.
            _cookies (list): A list of GameObject instances representing the cookies in the game.
            _hero (Hero): The hero object in the game.
    """

    def __init__(self, in_width: int, in_height: int) -> None:
        """
           Initializes a GameRenderer instance.

           Args:
               in_width (int): Width of the display window.
               in_height (int): Height of the display window.
        """
        pygame.init()
        self._width = in_width
        self._height = in_height
        self._screen = pygame.display.set_mode((in_width, in_height))
        pygame.display.set_caption('Pacman')
        self._clock = pygame.time.Clock()
        self._done = False
        self._game_objects = []
        self._walls = []
        self._cookies = []
        self._hero: Hero = None

    def tick(self, in_fps: int) -> None:
        """
            Runs the game loop with a defined limit of frames per second (in_fps).

            Args:
                in_fps (int): Frames per second to limit the game loop.
        """
        black = (0, 0, 0)
        while not self._done:
            for game_object in self._game_objects:
                game_object.tick()
                game_object.draw()

            pygame.display.flip()
            self._clock.tick(in_fps)
            self._screen.fill(black)
            self._handle_events()
        print("Game over")

    def add_game_object(self, obj: GameObject) -> None:
        """
           Adds a GameObject instance to the game rendering process.

           Args:
               obj (GameObject): An instance of GameObject.
        """
        self._game_objects.append(obj)

    def add_cookie(self, obj: GameObject) -> None:
        """
            Adds a GameObject instance representing a cookie to the game.

            Args:
                obj (GameObject): An instance of GameObject representing a cookie.
        """
        self._game_objects.append(obj)
        self._cookies.append(obj)

    def add_wall(self, obj: Wall) -> None:
        """
           Adds a Wall instance to the game.

           Args:
               obj (Wall): An instance of Wall.
        """
        self.add_game_object(obj)
        self._walls.append(obj)

    def get_walls(self) -> List[Wall]:
        """
            Returns the list of Wall instances in the game.

            Returns:
                List[Wall]: A list of Wall instances.
        """
        return self._walls

    def get_cookies(self) -> List[GameObject]:
        """
            Returns the list of GameObject instances representing the cookies in the game.

            Returns:
                List[GameObject]: A list of GameObject instances representing the cookies.
        """
        return self._cookies

    def get_game_objects(self) -> List[GameObject]:
        """
            Returns the list of GameObject instances in the game.

            Returns:
                List[GameObject]: A list of GameObject instances.
        """
        return self._game_objects

    def add_hero(self, in_hero) -> None:
        """
            Adds a Hero instance to the game and sets it as the main hero.

            Args:
                in_hero (Hero): An instance of Hero.
        """
        self.add_game_object(in_hero)
        self._hero = in_hero

    def _handle_events(self) -> None:
        """
            Handles user input events like quitting the game
            and controlling the hero using arrow keys.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self._hero.set_direction(Direction.UP)
        elif pressed[pygame.K_LEFT]:
            self._hero.set_direction(Direction.LEFT)
        elif pressed[pygame.K_DOWN]:
            self._hero.set_direction(Direction.DOWN)
        elif pressed[pygame.K_RIGHT]:
            self._hero.set_direction(Direction.RIGHT)


class MovableObject(GameObject):
    """
    An implementation of the MovableObject game object that inherits from GameObject class.
    Represent objects in the game that can move on the screen.

    Attributes:
        current_direction (Direction): The current direction of the object's movement.
        direction_buffer (Direction): The next direction to be considered in movement.
        last_working_direction (Direction): The previous direction that allowed movement.
        location_queue (list): A list of target locations for the object to move towards.
        next_target (Optional[Tuple[int, int]]): The next target location in the location_queue.
    """

    def __init__(self, in_surface, x, y, in_size: int,
                 in_color=(255, 0, 0), is_circle: bool = False) -> None:
        """
            Initializes a MovableObject instance.

            Args:
                in_surface (GameRenderer): The renderer instance for drawing game objects.
                x (int): X coordinate of the object's position.
                y (int): Y coordinate of the object's position.
                in_size (int): The size of the object.
                in_color (tuple, optional): RGB color of the object. Defaults to (255, 0, 0).
                is_circle (bool, optional): Indicates if the object should be rendered as a circle.
                Defaults to False.
        """
        super().__init__(in_surface, x, y, in_size, in_color, is_circle)
        self.current_direction = Direction.NONE
        self.direction_buffer = Direction.NONE
        self.last_working_direction = Direction.NONE
        self.location_queue = []
        self.next_target = None

    def get_next_location(self) -> Optional[Tuple[int, int]]:
        """
            Returns the next location in the location_queue, or None if the queue is empty.

            Returns:
                Optional[Tuple[int, int]]: A tuple of the next target X and Y coordinates, or None.
        """
        return None if len(self.location_queue) == 0 else self.location_queue.pop(0)

    def set_direction(self, in_direction) -> None:
        """
            Sets the current direction for the object.

            Args:
                in_direction (Direction): The direction in which the object should move.
         """
        self.current_direction = in_direction
        self.direction_buffer = in_direction

    def collides_with_wall(self, in_position) -> bool:
        """
           Checks if the object collides with any walls at the specified position.

           Args:
               in_position (Tuple[int, int]): The position to check for wall collisions.

           Returns:
               bool: True if the object collides with a wall, otherwise False.
        """
        collision_rect = pygame.Rect(in_position[0], in_position[1], self._size, self._size)
        collides = False
        walls = self._renderer.get_walls()
        for wall in walls:
            collides = collision_rect.colliderect(wall.get_shape())
            if collides: break
        return collides

    def check_collision_in_direction(self, in_direction: Direction) -> Tuple[bool, Tuple[int, int]]:
        """
           Checks if the object would collide with any walls if it moves in the given direction.

           Args:
               in_direction (Direction): The direction to check for collision.

           Returns:
               Tuple[bool, Tuple[int, int]]: True if the object would collide with a wall, and the desired position.
        """
        desired_position = (0, 0)
        if in_direction == Direction.NONE: return False, desired_position
        if in_direction == Direction.UP:
            desired_position = (self.x, self.y - 1)
        elif in_direction == Direction.DOWN:
            desired_position = (self.x, self.y + 1)
        elif in_direction == Direction.LEFT:
            desired_position = (self.x - 1, self.y)
        elif in_direction == Direction.RIGHT:
            desired_position = (self.x + 1, self.y)

        return self.collides_with_wall(desired_position), desired_position

    def automatic_move(self, in_direction: Direction) -> None:
        """
            Automatically moves the object in the given direction.

            Args:
                in_direction (Direction): The direction in which the object should move.
        """
        pass

    def tick(self) -> None:
        """
            Performs tasks related to the game loop specific to the MovableObject.

            Updates the position based on achieved target and automatically moves the object.
        """
        self.reached_target()
        self.automatic_move(self.current_direction)

    def reached_target(self) -> None:
        """
            Performs actions when the object has reached its target in the location_queue.

            e.g., Can be used to remove cookies when a hero object reaches the cookie.
        """
        pass


class Hero(MovableObject):
    """
    A subclass of MovableObject representing the Hero character in the game.

    Attributes:
        last_non_colliding_position (Tuple[int, int]): The last position where the Hero did not collide with any walls.
    """

    def __init__(self, in_surface, x, y, in_size: int) -> None:
        """
            Initializes a Hero instance.

            Args:
                in_surface (GameRenderer): The renderer instance for drawing game objects.
                x (int): X coordinate of the object's position.
                y (int): Y coordinate of the object's position.
                in_size (int): The size of the object.
        """
        super().__init__(in_surface, x, y, in_size, (255, 255, 0), False)
        self.last_non_colliding_position = (0, 0)

    def tick(self) -> None:
        """
          Performs tasks related to the game loop specific to the Hero character.

          Takes care of teleportation, movement, and cookie pickup.
        """
        # TELEPORT
        if self.x < 0:
            self.x = self._renderer._width

        if self.x > self._renderer._width:
            self.x = 0

        self.last_non_colliding_position = self.get_position()

        if self.check_collision_in_direction(self.direction_buffer)[0]:
            self.automatic_move(self.current_direction)
        else:
            self.automatic_move(self.direction_buffer)
            self.current_direction = self.direction_buffer

        if self.collides_with_wall((self.x, self.y)):
            self.set_position(self.last_non_colliding_position[0],
                              self.last_non_colliding_position[1])

        self.handle_cookie_pickup()

    def automatic_move(self, in_direction: Direction) -> None:
        """
            Automatically moves the Hero in the given direction.

            Args:
                in_direction (Direction): The direction in which the object should move.
        """
        collision_result = self.check_collision_in_direction(in_direction)

        desired_position_collides = collision_result[0]
        if not desired_position_collides:
            self.last_working_direction = self.current_direction
            desired_position = collision_result[1]
            self.set_position(desired_position[0], desired_position[1])
        else:
            self.current_direction = self.last_working_direction

    def handle_cookie_pickup(self) -> None:
        """
            Handles the logic for picking up cookies during the game.
        """
        collision_rect = pygame.Rect(self.x, self.y, self._size, self._size)
        cookies = self._renderer.get_cookies()
        game_objects = self._renderer.get_game_objects()
        for cookie in cookies:
            collides = collision_rect.colliderect(cookie.get_shape())
            if collides and cookie in game_objects:
                game_objects.remove(cookie)

    def draw(self) -> None:
        """
            Draws the Hero on the GameRenderer's surface.
        """
        half_size = self._size / 2
        pygame.draw.circle(self._surface, self._color,
                           (self.x + half_size, self.y + half_size), half_size)


class Ghost(MovableObject):
    """
    A subclass of MovableObject representing a Ghost character in the game.

    Attributes:
        game_controller (object): Reference to the game controller instance.
    """

    def __init__(self, in_surface, x, y, in_size: int, in_game_controller, in_color=(255, 0, 0)):
        """
           Initializes a Ghost instance.

           Args:
               in_surface (GameRenderer): The renderer instance for drawing game objects.
               x (int): X coordinate of the object's position.
               y (int): Y coordinate of the object's position.
               in_size (int): The size of the object.
               in_game_controller (object): Reference to the game controller instance.
               in_color (tuple, optional): RGB color of the object. Defaults to (255, 0, 0).
        """
        super().__init__(in_surface, x, y, in_size, in_color, False)
        self.game_controller = in_game_controller

    def reached_target(self) -> None:
        """
            Handles the logic for when the Ghost reaches its target location.
        """
        if (self.x, self.y) == self.next_target:
            self.next_target = self.get_next_location()
        self.current_direction = self.calculate_direction_to_next_target()

    def set_new_path(self, in_path) -> None:
        """
            Sets the new path for the Ghost to follow.

            Args:
                in_path (list): A list of target locations for the object to move towards.
        """
        for item in in_path:
            self.location_queue.append(item)
        self.next_target = self.get_next_location()

    def calculate_direction_to_next_target(self) -> Direction:
        """
            Calculates the direction for the Ghost to move toward its next target.

            Returns:
                Direction: The direction to move toward the next target or request a new path.
        """
        if self.next_target is None:
            self.game_controller.request_new_random_path(self)
            return Direction.NONE
        diff_x = self.next_target[0] - self.x
        diff_y = self.next_target[1] - self.y
        if diff_x == 0:
            return Direction.DOWN if diff_y > 0 else Direction.UP
        if diff_y == 0:
            return Direction.LEFT if diff_x < 0 else Direction.RIGHT
        self.game_controller.request_new_random_path(self)
        return Direction.NONE

    def automatic_move(self, in_direction: Direction) -> None:
        """
        Automatically moves the Ghost in the given direction.

        Args:
            in_direction (Direction): The direction in which the object should move.
        """
        if in_direction == Direction.UP:
            self.set_position(self.x, self.y - 1)
        elif in_direction == Direction.DOWN:
            self.set_position(self.x, self.y + 1)
        elif in_direction == Direction.LEFT:
            self.set_position(self.x - 1, self.y)
        elif in_direction == Direction.RIGHT:
            self.set_position(self.x + 1, self.y)


class Cookie(GameObject):
    """
    A subclass of GameObject representing a Cookie object in the game.
    """
    def __init__(self, in_surface, x, y) -> None:
        """
        Initializes a Cookie instance.

        Args:
            in_surface (GameRenderer): The renderer instance for drawing game objects.
            x (int): X coordinate of the object's position.
            y (int): Y coordinate of the object's position.
        """
        super().__init__(in_surface, x, y, 4, (255, 255, 0), True)


class Pathfinder:
    """
    A class responsible for calculating the path for the Ghost characters in the game.

    Attributes:
        pf (tcod.path.AStar object): A pathfinding instance for calculating the shortest path.
    """
    def __init__(self, in_arr) -> None:
        """
        Initializes a Pathfinder instance.

        Args:
            in_arr (list): A list of cost values for each position in the game grid.
        """
        cost = np.array(in_arr, dtype=np.bool_).tolist()
        self.pf = tcod.path.AStar(cost=cost, diagonal=0)

    def get_path(self, from_x, from_y, to_x, to_y) -> object:
        """
        Returns the shortest path from one point to another.

        Args:
            from_x (int): The starting point's X coordinate.
            from_y (int): The starting point's Y coordinate.
            to_x (int): The target point's X coordinate.
            to_y (int): The target point's Y coordinate.

        Returns:
            object: An ordered list of points for the shortest path from the starting point
            to the target.
        """
        res = self.pf.get_path(from_x, from_y, to_x, to_y)
        return [(sub[1], sub[0]) for sub in res]


class PacmanGameController:
    """
    A class responsible for managing the game state, maze, and pathfinding functionality in a Pac-Man game.
    """
    def __init__(self):
        """
            Initializes a PacmanGameController instance and sets up the maze configuration.
        """
        self.ascii_maze = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XP           XX            X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X                          X",
            "X XXXX XX XXXXXXXX XX XXXX X",
            "X XXXX XX XXXXXXXX XX XXXX X",
            "X      XX    XX    XX      X",
            "XXXXXX XXXXX XX XXXXX XXXXXX",
            "XXXXXX XXXXX XX XXXXX XXXXXX",
            "XXXXXX XX          XX XXXXXX",
            "XXXXXX XX XXXXXXXX XX XXXXXX",
            "XXXXXX XX X   G  X XX XXXXXX",
            "          X G    X          ",
            "XXXXXX XX X   G  X XX XXXXXX",
            "XXXXXX XX XXXXXXXX XX XXXXXX",
            "XXXXXX XX          XX XXXXXX",
            "XXXXXX XX XXXXXXXX XX XXXXXX",
            "XXXXXX XX XXXXXXXX XX XXXXXX",
            "X            XX            X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X XXXX XXXXX XX XXXXX XXXX X",
            "X   XX       G        XX   X",
            "XXX XX XX XXXXXXXX XX XX XXX",
            "XXX XX XX XXXXXXXX XX XX XXX",
            "X      XX    XX    XX      X",
            "X XXXXXXXXXX XX XXXXXXXXXX X",
            "X XXXXXXXXXX XX XXXXXXXXXX X",
            "X                          X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        ]

        self.numpy_maze = []
        self.cookie_spaces = []
        self.reachable_spaces = []
        self.ghost_spawns = []
        self.ghost_colors = [
            (255, 184, 255),
            (255, 0, 20),
            (0, 255, 255),
            (255, 184, 82)
        ]
        self.size = (0, 0)
        self.convert_maze_to_numpy()
        self.p = Pathfinder(self.numpy_maze)

    def request_new_random_path(self, in_ghost: Ghost) -> None:
        """
        Generates a random path for the provided Ghost object by selecting a random reachable space on the maze.

        Args:
            in_ghost (Ghost): The Ghost object for which a new random path needs to be generated.
        """
        random_space = random.choice(self.reachable_spaces)
        current_maze_coord = translate_screen_to_maze(in_ghost.get_position())

        path = self.p.get_path(current_maze_coord[1], current_maze_coord[0], random_space[1],
                               random_space[0])
        test_path = [translate_maze_to_screen(item) for item in path]
        in_ghost.set_new_path(test_path)

    def convert_maze_to_numpy(self) -> None:
        """
        Converts the initial ASCII maze representation into a NumPy array for easier maze operations and pathfinding.
        """
        for x, row in enumerate(self.ascii_maze):
            self.size = (len(row), x + 1)
            binary_row = []
            for y, column in enumerate(row):
                if column == "G":
                    self.ghost_spawns.append((y, x))

                if column == "X":
                    binary_row.append(0)
                else:
                    binary_row.append(1)
                    self.cookie_spaces.append((y, x))
                    self.reachable_spaces.append((y, x))
            self.numpy_maze.append(binary_row)


if __name__ == "__main__":
    unified_size = 32
    pacman_game = PacmanGameController()
    size = pacman_game.size
    game_renderer = GameRenderer(size[0] * unified_size, size[1] * unified_size)

    for y, row in enumerate(pacman_game.numpy_maze):
        for x, column in enumerate(row):
            if column == 0:
                game_renderer.add_wall(Wall(game_renderer, x, y, unified_size))

    for cookie_space in pacman_game.cookie_spaces:
        translated = translate_maze_to_screen(cookie_space)
        cookie = Cookie(game_renderer, translated[0] + unified_size / 2,
                        translated[1] + unified_size / 2)
        game_renderer.add_cookie(cookie)

    for i, ghost_spawn in enumerate(pacman_game.ghost_spawns):
        translated = translate_maze_to_screen(ghost_spawn)
        ghost = Ghost(game_renderer, translated[0], translated[1], unified_size, pacman_game,
                      pacman_game.ghost_colors[i % 4])
        game_renderer.add_game_object(ghost)

    pacman = Hero(game_renderer, unified_size, unified_size, unified_size)
    game_renderer.add_hero(pacman)
    game_renderer.tick(120)

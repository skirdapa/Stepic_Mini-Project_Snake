import copy
import random
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SnakeTheGame(metaclass=SingletonMeta):

    class Snake:

        def __init__(self):
            self.length = 2
            self.head_position = [1, 1]
            self.body_position = [[0, 1]]

        def move_body(self, meal_position):
            if self.head_position != meal_position:
                self.body_position.pop()
            self.body_position.insert(0, copy.deepcopy(self.head_position))

        def step_left(self):
            self.head_position[0] -= 1

        def step_right(self):
            self.head_position[0] += 1

        def step_up(self):
            self.head_position[1] -= 1

        def step_down(self):
            self.head_position[1] += 1

    def __init__(self, height=10, width=15, type_of_game="step", field_is_infinity=True):
        self.height = height
        self.width = width
        self.type_of_game = type_of_game
        self.field_is_infinity = field_is_infinity
        self.snake = self.Snake()
        self.meal_position = self.get_meal_position()

    def get_meal_position(self):
        pos = [random.randint(0, self.width-1), random.randint(0, self.height-1)]
        print("я гетмил позишн", pos)
        if pos in self.snake.body_position or pos == self.snake.head_position:
            print("Гетмил: Позиция еды совпала с позицией змейки")
            return self.change_meal_position()
        return pos

    def change_meal_position(self):
        self.meal_position = self.get_meal_position()
        if self.meal_position in self.snake.body_position or self.meal_position == self.snake.head_position:
            print("Ченджмил: Позиция еды совпала с позицией змейки", self.meal_position)
            return self.change_meal_position()

    def snake_move(self, direction):
        direction_dict = {
            "up": self.snake.step_up,
            "down": self.snake.step_down,
            "right": self.snake.step_right,
            "left": self.snake.step_left
        }
        self.snake.move_body(self.meal_position)
        if self.snake.head_position == self.meal_position:
            self.change_meal_position()
        direction_dict[direction]()
        print("Змейка движется", direction)
        # Следующие две строки должны научить змейку ходить сквозь стены
        self.snake.head_position[0] = self.snake.head_position[0] % self.width
        self.snake.head_position[1] = self.snake.head_position[1] % self.height


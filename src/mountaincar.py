import random
from math import cos
from typing import Literal, Tuple, Union

Action = Union[Literal[-1], Literal[0], Literal[1]]
State = Tuple[float, float]
Output = Tuple[State, int, bool]


class MountainCar:

    position_bound = (-1.2, 0.6)
    velocity_bound = (-0.07, 0.07)
    position_range = abs(position_bound[0] - position_bound[1])
    velocity_range = abs(velocity_bound[0] - velocity_bound[1])

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> Output:
        self.position = -0.6 + random.random() * 0.2
        self.velocity = 0.0
        return (self.position, self.velocity), -1, False

    def step(self, action: Action) -> Output:
        self.velocity = self.__bound_velocity(self.velocity + 0.001 * action - 0.0025 * cos(3 * self.position))
        self.position = self.__bound_position(self.position + self.velocity)
        return (self.position, self.velocity), self.get_reward(), self.is_final_state()

    def is_final_state(self) -> bool:
        return self.position >= MountainCar.position_bound[1]

    def __bound_position(self, position: float) -> float:
        self.velocity *= int(position < MountainCar.position_bound[0])  # set velocity to zero if out of bounds
        return max(MountainCar.position_bound[0], position)

    def __bound_velocity(self, velocity: float) -> float:
        return min(MountainCar.velocity_bound[1], max(MountainCar.velocity_bound[0], velocity))

    def get_reward(self) -> int:
        return 1 - 2 * int(self.is_final_state())

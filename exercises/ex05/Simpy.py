"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730395244"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
       self.values = values 

    def __repr__(self) -> str:
        return f"Simpy({self.values})"

    def fill(self, x_val: float, y_index: int) -> None:
        self.values = []
        for i in range(y_index):
            self.values.append(x_val)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None: 
        self.values = []
        step != 0.0
        self.values.append(start)
        value: float = start + step 
        if step > 0:
            while value < stop:
                self.values.append(value)
                value += step
        else:
            while value > stop:
                self.values.append(value)
                value += step

    def sum(self) -> float:
        return sum(self.values)

    def __add__(self,rhs: Union[float, Simpy]) -> Simpy:
        final: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                final.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                final.append(self.values[i] + rhs.values[i])
        
        return Simpy(final)

    def __pow__(self, power: Union[float, Simpy]) -> Simpy:
        final: list[float] = []
        if isinstance(power, float):
            for item in self.values:
                final.append(item ** power)
        else:
            assert len(self.values) == len(power.values)
            for i in range(len(self.values)):
                final.append(self.values[i] ** power.values[i])
        
        return Simpy(final)

    def __mod__(self, remain: Union[float, Simpy]) -> Simpy:
        final: list[float] = []
        if isinstance(remain, float):
            for item in self.values:
                final.append(item % remain)
        else:
            assert len(self.values) == len(remain.values)
            for i in range(len(self.values)):
                final.append(self.values[i] % remain.values[i])
        
        return Simpy(final)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        return self.values[rhs]

        

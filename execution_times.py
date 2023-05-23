# This Python file uses the following encoding: windows-1251

from typing import Optional, Callable, List, Tuple
from time import perf_counter
from util import check_values
from random import randint


class ExecutionTimeContextManager:
    # Контекстный менеджер для замера времени выполнения кода.
    #
    def __init__(self) -> None:
        self.__time: Optional[float] = None

    def __enter__(self) -> 'ExecutionTimeContextManager':
        self.__time = perf_counter()
        return self

    def __exit__(self, *exc) -> None:
        self.__time = perf_counter() - self.__time

    @property
    def time(self) -> Optional[float]:
        return self.__time


def get_values(number_of_runs: int, start: int,
               finish: int) -> List[Tuple[int, int, int]]:
    # Функция генерирует значения для проверки времени исполнения.
    # Значения подбираются для соответствия условиям методов.
    values = []
    for _ in range(number_of_runs):
        a, b, p = 0, 0, 0
        # Пока числа не соответствуют условиям метода
        # генерируем новые значения
        while not check_values(a, b, p):
            a, b, p = randint(
                start, finish), randint(
                start, finish), randint(
                start, finish)
        values.append((a, b, p))
    return values


def method_mean_execution_time(
        method: Callable, values: List[Tuple[int, int, int]]) -> float:
    # Вычисляет среднее время выполнения метода.
    #
    total_time = 0
    # Замеряем время выполнения кода для каждого значения
    for a, b, p in values:
        with ExecutionTimeContextManager() as time_context_manager:
            method(a, b, p)
        total_time += time_context_manager.time
    # Вычисляем среднее время выполнения метода
    return total_time / len(values)

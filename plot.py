from matplotlib import pyplot as plt
from params import *
import population
from typing import Callable
from crossbreed import fill_generation
from adaptation import get_highest_adaptation
from selection import add_elite
import numpy as np
from matplotlib import pyplot as plt


def can_quit(population_a: np.ndarray, population_b: np.ndarray) -> bool:
    can_quit_a = np.unique(
        population_a, axis=0).shape[0] < POPULATION_SIZE * MIN_CHANGE_RATIO
    can_quit_b = np.unique(
        population_b, axis=0).shape[0] < POPULATION_SIZE * MIN_CHANGE_RATIO
    return can_quit_a or can_quit_b


def plot_a(min: np.ndarray, mean: np.ndarray, max: np.ndarray, name: str) -> None:
    x_points = list(range(len(mean)))
    plt.plot(x_points, min, color='thistle',
             label=f'min ({name})', linestyle='dashed')
    plt.plot(x_points, max, color='pink',
             label=f'max ({name})', linestyle='dashed')
    plt.plot(x_points, mean, color='palevioletred',
             label=f'mean ({name})', lw=2)


def plot_b(min: np.ndarray, mean: np.ndarray, max: np.ndarray, name: str) -> None:
    x_points = list(range(len(mean)))
    plt.plot(x_points, min, color='yellowgreen',
             label=f'min ({name})', linestyle='dashed')
    plt.plot(x_points, max, color='darkolivegreen',
             label=f'max ({name})', linestyle='dashed')
    plt.plot(x_points, mean, color='olive', label=f'mean ({name})', lw=2)


def plot_comparison(method_a: Callable, method_b: Callable, a_name: str, b_name: str, elite_a=False, elite_b=False) -> None:
    starting_population = population.random_population()
    values_a = []
    values_b = []

    for _ in range(REPEATS):
        population_a = starting_population.copy()
        population_b = starting_population.copy()
        values_a.append([])
        values_b.append([])

        for i in range(NO_OF_ITERATIONS):
            a_copy = population_a
            b_copy = population_b
            population_a = method_a(population_a)
            population_b = method_b(population_b)

            population_a = fill_generation(a_copy, population_a)
            population_b = fill_generation(b_copy, population_b)

            if elite_a:
                population_a = add_elite(population_a, a_copy)
            if elite_b:
                population_b = add_elite(population_b, b_copy)

            values_a[-1].append(get_highest_adaptation(population_a))
            values_b[-1].append(get_highest_adaptation(population_b))

            # if (can_quit(population_a, population_b) and i != 0):
            #     print(f"Stopped due to no alterations in {i} iterations.")
            #     break

    values_a = np.array(values_a)
    values_b = np.array(values_b)
    mean_a, mean_b = np.mean(values_a, axis=0), np.mean(values_b, axis=0)
    min_a, min_b = values_a[np.argmin(
        values_a[:, -1])], values_b[np.argmin(values_b[:, -1])]
    max_a, max_b = values_a[np.argmax(
        values_a[:, -1])], values_b[np.argmax(values_b[:, -1])]
    plt.figure()
    plot_a(min_a, mean_a, max_a, a_name)
    plot_b(min_b, mean_b, max_b, b_name)
    plt.legend()
    plt.title(f"{a_name} vs {b_name}")
    plt.xlabel("Iterations")
    plt.ylabel("Knapsack value")
    plt.savefig(f"plots/{a_name}_vs_{b_name}.png")

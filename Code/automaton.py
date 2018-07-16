#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Modules for Cellular Automata

Created by mitssi on 2018.07
Ported to Python by hwyncho on 2018.07
Last updated by hwyncho on 2018.07
"""
import numpy as np
import random

__N_NEIGHBOR__ = 1
random.seed = 1


def __find(lettice, x, y):
    ret = 0
    length_x = len(lettice)
    length_y = len(lettice[0])
    for i in range(x - __N_NEIGHBOR__, x + __N_NEIGHBOR__ + 1):
        for j in range(y - __N_NEIGHBOR__, y + __N_NEIGHBOR__ + 1):
            if (i >= 0) and (j >= 0):
                if (i < length_x) and (j < length_y):
                    if(i == x) and (j == y):
                        pass
                    else:
                        if(lettice[i][j] == 1):
                            ret += 1
    return ret


def __cnt_dead(lettice):
    num_dead = 0
    for i in lettice:
        for j in i:
            if j == 1:
                num_dead += 1
    return num_dead


def run(initial_lettice, rules, max_t):
    """
    Run cellular automaton

    Parameters
    ----------
    initial_lettice: list
        a two dimensional array of states (0, 1)
    rules: list
        the first row states the probabilities for getting sick,
        the second one states the probabilities for becoming healthy.
    max_t: int
        the maximum number of steps

    Returns
    -------
    percentage_of_dead_list: percentage of dead in each checkpoint
    """
    # temp_lettice = np.zeros(
    #     shape=(len(initial_lettice), len(initial_lettice[0])),
    #     dtype=np.int32
    # )
    lettice = initial_lettice
    infected_list = rules[0]
    healthy_list = rules[1]

    interval = int(max_t / 40)
    max_t = 40 * interval

    num_dead_list = []

    for t in range(max_t):
        for i in range(len(lettice)):
            for j in range(len(lettice[0])):
                ret = __find(lettice, i, j)
                if lettice[i][j] == 0:
                    # Healthy
                    if random.random() > infected_list[ret]:
                        lettice[i][j] = 1
                else:
                    # Infected
                    if random.random() > healthy_list[ret]:
                        lettice[i][j] = 0
        if t % interval == interval - 1:
            # Count Dead
            num_dead_list.append(__cnt_dead(lettice))

    return [p / (len(lettice) * len(lettice[0])) for p in num_dead_list]

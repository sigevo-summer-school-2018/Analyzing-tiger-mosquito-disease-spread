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


def __find(lettice):
    ret = 0
    for i in range(-__N_NEIGHBOR__, __N_NEIGHBOR__):
        for j in range(-__N_NEIGHBOR__, __N_NEIGHBOR__):
            if (i != 0) or (j != 0):
                try:
                    ret += 1
                except IndexError:
                    pass
    return ret


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
    list: the lettice after the last step
    """
    temp_lettice = np.zeros(
        shape=(len(initial_lettice), len(initial_lettice[0])),
        dtype=np.int32
    )

    for _ in range(max_t):
        for i in range(len(initial_lettice)):
            for j in range(len(initial_lettice[0])):
                ret = __find(initial_lettice)
                if ret > 8:
                    temp_lettice[i][j] = 0
                elif ret > random.randint(0, 9):
                    temp_lettice[i][j] = 1

        initial_lettice = np.copy(temp_lettice)

    return initial_lettice

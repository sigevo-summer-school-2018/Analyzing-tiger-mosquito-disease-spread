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
import visualization
import matplotlib.pyplot as plt
import time

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
    return np.sum(lettice)
    # num_dead = 0
    # for i in lettice:
    #     for j in i:
    #         if j == 1:
    #             num_dead += 1
    # return num_dead


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
    lettice = initial_lettice
    infected_list = rules[0]
    # infected_list[0] = 0
    # healthy_list = rules[1]
    healthy_list = [0 for i in range(9)]
    

    interval = int(max_t / 40)
    max_t = 40 * interval

    num_dead_list = []
    max_t = 100

    for t in range(max_t):
        for i in range(len(lettice)):
            for j in range(len(lettice[0])):
                ret = __find(lettice, i, j)
                if lettice[i][j] == 0:
                    # Healthy
                    if random.random() < infected_list[ret]:
                        lettice[i][j] = 1
                else:
                    # Infected
                    if random.random() < healthy_list[ret]:
                        lettice[i][j] = 0
        if t % interval == interval - 1:
            # Count Dead
            f = visualization.visualize(lettice)
            plt.savefig("{0}".format(t))
            plt.close()
            num_dead_list.append(__cnt_dead(lettice))

    return [p / (len(lettice) * len(lettice[0])) for p in num_dead_list]

if __name__ == "__main__":
    # rule = [0.0003297737907633886, 0, 0.00977004021178135, 0.06899429314114995, 0.03391205094844124, 0.047611355108938325, 0.396937675302771, 0.4009062256441605, 0.03301177071079503, 0.5970793732951427, 0.008563472492026492, 0.552986439666293, 0.8489031785472745, 0.042278492503549314, 0.025865979778054993, 0.061517985743333614, 0.5272793420488546, 0.014694425059099708]
    rule = [0, 0, 0.02344820705595596, 0.06275308998803553, 0.4422351603378323, 0.9288185356136194, 0.1805670902620428, 0.41711208810473793, 0.012761389933050094, 0.39243411117547716, 0.5552289174288184, 0.78865200576032, 0.7027009270818957, 0.18810640913625332, 0.2698189250463883, 0.7167234695630383, 0.14335972676938735, 0.4893772535423733]
    # rule = [rule[:9], rule[9:]]
    # rule[0] = 0
    rule = [rule[:9], [0 for i in range(9)]]
    initial_lattice = np.zeros(shape=(40,40))
    for i in range(10):
        initial_lattice[random.randint(15, 20)][random.randint(15, 20)] = 1
    # for i in range(13, 19):
    #     for j in range(13, 18):
    #         initial_lattice[i][j] = 1
    # for i in range(10):
    #     initial_lattice[random.randint(10, 30)][random.randint(10, 30)] = 1
    # initial_lattice[20][20] = 1
    # initial_lattice[21][20] = 1
    # initial_lattice[20][21] = 1
    # initial_lattice[19][20] = 1
    # initial_lattice[20][19] = 1
    run(initial_lattice,  rule, 40)

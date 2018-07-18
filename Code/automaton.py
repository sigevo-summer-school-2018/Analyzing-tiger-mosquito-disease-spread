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
                    if random.random() < infected_list[ret]:
                        lettice[i][j] = 1
                else:
                    # Infected
                    if random.random() < healthy_list[ret]:
                        lettice[i][j] = 0
        if t % interval == interval - 1:
            # Count Dead
            f = visualization.visualize(lettice)
            plt.show()
            time.sleep(10)
            plt.close()
            num_dead_list.append(__cnt_dead(lettice))

    return [p / (len(lettice) * len(lettice[0])) for p in num_dead_list]

if __name__ == "__main__":
    rule = [0.05853196952085602, 0.09743265622373784, 0.02773355886430057, 0.8227126156307412, 0.35361907624358124, 0.22257027943659416, 0.3965234075968833, 0.6054585763391022, 0.7320708933391471, 0.6341923245403308, 0.972395101523802, 0.7358390785672153, 0.9510975018484704, 0.7309558815442023, 0.48499094603492515, 0.015516943518788517, 0.10269183636745804, 0.8053372027588928]
    rule = [rule[:9], rule[9:]]
    initial_lattice = np.zeros(shape=(40,40))
    initial_lattice[20][20] = 1
    run(initial_lattice,  rule, 40)

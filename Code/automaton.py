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
            plt.close()
            num_dead_list.append(__cnt_dead(lettice))

    return [p / (len(lettice) * len(lettice[0])) for p in num_dead_list]

if __name__ == "__main__":
    # rule = [0.05853196952085602, 0.09743265622373784, 0.02773355886430057, 0.8227126156307412, 0.35361907624358124, 0.22257027943659416, 0.3965234075968833, 0.6054585763391022, 0.7320708933391471, 0.6341923245403308, 0.972395101523802, 0.7358390785672153, 0.9510975018484704, 0.7309558815442023, 0.48499094603492515, 0.015516943518788517, 0.10269183636745804, 0.8053372027588928]
    # rule = [0, 0.09743265622373784, 0.02773355886430057, 0.8227126156307412, 0.35361907624358124, 0.22257027943659416, 0.3965234075968833, 0.6054585763391022, 0.7320708933391471, 0.6341923245403308, 0.972395101523802, 0.7358390785672153, 0.9510975018484704, 0.7309558815442023, 0.48499094603492515, 0.015516943518788517, 0.10269183636745804, 0.8053372027588928]
    # rule = [0.36402717574033144, 0.024910302717958643, 2.5075922775321215e-06, 9.22308564228951e-05, 0.1240322787269696, 0, 1, 0.5056644072107338, 0.9986478412584208, 0.20634347146748827, 0.14071090781937973, 0.9940410011740464, 0.5022894968392613, 0.00028277824005017334, 0.9823022552227358, 0.17811337450347392, 0.9284668067568186, 0]
    rule = [0.0003297737907633886, 0, 0.00977004021178135, 0.06899429314114995, 0.03391205094844124, 0.047611355108938325, 0.396937675302771, 0.4009062256441605, 0.03301177071079503, 0.5970793732951427, 0.008563472492026492, 0.552986439666293, 0.8489031785472745, 0.042278492503549314, 0.025865979778054993, 0.061517985743333614, 0.5272793420488546, 0.014694425059099708]
    # rule = [0.31034613852186704, 0, 0.03279851419907594, 0.04176553543237709, 0.18956833024270292, 0.5320855211856265, 0.18779393106440617, 0.45574951630879174, 0.4084479191634173, 0, 1, 0.4781662130439799, 0, 0.8183085053747439, 0.36216808699458003, 0.31036123405697114, 0.32884693895749806, 0.04286343830763449]
    # rule = [rule[:9], rule[9:]]
    # rule[0] = 0
    rule = [rule[:9], [0 for i in range(9)]]
    initial_lattice = np.zeros(shape=(40,40))
    for i in range(13, 19):
        for j in range(13, 18):
            initial_lattice[i][j] = 1
    # for i in range(10):
    #     initial_lattice[random.randint(10, 30)][random.randint(10, 30)] = 1
    # initial_lattice[20][20] = 1
    # initial_lattice[21][20] = 1
    # initial_lattice[20][21] = 1
    # initial_lattice[19][20] = 1
    # initial_lattice[20][19] = 1
    run(initial_lattice,  rule, 40)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:27:41 2020

@author: quantuminw
"""
#Coin-tossing random walk simulation
import numpy as np
import matplotlib.pyplot as plt

def RANDOMWALK(walk_steps):
    #Initial position
    walker = 0
    POS = np.zeros(walk_steps)
    #Tossing results
    toss = np.round(np.random.random(walk_steps), 2)
    
    #Walk following the results
    for ii in range(len(toss)):
        if toss[ii] < PROB:
            walker -= 1
        else:
            walker += 1
        #Save position
        POS[ii] = walker
    return POS

#Fair coin
PROB = 0.50
walk_steps = 400
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, constrained_layout=True)

#Generate Walker's trajectories
DATA = []
for idx in range(1000):
    traj = RANDOMWALK(walk_steps)
    DATA.append(traj)
    plt.plot(range(len(traj)), traj)

#Get mean and variance
avg = np.mean(DATA, axis=0)
ax1.scatter(range(len(traj)), avg, ';')
var = np.std(DATA, axis=0)
ax2.scatter(range(len(traj)), var, ';')

ax0.title('Walk trajectories')
ax1.title.set_text('Average VS steps')
ax2.title.set_text('STD VS steps')

ax1.set_ylim([-20, 20])
#plt.savefig("RANDOMWALK", dpi=500)
# Remember to adjust your student ID in meta.xml
import numpy as np
import pickle
import random
import gym

def get_action(obs):
    stations = [[0,0] for _ in range(4)]
    taxi_row, taxi_col, stations[0][0], stations[0][1] , stations[1][0], stations[1][1], stations[2][0], stations[2][1], stations[3][0], stations[3][1], obstacle_north, obstacle_south, obstacle_east, obstacle_west, passenger_look, destination_look = obs

    actions = []
    if not obstacle_south:
        actions.append(0)
    if not obstacle_north:
        actions.append(1)
    if not obstacle_east:
        actions.append(2)
    if not obstacle_west:
        actions.append(3)
    
    #print([taxi_row, taxi_col], stations)
    if [taxi_row, taxi_col] in stations:
        #print("hello")
        actions.append(4)
        actions.append(5)
        
     
    return random.choice(actions) # Choose a random action
    # You can submit this random agent to evaluate the performance of a purely random strategy.


# Remember to adjust your student ID in meta.xml
import numpy as np
import pickle
import random
import gym

last_passenger = 0
last_destination = 0

def get_action(obs):
    global last_passenger
    global last_destination
    
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
    
    if [taxi_row, taxi_col] in stations and last_passenger:
        actions.append(4)
    if [taxi_row, taxi_col] in stations and last_destination:
        actions.append(5)
        
    last_passenger = passenger_look
    last_destination = destination_look
    if not actions: # just in case
        actions = [0,1,2,3,4,5]
    return random.choice(actions) # Choose a random action
    # You can submit this random agent to evaluate the performance of a purely random strategy.


# A reward function designed to avoid obstacles on the 2022 Re:Invent track. 
# The car is rewarded when it operates on a different lane than the object while approaching and maintains a safe distance from the center line.

import math
def reward_function(params):
    
    reward = 21
    
	# parameters 
    steps = params['steps']
    progress = params['progress']
    speed = params['speed']
    benchmark_time = 15.0
    agent_x = params['x']
    agent_y = params['y']
    on_track = not(params['is_offtrack'])
    track_length = params['track_length']
    track_width = params['track_width']
    objects_location = params['objects_location']
    object_distance = params['objects_distance']
    _, next_object_index = params['closest_objects'] # next object 
    objects_left_of_center = params['objects_left_of_center'] #is object on left lane 
    is_left_of_center = params['is_left_of_center'] # is agent on left lane 
    is_crash = params['is_crashed']
    distance_from_center = params['distance_from_center']
    
    # calculate the distance between agent and the closest object 
    #distance = abs(object_distance[next_object_index] - progress*track_length)
    next_object_loc = objects_location[next_object_index]
    distance_closest_object = math.sqrt((agent_x - next_object_loc[0])**2 + (agent_y - next_object_loc[1])**2)
	
    # check if the agent and the next object is on the same lane
    is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center
    
    if on_track:
        reward += 10
    else:
        reward -= 20
    
    # penalise if it crashes with an object 
    if is_crash:
        reward -= 20
        
    # Give higher reward if the car completes the track
    if progress >= 100:
        reward += 100
    elif progress >= 75:
        reward += 50
    elif progress >= 50:
        reward += 20
    elif progress >= 25:
        reward += 10
    else:
        reward -= 10 # not good progress 
        
    
    # reward if the agent and next object is close to each other, is not close to center line and is different lane, penalise otherwise 
	# reward if car stays within the border of the track
    if not is_same_lane:
        if distance_closest_object < 0.8:
            if 0.05 <= (0.5 * (track_width - distance_from_center)) <= 0.28:
                reward += 10 
            else:
                reward -= 10 # likely crash 
        else:
            reward += 10
    else:
        if distance_closest_object < 0.8:
            reward -= 10 #likely crash 
    
    
    return float(reward)
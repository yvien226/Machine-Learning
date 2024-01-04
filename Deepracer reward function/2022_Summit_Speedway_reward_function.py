# Reward the car for following the most optimal racing line + throttle 


def reward_function(params):
    center_variance = params["distance_from_center"] / params["track_width"]

	# waypoints
    left_lane = [85, 86, 87, 88, 89, 90, 91, 92, 93]
    
    center_lane = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,47,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,79,80,81,82,83,84,94,95,96,97,98,99,113,114,115,116]
    
    right_lane = [41, 42, 46, 48, 52, 53, 105, 106, 107, 121]
    
    fast = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
    slow = [0, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 98, 99, 100,  101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
    
	reward = 21
    
    steps = params['steps']
    progress = params['progress']
    benchmark_time = 11.0
    on_track = not(params['is_offtrack'])
    
    if on_track:
        reward += 10
    else:
        reward -= 10
        
    # Give higher reward if the car completes the track
    if progress > 75:
        reward += 10
    else:
        reward -= 10  # completion % is not good

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10
    if params["closest_waypoints"][1] in fast:
        if params["speed"] >= 3 :
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] <= 1.5 :
            reward += 10
        else:
            reward -= 10
    
    ### straight line reward ###
    steering = abs(params['steering_angle']) # Only need the absolute steering angle for calculations
    speed = params['speed']

    # Positive reward if the car is in a straight line going fast
    if abs(steering) < 2 and speed >2.5:
        reward += 10
        
    
    ### throttle reward ###
    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 100

    # Give additional reward if the car pass every 25 steps faster than expected
    if (steps % 25) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100:
        reward += 10
    
    return float(reward)
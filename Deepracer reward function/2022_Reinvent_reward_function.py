# Reward the car for speed on the fast lane and for taking fewer steps

def reward_function(params):
    
	fast_wp = [1,2,3,4,5,6,7,8,9,27,28,36,37,38,39,81,82,83,84,85,86,100,101,102,103,104,105,106,107,108,109,110,111]
    reward = 1e-3
    
    # Read input parameters
	progress = params['progress']
	speed = params['speed']
	steps = params['steps']
    
    
    # reward for going fast on the fast lane and taking less steps 
    if not off_track:
        if wp in fast_wp:
            reward += ((params['progress'])/params['steps']*100)+(params['speed']**2)
		else:
			reward += ((params['progress'])/params['steps']*100)
    else:
        reward = 1e-3 
		
        
    return float(reward)
	
	
	
	
	
# The map
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

# Initialization
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 

# The moves
delta = [[-1, 0 ], 
         [ 0, -1], 
         [ 1, 0 ], 
         [ 0, 1 ]] 

# Pictographs for the moves
delta_name = ['^', '<', 'v', '>']



def compute_value(grid,goal,cost):

    # Initialize the value    
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    # Control variable
    change = True

    # Main bool loop
    while change:

        change = False

        # Double loop over map coordinates        
        for x in range(len(grid)):
            for y in range(len(grid[0])):

                # Check if we have met the goal and value is legitimate
                if goal[0] == x and goal[1] == y and value[x][y] > 0:

                        # Update value
                        value[x][y] = 0
                        change = True
                       
                # Check if we are on a valid map cell 
                elif grid[x][y] == 0:

                    # Go through the possible moves
                    for a in range(len(delta)):

                        # Update position
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]
                       
                        # Check if we are on the map 
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:

                            # Update value based on new value and (fixed) cost
                            v2 = value[x2][y2] + cost

                            # If the new value is less than the old value
                            if v2 < value[x][y]:

                                # Update the old value
                                change = True
                                value[x][y] = v2

                                
    return value 



v = compute_value(grid, goal, cost)
for i in range(len(v)):
    print(v[i])

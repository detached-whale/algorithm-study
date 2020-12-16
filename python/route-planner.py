'''
https://www.testdome.com/questions/python/route-planner/41100


As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable, before using more computationally intensive procedures for finding the optimal route.

The roads on the map are rasterized and produce a matrix of boolean values - True if the road is present or False if it is not. The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the route_exists method so that it returns True if the destination is reachable or False if it is not. The from_row and from_column parameters are the starting row and column in the map_matrix. The to_row and to_column are the destination row and column in the map_matrix. The map_matrix parameter is the above mentioned matrix produced from the map.

For example, for the given map, the code below should return True since the destination is reachable:

map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

route_exists(0, 0, 2, 2, map_matrix)
'''

def route_exists(from_row, from_column, to_row, to_column, map_matrix):    
    if map_matrix[from_row][from_column] == False | map_matrix[to_row][to_column] == False:
        return False

    if from_row == to_row and from_column == to_column:
        return True

    row = len(map_matrix) - 1
    col = len(map_matrix[0]) - 1

    if from_row+1 <= row and map_matrix[from_row+1][from_column]:
        map_matrix[from_row][from_column] = False
        if route_exists(from_row+1, from_column, to_row, to_column, map_matrix):
            return True
        map_matrix[from_row][from_column] = True

    if from_row-1 >= 0 and map_matrix[from_row-1][from_column]:
        map_matrix[from_row][from_column] = False
        if route_exists(from_row-1, from_column, to_row, to_column, map_matrix):
            return True
        map_matrix[from_row][from_column] = True

    if from_column+1 <= col and map_matrix[from_row][from_column+1]:
        map_matrix[from_row][from_column] = False
        if route_exists(from_row, from_column+1, to_row, to_column, map_matrix):
            return True
        map_matrix[from_row][from_column] = True

    if from_column-1 >= 0 and map_matrix[from_row][from_column-1]:
        map_matrix[from_row][from_column] = False
        if route_exists(from_row, from_column-1, to_row, to_column, map_matrix):
            return True
        map_matrix[from_row][from_column] = True

    return False

map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

print(route_exists(0, 0, 2, 2, map_matrix))

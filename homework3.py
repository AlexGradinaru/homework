
def prim_algorithm(array) :
    nodes = [0] * 8
    spanning_graph = matrix = [[0]*2 for i in range(7)]
    main_graph = [0] * 2
    weight_graph = [0] * 7
    inf = float("inf")
    nodes[0] = 0
    graph = [
                    #  1    2    3    4    5    6    7    8
                     [inf, 8  , inf, 7  , 5  , inf, inf, inf],  # 1
                     [8  , inf, 2  , inf, inf, 6  , inf, inf],  # 2
                     [inf, 2  , inf, inf, inf, 6  , inf,   2],  # 3
                     [7  , inf, inf, inf, 6  , inf, 8  , inf],  # 4
                     [5  , inf, inf, 6  , inf, inf, 6  ,   8],  # 5
                     [inf, 6  , 6  , inf, inf, inf, inf,   2],  # 6
                     [inf, inf, inf,   8, 6  , inf, inf,   9],  # 7
                     [inf, inf, 2  , inf, 10 , 2  , 9  , inf]   # 8
                   ];

    for i in range(0, len(graph) - 1) :
        min = inf
        min_index = inf

        for k in range(0, len(graph)) :
            for n in range(0, len(graph[i])) :
                if (min > graph[k][n]) and (n not in nodes) and (k in nodes) :
                    min = graph[k][n]
                    min_index = n
                    weight_graph[i] = min

                    spanning_graph [i][0] = k + 1
                    spanning_graph [i][1] = n + 1
        nodes[i+1] = min_index
    main_graph[0] = spanning_graph
    main_graph[1] = weight_graph
    return main_graph



def kruskal_algorithm(array, weights) :
    inf = float("inf")
    spanning_node = matrix = [[0]*8 for i in range(8)]
    last_array = [[0]*2 for i in range(7)]
    graph = [
                    #  1    2    3    4    5    6    7    8
                     [inf, 8  , inf, 7  , 5  , inf, inf, inf],  # 1
                     [8  , inf, 2  , inf, inf, 6  , inf, inf],  # 2
                     [inf, 2  , inf, inf, inf, 6  , inf,   2],  # 3
                     [7  , inf, inf, inf, 6  , inf, 8  , inf],  # 4
                     [5  , inf, inf, 6  , inf, inf, 6  ,   8],  # 5
                     [inf, 6  , 6  , inf, inf, inf, inf,   2],  # 6
                     [inf, inf, inf,   8, 6  , inf, inf,   9],  # 7
                     [inf, inf, 2  , inf, 10 , 2  , 9  , inf]   # 8
                   ];


    for i in range(0, len(graph[0])) :
        spanning_node[i][0] = i;

    for d in range(0, len(graph) - 1) :
        min = inf
        min_index1 = inf
        min_index2 = inf

        for i in range(0, len(graph)) :
            for k in range(0, len(graph[i])) :
                if min > graph[i][k] and k not in spanning_node[i] :
                    min = graph[i][k]
                    weights[d] = min
                    min_index1 = i
                    min_index2 = k

        spanning_node[min_index1].append(min_index2)
        spanning_node[min_index2].append(min_index1)
        last_array[d][0], last_array[d][1]= min_index1 + 1, min_index2 + 1
    return last_array



print("Prim algorithm")
array = [9, 5, 3, 10, 7, 1,	8, 2, 8, 1,	3, 10, 2]
print("Consistent node connection")
spanning_array = prim_algorithm(array)
print(spanning_array[0])
print("weights")
print(spanning_array[1])
weights = [0] * 7
print("Kruskal algorithm")
spanning_array = kruskal_algorithm(array, weights)
print(spanning_array)
print("weights")
print(weights) 

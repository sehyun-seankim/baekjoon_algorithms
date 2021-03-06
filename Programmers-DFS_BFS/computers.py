from collections import deque

def dfs_count(n, computers, start, visited):
    visited[start] = True
    count = 0
    for node in range(n):
        if visited[node] == False and computers[start][node] == 1:
             count = dfs_count(n, computers, node, visited)
    return count

def solution_count(n, computers):
    visited = [False] * n
    answer = 0
    for node in range(n):
        if visited[node] == False:
            answer += 1
            _ = dfs_count(n, computers, node, visited)
    return answer

def dfs_visualize(visitedList, node, computers):
    visitedList[node] = True
    nodeNum = len(computers)
    part = []
    for n in range(nodeNum):
        if computers[node][n] == 1 and visitedList[n] == False:
            part += dfs_visualize(visitedList, n, computers)

    return [node] + part

def solution_visualize(computers):
    nodeNum = len(computers)
    try:
        for n in range(nodeNum):
            if computers[n][n] != 1:
                raise ValueError
    except ValueError:
        print(f'{n, n}th element must be 1, but current value of computers[{n}][{n}] is: {computers[n][n]}')

    visited = [False] * nodeNum
    connected = []

    for n in range(nodeNum):
        if visited[n] == False:
            connected.append([])
            connected[-1] += dfs_visualize(visited, n, computers)
    return connected

def

test_comp1 = [[1,1,1,0],
             [1,1,1,0],
             [1,1,1,0],
             [0,0,0,1]]

test_comp2 = [[1,0],
              [0,1]]

test_comp3 = [[1,1,1,0,0,0,0,0,0],
              [1,1,0,0,0,0,0,0,0],
              [1,0,1,0,0,0,0,0,0],
              [0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,0],
              [0,0,0,0,0,0,1,1,0],
              [0,0,0,0,0,0,1,1,0],
              [0,0,0,0,0,0,0,0,1]]

test_comp4 = [[1,1,1],
              [1,1,0],
              [1,0,1]]

test_comp5 = [[1,1],
              [1,1]]

test_comp6 = [[1,1,0,0,0],
              [1,1,0,0,0],
              [0,0,1,1,0],
              [0,0,1,1,1],
              [0,0,0,1,1]]

testCases = [test_comp1, test_comp2, test_comp3, test_comp4, test_comp5, test_comp6]


for i in range(len(testCases)):
    print(f'{i+1}th test: {solution_visualize(testCases[i])}')
    print(f'{i + 1}th test: {solution_count(len(testCases[i]), testCases[i])}')




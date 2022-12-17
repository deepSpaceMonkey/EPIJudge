import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# White is open space. Black is walls
WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

'''
:param maze: the maze represented a 2d array (graph) 
:param s: source coordinate
:param e: end/destination coordinate
:return: if there is a valid path from source to end
:psuedocode: (1) add source node to queue of neighbors
             (2) while 1: the queue is not empty AND 2: end node not found
             (3) pop latest node from queue
             (4) if it is the end node, return
             (5) if not, add all of its neighbors to the queue
'''
def search_maze(maze: List[List[int]], start_node: Coordinate,
                dest_node: Coordinate) -> List[Coordinate]:
    # TODO - you fill in here.
    # We are given a source coordinate, we are given an end coordinate, and a maze as a list
    # apparently we need to return the path to destination

    explored_nodes = set()
    cellsToVisit = collections.deque()
    cellsToVisit.append(start_node)

    dest_found = False
    # Not adding (dest not found) as a condition in while because all nodes must be traversed to find shortest path
    while len(cellsToVisit) > 0:
        cur_node = cellsToVisit.popleft()
        if (path_element_is_feasible(maze, cur_node, cur_node)
                and (cur_node not in explored_nodes)
                and (not checkIfNodesAreSame(cur_node, dest_node))):
            explored_nodes.add(cur_node)
            

        if cur_node == dest_node:
            dest_found = True
        else:
            dest_found = False



    return []

def checkIfNodesAreSame(node1: Coordinate, node2: Coordinate) -> bool:
    return node1 == node2

def path_element_is_feasible(maze, prev, cur) -> bool:
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1) or \
           cur == cur


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))

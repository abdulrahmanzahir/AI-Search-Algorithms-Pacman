# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch():
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):

    # Creating a stack to implement the depth-first search algorithm
    stack = util.Stack()

    # Getting the initial state from the problem
    start_state = problem.getStartState()

    # Pushing the start state and an empty list of actions onto the stack
    stack.push((start_state, []))

    # Creating a set to keep track of reached states
    reached_states = set()

    while not stack.isEmpty():
        # Popping the current state and its corresponding actions from the stack
        current_state, actions = stack.pop()

        # Checking if the current state is a goal state
        if problem.isGoalState(current_state):
            return actions  # Returning the list of actions if the goal is reached

        # If the current state is not a goal, mark it as reached
        if current_state not in reached_states:
            reached_states.add(current_state)

            # Getting the successors of the current state from the problem
            successors = problem.getSuccessors(current_state)

            # Exploring the successors
            for successor_state, action, _ in successors:
                if successor_state not in reached_states:
                    # Appending the current action to the list of actions
                    new_actions = actions + [action]
                    # Pushing the successor state and the new list of actions onto the stack
                    stack.push((successor_state, new_actions))

    # If no goal state is found, return an empty list of actions
    return []


def breadthFirstSearch(problem: SearchProblem):

    # Creating a queue to implement the breadth-first search algorithm
    queue = util.Queue()

    # Getting the initial state from the problem
    start_state = problem.getStartState()

    # Pushing the start state and an empty list of actions into the queue
    queue.push((start_state, []))

    # Creating a set to keep track of reached states
    reached_states = set()

    while not queue.isEmpty():
        # Dequeuing the current state and its corresponding actions from the queue
        current_state, actions = queue.pop()

        # Checking if the current state is a goal state
        if problem.isGoalState(current_state):
            return actions  # Returning the list of actions if the goal is reached

        # If the current state is not a goal, mark it as reached
        if current_state not in reached_states:
            reached_states.add(current_state)

            # Getting the successors of the current state from the problem
            successors = problem.getSuccessors(current_state)

            # Exploring the successors
            for successor_state, action, _ in successors:
                if successor_state not in reached_states:
                    # Appending the current action to the list of actions
                    new_actions = actions + [action]
                    # Enqueuing the successor state and the new list of actions
                    queue.push((successor_state, new_actions))

    # If no goal state is found, return an empty list of actions
    return []


def uniformCostSearch(problem: SearchProblem):

    # Creating a priority queue to implement the uniform cost search algorithm
    priority_queue = util.PriorityQueue()

    # Getting the initial state from the problem
    start_state = problem.getStartState()

    # Pushing the start state, an empty list of actions, and an initial cost of 0 into the priority queue
    priority_queue.push((start_state, [], 0), 0)

    # Creating a set to keep track of reached states
    reached_states = set()

    while not priority_queue.isEmpty():
        # Dequeuing the current state, its corresponding actions, and the current cost from the priority queue
        current_state, actions, current_cost = priority_queue.pop()

        # Checking if the current state is a goal state
        if problem.isGoalState(current_state):
            return actions  # Returning the list of actions if the goal is reached

        # If the current state is not a goal, mark it as reached
        if current_state not in reached_states:
            reached_states.add(current_state)

            # Getting the successors of the current state from the problem
            successors = problem.getSuccessors(current_state)

            # Exploring the successors
            for successor_state, action, step_cost in successors:
                if successor_state not in reached_states:
                    # Appending the current action to the list of actions
                    new_actions = actions + [action]
                    # Calculating the new cost by adding the step cost to the current cost
                    new_cost = current_cost + step_cost
                    # Pushing the successor state, the new list of actions, and the new cost into the priority queue
                    priority_queue.push((successor_state, new_actions, new_cost), new_cost)

    # If no goal state is found, return an empty list of actions
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):

    # Creating a priority queue to implement the A* search algorithm
    priority_queue = util.PriorityQueue()

    # Getting the initial state from the problem
    start_state = problem.getStartState()

    # Pushing the start state, an empty list of actions, and an initial cost of 0 into the priority queue
    priority_queue.push((start_state, [], 0), 0)

    # Creating a set to keep track of reached states
    reached_states = set()

    while not priority_queue.isEmpty():
        # Dequeuing the current state, its corresponding actions, and the current cost from the priority queue
        current_state, actions, current_cost = priority_queue.pop()

        # Checking if the current state is a goal state
        if problem.isGoalState(current_state):
            return actions  # Returning the list of actions if the goal is reached

        # If the current state is not a goal, mark it as reached
        if current_state not in reached_states:
            reached_states.add(current_state)

            # Getting the successors of the current state from the problem
            successors = problem.getSuccessors(current_state)

            # Exploring the successors
            for successor_state, action, step_cost in successors:
                if successor_state not in reached_states:
                    # Appending the current action to the list of actions
                    new_actions = actions + [action]
                    # Calculating the new cost by adding the step cost to the current cost
                    new_cost = current_cost + step_cost
                    # Calculating the heuristic cost using the provided heuristic function
                    heuristic_cost = new_cost + heuristic(successor_state, problem)
                    # Pushing the successor state, the new list of actions, and the heuristic cost into the priority queue
                    priority_queue.push((successor_state, new_actions, new_cost), heuristic_cost)

    # If no goal state is found, return an empty list of actions
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

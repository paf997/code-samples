# CMPT 317, Assignment 1, Problem Class
# Paolo Fenu, 10281648
# Sept 27th, 2019
#
# Mac OS Mojave Version 10.14.6
# Python

import time as time
import Frontier as Frontiers
import InformedSearch as iSearch


class State(object):
    """The Problem State objects record data needed to solve the search problem.
    """
    def __init__(self, list1, list2, n, m):
        """
        Initialize the State object.
        Your definition can add constructor arguments as necessary.
        """
        # Both lists are used to represent state
        self.list1 = list1
        self.list2 = list2

        # column and row used to represent the linear list as a n x m matrix
        self.column = n
        self.row = m

        # The top, bottom, left and right sides of the matrix
        self.top = 0
        self.bottom = (m - 1)
        self.left = 0
        self.right = (n - 1)

        hval = 0
        self.hValue()

    def hValue(self):
        self.hval = 0
        for x in range(len(self.list1)):
            y = x
            if self.list1[x] != self.list2[x]:
                self.hval+=1

    def __repr__(self):
        return '{list 1:' + str(self.list1) + ', list 2:' + str(self.list2) + '}'

    def __eq__(self, other):
        """ Allows states to be compared by comparing their data """
        return False


class Action(object):
    """
        Used to create the actions that will be used to alter the State
        Direction = 1,2,3,4 correspond to the direction in which the matrix will shift
        South, North East or West
    """
    def __init__(self, column, row, direction):
        self.column = column
        self.row = row
        self.direction = direction


class Problem(object):
    # A list to store all of the actions
    """The Problem class defines aspects of the problem.
        One of the important definitions is the transition model for states.
        To interact with search classes, the transition model is defined by:
            is_goal(s): returns true if the state is the goal state.
            actions(s): returns a list of all legal actions in state s
            result(s,a): returns a new state, the result of doing action a in state s
        Other methods here are not part of the interface, but support debugging or the
        transition model.

        """
    # Used to dipslay state
    def initial(self,a_state):
        return self.a_state

    # Test whether list1 and list2 are the same
    def is_goal(self, a_state):
        """Returns true if the given state is a goal state"""
        if a_state.list1 == a_state.list2:
            return True
        else:
            return False

    def actions(self, a_state):
        actionList = []
        """ Returns a list of all the actions that are legal in the given state.
            You decide what an action looks like.  Put 'em in a list.
        """

        #add all the North and South actions to the list
        for x in range(a_state.column):
            action = Action(x, 0, 1)
            actionList.append(action)
            action = Action(x, a_state.bottom, 2)
            actionList.append(action)

        # add all the East and West actions to the list
        for x in range(a_state.row):
            action = Action(0, x, 3)
            actionList.append(action)
            action = Action(a_state.right, x, 4)
            actionList.append(action)
        return actionList

    # Check the direction and "push" the integer(column, row) in the respective direction
    def result(self, a_state, action):
        copyState = a_state

        if action.direction == 1:
            index = action.column
            index2 = (a_state.bottom * a_state.column) + action.column
            temp = a_state.list1[index2]
            for cnt in range (index2, index, -a_state.column):
                a_state.list1[cnt] = a_state.list1[cnt-a_state.column]
            a_state.list1[index] = temp

        # Push North action
        elif action.direction == 2:
            index = (a_state.bottom * a_state.column) + action.column
            index2 = action.column
            temp = a_state.list1[index2]
            for cnt in range(index2, index, a_state.column):
                a_state.list1[cnt] = a_state.list1[cnt+a_state.column]
            a_state.list1[index] = temp

        # Push East Action
        elif action.direction == 3:
            index = (action.row * a_state.column)
            index2 = (action.row * a_state.column) + a_state.right
            temp = a_state.list1[index2]
            for cnt in range(index2, index, -1):
                a_state.list1[cnt] = a_state.list1[cnt-1]
            a_state.list1[index] = temp

        else:
            index = (action.row * a_state.column) + a_state.right
            index2 = (action.row * a_state.column)
            temp = a_state.list1[index2]
            for cnt in range(index2, index, 1):
                a_state.list1[cnt] = a_state.list1[cnt+1]
            a_state.list1[index] = temp
        newList1 = []
        newList2 =  []
        for cnt in range(len(a_state.list1)):
            newList1.append(a_state.list1[cnt])
            newList2.append(a_state.list2[cnt])
        newState = State(newList1, newList2, a_state.column, a_state.row)

        return newState


###############################################################################################


# Department of Computer Science, University of Saskatchewan

# This file is provided solely for the use of CMPT 317 students.  Students are permitted
# to use this file for their own studies, and to make copies for their own personal use.

# This file should not be posted on any public server, or made available to any party not
# enrolled in CMPT 317.

# This implementation is provided on an as-is basis, suitable for educational purposes only.

# This module defines the classes:
#     SearchNode (inherits from Python object class)
#     SearchTerminationRecord (inherits from Python object class)
#     Search (inherits from Python object class)

# Assumes a problem class with the methods:
#   is_goal(problem_state): returns True if the state is the goal state
#   actions(problem_state): returns a list of all valid actions in state
#                           (the actions are only passed to result())
#   result(state, action): returns a new state that is the result of doing action in state.
#
# Search methods are based on TreeSearch (no repeated state checking):
# 1. DepthFirstSearch(s)
# 2. BreadthFirstSearch(s)
# 3. DepthLimitedSearch(s, dlimit)
# 4. IDS(s)
# These methods return a SearchTerminationRecord object, containing information about the search.  See the definition below.
#
# Usage:
#   import UninformedSearch as Search
#   pi = <create a problem instance from some Problem class>
#   searcher = Search.Search(pi, <timelimit>)
#   s = <create an initial state for the problem, possibly a method from the Problem class>
#   result = searcher.DepthFirstSearch(s)
#            # or any of the methods above
#   print(str(result))
#   or public access to any of the data stored in the result.

# ALL SEARCH IS SUBJECT TO A TIME LIMIT.


#########################################################################################
class SearchNode(object):
    """A data structure to store search information"""

    def __init__(self, state, parent_node, step_cost=1):
        """A SearchNode stores
             a single Problem state,
             a parent node
             the node's depth
             the node's path cost
        """
        self.state = state
        self.parent = parent_node
        if parent_node is None:
            self.path_cost = 0
            self.depth = 0
        else:
            self.path_cost = parent_node.path_cost + step_cost
            self.depth = parent_node.depth + 1

    def __str__(self):
        """ Create and return a string representation of the object"""
        return '<{}> {} ({})'.format(str(self.depth), str(self.state), str(self.path_cost))

    def display_steps(self):
        """Because a SearchNode stores a parent Node, we can trace the actions from
           initial state to the current state by stepping backwards up the tree.
           This does assume that your state stores the action that caused it to be
           created, as an attribute.
        """
        def disp(node):
            """ recursive function that displays actions
            """
            if node.parent is not None:
                disp(node.parent)
                print(str(node.state.action))

        print("Solution:")
        disp(self)


#########################################################################################
class SearchTerminationRecord(object):
    """A record to return information about how the search turned out.
       All the details are provided in a record, to avoid needing to print out the details
       at different parts of the code.
    """

    def __init__(self, success=False, result=None, time=0, nodes=0, space=0, cutoff=False):
        # type: (object, object, object, object, object, object) -> object
        self.success = success  # Boolean: True if a solution was found
        self.result = result    # SearchNode: a node containing a goal state, or None if no solution found
        self.time = time        # float: time was spent searching.  Not scientifically accurate, but good enough for fun
        self.nodes = nodes      # integer: number of nodes expanded during the search
        self.space = space      # integer: maximum size of the frontier during search
        self.cutoff = cutoff    # Boolean: For IDS, True if depth limited search reach the depth limit before failing

    def __str__(self):
        """Create a string representation of the Result data
           This string doesn't show everything it could.
        """
        text = 'Search {} ({} sec, {} nodes, {} queue)'
        if self.success:
            textsuccess = 'successful'
        else:
            textsuccess = 'failed'
        return text.format(textsuccess, str(self.time), str(self.nodes), str(self.space))


#########################################################################################
class Search(object):
    """A class to contain uninformed search algorithms.
       API users should call the public methods.
       Subclasses inheriting this class can call _treeSearch() or _dltree_search()
    """

    def __init__(self, problem, timelimit=10):
        """The Search object needs to be given:
            the search Problem
            an optional timelime (default set above)
        """
        self._problem = problem
        self._frontier = None
        self._time_limit = timelimit


    def _tree_search(self, initial_state):
        """Search through the State space starting from an initial State.
           Simple tree search algorithm, used by API methods below.
           Monitors:
                time so as not to exceed a time limit.
                number of nodes expanded
                size of the frontier at any point
        """

        start_time = time.time()
        now = start_time
        self._frontier.add(SearchNode(initial_state, None))
        node_counter = 0
        max_space = 0

        # keep searching if there are nodes in the Frontier, and time left before the limit
        while not self._frontier.is_empty() and now - start_time < self._time_limit:
            max_space = max(max_space, len(self._frontier))
            this_node = self._frontier.remove()
            #print "pop: ", this_node.state
            node_counter += 1
            now = time.time()
            if self._problem.is_goal(this_node.state):
                return SearchTerminationRecord(success=True, result=this_node,
                                    nodes=node_counter, space=max_space, time=now - start_time)
            else:
                for act in self._problem.actions(this_node.state):
                    child = self._problem.result(this_node.state, act)
                    #print "add: ", child
                    self._frontier.add(SearchNode(child, this_node))

        # didn't find a solution!
        now = time.time()
        return SearchTerminationRecord(success=False, result=None,
                            nodes=node_counter, space=max_space, time=now - start_time)


    def DepthFirstSearch(self, initial_state):
        """
        Perform depth-first search of the problem,
        starting at a given initial state.
        :param initial_state: a Problem State
        :return: SearchTerminationRecord
        """
        # configure search: for DFS, we want the Frotnier with the LIFO Stack
        self._frontier = Frontiers.FrontierLIFO()

        # run search
        return self._tree_search(initial_state)

    def BreadthFirstSearch(self, initial_state):
        """
        Perform breadth-first search of the problem,
        starting at a given initial state.
        :param initial_state: a Problem State
        :return: SearchTerminationRecord
        """
        # configure search: for BFS, we want the Frontier with the FIFO Queue
        self._frontier = Frontiers.FrontierFIFO()

        # run search
        return self._tree_search(initial_state)

    def DepthLimitedSearch(self, initial_state, limit):
        """
        Perform depth-limited search of the problem,
        starting at a given initial state.
        :param initial_state: a Problem State
        :param limit: the maximum allowable depth
        :return: SearchTerminationRecord
        """
        # configure search: We want the FIFO Frontier with the depth limit
        self._frontier = Frontiers.FrontierLIFO_DL(limit)

        # run search
        result = self._tree_search(initial_state)

        # another attribute to indicate whether we ran out of time (cutoff = True)
        # or if the search space was less deep than the limit, and we searched it all
        # (cutoff = False)
        # This is needed by Iterative Deepening, so that we know to stop searching deeper.
        result.cutoff = self._frontier._cutoff
        return result

    def IDS(self, initial_state):
        """Iterative deepening Search successively increases the search depth
           the search depth until a solution is found."""
        limit = 0
        nodes = 0
        time = 0
        space = 0
        while time < self._time_limit:
            answer = self.DepthLimitedSearch(initial_state, limit)
            if answer.success:
                answer.time += time
                answer.nodes += nodes
                answer.space = max(answer.space, space)
                return answer
            elif not self._frontier._cutoff:
                return SearchTerminationRecord(success=False, result=None, nodes=nodes, space=space, time=time)
            else:
                nodes += answer.nodes
                time += answer.time    # this could result in search that is substantial longer than the limit
                limit += 1
                space = max(answer.space, space)

        return SearchTerminationRecord(success=False, result=None, nodes=nodes, space=space, time=time)

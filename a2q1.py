#a2q1.txt
#Paolo Fenu, 10281648, paf997
#U of S, Cmpt 317
#Oct 15th, 2019

# macOs 10.14.6
# python 2.7

import machine as calc
import math
import random
import copy

class State(object):
    """  A State object stores a potential solution to a search problem.
         Its two methods are needed by localsearch.py
    """
    # a list of the values form each line once calculated and operators applied

    def __init__(self, operands, operators, L, N, goal):
        self.operands = operands
        self.L = L
        self.N = N
        self.goal = goal
        self.operators = operators
        self.listOfValues = []
        self.value = 0

        # create a list of tuples to pass a parameter to the machine class
        for line in operands:
            pairing = []
            for index in range(len(line)):
                tuple = []
                # add operator to tuple
                tuple.append(operators[index])
                # add operand to tuple
                tuple.append(line[index])
                pairing.append(tuple)

            # pass tuples to machine
            self.value = round(calc.machine_exec(pairing), 4)

            # store returned value in a list to later pass to objective functions
            self.listOfValues.append(self.value)

    def is_better_than(self, other):
        """
            Return True if self is a better solution than other
            :param: other: a State object
            :return: boolean
        """

        # create 2 problems and and use the objective function as a comparison for states
        p = Problem(self)
        p2 = Problem(other)
        if p.objective_function() < p2.objective_function():
            return True
        else:
            return False

    def is_equal_to(self, other):
        """
            Return True if self is as good a solution as other
            :param: other: a State object
            :return: boolean
        """

        # create problems and and use the objective function as a comparison
        p = Problem(self)
        p2 = Problem(other)
        if p.objective_function() == p2.objective_function():
            return True
        else:
            return False


class Problem(object):
    """  A Problem object implements the methods needed by the
         algorithms in localsearch.py
    """
    def __init__(self, state):
        self.state = state

    # used for displaying the operators if needed
    def print_state(self):
        return "The o's: ", self.state.operands, "the value: ", self.state.value

    # used to convert the operators to strings if needed
    def translate(operator):
        if operator == 1:
            return 'ADD'
        elif operator == 2:
            return 'SUB'
        elif operator == 3:
            return 'MUL'
        elif operator == 4:
            return 'DIV'
        elif operator == 5:
            return 'NOP'
        else:
            print('unknown operator', operator)

    def new_state(self, state, ops):

        """
            :param state - the current state and it's values

            :param ops - the new set of operators to be used in the new state
            Used to replicate the current state, but with different operators
            Returns the new state.
        """

        # copy values of state into new state
        newOps, newG = [], []
        for y in range(len(self.state.operands)):
            newOps.append(self.state.operands[y])
        newOts = ops
        newL = self.state.L
        newN = self.state.N
        for y in range(len(state.goal)):
            newG.append(self.state.goal[y])
        return State(newOps, newOts, newL, newN, newG)

    def objective_function(self):
        """
            Returns the objective value of the given state.
        """

        # objective function
        eVAlue = 0.0
        for x in range(self.state.N):
            eVAlue +=  round((self.state.goal[x] - self.state.listOfValues[x]) ** 2, 4)
        rmse = math.sqrt(eVAlue/self.state.N)
        rmse = round(rmse,4)
        return rmse

    def random_state(self):
        """ Return a random State, completely independent of any other State.
        """
        # create a list of random operators for the new state
        randoms = []
        for x in range (self.state.L):
            randoms.append (random.randint (1, 5))

        newState = self.new_state(self.state, randoms)

        return newState

    def random_step(self, state):
        """ Return a State that is a random neighbour of the given State.
            :param: state: A State object
        """
        # to determine neighbours, the functions iterates through the list of operands and
        # determines if there is a numerically lower or higher operand then creates a new state
        # and compares the object value of that state the the current state

        #copy state operators for new state
        newOts = copy.deepcopy(state.operators)

        # choose random operator and randomly change the operation. Do this twice to reduce
        # the possibility of values being the smaw
        randomStep = random.randint(1,5)
        randomOp = random.randint(0, (self.state.L-1))
        newOts[randomOp] = randomStep

        randomStep = random.randint(1,5)
        randomOp = random.randint(0, (self.state.L-1))
        newOts[randomOp] = randomStep

        newState = self.new_state(state,newOts)
        return newState

    def best_step(self, state):
        """ Return the best neighbouring State for the given State
            :param: state: A State object
        """
        # To determine neighbours, the functions iterates through the list of operands and
        # determines if there is a numerically lower or higher operand then creates a new state
        # After the state is created, is_better is called for comparison

        best = state
        for x in range(state.L):
            if state.operators[x] > 1:
                newOts = copy.deepcopy(state.operators)
                newOts[x] -= 1
                newState = self.new_state(state,newOts)

                if state.is_better_than(newState) is False:
                    best = newState

            if state.operators[x] < 5:
                newOts = copy.deepcopy(state.operators)
                newOts[x] += 1
                newState = self.new_state(state,newOts)
                if state.is_better_than (newState) is False:
                    best = newState
        return best

    def random_better(self, state):
        """ Return a State that is a random BETTER neighbour of the given State.
            :param: state: A State object
        """

        # To determine neighbours, the functions iterates through the list of operands and
        # determines if there is a numerically lower or higher operand then creates a new state
        # After the state is created, is_better is called for comparison and if true, it is add
        # to a list of States. A random state is returned if there is one in the list.

        states = []
        for x in range(state.L):
            if state.operators[x] > 1:
                newOts = copy.deepcopy(state.operators)
                newOts[x] -= 1
                newState = self.new_state(state,newOts)
                if newState.is_better_than(state):
                    states.append(newState)
            if state.operators[x] < 5:
                newOts = copy.deepcopy(state.operators)
                newOts[x] += 1
                newState = self.new_state(state,newOts)
                if newState.is_better_than(state):
                    states.append(newState)
        if len(states) > 0:
            return states[random.randint(0, len(states) - 1)]
        else:
            return None


###################################################################################################################


# Paolo Fenu, 10281648, paf997
# CMPT 317, A4Q4
# November 20th, 2019

# Python 3.7, Mac OS Mojave,  10.14.6


# CMPT 317 A Skeleton Python Class for any 2 player perfect information game

# Copyright (c) 2016-2019 Michael C Horsch,
# Department of Computer Science, University of Saskatchewan

# This file is provided solely for the use of CMPT 317 students.  Students are permitted
# to use this file for their own studies, and to make copies for their own personal use.

# This file should not be posted on any public server, or made available to any party not
# enrolled in CMPT 317.

# This implementation is provided on an as-is basis, suitable for educational purposes only.

# The Game Class encodes the rules of a game.
# Game Class Interface:
#    initial_state(self)
#       - returns an initial game state
#       - the state can be any object that stores the details
#         needed to keep track of the game, including any information
#         convenient to store
#
#    is_mins_turn(self, state)
#    is_maxs_turn(self, state)
#       - return a boolean that indicates if it's Min/Max's turn
#
#    is_terminal(self, state)
#       - return a boolean that indicates if the state represents
#         a true end of the game situation, i.e, a win or a draw
#
#    utility(self, state)
#       - return the utility value of the given terminal state
#       - must return one of three values: k_min, k_draw, k_max
#           k_min: the value returned if Min is the winner
#           k_max: the value returned if Max is the winner
#           k_draw: the value returned if the game ends in a draw
#           - any range is allowed.
#           - probably best if k_min < k_draw < k_max
#             and k_draw half way between k_min, k_max
#       - will only be called if the state is determined to be
#         a terminal state by is_terminal()
#       - only terminal states have utility; other states get
#         their value from searching.
#
#    actions(self, state)
#       - returns a list of actions legal in the given state
#
#    result(self, state, action)
#       - returns the state resulting from the action in the given state
#
#    cutoff_test(self, state, depth)
#       - returns a bolean that indicates if this state and depth is suitable
#         to limit depth of search.  A simple implementation might just look
#         at the depth; a more sophisticated implementation might look at
#         the state as well as the depth.
#
#    eval(self, state)
#       - returns a numeric value that estimates the minimax value of the
#         given state.  This gets called if cutoff_test() returns true.
#         Instead of searching to the bottom of the tree, this function
#         tries to guess who might win.  The function should return a value
#         that is in the range defined by utility().  Because this is an
#         estimate, values close to k_min (see utility()) indicate that
#         a win for Min is likely, and values close to k_max should indicate
#         a win for Max is likely.  Should not return values outside the range
#         (k_min, k_max).  k_min means "Min wins"; a value smaller than k_min
#         makes no sense.  An estimate from eval() cannot be more extreme than a
#         fact known from utility().
#
#    transposition_string(self)
#       - return a string representation of the state
#       - for use in a transposition table
#       - this string should represent the state exactly, but also without
#         too much waste.  In a normal game, lots of these get stored!
#
#    congratulate(self)
#       - could be called at the end of the game to indicate who wins
#       - this is not absolutely necessary, but could be informative

class GameState(object):
    """ The GameState class stores the information about the state of the game.
    """
    _ablank = ' '
    sith = 'S'
    rebel = 'r'
    Jedi = 'J'
    jCount = 0
    rCount = 5
    sCount = 1
    turn_count = 0;

    def __init__(self):
        # the gameState dictionary stores the position of each piece

        # Set yp the initial state
        self.gameState = dict()
        for r in range(1, 6):
            for c in range(1, 6):
                self.gameState[r, c] = self._ablank

        # Then intital state with 5 rebel along the bottom...
        for c in range(1, 6):
            self.gameState[5, c] = self.rebel

        # and one Sith at the middle top
        self.gameState[1, 3] = self.sith

        # the blanks show what's left to choose from
        self.blanks = {v for v in self.gameState}

        # a boolean to store if it's Max's turn; True by default
        self.maxs_turn = True

        # if this state is a winning state, store that information
        # because it is cheaper to check once, than a bunch of times
        self.cachedWin = False

        # if cachedWin is True, then cachedWinner is a boolean
        # True means Max won; False means Min won
        self.cachedWinner = None

        # now cache the string that represents this state
        self.stringified = str(self)

    def myclone(self):
        new_state = GameState()
        for rc in self.gameState:
            new_state.gameState[rc] = self.gameState[rc]
        new_state.blanks = {v for v in self.blanks}  # copy the data not the reference
        new_state.maxs_turn = self.maxs_turn
        new_state.cachedWin = self.cachedWin
        new_state.cachedWinner = self.cachedWinner
        new_state.stringified = self.stringified  # copy the reference not the string
        new_state.sCount = self.sCount
        new_state.jCount = self.jCount
        new_state.rCount = self.rCount
        new_state.turn_count = self.turn_count + 1

        return new_state

    def display(self):
        for r in range(1, 6):
            print("+-+-+-+-+-+")
            print("|", end="")
            for c in range(1, 5):
                print(self.gameState[r, c], end="")
                print("|", end="")
            print(self.gameState[r, 5], end="")
            print("|")
        print("+-+-+-+-+-+")

    def __str__(self):
        """ Translate the board description into a string.
            Could be used as a key for a hash table.
            :return: A string that describes the board in the current state.
        """
        s = ""
        for r in range(1, 6):
            for c in range(1, 6):
                s += self.gameState[r, c]
        return s


class Game(object):
    """ The Game object defines the interface that is used by Game Tree Search
        implementation.
    """

    def __init__(self, depthlimit=0):
        """ Initialization.
        """
        self.depth_limit = depthlimit

    def initial_state(self):
        """ Return an initial state for the game.
        """
        # the default TTTBoard constructor creates an empty board
        state = GameState()
        return state

    def is_maxs_turn(self, state):
        """ Indicate if it's Min's turn
            :return: True if it's Max's turn to play
        """
        return state.maxs_turn

    def is_mins_turn(self, state):
        """ Indicate if it's Min's turn
            :param state: a legal game state
            :return: True if it's Min's turn to play
        """
        return not state.maxs_turn

    def is_terminal(self, state):
        """ Indicate if the game is over.
            :param state: a legal game state
            :return: a boolean indicating if node is terminal
        """
        return state.cachedWin or len(state.blanks) == 0

    def actions(self, state):
        """ Returns all the legal actions in the given state.
            :param state: a state object
            :return: a list of actions legal in the given state
        """
        actions = []  # a list to hold all of the actions

        # Rebel's turn, check for all the middle pawn
        if (state.maxs_turn):
            for r in range(2, 6):
                for c in range(2, 5):
                    if state.gameState[r, c] == 'r':
                        for x in range(c - 1, c + 2):
                            if state.gameState[r - 1, x] == state._ablank and (c == x) or (
                                    state.gameState[r - 1, x] == state.sith and x != c):
                                # add rebel action if it's valid
                                actions.append((state.maxs_turn, (r, c), 'r', (r - 1, x)))
                    elif state.gameState[r, c] == 'J':
                        pass

            # Rebel's turn, check rebels on the left flank
            for r in range(2, 6):
                if state.gameState[r, 1] == 'r':
                    for x in range(1, 3):
                        if (state.gameState[r - 1, x] == state._ablank and (x == 1)) or (
                                state.gameState[r - 1, x] == state.sith and x != 1):
                            # Add the valid action
                            actions.append((state.maxs_turn, (r, x), 'r', (r - 1, x)))

            # Rebel's turn, check rebels on the right flank
            for r in range(2, 6):
                if state.gameState[r, 5] == 'r':
                    for x in range(4, 6):
                        if (state.gameState[r - 1, x] == state._ablank and (x == 5)) or (
                                state.gameState[r - 1, x] == state.sith and x != 5):
                            # Add the valid actions
                            actions.append((state.maxs_turn, (r, x), 'r', (r - 1, x)))
            # Jedi moves
            for r in range(1, 6):
                for c in range(1, 6):
                    if state.gameState[r, c] == 'J':

                        minX = min(r, c)  # Use the smallest value from row or column for the upcomoing loops
                        # check if Jedi can go right to left
                        for x in range(c - 1, 0, -1):
                            if state.gameState[r, x] == state._ablank or state.gameState[r, x] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (r, x)))
                            else:
                                break

                        # check if Jedi can go  left to right
                        for x in range(c + 1, 6, 1):
                            if state.gameState[r, x] == state._ablank or state.gameState[r, x] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (r, x)))
                            else:
                                break

                        # check if Jedi can go right to left diagonally up
                        x = minX - 1
                        while (r - (minX - x) > 0 and c - (minX - x) > 0):
                            if state.gameState[r - (minX - x), c - (minX - x)] == state._ablank or state.gameState[
                                r - (minX - x), c - (minX - x)] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (r - (minX - x), c - (minX - x))))
                            else:
                                break
                            x -= 1

                        # check if Jedi can go  left to right diagonally down
                        x = minX - 1
                        while (r + (minX - x) <= 5 and c + (minX - x) <= 5):
                            if state.gameState[r + (minX - x), c + (minX - x)] == state._ablank or state.gameState[
                                r + (minX - x), c + (minX - x)] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (r + (minX - x), c + (minX - x))))
                            else:
                                break
                            x -= 1

                        # check if Jedi can go  right to left diagonally down
                        x = minX - 1
                        while (r + (minX - x) <= 5 and c - (minX - x) > 0):
                            if state.gameState[r + (minX - x), c - (minX - x)] == state._ablank or state.gameState[
                                r + (minX - x), c - (minX - x)] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (r + (minX - x), c - (minX - x))))
                            else:
                                break
                            x -= 1

                        # check if Jedi can go left to right diagonally up
                        x = minX - 1
                        while (r - (minX - x) > 0 and c + (minX - x) <= 5):
                            if state.gameState[r - (minX - x), c + (minX - x)] == state._ablank or state.gameState[
                                r - (minX - x), c + (minX - x)] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (r - (minX - x), c + (minX - x))))
                            else:
                                break
                            x -= 1

                        # check if Jedi can go top to bottom
                        for x in range(r + 1, 6):
                            if state.gameState[x, c] == state._ablank or state.gameState[x, c] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (x, c)))
                            else:
                                break

                        # check if Jedi can go bottom to top
                        for x in range(r - 1, 0, -1):
                            if state.gameState[x, c] == state._ablank or state.gameState[x, c] == state.sith:
                                actions.append((state.maxs_turn, (r, c), 'J', (x, c)))
                            else:
                                break

        # else not max's turn, it's min's turn
        else:
            for r in range(1, 6):
                for c in range(1, 6):
                    if (state.gameState[r, c] == state.sith):
                        for x in range(r - 1, r + 2):
                            for y in range(c - 1, c + 2, ):
                                if x > 0 and x < 6 and y > 0 and y < 6:
                                    if state.gameState[x, y] == state.sith:
                                        pass  # spot blocked by ally
                                    else:
                                        actions.append((state.maxs_turn, (r, c), 'S', (x, y)))
        return actions

    def result(self, state, action):
        """ Return the state that results from the application of the
            given action in the given state.
            :param state: a legal game state
            :param action: a legal action in the game state
            :return: a new game state
        """

        # make a clone of this state
        new_state = state.myclone()

        # The current player, their current position, the type of unit and the new position
        who, curPos, type, newPos = action

        # remove the moving piece from the current position then...
        new_state.gameState[action[1]] = new_state._ablank

        # remove the respective piece and reduce the piece count
        if new_state.gameState[action[3]] == new_state.rebel:
            new_state.rCount -= 1
        elif new_state.gameState[action[3]] == new_state.Jedi:
            new_state.jCount -= 1
        elif new_state.gameState[action[3]] == new_state.sith:
            new_state.sCount -= 1
        else:
            # a blank space
            pass

        if type == 'r':
            # check for Jedi promtion
            if (newPos[0] == 1):
                new_state.gameState[action[3]] = new_state.Jedi
                new_state.jCount += 1
                new_state.rCount -= 1
            else:
                new_state.gameState[action[3]] = new_state.rebel
        elif type == 'J':
            new_state.gameState[action[3]] = new_state.Jedi
        else:
            # check if Jedi is converted and increase Sith count
            if new_state.gameState[newPos] == new_state.Jedi:
                new_state.gameState[newPos] = new_state.sith
                new_state.gameState[curPos] = new_state.sith
                new_state.sCount += 1
            else:
                pass
            new_state.gameState[action[3]] = new_state.sith

        new_state.maxs_turn = not state.maxs_turn

        self._cache_winner(who, new_state)
        new_state.stringified = str(new_state)
        return new_state

    def utility(self, state):
        """ Calculate the utility of the given state.
            :param state: a legal game state
            :return: utility of the terminal state

        """
        if state.cachedWin and state.turn_count > 40:
            return 0
        elif state.cachedWin and state.cachedWinner:
            return 1
        elif state.cachedWin and not state.cachedWinner:
            return -1
        else:
            return 0

    def cutoff_test(self, state, depth):
        """
            Check if the search should be cut-off early.
            :param state: a game state
            :param depth: the depth of the state,
                          in terms of levels below the start of search.
            :return: True if search should be cut off here.
        """
        # here we're implementing a simple cut-off.
        # In a more interesting game, you might look at the state
        # and allow a deeper search in important branches, and a shallower
        # search in boring branches.

        return self.depth_limit > 0 and depth > self.depth_limit

    def eval(self, state):
        """
            When a depth limit is applied, we need to evaluate the
            given state to estimate who might win.
            state: a legal game state
            :return: a numeric value in the range of the utility function
        """
        # This portion probably isn't needed since the minmax function should check for this, but it is an extra layer or cheking
        if state.jCount == 0 and state.rCount == 0:
            e = -1
        elif state.sCount == 0:
            e = 1
        else:

            # Start by giving values to each piece.  The magic numbers are Arbitrary values that seem to work well within the game
            light = (state.rCount * 13) + (state.jCount * 15)
            dark = -state.sCount * 16
            topBoard = 5  # make the   top of the board more valuable for rebels
            for r in range(1, 6):
                topBoard -= 1
                for c in range(1, 6):

                    # The 3rd row is considered more valuable for the Sith player, followed by the 2nd, then 1st.
                    if state.gameState[r, c] == state.sith:
                        if r == 1:
                            dark -= 6
                        elif r == 2:
                            dark -= 7
                        elif r == 3:
                            dark -= 8
                        else:
                            pass
                        cnt = 1  # used to see if the adjacent space is diagonal or othogonal
                        for x in range(r - 1, r + 2):
                            for y in range(c - 1, c + 2, ):
                                cnt += 1

                                # check if the sith have moved close to a Jedi
                                if x > 0 and x < 6 and y > 0 and y < 6:
                                    if state.gameState[x, y] == state.Jedi:
                                        light += 8

                                    # check if Sith are in danger next to a rebel
                                    if state.gameState[x, y] == state.rebel and (
                                            cnt == 1 or cnt == 3):
                                        light += 7

                                    # check if the Sith are in range of destroying a Jedi
                                    if state.gameState[x, y] == state.rebel and (
                                            cnt == 2 or cnt == 4 or cnt == 6 or cnt == 8):
                                        dark -= 9
                    # Make the top of the board more valuable for the rebels
                    elif state.gameState[r, c] == state.rebel:
                        light += (topBoard)
                    # Check if the Jedi is in the same row or column as a Sith
                    elif state.gameState[r, c] == state.Jedi:
                        light += topBoard
            e = (light + dark) / 100  # keep the e values within -1 nd 1
        return e

    def congratulate(self, state):
        """ Called at the end of a game, display some appropriate
            sentiments to the console.
            :param state: a legal game state
        """
        winstring = 'Congratulations, {} wins (utility: {})'

        # really, there is no winner, but the turn count is above 40 so we need to stop the game
        if state.turn_count > 40:
            print('No winner')
        elif state.cachedWin and state.cachedWinner:
            print(winstring.format("Light Side", self.utility(state)))
        elif state.cachedWin and not state.cachedWinner:
            print(winstring.format("Dark Side", self.utility(state)))
        else:
            print('No winner')
        return

    def transposition_string(self, state):
        """ Returns a unique string for the given state.  For use in
            any Game Tree Search that employs a transposition table.
            :param state: a legal game state
            :return: a unique string representing the state
        """
        return state.stringified

    def _cache_winner(self, who, state):
        if state.turn_count > 40:
            state.cachedWin = True
        elif state.sCount == 0:
            # print("inside utility checking for light win")
            state.cachedWin = True
            state.cachedWinner = True
        elif state.rCount == 0 and state.jCount == 0:
            state.cachedWin = True
            state.cachedWinner = False
        else:
            state.cachedWinner = None
        return

# Austin Sharp
# CS533 Winter '14 Homework 1
# Finite Horizon MDP Solver
from mdp import MDP

def bellman_backup():
    """
    Expected value of a state = immediate reward plus max over all actions of the
    weighted-average reward of the possible next states.
    """


def plan(mdp, horizon):
    """
    Main algorithm. The input to your algorithm should be a description of an MDP and
    a time horizon H (positive integer). The output should be an optimal non-stationary value
    function and non-stationary policy for the MDP and time horizon .
    """


"""
Main program flow. Test plan() on two MDPs, each with two different time horizons.
"""

test = MDP("simple.txt")
test.show()
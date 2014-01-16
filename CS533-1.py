# Austin Sharp
# CS533 Winter '14 Homework 1
# Finite Horizon MDP Solver
import operator
from mdp import MDP

def bellman_backup(mdp, value_k):
    """
    Given an MDP and its value function with time-to-go k, returns its value function with time-to-go k+1.
    """
    # computing a new value function, ie list over all states
    new_value_fn = []
    actions = []
    for s in range(mdp.num_states):
        # R(s) + max_a[sum_s'(T(s,a,s') dot Vk(s'))]
        action_results = []
        for a in range(mdp.num_actions):
            action_results.append(sum([mdp.transition(s, a, s_next) * value_k[s_next] for s_next in range(mdp.num_states)]))

        max_index, max_value = max(enumerate(action_results), key=operator.itemgetter(1))
        actions.append(max_index)
        new_value_fn.append(mdp.rewards[s] + max_value)

    return new_value_fn, actions


def plan(mdp, horizon):
    """
    Main algorithm. The input to your algorithm should be a description of an MDP and
    a time horizon H (positive integer). The output should be an optimal non-stationary value
    function and non-stationary policy for the MDP and time horizon .
    """
    # list of value functions indexed by time-to-go k
    value_functions = []
    policy = []
    # initialize at time-to-go 0 with reward of each state
    value_functions.append(mdp.rewards)
    for i in range(horizon):
        vals, actions = bellman_backup(mdp, value_functions[i])
        value_functions.append(vals)
        policy.append(actions)
    # at this point value functions should be filled up to horizon
    return value_functions, policy


def show_plan(values, policy):
    """
    Pretty printing for a plan returned by plan(mdp, horizon)
    """
    print "Value function from time-to-go 0 up to " + str(len(values) - 1)
    for i in range(len(values)):
        print values[i]
    print "Policy from time-to-go 1 up to " + str(len(values) - 1)
    for i in range(len(policy)):
        print policy[i]


# Main program flow. Test plan() on two MDPs, each with two different time horizons.

mdp1 = MDP("mdp1.txt")
values1, policy1 = plan(mdp1, 4)
print "MDP 1 results for horizon = 4"
show_plan(values1, policy1)

values1, policy1 = plan(mdp1, 10)
print "MDP 1 results for horizon = 10"
show_plan(values1, policy1)

mdp2 = MDP("mdp2.txt")
values2, policy2 = plan(mdp2, 4)
print "MDP 2 results for horizon = 4"
show_plan(values2, policy2)

values2, policy2 = plan(mdp2, 10)
print "MDP 2 results for horizon = 10"
show_plan(values2, policy2)
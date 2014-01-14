__author__ = 'Austin'


class MDP(object):
    def show(self):
        print self.name
        print "Actions: " + str(self.num_actions)
        print "States: " + str(self.num_states)
        print "Rewards: " + str(self.rewards)

    def __init__(self, filename):
        self.name = filename

        with open(filename, "r") as in_file:
            self.num_states = int(in_file.readline().strip())
            self.num_actions = int(in_file.readline().strip())

            # reward: next line of file, split on space, convert to ints
            self.rewards = [int(x) for x in in_file.readline().strip().split()]

            #for i in range(self.num_actions):
                # read in transition probability matrix
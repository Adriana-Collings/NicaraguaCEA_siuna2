class Node:
    def __init__(self, name, cost, utility):
        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_expected_utility(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):
    def __init__(self, name, cost, future_nodes, probs, utility):
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        exp_cost = self.cost
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_utility(self):
        exp_utility = self.utility
        i = 0
        for node in self.futureNodes:
            exp_utility += self.probs[i]*node.get_expected_utility()
            i += 1
        return exp_utility


class TerminalNode(Node):
    def __init__(self,name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        return self.cost

    def get_expected_utility(self):
        return self.utility


class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes, utility):
        Node.__init__(self, name, cost, utility)
        self.futureNode = future_nodes

    def get_expected_cost(self):
        outcomes = dict()
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_cost()
        return outcomes

    def get_expected_utility(self):
        utility_outcomes = dict()
        for node in self.futureNode:
            utility_outcomes[node.name] = node.get_expected_utility()
        return utility_outcomes


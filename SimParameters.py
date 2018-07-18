import numpy as np
from scipy.stats import expon
import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as StatCls
import numpy
from numpy.random import choice


# you should really make sure that your CEA plane will work

class Patient:
    def __init__(self, id):
        self._id = id
        # self._rnd = np.random

        # if you set the seed then you end up with the same randomization of conditions each time and thus the same
        # results each time, this is due to the way that you have built in the dirichlet distribution so that you can
        # get sum stats for each condition

        # self._rnd.seed(self._id)
        self._cost_utility = []         # list for cost and utilities - can probably be removed- depends on CEA plane
        self._OS_cost = 0               # OpSmile Costs
        self._NoOS_cost = 0             # No OpSmile Costs
        self._OS_utility = 0            # OpSmile Utilities
        self._NoOS_utility = 0          # No OpSmile Utilities
        self._DALY = 0                  # DALY saved
        self._draw = 0                  # empty vector for Dirichlet distribution draw

        # dirichlet distribution:
        probs = numpy.random.dirichlet(alpha=(1, 3, 1), size=None)      # the numbers of alpha determine the
        # concentration of the probability for each option
        conditions_list = ['a', 'b', 'c']                               # list of conditions (refer to Conditions.py)

        self.draw = choice(a=conditions_list, p=probs)                  # drawing a random condition

    def simulate(self):
        # simulates a patient through a given decision tree based off of the condition chosen
        if self.draw == 'a':                # chooses tree/condition based off of Dirichlet distribution draw
            import DT_Condition_1 as DT
            # OpSmile Tree
            tree_OS=DT.DT.DecisionNode('d1', dict_decisions=DT.dictDecisions_OS,
                                       cum_prob=1, dict_chances=DT.dictChances_OS, dict_terminals=DT.dictTerminal_OS)
            self._cost_utility=tree_OS.get_cost_utility()
            self._OS_cost=tree_OS.get_OS_cost()
            self._OS_utility=tree_OS.get_OS_utility()
            # No OpSmile Tree
            tree_NoOS = DT.DT.DecisionNode('d2', dict_decisions=DT.dictDecisions_NoOS, cum_prob=1,
                                              dict_chances=DT.dictChances_NoOS, dict_terminals=DT.dictTerminal_NoOS)
            self._cost_utility=tree_NoOS.get_cost_utility()
            self._NoOS_cost=tree_NoOS.get_NoOS_cost()
            self._NoOS_utility=tree_NoOS.get_NoOS_utility()
            self._DALY = DT.get_DALY(self)

        if self.draw == 'b':
            import DT_Condition_2 as DT
            # OpSmile Tree
            tree_OS = DT.DT.DecisionNode('d1', dict_decisions=DT.dictDecisions_OS,
                                          cum_prob=1, dict_chances=DT.dictChances_OS,
                                         dict_terminals=DT.dictTerminal_OS)

            self._cost_utility = tree_OS.get_cost_utility()
            self._OS_cost = tree_OS.get_OS_cost()
            self._OS_utility = tree_OS.get_OS_utility()
            # No OpSmile Tree
            tree_NoOS = DT.DT.DecisionNode('d2', dict_decisions=DT.dictDecisions_NoOS, cum_prob=1,
                                            dict_chances=DT.dictChances_NoOS,
                                           dict_terminals=DT.dictTerminal_NoOS)
            self._cost_utility = tree_NoOS.get_cost_utility()
            self._NoOS_cost = tree_NoOS.get_NoOS_cost()
            self._NoOS_utility = tree_NoOS.get_NoOS_utility()
            self._DALY = DT.get_DALY(self)

    def get_DALY(self):
        return self._DALY

    def get_cost_utility(self):
        return self._cost_utility

    def get_OS_cost(self):
        return self._OS_cost

    def get_NoOS_cost(self):
        return self._NoOS_cost

    def get_OS_utility(self):
        return self._OS_utility

    def get_NoOS_utility(self):
        return self._NoOS_utility


class YearofPatients:
    def __init__(self, id):
        self._patients = []
        self._con_a_patients = []
        self._con_b_patients = []
        # eventually we'll want to add other metrics here. Like how many died, etc.

        self._initial_pop_size=100
        # fixed internally because we're going to make this number random eventually.
        # Maybe we'll change this later, but this should work for now.

        for i in range(self._initial_pop_size):
            # create a new patient (use id * pop_size + i as patient id)
            patient = Patient(id * self._initial_pop_size + i)
            self._patients.append(patient)
            self.draw = patient.draw
            #print(self.draw)
            if self.draw == 'a':
                self._con_a_patients.append(patient)
            if self.draw == 'b':
                self._con_b_patients.append(patient)

    def simulate(self):
        """ simulate the cohort of patients over the specified number of time-steps
        :returns outputs from simulating this cohort
        """

        # simulate all patients
        for patient in self._patients:
            patient.simulate()

        # return the cohort outputs
        return YearofPatientsOutputs(self)

    def get_number_of_patients(self):
        return self._initial_pop_size

    def get_patients(self):
        return self._patients

    def get_con_a_patients(self):
        return self._con_a_patients

    def get_con_b_patients(self):
        return self._con_b_patients

class YearofPatientsOutputs:
    def __init__(self, simulated_cohort):
        """ extracts outputs from a simulated cohort
        :param simulated_cohort: a cohort after being simulated
        """

        #self._costs_utilities = []
        self._OS_costs = []
        self._NoOS_costs = []
        self._OS_utilities = []
        self._NoOS_utilities = []
        self._DALY = []

        self._con_a_patients_OS_costs = []
        self._con_a_patients_NoOS_costs = []
        self._con_a_patients_OS_utilities = []
        self._con_a_patients_NoOS_utilities = []
        self._con_a_patients_DALY = []

        self._con_b_patients_OS_costs = []
        self._con_b_patients_NoOS_costs = []
        self._con_b_patients_OS_utilities = []
        self._con_b_patients_NoOS_utilities = []
        self._con_b_patients_DALY = []

        # find patients' survival times
        for patient in simulated_cohort.get_patients():

            # cost and utility
            #self._costs_utilities.append(patient.get_cost_utility())
            self._OS_costs.append(patient.get_OS_cost())
            self._NoOS_costs.append(patient.get_NoOS_cost())
            self._OS_utilities.append(patient.get_OS_utility())
            self._NoOS_utilities.append(patient.get_NoOS_utility())
            self._DALY.append(patient.get_DALY())

        for patient in simulated_cohort.get_con_a_patients():

            self._con_a_patients_OS_costs.append(patient.get_OS_cost())
            self._con_a_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_a_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_a_patients_NoOS_utilities.append(patient.get_NoOS_utility())
            self._con_a_patients_DALY.append(patient.get_DALY())

        for patient in simulated_cohort.get_con_b_patients():
            self._con_b_patients_OS_costs.append(patient.get_OS_cost())
            self._con_b_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_b_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_b_patients_NoOS_utilities.append(patient.get_NoOS_utility())
            self._con_b_patients_DALY.append(patient.get_DALY())

        # summary statistics
        self._sumStat_OS_cost = StatCls.SummaryStat('Expected Op Smile Cost', self._OS_costs)
        self._sumStat_NoOS_cost = StatCls.SummaryStat('Expected No Op Smile Cost', self._NoOS_costs)
        self._sumStat_OS_utility = StatCls.SummaryStat('Expected Op Smile utility', self._OS_utilities)
        self._sumStat_NoOS_utility = StatCls.SummaryStat('Expected No Op Smile utility', self._NoOS_utilities)
        self._sumStat_DALY = StatCls.SummaryStat('DALY', self._DALY)

        self._sumStat_con_a_OS_cost = StatCls.SummaryStat("Condition A Op Smile Cost", self._con_a_patients_OS_costs)
        self._sumStat_con_a_NoOS_cost = StatCls.SummaryStat("Condition A No Op Smile Cost", self._con_a_patients_NoOS_costs)
        self._sumStat_con_a_OS_utilities = StatCls.SummaryStat("Condition A Op Smile Utilities", self._con_a_patients_OS_utilities)
        self._sumStat_con_a_NoOS_utilities = StatCls.SummaryStat("Condition A No Op Smile Utilities", self._con_a_patients_NoOS_utilities)
        self._sumStat_con_a_DALY = StatCls.SummaryStat("Condition A DALY", self._con_a_patients_DALY)

        self._sumStat_con_b_OS_cost = StatCls.SummaryStat("Condition B Op Smile Cost", self._con_b_patients_OS_costs)
        self._sumStat_con_b_NoOS_cost = StatCls.SummaryStat("Condition B No Op Smile Cost",
                                                            self._con_b_patients_NoOS_costs)
        self._sumStat_con_b_OS_utilities = StatCls.SummaryStat("Condition B Op Smile Utilities",
                                                               self._con_b_patients_OS_utilities)
        self._sumStat_con_b_NoOS_utilities = StatCls.SummaryStat("Condition B No Op Smile Utilities",
                                                                 self._con_b_patients_NoOS_utilities)
        self._sumStat_con_b_DALY = StatCls.SummaryStat("Condition B DALY", self._con_b_patients_DALY)

    def get_DALY(self):
        return self._DALY

    def get_OS_costs(self):
        return self._OS_costs

    def get_NoOS_costs(self):
        return self._NoOS_costs

    def get_OS_utilities(self):
        return self._OS_utilities

    def get_NoOS_utilities(self):
        return self._NoOS_utilities

    def get_sumStat_OS_cost(self):
        return self._sumStat_OS_cost

    def get_sumStat_NoOS_cost(self):
        return self._sumStat_NoOS_cost

    def get_sumStat_OS_utility(self):
        return self._sumStat_OS_utility

    def get_sumStat_NoOS_utility(self):
        return self._sumStat_NoOS_utility

    def get_sumStat_DALY(self):
        return self._sumStat_DALY

    def get_sumStat_con_a_OS_cost(self):
        return self._sumStat_con_a_OS_cost

    def get_sumStat_con_a_NoOS_cost(self):
        return self._sumStat_con_a_NoOS_cost

    def get_sumStat_con_a_OS_utilities(self):
        return self._sumStat_con_a_OS_utilities

    def get_sumStat_con_a_NoOS_utilities(self):
        return self._sumStat_con_a_NoOS_utilities

    def get_sumStat_con_a_DALY(self):
        return self._sumStat_con_a_DALY

    def get_sumStat_con_b_OS_cost(self):
        return self._sumStat_con_b_OS_cost

    def get_sumStat_con_b_NoOS_cost(self):
        return self._sumStat_con_b_NoOS_cost

    def get_sumStat_con_b_OS_utilities(self):
        return self._sumStat_con_b_OS_utilities

    def get_sumStat_con_b_NoOS_utilities(self):
        return self._sumStat_con_b_NoOS_utilities

    def get_sumStat_con_b_DALY(self):
        return self._sumStat_con_b_DALY


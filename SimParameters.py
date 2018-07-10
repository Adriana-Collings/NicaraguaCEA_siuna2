import numpy as np
from scipy.stats import expon
import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as StatCls
import Surgeries as S
import ContitionTypeProbs as C_P
import DT_Condition_1 as DT_C1
import DT_Condition_2 as DT_C2

class Patient:
    def __init__(self, id):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(self._id)
        self._cost_utility = []

    def simulate (self):
        if self._rnd.random_sample() < C_P.PROB_CONDITION_1:
            tree=DT_C1.DT.DecisionNode('d1', dict_decisions=DT_C1.dictDecisions,
                                       cum_prob=1, dict_chances=DT_C1.dictChances, dict_terminals=DT_C1.dictTerminal)
            self._cost_utility=tree.get_cost_utility()
        else:
            tree=DT_C2.DT.DecisionNode('d1', dict_decisions=DT_C2.dictDecisions,
                                       cum_prob=1, dict_chances=DT_C2.dictChances, dict_terminals=DT_C2.dictTerminal)

    def get_cost_utility(self):
        return self._cost_utility

class YearofPatients:
    def __init__(self, id):
        self._patients = []
        ##eventually we'll want to add other metrics here. Like how manhy died, etc.

        self._initial_pop_size=100
        #fixed internally because we're going to make this number random eventually.
        # Maybe we'll change this later, but this
        #should work for now.

        for i in range(self._initial_pop_size):
            # create a new patient (use id * pop_size + i as patient id)
            patient = Patient(id * self._initial_pop_size + i)
            self._patients.append(patient)

    def simulate(self):
        """ simulate the cohort of patients over the specified number of time-steps
        :returns outputs from simulating this cohort
        """

        # simulate all patients
        for patient in self._patients:
            patient.simulate()

        # return the cohort outputs
        return CohortOutputs(self)

    def get_number_of_patients(self):
        return self._initial_pop_size

    def get_patients(self):
        return self._patients


class CohortOutputs:
    def __init__(self, simulated_cohort):
        """ extracts outputs from a simulated cohort
        :param simulated_cohort: a cohort after being simulated
        """

        self._costs_utilities = []

        # find patients' survival times
        for patient in simulated_cohort.get_patients():

            # cost and utility
            self._costs_utilities.append(patient.get_cost_utility())

        # summary statistics
        #self._sumStat_cost = StatCls.SummaryStat('Patient discounted cost', self._costs)
        #self._sumStat_utility = StatCls.SummaryStat('Patient discounted utility', self._utilities)

        ##This will be right once we can parse out the utilities from the costs. Shouldn't be TOO hard.

    def get_costs_utilities(self):
        return self._costs_utilities

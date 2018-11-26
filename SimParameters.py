import numpy as np
from scipy.stats import expon
import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as StatCls
import numpy
from numpy.random import choice
import DT as DTb
from scipy.stats import expon
from numpy.random import choice
import random as random
import costs as Co

random.seed(1)

class Patient:
    # ##run more than one patient through tree to find costs and utilities
    # run a patient
    def __init__(self, id):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(self._id)
        # counts
        self._count_OS_S = 0
        self._count_OS_NS = 0
        self._count_NoOS_S = 0
        self._count_NoOS_NS = 0
        # count * cost/utility value
        self._S_OS_S = 0
        self._S_OS_NS = 0
        self._S_NoOS_S = 0
        self._S_NoOS_NS = 0

        self._total_OpSmile_costs = 0
        self._total_OpSmile_utilities = 0
        self._total_NoOpSmile_costs = 0
        self._total_NoOpSmile_utilities = 0

        # dirichlet distribution:
        probs = np.random.dirichlet(alpha=(0.033, # 1
                                           0.061, # 2
                                           #0.056, # 3
                                           0.003, # 4
                                          # 0.395, # 5
                                           0.009, # 6
                                         #  0.003, # 8
                                         #  0.003, # 10
                                           0.006, # 12
                                           0.008, # 13
                                           0.022, # 14
                                          # 0.015, # 16
                                         #  0.003, # 17
                                          # 0.017, # 18
                                         #  0.003, # 19
                                         #  0.003, # 20
                                         #  0.003, # 22
                                           0.067, # 24
                                         #  0.003, # 25
                                           0.004, # 28
                                         #  0.002, # 30
                                           0.027, # 32
                                          # 0.005, # 33
                                           0.009, # 34
                                           0.025, # 35
                                           0.048, # 37
                                           0.009, # 41
                                          # 0.004, # 42
                                           0.012, # 43
                                          # 0.004, # 44
                                           0.048, # 45
                                          # 0.004, # 46
                                         #  0.003, # 47
                                           0.011, # 48
                                         #  0.005, # 49
                                           0.005, # 50
                                          # 0.004, # 51
                                           0.003, # 53
                                          # 0.02, # 54
                                          # 0.004 # 59
                                           ), size=None)
        # the numbers of alpha determine the concentration of the probability for each option
        conditions_list = ['a', 'b',
                           #'c',
                           'd',
                           #'e',
                           'f',
                           #'g',
                           #'h',
                           'i', 'j', 'k',
                           #'l',
                           #'m',
                           #'n',
                           #'o',
                           #'p',
                           # 'q',
                           'r',
                           #'s',
                           't',
                           #'u',
                           'v',
                           # 'w',
                           'x', 'y', 'z', 'aa',
                           # 'bb',
                           'cc',
                           #'dd',
                           'ee',
                           #'ff',
                           #'gg',
                           'hh',
                           #'ii',
                           'jj',
                           #'kk',
                           'll',
                           #'mm',
                           #'nn'
                           ]  # list of conditions
# what you are trying to do now is build a function in R that will tell you the concentration of each disease to input above
        self.draw = choice(a=conditions_list, p=probs)                  # drawing a random

    def simulate(self, n_of_patients):
        if self.draw == 'a':                # chooses tree/condition based off of Dirichlet distribution draw
            import DT_Condition_1 as D
        if self.draw == 'b':
            import DT_Condition_2 as D
        #if self.draw == 'c':
        #    import DT_Condition_3 as D
        if self.draw == 'd':
            import DT_Condition_4 as D
        #if self.draw == 'e':
        #    import _DT_Condition_5 as D
        if self.draw == 'f':
            import DT_Condition_6 as D
        #if self.draw == 'g':
        #    import DT_Condition_8 as D
        #if self.draw == 'h':
        #    import DT_Condition_10 as D
        if self.draw == 'i':
            import DT_Condition_12 as D
        if self.draw == 'j':
            import DT_Condition_13 as D
        if self.draw == 'k':
            import DT_Condition_14 as D
        #if self.draw == 'l':
        #    import _DT_Condition_16 as D
        #if self.draw == 'm':
        #    import DT_Condition_17 as D
        #if self.draw == 'n':
        #    import _DT_Condition_18 as D
        #if self.draw == 'o':
        #    import DT_Condition_19 as D
        #if self.draw =='p':
        #    import _DT_Condition_20 as D
        #if self.draw =='q':
        #    import _DT_Condition_22 as D
        if self.draw == 'r':
            import DT_Condition_24 as D
        #if self.draw == 's':
        #    import DT_Condition_25 as D
        if self.draw =='t':
            import DT_Condition_28 as D
        #if self.draw == 'u':
        #    import DT_Condition_30 as D
        if self.draw == 'v':
            import DT_Condition_32 as D
        #if self.draw == 'w':
        #    import _DT_Condition_33 as D
        if self.draw == 'x':
            import DT_Condition_34 as D
        if self.draw == 'y':
            import DT_Condition_35 as D
        if self.draw == 'z':
            import DT_Condition_37 as D
        if self.draw == 'aa':
            import DT_Condition_41 as D
        #if self.draw == 'bb':
        #    import _DT_Condition_42 as D
        if self.draw == 'cc':
            import DT_Condition_43 as D
        #if self.draw == 'dd':
        #    import _DT_Condition_44 as D
        if self.draw == 'ee':
            import DT_Condition_45 as D
        #if self.draw == 'ff':
        #    import _DT_Condition_46 as D
        #if self.draw == 'gg':
        #    import DT_Condition_47 as D
        if self.draw == 'hh':
            import DT_Condition_48 as D
        #if self.draw == 'ii':
        #    import DT_Condition_49 as D
        if self.draw == 'jj':
            import DT_Condition_50 as D
        #if self.draw =='kk':
        #    import _DT_Condition_51 as D
        if self.draw =='ll':
            import DT_Condition_53 as D
        #if self.draw == 'mm':
        #    import _DT_Condition_54 as D
        #if self.draw == 'nn':
        #    import DT_Condition_59 as D

        t = 0
        z = 0

        # for those counts, you randomize them further
        for i in range(n_of_patients):
            if self._rnd.random_sample() < D.PR_OS_Surgery:
                self._count_OS_NS += 1
            else:
                self._count_OS_S += 1

        for i in range(n_of_patients):
            if self._rnd.random_sample() < D.PR_NoOS_Surgery:
                self._count_NoOS_NS += 1
            else:
                self._count_NoOS_S += 1

        # multiply counts by cost and utilities and return total
        self._S_OS_S_C = self._count_OS_S * D.OS_Surgery_C
        self._S_OS_S_U = self._count_OS_S * D.OS_Surgery_U

        self._S_OS_NS_C = self._count_OS_NS * D.OS_NoSurgery_C
        self._S_OS_NS_U = self._count_OS_NS * D.OS_NoSurgery_U

        self._S_NoOS_S_C = self._count_NoOS_S * D.NoOS_Surgery_C
        self._S_NoOS_S_U = self._count_NoOS_S * D.NoOS_Surgery_U

        self._S_NoOS_NS_C = self._count_NoOS_NS * D.NoOS_NoSurgery_C
        self._S_NoOS_NS_U = self._count_NoOS_NS * D.NoOS_NoSurgery_U

        self._total_OpSmile_costs = self._S_OS_S_C + self._S_OS_NS_C

        self._total_OpSmile_utilities = self._S_OS_S_U + self._S_OS_NS_U

        self._total_NoOpSmile_costs = self._S_NoOS_S_C + self._S_NoOS_NS_C

        self._total_NoOpSmile_utilities = self._S_NoOS_S_U + self._S_NoOS_NS_U

    def get_OS_cost(self):
        return self._total_OpSmile_costs + Co.OpSmile_C

    def get_NoOS_cost(self):
        return self._total_NoOpSmile_costs + Co.NoOS_C

    def get_OS_utility(self):
        return self._total_OpSmile_utilities

    def get_NoOS_utility(self):
        return  self._total_NoOpSmile_utilities


class YearofPatients:
    def __init__(self, id):
        self._patients = []
        self._con_a_patients = []
        self._con_b_patients = []
        self._con_c_patients = []
        self._con_d_patients = []
        self._con_e_patients = []
        self._con_f_patients = []
        self._con_g_patients = []
        self._con_h_patients = []
        self._con_i_patients = []
        self._con_j_patients = []
        self._con_k_patients = []
        self._con_l_patients = []
        self._con_m_patients = []
        self._con_n_patients = []
        self._con_o_patients = []
        self._con_p_patients = []
        self._con_q_patients = []
        self._con_r_patients = []
        self._con_s_patients = []
        self._con_t_patients = []
        self._con_u_patients = []
        self._con_v_patients = []
        self._con_w_patients = []
        self._con_x_patients = []
        self._con_y_patients = []
        self._con_z_patients = []
        self._con_aa_patients = []
        self._con_bb_patients = []
        self._con_cc_patients = []
        self._con_dd_patients = []
        self._con_ee_patients = []
        self._con_ff_patients = []
        self._con_gg_patients = []
        self._con_hh_patients = []
        self._con_ii_patients = []
        self._con_jj_patients = []
        self._con_kk_patients = []
        self._con_ll_patients = []
        self._con_mm_patients = []
        self._con_nn_patients = []
        # eventually we'll want to add other metrics here. Like how many died, etc.

        self._initial_pop_size_pre= 1451
        self._initial_pop_size_post = 2658
        # fixed internally because we're going to make this number random eventually.
        # Maybe we'll change this later, but this should work for now.

        for i in range(self._initial_pop_size_pre):
            patient = Patient(id=3)
            self._patients.append(patient)
            self.draw = patient.draw
            if self.draw == 'a':
                self._con_a_patients.append(patient)
            if self.draw == 'b':
                self._con_b_patients.append(patient)
            if self.draw == 'c':
                self._con_c_patients.append(patient)
            if self.draw == 'd':
                self._con_d_patients.append(patient)
            if self.draw == 'e':
                self._con_e_patients.append(patient)
            if self.draw == 'f':
                self._con_f_patients.append(patient)
            if self.draw == 'g':
                self._con_g_patients.append(patient)
            if self.draw == 'h':
                self._con_h_patients.append(patient)
            if self.draw == 'i':
                self._con_i_patients.append(patient)
            if self.draw == 'j':
                self._con_j_patients.append(patient)
            if self.draw == 'k':
                self._con_k_patients.append(patient)
            if self.draw == 'l':
                self._con_l_patients.append(patient)
            if self.draw == 'm':
                self._con_m_patients.append(patient)
            if self.draw == 'n':
                self._con_n_patients.append(patient)
            if self.draw == 'o':
                self._con_o_patients.append(patient)
            if self.draw == 'p':
                self._con_p_patients.append(patient)
            if self.draw == 'q':
                self._con_q_patients.append(patient)
            if self.draw == 'r':
                self._con_r_patients.append(patient)
            if self.draw == 's':
                self._con_s_patients.append(patient)
            if self.draw == 't':
                self._con_t_patients.append(patient)
            if self.draw == 'u':
                self._con_u_patients.append(patient)
            if self.draw == 'v':
                self._con_v_patients.append(patient)
            if self.draw == 'w':
                self._con_w_patients.append(patient)
            if self.draw == 'x':
                self._con_x_patients.append(patient)
            if self.draw == 'y':
                self._con_y_patients.append(patient)
            if self.draw == 'z':
                self._con_z_patients.append(patient)
            if self.draw == 'aa':
                self._con_aa_patients.append(patient)
            if self.draw == 'bb':
                self._con_bb_patients.append(patient)
            if self.draw == 'cc':
                self._con_cc_patients.append(patient)
            if self.draw == 'dd':
                self._con_dd_patients.append(patient)
            if self.draw == 'ee':
                self._con_ee_patients.append(patient)
            if self.draw == 'f':
                self._con_ff_patients.append(patient)
            if self.draw == 'gg':
                self._con_gg_patients.append(patient)
            if self.draw == 'hh':
                self._con_hh_patients.append(patient)
            if self.draw == 'ii':
                self._con_ii_patients.append(patient)
            if self.draw == 'jj':
                self._con_jj_patients.append(patient)
            if self.draw == 'kk':
                self._con_kk_patients.append(patient)
            if self.draw == 'll':
                self._con_ll_patients.append(patient)
            if self.draw == 'mm':
                self._con_mm_patients.append(patient)
            if self.draw == 'nn':
                self._con_nn_patients.append(patient)

        for i in range(self._initial_pop_size_post):
            patient = Patient(id=3)
            self._patients.append(patient)
            self.draw = patient.draw
            if self.draw == 'a':
                self._con_a_patients.append(patient)
            if self.draw == 'b':
                self._con_b_patients.append(patient)
            if self.draw == 'c':
                self._con_c_patients.append(patient)
            if self.draw == 'd':
                self._con_d_patients.append(patient)
            if self.draw == 'e':
                self._con_e_patients.append(patient)
            if self.draw == 'f':
                self._con_f_patients.append(patient)
            if self.draw == 'g':
                self._con_g_patients.append(patient)
            if self.draw == 'h':
                self._con_h_patients.append(patient)
            if self.draw == 'i':
                self._con_i_patients.append(patient)
            if self.draw == 'j':
                self._con_j_patients.append(patient)
            if self.draw == 'k':
                self._con_k_patients.append(patient)
            if self.draw == 'l':
                self._con_l_patients.append(patient)
            if self.draw == 'm':
                self._con_m_patients.append(patient)
            if self.draw == 'n':
                self._con_n_patients.append(patient)
            if self.draw == 'o':
                self._con_o_patients.append(patient)
            if self.draw == 'p':
                self._con_p_patients.append(patient)
            if self.draw == 'q':
                self._con_q_patients.append(patient)
            if self.draw == 'r':
                self._con_r_patients.append(patient)
            if self.draw == 's':
                self._con_s_patients.append(patient)
            if self.draw == 't':
                self._con_t_patients.append(patient)
            if self.draw == 'u':
                self._con_u_patients.append(patient)
            if self.draw == 'v':
                self._con_v_patients.append(patient)
            if self.draw == 'w':
                self._con_w_patients.append(patient)
            if self.draw == 'x':
                self._con_x_patients.append(patient)
            if self.draw == 'y':
                self._con_y_patients.append(patient)
            if self.draw == 'z':
                self._con_z_patients.append(patient)
            if self.draw == 'aa':
                self._con_aa_patients.append(patient)
            if self.draw == 'bb':
                self._con_bb_patients.append(patient)
            if self.draw == 'cc':
                self._con_cc_patients.append(patient)
            if self.draw == 'dd':
                self._con_dd_patients.append(patient)
            if self.draw == 'ee':
                self._con_ee_patients.append(patient)
            if self.draw == 'f':
                self._con_ff_patients.append(patient)
            if self.draw == 'gg':
                self._con_gg_patients.append(patient)
            if self.draw == 'hh':
                self._con_hh_patients.append(patient)
            if self.draw == 'ii':
                self._con_ii_patients.append(patient)
            if self.draw == 'jj':
                self._con_jj_patients.append(patient)
            if self.draw == 'kk':
                self._con_kk_patients.append(patient)
            if self.draw == 'll':
                self._con_ll_patients.append(patient)
            if self.draw == 'mm':
                self._con_mm_patients.append(patient)
            if self.draw == 'nn':
                self._con_nn_patients.append(patient)


    def simulate(self):
        """ simulate the cohort of patients over the specified number of time-steps
        :returns outputs from simulating this cohort
        """

        for patient in self._con_a_patients:
            patient.simulate(n_of_patients=len(self._con_a_patients))

        for patient in self._con_b_patients:
            patient.simulate(n_of_patients=len(self._con_b_patients))

        for patient in self._con_c_patients:
            patient.simulate(n_of_patients=len(self._con_c_patients))

        for patient in self._con_d_patients:
            patient.simulate(n_of_patients=len(self._con_d_patients))

        for patient in self._con_e_patients:
            patient.simulate(n_of_patients=len(self._con_e_patients))

        for patient in self._con_f_patients:
            patient.simulate(n_of_patients=len(self._con_f_patients))

        for patient in self._con_g_patients:
            patient.simulate(n_of_patients=len(self._con_g_patients))

        for patient in self._con_h_patients:
            patient.simulate(n_of_patients=len(self._con_h_patients))

        for patient in self._con_i_patients:
            patient.simulate(n_of_patients=len(self._con_i_patients))

        for patient in self._con_j_patients:
            patient.simulate(n_of_patients=len(self._con_j_patients))

        for patient in self._con_k_patients:
            patient.simulate(n_of_patients=len(self._con_k_patients))

        for patient in self._con_l_patients:
            patient.simulate(n_of_patients=len(self._con_l_patients))

        for patient in self._con_m_patients:
            patient.simulate(n_of_patients=len(self._con_m_patients))

        for patient in self._con_n_patients:
            patient.simulate(n_of_patients=len(self._con_n_patients))

        for patient in self._con_o_patients:
            patient.simulate(n_of_patients=len(self._con_o_patients))

        for patient in self._con_p_patients:
            patient.simulate(n_of_patients=len(self._con_p_patients))

        for patient in self._con_q_patients:
            patient.simulate(n_of_patients=len(self._con_q_patients))

        for patient in self._con_r_patients:
            patient.simulate(n_of_patients=len(self._con_r_patients))

        for patient in self._con_s_patients:
            patient.simulate(n_of_patients=len(self._con_s_patients))

        for patient in self._con_t_patients:
            patient.simulate(n_of_patients=len(self._con_t_patients))

        for patient in self._con_u_patients:
            patient.simulate(n_of_patients=len(self._con_u_patients))

        for patient in self._con_v_patients:
            patient.simulate(n_of_patients=len(self._con_v_patients))

        for patient in self._con_w_patients:
            patient.simulate(n_of_patients=len(self._con_w_patients))

        for patient in self._con_x_patients:
            patient.simulate(n_of_patients=len(self._con_x_patients))

        for patient in self._con_y_patients:
            patient.simulate(n_of_patients=len(self._con_y_patients))

        for patient in self._con_z_patients:
            patient.simulate(n_of_patients=len(self._con_z_patients))

        for patient in self._con_aa_patients:
            patient.simulate(n_of_patients=len(self._con_aa_patients))

        for patient in self._con_bb_patients:
            patient.simulate(n_of_patients=len(self._con_bb_patients))

        for patient in self._con_cc_patients:
            patient.simulate(n_of_patients=len(self._con_cc_patients))

        for patient in self._con_dd_patients:
            patient.simulate(n_of_patients=len(self._con_dd_patients))

        for patient in self._con_ee_patients:
            patient.simulate(n_of_patients=len(self._con_ee_patients))

        for patient in self._con_ff_patients:
            patient.simulate(n_of_patients=len(self._con_ff_patients))

        for patient in self._con_gg_patients:
            patient.simulate(n_of_patients=len(self._con_gg_patients))

        for patient in self._con_hh_patients:
            patient.simulate(n_of_patients=len(self._con_hh_patients))

        for patient in self._con_ii_patients:
            patient.simulate(n_of_patients=len(self._con_ii_patients))

        for patient in self._con_jj_patients:
            patient.simulate(n_of_patients=len(self._con_jj_patients))

        for patient in self._con_kk_patients:
            patient.simulate(n_of_patients=len(self._con_kk_patients))

        for patient in self._con_ll_patients:
            patient.simulate(n_of_patients=len(self._con_ll_patients))

        for patient in self._con_nn_patients:
            patient.simulate(n_of_patients=len(self._con_mm_patients))

        # return the cohort outputs
        return YearofPatientsOutputs(self)

    def get_number_of_patients_pre(self):
        return self._initial_pop_size_pre

    def get_number_of_patients_post(self):
        return self._initial_pop_size_post

    def get_patients(self):
        return self._patients

    def get_con_a_patients(self):
        return self._con_a_patients

    def get_con_b_patients(self):
        return self._con_b_patients

    def get_con_c_patients(self):
        return self._con_c_patients

    def get_con_d_patients(self):
        return self._con_d_patients

    def get_con_e_patients(self):
        return self._con_e_patients

    def get_con_f_patients(self):
        return self._con_f_patients

    def get_con_g_patients(self):
        return self._con_g_patients

    def get_con_h_patients(self):
        return self._con_h_patients

    def get_con_i_patients(self):
        return self._con_i_patients

    def get_con_j_patients(self):
        return self._con_j_patients

    def get_con_k_patients(self):
        return self._con_k_patients

    def get_con_l_patients(self):
        return self._con_l_patients

    def get_con_m_patients(self):
        return self._con_m_patients

    def get_con_n_patients(self):
        return self._con_n_patients

    def get_con_o_patients(self):
        return self._con_o_patients

    def get_con_p_patients(self):
        return self._con_p_patients

    def get_con_q_patients(self):
        return self._con_q_patients

    def get_con_r_patients(self):
        return self._con_r_patients

    def get_con_s_patients(self):
        return self._con_s_patients

    def get_con_t_patients(self):
        return self._con_t_patients

    def get_con_u_patients(self):
        return self._con_u_patients

    def get_con_v_patients(self):
        return self._con_v_patients

    def get_con_w_patients(self):
        return self._con_w_patients

    def get_con_x_patients(self):
        return self._con_x_patients

    def get_con_y_patients(self):
        return self._con_y_patients

    def get_con_z_patients(self):
        return self._con_z_patients

    def get_con_aa_patients(self):
        return self._con_aa_patients

    def get_con_bb_patients(self):
        return self._con_bb_patients

    def get_con_cc_patients(self):
        return self._con_cc_patients

    def get_con_dd_patients(self):
        return self._con_dd_patients

    def get_con_ee_patients(self):
        return self._con_ee_patients

    def get_con_ff_patients(self):
        return self._con_ff_patients

    def get_con_gg_patients(self):
        return self._con_gg_patients

    def get_con_hh_patients(self):
        return self._con_hh_patients

    def get_con_ii_patients(self):
        return self._con_ii_patients

    def get_con_jj_patients(self):
        return self._con_jj_patients

    def get_con_kk_patients(self):
        return self._con_kk_patients

    def get_con_ll_patients(self):
        return self._con_ll_patients

    def get_con_mm_patients(self):
        return self._con_mm_patients

    def get_con_nn_patients(self):
        return self._con_nn_patients


class YearofPatientsOutputs:
    def __init__(self, simulated_cohort):
        """ extracts outputs from a simulated cohort
        :param simulated_cohort: a cohort after being simulated
        """

        self._OS_costs = []
        self._NoOS_costs = []
        self._OS_utilities = []
        self._NoOS_utilities = []

        self._con_a_patients_OS_costs = []
        self._con_a_patients_NoOS_costs = []
        self._con_a_patients_OS_utilities = []
        self._con_a_patients_NoOS_utilities = []

        self._con_b_patients_OS_costs = []
        self._con_b_patients_NoOS_costs = []
        self._con_b_patients_OS_utilities = []
        self._con_b_patients_NoOS_utilities = []

        self._con_c_patients_OS_costs = []
        self._con_c_patients_NoOS_costs = []
        self._con_c_patients_OS_utilities = []
        self._con_c_patients_NoOS_utilities = []

        self._con_d_patients_OS_costs = []
        self._con_d_patients_NoOS_costs = []
        self._con_d_patients_OS_utilities = []
        self._con_d_patients_NoOS_utilities = []

        self._con_e_patients_OS_costs = []
        self._con_e_patients_NoOS_costs = []
        self._con_e_patients_OS_utilities = []
        self._con_e_patients_NoOS_utilities = []

        self._con_f_patients_OS_costs = []
        self._con_f_patients_NoOS_costs = []
        self._con_f_patients_OS_utilities = []
        self._con_f_patients_NoOS_utilities = []

        self._con_g_patients_OS_costs = []
        self._con_g_patients_NoOS_costs = []
        self._con_g_patients_OS_utilities = []
        self._con_g_patients_NoOS_utilities = []

        self._con_h_patients_OS_costs = []
        self._con_h_patients_NoOS_costs = []
        self._con_h_patients_OS_utilities = []
        self._con_h_patients_NoOS_utilities = []

        self._con_i_patients_OS_costs = []
        self._con_i_patients_NoOS_costs = []
        self._con_i_patients_OS_utilities = []
        self._con_i_patients_NoOS_utilities = []

        self._con_j_patients_OS_costs = []
        self._con_j_patients_NoOS_costs = []
        self._con_j_patients_OS_utilities = []
        self._con_j_patients_NoOS_utilities = []

        self._con_k_patients_OS_costs = []
        self._con_k_patients_NoOS_costs = []
        self._con_k_patients_OS_utilities = []
        self._con_k_patients_NoOS_utilities = []

        self._con_l_patients_OS_costs = []
        self._con_l_patients_NoOS_costs = []
        self._con_l_patients_OS_utilities = []
        self._con_l_patients_NoOS_utilities = []

        self._con_m_patients_OS_costs = []
        self._con_m_patients_NoOS_costs = []
        self._con_m_patients_OS_utilities = []
        self._con_m_patients_NoOS_utilities = []

        self._con_n_patients_OS_costs = []
        self._con_n_patients_NoOS_costs = []
        self._con_n_patients_OS_utilities = []
        self._con_n_patients_NoOS_utilities = []

        self._con_o_patients_OS_costs = []
        self._con_o_patients_NoOS_costs = []
        self._con_o_patients_OS_utilities = []
        self._con_o_patients_NoOS_utilities = []

        self._con_p_patients_OS_costs = []
        self._con_p_patients_NoOS_costs = []
        self._con_p_patients_OS_utilities = []
        self._con_p_patients_NoOS_utilities = []

        self._con_q_patients_OS_costs = []
        self._con_q_patients_NoOS_costs = []
        self._con_q_patients_OS_utilities = []
        self._con_q_patients_NoOS_utilities = []

        self._con_r_patients_OS_costs = []
        self._con_r_patients_NoOS_costs = []
        self._con_r_patients_OS_utilities = []
        self._con_r_patients_NoOS_utilities = []

        self._con_s_patients_OS_costs = []
        self._con_s_patients_NoOS_costs = []
        self._con_s_patients_OS_utilities = []
        self._con_s_patients_NoOS_utilities = []

        self._con_t_patients_OS_costs = []
        self._con_t_patients_NoOS_costs = []
        self._con_t_patients_OS_utilities = []
        self._con_t_patients_NoOS_utilities = []

        self._con_u_patients_OS_costs = []
        self._con_u_patients_NoOS_costs = []
        self._con_u_patients_OS_utilities = []
        self._con_u_patients_NoOS_utilities = []

        self._con_v_patients_OS_costs = []
        self._con_v_patients_NoOS_costs = []
        self._con_v_patients_OS_utilities = []
        self._con_v_patients_NoOS_utilities = []

        self._con_w_patients_OS_costs = []
        self._con_w_patients_NoOS_costs = []
        self._con_w_patients_OS_utilities = []
        self._con_w_patients_NoOS_utilities = []

        self._con_x_patients_OS_costs = []
        self._con_x_patients_NoOS_costs = []
        self._con_x_patients_OS_utilities = []
        self._con_x_patients_NoOS_utilities = []

        self._con_y_patients_OS_costs = []
        self._con_y_patients_NoOS_costs = []
        self._con_y_patients_OS_utilities = []
        self._con_y_patients_NoOS_utilities = []

        self._con_z_patients_OS_costs = []
        self._con_z_patients_NoOS_costs = []
        self._con_z_patients_OS_utilities = []
        self._con_z_patients_NoOS_utilities = []

        self._con_aa_patients_OS_costs = []
        self._con_aa_patients_NoOS_costs = []
        self._con_aa_patients_OS_utilities = []
        self._con_aa_patients_NoOS_utilities = []

        self._con_bb_patients_OS_costs = []
        self._con_bb_patients_NoOS_costs = []
        self._con_bb_patients_OS_utilities = []
        self._con_bb_patients_NoOS_utilities = []

        self._con_cc_patients_OS_costs = []
        self._con_cc_patients_NoOS_costs = []
        self._con_cc_patients_OS_utilities = []
        self._con_cc_patients_NoOS_utilities = []

        self._con_dd_patients_OS_costs = []
        self._con_dd_patients_NoOS_costs = []
        self._con_dd_patients_OS_utilities = []
        self._con_dd_patients_NoOS_utilities = []

        self._con_ee_patients_OS_costs = []
        self._con_ee_patients_NoOS_costs = []
        self._con_ee_patients_OS_utilities = []
        self._con_ee_patients_NoOS_utilities = []

        self._con_ff_patients_OS_costs = []
        self._con_ff_patients_NoOS_costs = []
        self._con_ff_patients_OS_utilities = []
        self._con_ff_patients_NoOS_utilities = []

        self._con_gg_patients_OS_costs = []
        self._con_gg_patients_NoOS_costs = []
        self._con_gg_patients_OS_utilities = []
        self._con_gg_patients_NoOS_utilities = []

        self._con_hh_patients_OS_costs = []
        self._con_hh_patients_NoOS_costs = []
        self._con_hh_patients_OS_utilities = []
        self._con_hh_patients_NoOS_utilities = []

        self._con_ii_patients_OS_costs = []
        self._con_ii_patients_NoOS_costs = []
        self._con_ii_patients_OS_utilities = []
        self._con_ii_patients_NoOS_utilities = []

        self._con_jj_patients_OS_costs = []
        self._con_jj_patients_NoOS_costs = []
        self._con_jj_patients_OS_utilities = []
        self._con_jj_patients_NoOS_utilities = []

        self._con_kk_patients_OS_costs = []
        self._con_kk_patients_NoOS_costs = []
        self._con_kk_patients_OS_utilities = []
        self._con_kk_patients_NoOS_utilities = []

        self._con_ll_patients_OS_costs = []
        self._con_ll_patients_NoOS_costs = []
        self._con_ll_patients_OS_utilities = []
        self._con_ll_patients_NoOS_utilities = []

        self._con_mm_patients_OS_costs = []
        self._con_mm_patients_NoOS_costs = []
        self._con_mm_patients_OS_utilities = []
        self._con_mm_patients_NoOS_utilities = []

        self._con_nn_patients_OS_costs = []
        self._con_nn_patients_NoOS_costs = []
        self._con_nn_patients_OS_utilities = []
        self._con_nn_patients_NoOS_utilities = []

        for patient in simulated_cohort.get_patients():
            self._OS_costs.append(patient.get_OS_cost())
            self._NoOS_costs.append(patient.get_NoOS_cost())
            self._OS_utilities.append(patient.get_OS_utility())
            self._NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_a_patients():
            self._con_a_patients_OS_costs.append(patient.get_OS_cost())
            self._con_a_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_a_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_a_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_b_patients():
            self._con_b_patients_OS_costs.append(patient.get_OS_cost())
            self._con_b_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_b_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_b_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_c_patients():
            self._con_c_patients_OS_costs.append(patient.get_OS_cost())
            self._con_c_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_c_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_c_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_d_patients():
            self._con_d_patients_OS_costs.append(patient.get_OS_cost())
            self._con_d_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_d_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_d_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_e_patients():
            self._con_e_patients_OS_costs.append(patient.get_OS_cost())
            self._con_e_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_e_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_e_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_f_patients():
            self._con_f_patients_OS_costs.append(patient.get_OS_cost())
            self._con_f_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_f_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_f_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_g_patients():
            self._con_g_patients_OS_costs.append(patient.get_OS_cost())
            self._con_g_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_g_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_g_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_h_patients():
            self._con_h_patients_OS_costs.append(patient.get_OS_cost())
            self._con_h_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_h_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_h_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_i_patients():
            self._con_i_patients_OS_costs.append(patient.get_OS_cost())
            self._con_i_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_i_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_i_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_j_patients():
            self._con_j_patients_OS_costs.append(patient.get_OS_cost())
            self._con_j_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_j_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_j_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_k_patients():
            self._con_k_patients_OS_costs.append(patient.get_OS_cost())
            self._con_k_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_k_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_k_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_l_patients():
            self._con_l_patients_OS_costs.append(patient.get_OS_cost())
            self._con_l_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_l_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_l_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_m_patients():
            self._con_m_patients_OS_costs.append(patient.get_OS_cost())
            self._con_m_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_m_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_m_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_n_patients():
            self._con_n_patients_OS_costs.append(patient.get_OS_cost())
            self._con_n_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_n_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_n_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_o_patients():
            self._con_o_patients_OS_costs.append(patient.get_OS_cost())
            self._con_o_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_o_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_o_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_p_patients():
            self._con_p_patients_OS_costs.append(patient.get_OS_cost())
            self._con_p_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_p_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_p_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_q_patients():
            self._con_q_patients_OS_costs.append(patient.get_OS_cost())
            self._con_q_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_q_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_q_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_r_patients():
            self._con_r_patients_OS_costs.append(patient.get_OS_cost())
            self._con_r_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_r_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_r_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_s_patients():
            self._con_s_patients_OS_costs.append(patient.get_OS_cost())
            self._con_s_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_s_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_s_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_t_patients():
            self._con_t_patients_OS_costs.append(patient.get_OS_cost())
            self._con_t_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_t_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_t_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_u_patients():
            self._con_u_patients_OS_costs.append(patient.get_OS_cost())
            self._con_u_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_u_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_u_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_v_patients():
            self._con_v_patients_OS_costs.append(patient.get_OS_cost())
            self._con_v_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_v_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_v_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_w_patients():
            self._con_w_patients_OS_costs.append(patient.get_OS_cost())
            self._con_w_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_w_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_w_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_x_patients():
            self._con_x_patients_OS_costs.append(patient.get_OS_cost())
            self._con_x_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_x_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_x_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_y_patients():
            self._con_y_patients_OS_costs.append(patient.get_OS_cost())
            self._con_y_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_y_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_y_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_z_patients():
            self._con_z_patients_OS_costs.append(patient.get_OS_cost())
            self._con_z_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_z_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_z_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_aa_patients():
            self._con_aa_patients_OS_costs.append(patient.get_OS_cost())
            self._con_aa_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_aa_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_aa_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_bb_patients():
            self._con_bb_patients_OS_costs.append(patient.get_OS_cost())
            self._con_bb_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_bb_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_bb_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_cc_patients():
            self._con_cc_patients_OS_costs.append(patient.get_OS_cost())
            self._con_cc_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_cc_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_cc_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_dd_patients():
            self._con_dd_patients_OS_costs.append(patient.get_OS_cost())
            self._con_dd_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_dd_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_dd_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_ee_patients():
            self._con_ee_patients_OS_costs.append(patient.get_OS_cost())
            self._con_ee_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_ee_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_ee_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_ff_patients():
            self._con_ff_patients_OS_costs.append(patient.get_OS_cost())
            self._con_ff_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_ff_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_ff_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_gg_patients():
            self._con_gg_patients_OS_costs.append(patient.get_OS_cost())
            self._con_gg_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_gg_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_gg_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_hh_patients():
            self._con_hh_patients_OS_costs.append(patient.get_OS_cost())
            self._con_hh_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_hh_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_hh_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_ii_patients():
            self._con_ii_patients_OS_costs.append(patient.get_OS_cost())
            self._con_ii_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_ii_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_ii_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_jj_patients():
            self._con_jj_patients_OS_costs.append(patient.get_OS_cost())
            self._con_jj_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_jj_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_jj_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_kk_patients():
            self._con_kk_patients_OS_costs.append(patient.get_OS_cost())
            self._con_kk_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_kk_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_kk_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_ll_patients():
            self._con_ll_patients_OS_costs.append(patient.get_OS_cost())
            self._con_ll_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_ll_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_ll_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_mm_patients():
            self._con_mm_patients_OS_costs.append(patient.get_OS_cost())
            self._con_mm_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_mm_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_mm_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_nn_patients():
            self._con_nn_patients_OS_costs.append(patient.get_OS_cost())
            self._con_nn_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_nn_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_nn_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        # summary statistics
        self._sumStat_OS_cost = StatCls.SummaryStat('Expected Op Smile Cost', self._OS_costs)
        self._sumStat_NoOS_cost = StatCls.SummaryStat('Expected No Op Smile Cost', self._NoOS_costs)
        self._sumStat_OS_utility = StatCls.SummaryStat('Expected Op Smile utility', self._OS_utilities)
        self._sumStat_NoOS_utility = StatCls.SummaryStat('Expected No Op Smile utility', self._NoOS_utilities)

        # summary Statistics condition A
        self._sumStat_con_a_OS_cost = StatCls.SummaryStat("Condition A Op Smile Cost", self._con_a_patients_OS_costs)
        self._sumStat_con_a_NoOS_cost = StatCls.SummaryStat("Condition A No Op Smile Cost", self._con_a_patients_NoOS_costs)
        self._sumStat_con_a_OS_utilities = StatCls.SummaryStat("Condition A Op Smile Utilities", self._con_a_patients_OS_utilities)
        self._sumStat_con_a_NoOS_utilities = StatCls.SummaryStat("Condition A No Op Smile Utilities", self._con_a_patients_NoOS_utilities)

        # summary statistics condition B
        self._sumStat_con_b_OS_cost = StatCls.SummaryStat("Condition B Op Smile Cost", self._con_b_patients_OS_costs)
        self._sumStat_con_b_NoOS_cost = StatCls.SummaryStat("Condition B No Op Smile Cost",
                                                            self._con_b_patients_NoOS_costs)
        self._sumStat_con_b_OS_utilities = StatCls.SummaryStat("Condition B Op Smile Utilities",
                                                               self._con_b_patients_OS_utilities)
        self._sumStat_con_b_NoOS_utilities = StatCls.SummaryStat("Condition B No Op Smile Utilities",
                                                                 self._con_b_patients_NoOS_utilities)

        # summary statistics condition C
        self._sumStat_con_c_OS_cost = StatCls.SummaryStat("Condition C Op Smile Cost", self._con_c_patients_OS_costs)
        self._sumStat_con_c_NoOS_cost = StatCls.SummaryStat("Condition C No Op Smile Cost",
                                                            self._con_c_patients_NoOS_costs)
        self._sumStat_con_c_OS_utilities = StatCls.SummaryStat("Condition C Op Smile Utilities",
                                                               self._con_c_patients_OS_utilities)
        self._sumStat_con_c_NoOS_utilities = StatCls.SummaryStat("Condition C No Op Smile Utilities",
                                                                 self._con_c_patients_NoOS_utilities)
        # summary statistics condition D
        self._sumStat_con_d_OS_cost = StatCls.SummaryStat("Condition D Op Smile Cost", self._con_d_patients_OS_costs)
        self._sumStat_con_d_NoOS_cost = StatCls.SummaryStat("Condition D No Op Smile Cost",
                                                            self._con_d_patients_NoOS_costs)
        self._sumStat_con_d_OS_utilities = StatCls.SummaryStat("Condition D Op Smile Utilities",
                                                               self._con_d_patients_OS_utilities)
        self._sumStat_con_d_NoOS_utilities = StatCls.SummaryStat("Condition D No Op Smile Utilities",
                                                                 self._con_d_patients_NoOS_utilities)
        # summary statistics condition E
        self._sumStat_con_e_OS_cost = StatCls.SummaryStat("Condition E Op Smile Cost", self._con_e_patients_OS_costs)
        self._sumStat_con_e_NoOS_cost = StatCls.SummaryStat("Condition E No Op Smile Cost",
                                                            self._con_e_patients_NoOS_costs)
        self._sumStat_con_e_OS_utilities = StatCls.SummaryStat("Condition E Op Smile Utilities",
                                                               self._con_e_patients_OS_utilities)
        self._sumStat_con_e_NoOS_utilities = StatCls.SummaryStat("Condition E No Op Smile Utilities",
                                                                 self._con_e_patients_NoOS_utilities)
        # summary statistics condition F
        self._sumStat_con_f_OS_cost = StatCls.SummaryStat("Condition F Op Smile Cost", self._con_f_patients_OS_costs)
        self._sumStat_con_f_NoOS_cost = StatCls.SummaryStat("Condition F No Op Smile Cost",
                                                            self._con_f_patients_NoOS_costs)
        self._sumStat_con_f_OS_utilities = StatCls.SummaryStat("Condition F Op Smile Utilities",
                                                               self._con_f_patients_OS_utilities)
        self._sumStat_con_f_NoOS_utilities = StatCls.SummaryStat("Condition F No Op Smile Utilities",
                                                                 self._con_f_patients_NoOS_utilities)
        # summary statistics condition G
        self._sumStat_con_g_OS_cost = StatCls.SummaryStat("Condition G Op Smile Cost", self._con_g_patients_OS_costs)
        self._sumStat_con_g_NoOS_cost = StatCls.SummaryStat("Condition G No Op Smile Cost",
                                                            self._con_g_patients_NoOS_costs)
        self._sumStat_con_g_OS_utilities = StatCls.SummaryStat("Condition G Op Smile Utilities",
                                                               self._con_g_patients_OS_utilities)
        self._sumStat_con_g_NoOS_utilities = StatCls.SummaryStat("Condition G No Op Smile Utilities",
                                                                 self._con_g_patients_NoOS_utilities)
        # summary statistics condition H
        self._sumStat_con_h_OS_cost = StatCls.SummaryStat("Condition H Op Smile Cost", self._con_h_patients_OS_costs)
        self._sumStat_con_h_NoOS_cost = StatCls.SummaryStat("Condition H No Op Smile Cost",
                                                            self._con_h_patients_NoOS_costs)
        self._sumStat_con_h_OS_utilities = StatCls.SummaryStat("Condition H Op Smile Utilities",
                                                               self._con_h_patients_OS_utilities)
        self._sumStat_con_h_NoOS_utilities = StatCls.SummaryStat("Condition H No Op Smile Utilities",
                                                                 self._con_h_patients_NoOS_utilities)
        # summary statistics condition I
        self._sumStat_con_i_OS_cost = StatCls.SummaryStat("Condition I Op Smile Cost", self._con_i_patients_OS_costs)
        self._sumStat_con_i_NoOS_cost = StatCls.SummaryStat("Condition I No Op Smile Cost",
                                                            self._con_i_patients_NoOS_costs)
        self._sumStat_con_i_OS_utilities = StatCls.SummaryStat("Condition I Op Smile Utilities",
                                                               self._con_i_patients_OS_utilities)
        self._sumStat_con_i_NoOS_utilities = StatCls.SummaryStat("Condition I No Op Smile Utilities",
                                                                 self._con_i_patients_NoOS_utilities)
        # summary statistics condition J
        self._sumStat_con_j_OS_cost = StatCls.SummaryStat("Condition J Op Smile Cost", self._con_j_patients_OS_costs)
        self._sumStat_con_j_NoOS_cost = StatCls.SummaryStat("Condition J No Op Smile Cost",
                                                            self._con_j_patients_NoOS_costs)
        self._sumStat_con_j_OS_utilities = StatCls.SummaryStat("Condition J Op Smile Utilities",
                                                               self._con_j_patients_OS_utilities)
        self._sumStat_con_j_NoOS_utilities = StatCls.SummaryStat("Condition J No Op Smile Utilities",
                                                                 self._con_j_patients_NoOS_utilities)
        # summary statistics condition K
        self._sumStat_con_k_OS_cost = StatCls.SummaryStat("Condition K Op Smile Cost", self._con_k_patients_OS_costs)
        self._sumStat_con_k_NoOS_cost = StatCls.SummaryStat("Condition K No Op Smile Cost",
                                                            self._con_k_patients_NoOS_costs)
        self._sumStat_con_k_OS_utilities = StatCls.SummaryStat("Condition K Op Smile Utilities",
                                                               self._con_k_patients_OS_utilities)
        self._sumStat_con_k_NoOS_utilities = StatCls.SummaryStat("Condition K No Op Smile Utilities",
                                                                 self._con_k_patients_NoOS_utilities)
        # summary statistics condition L
        self._sumStat_con_l_OS_cost = StatCls.SummaryStat("Condition L Op Smile Cost", self._con_l_patients_OS_costs)
        self._sumStat_con_l_NoOS_cost = StatCls.SummaryStat("Condition L No Op Smile Cost",
                                                            self._con_l_patients_NoOS_costs)
        self._sumStat_con_l_OS_utilities = StatCls.SummaryStat("Condition L Op Smile Utilities",
                                                               self._con_l_patients_OS_utilities)
        self._sumStat_con_l_NoOS_utilities = StatCls.SummaryStat("Condition L No Op Smile Utilities",
                                                                 self._con_l_patients_NoOS_utilities)
        # summary statistics condition M
        self._sumStat_con_m_OS_cost = StatCls.SummaryStat("Condition M Op Smile Cost", self._con_m_patients_OS_costs)
        self._sumStat_con_m_NoOS_cost = StatCls.SummaryStat("Condition M No Op Smile Cost",
                                                            self._con_m_patients_NoOS_costs)
        self._sumStat_con_m_OS_utilities = StatCls.SummaryStat("Condition M Op Smile Utilities",
                                                               self._con_m_patients_OS_utilities)
        self._sumStat_con_m_NoOS_utilities = StatCls.SummaryStat("Condition M No Op Smile Utilities",
                                                                 self._con_m_patients_NoOS_utilities)
        # summary statistics condition N
        self._sumStat_con_n_OS_cost = StatCls.SummaryStat("Condition N Op Smile Cost", self._con_n_patients_OS_costs)
        self._sumStat_con_n_NoOS_cost = StatCls.SummaryStat("Condition N No Op Smile Cost",
                                                            self._con_n_patients_NoOS_costs)
        self._sumStat_con_n_OS_utilities = StatCls.SummaryStat("Condition N Op Smile Utilities",
                                                               self._con_n_patients_OS_utilities)
        self._sumStat_con_n_NoOS_utilities = StatCls.SummaryStat("Condition N No Op Smile Utilities",
                                                                 self._con_n_patients_NoOS_utilities)
        # summary statistics condition O
        self._sumStat_con_o_OS_cost = StatCls.SummaryStat("Condition O Op Smile Cost", self._con_o_patients_OS_costs)
        self._sumStat_con_o_NoOS_cost = StatCls.SummaryStat("Condition O No Op Smile Cost",
                                                            self._con_o_patients_NoOS_costs)
        self._sumStat_con_o_OS_utilities = StatCls.SummaryStat("Condition O Op Smile Utilities",
                                                               self._con_o_patients_OS_utilities)
        self._sumStat_con_o_NoOS_utilities = StatCls.SummaryStat("Condition O No Op Smile Utilities",
                                                                 self._con_o_patients_NoOS_utilities)
        # summary statistics condition P
        self._sumStat_con_p_OS_cost = StatCls.SummaryStat("Condition P Op Smile Cost", self._con_p_patients_OS_costs)
        self._sumStat_con_p_NoOS_cost = StatCls.SummaryStat("Condition P No Op Smile Cost",
                                                            self._con_p_patients_NoOS_costs)
        self._sumStat_con_p_OS_utilities = StatCls.SummaryStat("Condition P Op Smile Utilities",
                                                               self._con_p_patients_OS_utilities)
        self._sumStat_con_p_NoOS_utilities = StatCls.SummaryStat("Condition P No Op Smile Utilities",
                                                                 self._con_p_patients_NoOS_utilities)
        # summary statistics condition Q
        self._sumStat_con_q_OS_cost = StatCls.SummaryStat("Condition Q Op Smile Cost", self._con_q_patients_OS_costs)
        self._sumStat_con_q_NoOS_cost = StatCls.SummaryStat("Condition Q No Op Smile Cost",
                                                            self._con_q_patients_NoOS_costs)
        self._sumStat_con_q_OS_utilities = StatCls.SummaryStat("Condition Q Op Smile Utilities",
                                                               self._con_q_patients_OS_utilities)
        self._sumStat_con_q_NoOS_utilities = StatCls.SummaryStat("Condition Q No Op Smile Utilities",
                                                                 self._con_q_patients_NoOS_utilities)
        # summary statistics condition R
        self._sumStat_con_r_OS_cost = StatCls.SummaryStat("Condition R Op Smile Cost", self._con_r_patients_OS_costs)
        self._sumStat_con_r_NoOS_cost = StatCls.SummaryStat("Condition R No Op Smile Cost",
                                                            self._con_r_patients_NoOS_costs)
        self._sumStat_con_r_OS_utilities = StatCls.SummaryStat("Condition R Op Smile Utilities",
                                                               self._con_r_patients_OS_utilities)
        self._sumStat_con_r_NoOS_utilities = StatCls.SummaryStat("Condition R No Op Smile Utilities",
                                                                 self._con_r_patients_NoOS_utilities)
        # summary statistics condition S
        self._sumStat_con_s_OS_cost = StatCls.SummaryStat("Condition S Op Smile Cost", self._con_s_patients_OS_costs)
        self._sumStat_con_s_NoOS_cost = StatCls.SummaryStat("Condition S No Op Smile Cost",
                                                            self._con_s_patients_NoOS_costs)
        self._sumStat_con_s_OS_utilities = StatCls.SummaryStat("Condition S Op Smile Utilities",
                                                               self._con_s_patients_OS_utilities)
        self._sumStat_con_s_NoOS_utilities = StatCls.SummaryStat("Condition S No Op Smile Utilities",
                                                                 self._con_s_patients_NoOS_utilities)
        # summary statistics condition T
        self._sumStat_con_t_OS_cost = StatCls.SummaryStat("Condition T Op Smile Cost", self._con_t_patients_OS_costs)
        self._sumStat_con_t_NoOS_cost = StatCls.SummaryStat("Condition T No Op Smile Cost",
                                                            self._con_t_patients_NoOS_costs)
        self._sumStat_con_t_OS_utilities = StatCls.SummaryStat("Condition T Op Smile Utilities",
                                                               self._con_t_patients_OS_utilities)
        self._sumStat_con_t_NoOS_utilities = StatCls.SummaryStat("Condition T No Op Smile Utilities",
                                                                 self._con_t_patients_NoOS_utilities)
        # summary statistics condition U
        self._sumStat_con_u_OS_cost = StatCls.SummaryStat("Condition U Op Smile Cost", self._con_u_patients_OS_costs)
        self._sumStat_con_u_NoOS_cost = StatCls.SummaryStat("Condition U No Op Smile Cost",
                                                            self._con_u_patients_NoOS_costs)
        self._sumStat_con_u_OS_utilities = StatCls.SummaryStat("Condition U Op Smile Utilities",
                                                               self._con_u_patients_OS_utilities)
        self._sumStat_con_u_NoOS_utilities = StatCls.SummaryStat("Condition U No Op Smile Utilities",
                                                                 self._con_u_patients_NoOS_utilities)

        # summary statistics condition v
        self._sumStat_con_v_OS_cost = StatCls.SummaryStat("Condition v Op Smile Cost", self._con_v_patients_OS_costs)
        self._sumStat_con_v_NoOS_cost = StatCls.SummaryStat("Condition v No Op Smile Cost",
                                                            self._con_v_patients_NoOS_costs)
        self._sumStat_con_v_OS_utilities = StatCls.SummaryStat("Condition v Op Smile Utilities",
                                                               self._con_v_patients_OS_utilities)
        self._sumStat_con_v_NoOS_utilities = StatCls.SummaryStat("Condition v No Op Smile Utilities",
                                                                 self._con_v_patients_NoOS_utilities)

        # summary statistics condition w
        self._sumStat_con_w_OS_cost = StatCls.SummaryStat("Condition w Op Smile Cost", self._con_w_patients_OS_costs)
        self._sumStat_con_w_NoOS_cost = StatCls.SummaryStat("Condition w No Op Smile Cost",
                                                            self._con_w_patients_NoOS_costs)
        self._sumStat_con_w_OS_utilities = StatCls.SummaryStat("Condition w Op Smile Utilities",
                                                               self._con_w_patients_OS_utilities)
        self._sumStat_con_w_NoOS_utilities = StatCls.SummaryStat("Condition w No Op Smile Utilities",
                                                                 self._con_w_patients_NoOS_utilities)

        # summary statistics condition x
        self._sumStat_con_x_OS_cost = StatCls.SummaryStat("Condition x Op Smile Cost", self._con_x_patients_OS_costs)
        self._sumStat_con_x_NoOS_cost = StatCls.SummaryStat("Condition x No Op Smile Cost",
                                                            self._con_x_patients_NoOS_costs)
        self._sumStat_con_x_OS_utilities = StatCls.SummaryStat("Condition x Op Smile Utilities",
                                                               self._con_x_patients_OS_utilities)
        self._sumStat_con_x_NoOS_utilities = StatCls.SummaryStat("Condition x No Op Smile Utilities",
                                                                 self._con_x_patients_NoOS_utilities)

        # summary statistics condition y
        self._sumStat_con_y_OS_cost = StatCls.SummaryStat("Condition y Op Smile Cost", self._con_y_patients_OS_costs)
        self._sumStat_con_y_NoOS_cost = StatCls.SummaryStat("Condition y No Op Smile Cost",
                                                            self._con_y_patients_NoOS_costs)
        self._sumStat_con_y_OS_utilities = StatCls.SummaryStat("Condition y Op Smile Utilities",
                                                               self._con_y_patients_OS_utilities)
        self._sumStat_con_y_NoOS_utilities = StatCls.SummaryStat("Condition y No Op Smile Utilities",
                                                                 self._con_y_patients_NoOS_utilities)

        # summary statistics condition z
        self._sumStat_con_z_OS_cost = StatCls.SummaryStat("Condition z Op Smile Cost", self._con_z_patients_OS_costs)
        self._sumStat_con_z_NoOS_cost = StatCls.SummaryStat("Condition z No Op Smile Cost",
                                                            self._con_z_patients_NoOS_costs)
        self._sumStat_con_z_OS_utilities = StatCls.SummaryStat("Condition z Op Smile Utilities",
                                                               self._con_z_patients_OS_utilities)
        self._sumStat_con_z_NoOS_utilities = StatCls.SummaryStat("Condition z No Op Smile Utilities",
                                                                 self._con_z_patients_NoOS_utilities)

        # summary statistics condition aa
        self._sumStat_con_aa_OS_cost = StatCls.SummaryStat("Condition aa Op Smile Cost", self._con_aa_patients_OS_costs)
        self._sumStat_con_aa_NoOS_cost = StatCls.SummaryStat("Condition aa No Op Smile Cost",
                                                            self._con_aa_patients_NoOS_costs)
        self._sumStat_con_aa_OS_utilities = StatCls.SummaryStat("Condition aa Op Smile Utilities",
                                                               self._con_aa_patients_OS_utilities)
        self._sumStat_con_aa_NoOS_utilities = StatCls.SummaryStat("Condition aa No Op Smile Utilities",
                                                                 self._con_aa_patients_NoOS_utilities)

        # summary statistics condition bb
        self._sumStat_con_bb_OS_cost = StatCls.SummaryStat("Condition bb Op Smile Cost", self._con_bb_patients_OS_costs)
        self._sumStat_con_bb_NoOS_cost = StatCls.SummaryStat("Condition bb No Op Smile Cost",
                                                            self._con_bb_patients_NoOS_costs)
        self._sumStat_con_bb_OS_utilities = StatCls.SummaryStat("Condition bb Op Smile Utilities",
                                                               self._con_bb_patients_OS_utilities)
        self._sumStat_con_bb_NoOS_utilities = StatCls.SummaryStat("Condition bb No Op Smile Utilities",
                                                                 self._con_bb_patients_NoOS_utilities)

        # summary statistics condition cc
        self._sumStat_con_cc_OS_cost = StatCls.SummaryStat("Condition cc Op Smile Cost", self._con_cc_patients_OS_costs)
        self._sumStat_con_cc_NoOS_cost = StatCls.SummaryStat("Condition cc No Op Smile Cost",
                                                            self._con_cc_patients_NoOS_costs)
        self._sumStat_con_cc_OS_utilities = StatCls.SummaryStat("Condition cc Op Smile Utilities",
                                                               self._con_cc_patients_OS_utilities)
        self._sumStat_con_cc_NoOS_utilities = StatCls.SummaryStat("Condition cc No Op Smile Utilities",
                                                                 self._con_cc_patients_NoOS_utilities)

        # summary statistics condition dd
        self._sumStat_con_dd_OS_cost = StatCls.SummaryStat("Condition dd Op Smile Cost", self._con_dd_patients_OS_costs)
        self._sumStat_con_dd_NoOS_cost = StatCls.SummaryStat("Condition dd No Op Smile Cost",
                                                            self._con_dd_patients_NoOS_costs)
        self._sumStat_con_dd_OS_utilities = StatCls.SummaryStat("Condition dd Op Smile Utilities",
                                                               self._con_dd_patients_OS_utilities)
        self._sumStat_con_dd_NoOS_utilities = StatCls.SummaryStat("Condition dd No Op Smile Utilities",
                                                                 self._con_dd_patients_NoOS_utilities)

        # summary statistics condition ee
        self._sumStat_con_ee_OS_cost = StatCls.SummaryStat("Condition ee Op Smile Cost", self._con_ee_patients_OS_costs)
        self._sumStat_con_ee_NoOS_cost = StatCls.SummaryStat("Condition ee No Op Smile Cost",
                                                            self._con_ee_patients_NoOS_costs)
        self._sumStat_con_ee_OS_utilities = StatCls.SummaryStat("Condition ee Op Smile Utilities",
                                                               self._con_ee_patients_OS_utilities)
        self._sumStat_con_ee_NoOS_utilities = StatCls.SummaryStat("Condition ee No Op Smile Utilities",
                                                                 self._con_ee_patients_NoOS_utilities)

        # summary statistics condition ff
        self._sumStat_con_ff_OS_cost = StatCls.SummaryStat("Condition ff Op Smile Cost", self._con_ff_patients_OS_costs)
        self._sumStat_con_ff_NoOS_cost = StatCls.SummaryStat("Condition ff No Op Smile Cost",
                                                            self._con_ff_patients_NoOS_costs)
        self._sumStat_con_ff_OS_utilities = StatCls.SummaryStat("Condition ff Op Smile Utilities",
                                                               self._con_ff_patients_OS_utilities)
        self._sumStat_con_ff_NoOS_utilities = StatCls.SummaryStat("Condition ff No Op Smile Utilities",
                                                                 self._con_ff_patients_NoOS_utilities)

        # summary statistics condition gg
        self._sumStat_con_gg_OS_cost = StatCls.SummaryStat("Condition gg Op Smile Cost", self._con_gg_patients_OS_costs)
        self._sumStat_con_gg_NoOS_cost = StatCls.SummaryStat("Condition gg No Op Smile Cost",
                                                            self._con_gg_patients_NoOS_costs)
        self._sumStat_con_gg_OS_utilities = StatCls.SummaryStat("Condition gg Op Smile Utilities",
                                                               self._con_gg_patients_OS_utilities)
        self._sumStat_con_gg_NoOS_utilities = StatCls.SummaryStat("Condition gg No Op Smile Utilities",
                                                                 self._con_gg_patients_NoOS_utilities)

        # summary statistics condition hh
        self._sumStat_con_hh_OS_cost = StatCls.SummaryStat("Condition hh Op Smile Cost", self._con_hh_patients_OS_costs)
        self._sumStat_con_hh_NoOS_cost = StatCls.SummaryStat("Condition hh No Op Smile Cost",
                                                            self._con_hh_patients_NoOS_costs)
        self._sumStat_con_hh_OS_utilities = StatCls.SummaryStat("Condition hh Op Smile Utilities",
                                                               self._con_hh_patients_OS_utilities)
        self._sumStat_con_hh_NoOS_utilities = StatCls.SummaryStat("Condition h No Op Smile Utilities",
                                                                 self._con_hh_patients_NoOS_utilities)

        # summary statistics condition ii
        self._sumStat_con_ii_OS_cost = StatCls.SummaryStat("Condition ii Op Smile Cost", self._con_ii_patients_OS_costs)
        self._sumStat_con_ii_NoOS_cost = StatCls.SummaryStat("Condition ii No Op Smile Cost",
                                                            self._con_ii_patients_NoOS_costs)
        self._sumStat_con_ii_OS_utilities = StatCls.SummaryStat("Condition ii Op Smile Utilities",
                                                               self._con_ii_patients_OS_utilities)
        self._sumStat_con_ii_NoOS_utilities = StatCls.SummaryStat("Condition ii No Op Smile Utilities",
                                                                 self._con_ii_patients_NoOS_utilities)

        # summary statistics condition jj
        self._sumStat_con_jj_OS_cost = StatCls.SummaryStat("Condition jj Op Smile Cost", self._con_jj_patients_OS_costs)
        self._sumStat_con_jj_NoOS_cost = StatCls.SummaryStat("Condition jj No Op Smile Cost",
                                                            self._con_jj_patients_NoOS_costs)
        self._sumStat_con_jj_OS_utilities = StatCls.SummaryStat("Condition jj Op Smile Utilities",
                                                               self._con_jj_patients_OS_utilities)
        self._sumStat_con_jj_NoOS_utilities = StatCls.SummaryStat("Condition jj No Op Smile Utilities",
                                                                 self._con_jj_patients_NoOS_utilities)

        # summary statistics condition kk
        self._sumStat_con_kk_OS_cost = StatCls.SummaryStat("Condition kk Op Smile Cost", self._con_kk_patients_OS_costs)
        self._sumStat_con_kk_NoOS_cost = StatCls.SummaryStat("Condition kk No Op Smile Cost",
                                                            self._con_kk_patients_NoOS_costs)
        self._sumStat_con_kk_OS_utilities = StatCls.SummaryStat("Condition kk Op Smile Utilities",
                                                               self._con_kk_patients_OS_utilities)
        self._sumStat_con_kk_NoOS_utilities = StatCls.SummaryStat("Condition kk No Op Smile Utilities",
                                                                 self._con_kk_patients_NoOS_utilities)

        # summary statistics condition ll
        self._sumStat_con_ll_OS_cost = StatCls.SummaryStat("Condition ll Op Smile Cost", self._con_ll_patients_OS_costs)
        self._sumStat_con_ll_NoOS_cost = StatCls.SummaryStat("Condition ll No Op Smile Cost",
                                                            self._con_ll_patients_NoOS_costs)
        self._sumStat_con_ll_OS_utilities = StatCls.SummaryStat("Condition ll Op Smile Utilities",
                                                               self._con_ll_patients_OS_utilities)
        self._sumStat_con_ll_NoOS_utilities = StatCls.SummaryStat("Condition ll No Op Smile Utilities",
                                                                 self._con_ll_patients_NoOS_utilities)

        # summary statistics condition mm
        self._sumStat_con_mm_OS_cost = StatCls.SummaryStat("Condition mm Op Smile Cost", self._con_mm_patients_OS_costs)
        self._sumStat_con_mm_NoOS_cost = StatCls.SummaryStat("Condition mm No Op Smile Cost",
                                                            self._con_mm_patients_NoOS_costs)
        self._sumStat_con_mm_OS_utilities = StatCls.SummaryStat("Condition mm Op Smile Utilities",
                                                               self._con_mm_patients_OS_utilities)
        self._sumStat_con_mm_NoOS_utilities = StatCls.SummaryStat("Condition mm No Op Smile Utilities",
                                                                 self._con_mm_patients_NoOS_utilities)

        # summary statistics condition U
        self._sumStat_con_nn_OS_cost = StatCls.SummaryStat("Condition nn Op Smile Cost", self._con_nn_patients_OS_costs)
        self._sumStat_con_nn_NoOS_cost = StatCls.SummaryStat("Condition nn No Op Smile Cost",
                                                            self._con_nn_patients_NoOS_costs)
        self._sumStat_con_nn_OS_utilities = StatCls.SummaryStat("Condition nn Op Smile Utilities",
                                                               self._con_nn_patients_OS_utilities)
        self._sumStat_con_nn_NoOS_utilities = StatCls.SummaryStat("Condition nn No Op Smile Utilities",
                                                                 self._con_nn_patients_NoOS_utilities)

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

# condition A
    def get_sumStat_con_a_OS_cost(self):
        return self._sumStat_con_a_OS_cost

    def get_sumStat_con_a_NoOS_cost(self):
        return self._sumStat_con_a_NoOS_cost

    def get_sumStat_con_a_OS_utilities(self):
        return self._sumStat_con_a_OS_utilities

    def get_sumStat_con_a_NoOS_utilities(self):
        return self._sumStat_con_a_NoOS_utilities

# condition B
    def get_sumStat_con_b_OS_cost(self):
        return self._sumStat_con_b_OS_cost

    def get_sumStat_con_b_NoOS_cost(self):
        return self._sumStat_con_b_NoOS_cost

    def get_sumStat_con_b_OS_utilities(self):
        return self._sumStat_con_b_OS_utilities

    def get_sumStat_con_b_NoOS_utilities(self):
        return self._sumStat_con_b_NoOS_utilities

# condition C
    def get_sumStat_con_c_OS_cost(self):
        return self._sumStat_con_c_OS_cost

    def get_sumStat_con_c_NoOS_cost(self):
        return self._sumStat_con_c_NoOS_cost

    def get_sumStat_con_c_OS_utilities(self):
        return self._sumStat_con_c_OS_utilities

    def get_sumStat_con_c_NoOS_utilities(self):
        return self._sumStat_con_c_NoOS_utilities

# condition D
    def get_sumStat_con_d_OS_cost(self):
        return self._sumStat_con_d_OS_cost

    def get_sumStat_con_d_NoOS_cost(self):
        return self._sumStat_con_d_NoOS_cost

    def get_sumStat_con_d_OS_utilities(self):
        return self._sumStat_con_d_OS_utilities

    def get_sumStat_con_d_NoOS_utilities(self):
        return self._sumStat_con_d_NoOS_utilities

# condition E
    def get_sumStat_con_e_OS_cost(self):
        return self._sumStat_con_e_OS_cost

    def get_sumStat_con_e_NoOS_cost(self):
        return self._sumStat_con_e_NoOS_cost

    def get_sumStat_con_e_OS_utilities(self):
        return self._sumStat_con_e_OS_utilities

    def get_sumStat_con_e_NoOS_utilities(self):
        return self._sumStat_con_e_NoOS_utilities

# condition F
    def get_sumStat_con_f_OS_cost(self):
        return self._sumStat_con_f_OS_cost

    def get_sumStat_con_f_NoOS_cost(self):
        return self._sumStat_con_f_NoOS_cost

    def get_sumStat_con_f_OS_utilities(self):
        return self._sumStat_con_f_OS_utilities

    def get_sumStat_con_f_NoOS_utilities(self):
        return self._sumStat_con_f_NoOS_utilities

# condition G
    def get_sumStat_con_g_OS_cost(self):
        return self._sumStat_con_g_OS_cost

    def get_sumStat_con_g_NoOS_cost(self):
        return self._sumStat_con_g_NoOS_cost

    def get_sumStat_con_g_OS_utilities(self):
        return self._sumStat_con_g_OS_utilities

    def get_sumStat_con_g_NoOS_utilities(self):
        return self._sumStat_con_g_NoOS_utilities

# condition H
    def get_sumStat_con_h_OS_cost(self):
        return self._sumStat_con_h_OS_cost

    def get_sumStat_con_h_NoOS_cost(self):
        return self._sumStat_con_h_NoOS_cost

    def get_sumStat_con_h_OS_utilities(self):
        return self._sumStat_con_h_OS_utilities

    def get_sumStat_con_h_NoOS_utilities(self):
        return self._sumStat_con_h_NoOS_utilities

# condition I
    def get_sumStat_con_i_OS_cost(self):
        return self._sumStat_con_i_OS_cost

    def get_sumStat_con_i_NoOS_cost(self):
        return self._sumStat_con_i_NoOS_cost

    def get_sumStat_con_i_OS_utilities(self):
        return self._sumStat_con_i_OS_utilities

    def get_sumStat_con_i_NoOS_utilities(self):
        return self._sumStat_con_i_NoOS_utilities

# condition J
    def get_sumStat_con_j_OS_cost(self):
        return self._sumStat_con_j_OS_cost

    def get_sumStat_con_j_NoOS_cost(self):
        return self._sumStat_con_j_NoOS_cost

    def get_sumStat_con_j_OS_utilities(self):
        return self._sumStat_con_j_OS_utilities

    def get_sumStat_con_j_NoOS_utilities(self):
        return self._sumStat_con_j_NoOS_utilities

# condition K
    def get_sumStat_con_k_OS_cost(self):
        return self._sumStat_con_k_OS_cost

    def get_sumStat_con_k_NoOS_cost(self):
        return self._sumStat_con_k_NoOS_cost

    def get_sumStat_con_k_OS_utilities(self):
        return self._sumStat_con_k_OS_utilities

    def get_sumStat_con_k_NoOS_utilities(self):
        return self._sumStat_con_k_NoOS_utilities

# condition L
    def get_sumStat_con_l_OS_cost(self):
        return self._sumStat_con_l_OS_cost

    def get_sumStat_con_l_NoOS_cost(self):
        return self._sumStat_con_l_NoOS_cost

    def get_sumStat_con_l_OS_utilities(self):
        return self._sumStat_con_l_OS_utilities

    def get_sumStat_con_l_NoOS_utilities(self):
        return self._sumStat_con_l_NoOS_utilities

# condition M
    def get_sumStat_con_m_OS_cost(self):
        return self._sumStat_con_m_OS_cost

    def get_sumStat_con_m_NoOS_cost(self):
        return self._sumStat_con_m_NoOS_cost

    def get_sumStat_con_m_OS_utilities(self):
        return self._sumStat_con_m_OS_utilities

    def get_sumStat_con_m_NoOS_utilities(self):
        return self._sumStat_con_m_NoOS_utilities

# condition N
    def get_sumStat_con_n_OS_cost(self):
        return self._sumStat_con_n_OS_cost

    def get_sumStat_con_n_NoOS_cost(self):
        return self._sumStat_con_n_NoOS_cost

    def get_sumStat_con_n_OS_utilities(self):
        return self._sumStat_con_n_OS_utilities

    def get_sumStat_con_n_NoOS_utilities(self):
        return self._sumStat_con_n_NoOS_utilities

# condition O
    def get_sumStat_con_o_OS_cost(self):
        return self._sumStat_con_o_OS_cost

    def get_sumStat_con_o_NoOS_cost(self):
        return self._sumStat_con_o_NoOS_cost

    def get_sumStat_con_o_OS_utilities(self):
        return self._sumStat_con_o_OS_utilities

    def get_sumStat_con_o_NoOS_utilities(self):
        return self._sumStat_con_o_NoOS_utilities

# condition P
    def get_sumStat_con_p_OS_cost(self):
        return self._sumStat_con_p_OS_cost

    def get_sumStat_con_p_NoOS_cost(self):
        return self._sumStat_con_p_NoOS_cost

    def get_sumStat_con_p_OS_utilities(self):
        return self._sumStat_con_p_OS_utilities

    def get_sumStat_con_p_NoOS_utilities(self):
        return self._sumStat_con_p_NoOS_utilities

# condition Q
    def get_sumStat_con_q_OS_cost(self):
        return self._sumStat_con_q_OS_cost

    def get_sumStat_con_q_NoOS_cost(self):
        return self._sumStat_con_q_NoOS_cost

    def get_sumStat_con_q_OS_utilities(self):
        return self._sumStat_con_q_OS_utilities

    def get_sumStat_con_q_NoOS_utilities(self):
        return self._sumStat_con_q_NoOS_utilities

# condition R
    def get_sumStat_con_r_OS_cost(self):
        return self._sumStat_con_r_OS_cost

    def get_sumStat_con_r_NoOS_cost(self):
        return self._sumStat_con_r_NoOS_cost

    def get_sumStat_con_r_OS_utilities(self):
        return self._sumStat_con_r_OS_utilities

    def get_sumStat_con_r_NoOS_utilities(self):
        return self._sumStat_con_r_NoOS_utilities

# condition S
    def get_sumStat_con_s_OS_cost(self):
        return self._sumStat_con_s_OS_cost

    def get_sumStat_con_s_NoOS_cost(self):
        return self._sumStat_con_s_NoOS_cost

    def get_sumStat_con_s_OS_utilities(self):
        return self._sumStat_con_s_OS_utilities

    def get_sumStat_con_s_NoOS_utilities(self):
        return self._sumStat_con_s_NoOS_utilities

# condition T
    def get_sumStat_con_t_OS_cost(self):
        return self._sumStat_con_t_OS_cost

    def get_sumStat_con_t_NoOS_cost(self):
        return self._sumStat_con_t_NoOS_cost

    def get_sumStat_con_t_OS_utilities(self):
        return self._sumStat_con_t_OS_utilities

    def get_sumStat_con_t_NoOS_utilities(self):
        return self._sumStat_con_t_NoOS_utilities

# condition U
    def get_sumStat_con_u_OS_cost(self):
        return self._sumStat_con_u_OS_cost

    def get_sumStat_con_u_NoOS_cost(self):
        return self._sumStat_con_u_NoOS_cost

    def get_sumStat_con_u_OS_utilities(self):
        return self._sumStat_con_u_OS_utilities

    def get_sumStat_con_u_NoOS_utilities(self):
        return self._sumStat_con_u_NoOS_utilities

# condition v
    def get_sumStat_con_v_OS_cost(self):
        return self._sumStat_con_v_OS_cost

    def get_sumStat_con_v_NoOS_cost(self):
        return self._sumStat_con_v_NoOS_cost

    def get_sumStat_con_v_OS_utilities(self):
        return self._sumStat_con_v_OS_utilities

    def get_sumStat_con_v_NoOS_utilities(self):
        return self._sumStat_con_v_NoOS_utilities

# condition w
    def get_sumStat_con_w_OS_cost(self):
        return self._sumStat_con_w_OS_cost

    def get_sumStat_con_w_NoOS_cost(self):
        return self._sumStat_con_w_NoOS_cost

    def get_sumStat_con_w_OS_utilities(self):
        return self._sumStat_con_w_OS_utilities

    def get_sumStat_con_w_NoOS_utilities(self):
        return self._sumStat_con_w_NoOS_utilities

# condition x
    def get_sumStat_con_x_OS_cost(self):
        return self._sumStat_con_x_OS_cost

    def get_sumStat_con_x_NoOS_cost(self):
        return self._sumStat_con_x_NoOS_cost

    def get_sumStat_con_x_OS_utilities(self):
        return self._sumStat_con_x_OS_utilities

    def get_sumStat_con_x_NoOS_utilities(self):
        return self._sumStat_con_x_NoOS_utilities

# condition y
    def get_sumStat_con_y_OS_cost(self):
        return self._sumStat_con_y_OS_cost

    def get_sumStat_con_y_NoOS_cost(self):
        return self._sumStat_con_y_NoOS_cost

    def get_sumStat_con_y_OS_utilities(self):
        return self._sumStat_con_y_OS_utilities

    def get_sumStat_con_y_NoOS_utilities(self):
        return self._sumStat_con_y_NoOS_utilities

# condition z
    def get_sumStat_con_z_OS_cost(self):
        return self._sumStat_con_z_OS_cost

    def get_sumStat_con_z_NoOS_cost(self):
        return self._sumStat_con_z_NoOS_cost

    def get_sumStat_con_z_OS_utilities(self):
        return self._sumStat_con_z_OS_utilities

    def get_sumStat_con_z_NoOS_utilities(self):
        return self._sumStat_con_z_NoOS_utilities

# condition aa
    def get_sumStat_con_aa_OS_cost(self):
        return self._sumStat_con_aa_OS_cost

    def get_sumStat_con_aa_NoOS_cost(self):
        return self._sumStat_con_aa_NoOS_cost

    def get_sumStat_con_aa_OS_utilities(self):
        return self._sumStat_con_aa_OS_utilities

    def get_sumStat_con_aa_NoOS_utilities(self):
        return self._sumStat_con_aa_NoOS_utilities

# condition bb
    def get_sumStat_con_bb_OS_cost(self):
        return self._sumStat_con_bb_OS_cost

    def get_sumStat_con_bb_NoOS_cost(self):
        return self._sumStat_con_bb_NoOS_cost

    def get_sumStat_con_bb_OS_utilities(self):
        return self._sumStat_con_bb_OS_utilities

    def get_sumStat_con_bb_NoOS_utilities(self):
        return self._sumStat_con_bb_NoOS_utilities

# condition cc
    def get_sumStat_con_cc_OS_cost(self):
        return self._sumStat_con_cc_OS_cost

    def get_sumStat_con_cc_NoOS_cost(self):
        return self._sumStat_con_cc_NoOS_cost

    def get_sumStat_con_cc_OS_utilities(self):
        return self._sumStat_con_cc_OS_utilities

    def get_sumStat_con_cc_NoOS_utilities(self):
        return self._sumStat_con_cc_NoOS_utilities

# condition dd
    def get_sumStat_con_dd_OS_cost(self):
        return self._sumStat_con_dd_OS_cost

    def get_sumStat_con_dd_NoOS_cost(self):
        return self._sumStat_con_dd_NoOS_cost

    def get_sumStat_con_dd_OS_utilities(self):
        return self._sumStat_con_dd_OS_utilities

    def get_sumStat_con_dd_NoOS_utilities(self):
        return self._sumStat_con_dd_NoOS_utilities

# condition ee
    def get_sumStat_con_ee_OS_cost(self):
        return self._sumStat_con_ee_OS_cost

    def get_sumStat_con_ee_NoOS_cost(self):
        return self._sumStat_con_ee_NoOS_cost

    def get_sumStat_con_ee_OS_utilities(self):
        return self._sumStat_con_ee_OS_utilities

    def get_sumStat_con_ee_NoOS_utilities(self):
        return self._sumStat_con_ee_NoOS_utilities

# condition ff
    def get_sumStat_con_ff_OS_cost(self):
        return self._sumStat_con_ff_OS_cost

    def get_sumStat_con_ff_NoOS_cost(self):
        return self._sumStat_con_ff_NoOS_cost

    def get_sumStat_con_ff_OS_utilities(self):
        return self._sumStat_con_ff_OS_utilities

    def get_sumStat_con_ff_NoOS_utilities(self):
        return self._sumStat_con_ff_NoOS_utilities

# condition gg
    def get_sumStat_con_gg_OS_cost(self):
        return self._sumStat_con_gg_OS_cost

    def get_sumStat_con_gg_NoOS_cost(self):
        return self._sumStat_con_gg_NoOS_cost

    def get_sumStat_con_gg_OS_utilities(self):
        return self._sumStat_con_gg_OS_utilities

    def get_sumStat_con_gg_NoOS_utilities(self):
        return self._sumStat_con_gg_NoOS_utilities

# condition hh
    def get_sumStat_con_hh_OS_cost(self):
        return self._sumStat_con_h_OS_cost

    def get_sumStat_con_hh_NoOS_cost(self):
        return self._sumStat_con_h_NoOS_cost

    def get_sumStat_con_hh_OS_utilities(self):
        return self._sumStat_con_hh_OS_utilities

    def get_sumStat_con_hh_NoOS_utilities(self):
        return self._sumStat_con_hh_NoOS_utilities

# condition ii
    def get_sumStat_con_ii_OS_cost(self):
        return self._sumStat_con_ii_OS_cost

    def get_sumStat_con_ii_NoOS_cost(self):
        return self._sumStat_con_ii_NoOS_cost

    def get_sumStat_con_ii_OS_utilities(self):
        return self._sumStat_con_ii_OS_utilities

    def get_sumStat_con_ii_NoOS_utilities(self):
        return self._sumStat_con_ii_NoOS_utilities

# condition jj
    def get_sumStat_con_jj_OS_cost(self):
        return self._sumStat_con_jj_OS_cost

    def get_sumStat_con_jj_NoOS_cost(self):
        return self._sumStat_con_jj_NoOS_cost

    def get_sumStat_con_jj_OS_utilities(self):
        return self._sumStat_con_jj_OS_utilities

    def get_sumStat_con_jj_NoOS_utilities(self):
        return self._sumStat_con_jj_NoOS_utilities

# condition kk
    def get_sumStat_con_kk_OS_cost(self):
        return self._sumStat_con_kk_OS_cost

    def get_sumStat_con_kk_NoOS_cost(self):
        return self._sumStat_con_kk_NoOS_cost

    def get_sumStat_con_kk_OS_utilities(self):
        return self._sumStat_con_kk_OS_utilities

    def get_sumStat_con_kk_NoOS_utilities(self):
        return self._sumStat_con_kk_NoOS_utilities

# condition ll
    def get_sumStat_con_ll_OS_cost(self):
        return self._sumStat_con_ll_OS_cost

    def get_sumStat_con_ll_NoOS_cost(self):
        return self._sumStat_con_ll_NoOS_cost

    def get_sumStat_con_ll_OS_utilities(self):
        return self._sumStat_con_ll_OS_utilities

    def get_sumStat_con_ll_NoOS_utilities(self):
        return self._sumStat_con_ll_NoOS_utilities

# condition mm
    def get_sumStat_con_mm_OS_cost(self):
        return self._sumStat_con_m_OS_cost

    def get_sumStat_con_mm_NoOS_cost(self):
        return self._sumStat_con_mm_NoOS_cost

    def get_sumStat_con_mm_OS_utilities(self):
        return self._sumStat_con_mm_OS_utilities

    def get_sumStat_con_mm_NoOS_utilities(self):
        return self._sumStat_con_mm_NoOS_utilities

# condition nn
    def get_sumStat_con_nn_OS_cost(self):
        return self._sumStat_con_nn_OS_cost

    def get_sumStat_con_nn_NoOS_cost(self):
        return self._sumStat_con_nn_NoOS_cost

    def get_sumStat_con_nn_OS_utilities(self):
        return self._sumStat_con_nn_OS_utilities

    def get_sumStat_con_nn_NoOS_utilities(self):
        return self._sumStat_con_nn_NoOS_utilities

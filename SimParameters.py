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

random.seed(7896)

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
        self._S_OS_NS= 0
        self._S_NoOS_S = 0
        self._S_NoOS_NS = 0

        self._total_OpSmile_costs = 0
        self._total_OpSmile_utilities = 0
        self._total_NoOpSmile_costs = 0
        self._total_NoOpSmile_utilities = 0

        # dirichlet distribution:
        # dirichlet distribution:
        probs = np.random.dirichlet(alpha=(0.050,  # 1
                                           0.071,  # 2
                                           0.008,  # 4
                                           0.003,  # 6
                                           0.004,  # 12
                                           0.007,  # 13
                                           0.011,  # 14
                                           0.066,  # 24
                                           0.009,  # 28
                                           0.013,  # 32
                                           0.014,  # 34
                                           0.020,  # 35
                                           0.057,  # 37
                                           0.005,  # 41
                                           0.004,  # 43
                                           0.032,  # 45
                                           0.011,  # 48
                                           0.005,  # 50
                                           0.003,  # 53
                                           ), size=None)
        # the numbers of alpha determine the concentration of the probability for each option
        conditions_list = ['a', 'b',
                           # 'c',
                           'd',
                           # 'e',
                           'f',
                           # 'g',
                           # 'h',
                           'i', 'j', 'k',
                           # 'l',
                           # 'm',
                           # 'n',
                           # 'o',
                           # 'p',
                           # 'q',
                           'r',
                           # 's',
                           't',
                           # 'u',
                           'v',
                           # 'w',
                           'x', 'y', 'z', 'aa',
                           # 'bb',
                           'cc',
                           # 'dd',
                           'ee',
                           # 'ff',
                           # 'gg',
                           'hh',
                           # 'ii',
                           'jj',
                           # 'kk',
                           'll',
                           # 'mm',
                           # 'nn'
                           ]  # list of conditions
        # what you are trying to do now is build a function in R that will tell you the concentration of each disease to input above
        self.draw = choice(a=conditions_list, p=probs)  # drawing a random

    def simulate(self, n_of_patients):
        if self.draw == 'a':  # chooses tree/condition based off of Dirichlet distribution draw
            import DT_Condition_1 as D
        if self.draw == 'b':
            import DT_Condition_2 as D
        # if self.draw == 'c':
        #    import DT_Condition_3 as D
        if self.draw == 'd':
            import DT_Condition_4 as D
        # if self.draw == 'e':
        #    import _DT_Condition_5 as D
        if self.draw == 'f':
            import DT_Condition_6 as D
        # if self.draw == 'g':
        #    import DT_Condition_8 as D
        # if self.draw == 'h':
        #    import DT_Condition_10 as D
        if self.draw == 'i':
            import DT_Condition_12 as D
        if self.draw == 'j':
            import DT_Condition_13 as D
        if self.draw == 'k':
            import DT_Condition_14 as D
        # if self.draw == 'l':
        #    import _DT_Condition_16 as D
        # if self.draw == 'm':
        #    import DT_Condition_17 as D
        # if self.draw == 'n':
        #    import _DT_Condition_18 as D
        # if self.draw == 'o':
        #    import DT_Condition_19 as D
        # if self.draw =='p':
        #    import _DT_Condition_20 as D
        # if self.draw =='q':
        #    import _DT_Condition_22 as D
        if self.draw == 'r':
            import DT_Condition_24 as D
        # if self.draw == 's':
        #    import DT_Condition_25 as D
        if self.draw == 't':
            import DT_Condition_28 as D
        # if self.draw == 'u':
        #    import DT_Condition_30 as D
        if self.draw == 'v':
            import DT_Condition_32 as D
        # if self.draw == 'w':
        #    import _DT_Condition_33 as D
        if self.draw == 'x':
            import DT_Condition_34 as D
        if self.draw == 'y':
            import DT_Condition_35 as D
        if self.draw == 'z':
            import DT_Condition_37 as D
        if self.draw == 'aa':
            import DT_Condition_41 as D
        # if self.draw == 'bb':
        #    import _DT_Condition_42 as D
        if self.draw == 'cc':
            import DT_Condition_43 as D
        # if self.draw == 'dd':
        #    import _DT_Condition_44 as D
        if self.draw == 'ee':
            import DT_Condition_45 as D
        # if self.draw == 'ff':
        #    import _DT_Condition_46 as D
        # if self.draw == 'gg':
        #    import DT_Condition_47 as D
        if self.draw == 'hh':
            import DT_Condition_48 as D
        # if self.draw == 'ii':
        #    import DT_Condition_49 as D
        if self.draw == 'jj':
            import DT_Condition_50 as D
        # if self.draw =='kk':
        #    import _DT_Condition_51 as D
        if self.draw == 'll':
            import DT_Condition_53 as D
        # if self.draw == 'mm':
        #    import _DT_Condition_54 as D
        # if self.draw == 'nn':
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
        return self._total_NoOpSmile_utilities


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

        self._initial_pop_size_pre=  1513 #474
        self._initial_pop_size_post = 1513
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


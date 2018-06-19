import numpy as np
from scipy.stats import expon
import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as Stat
import Surgeries as S


class Patient:
    def __init__(self, id):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(self._id)
        self._healthState = S.HealthState.HEALTHY
        # no access
        self._countNoSurgery = 0
        self._countNoSurgeryDeaths = 0
        self._countNoSurgerySurvive = 0
        # access
        self._countSurgeries = 0
        # Surgery performed by surgeon or nonsurgeon?
        self._countSurgeon = 0
        self._countNoSurgeon = 0
        # performed by surgeon
        self._countSurgeonDeath = 0
        self._countSurgeonSurvive = 0
        # complications
        self._countNoComplications = 0
        self._countComplications = 0
        self._countMajorComplication = 0
        self._countMinorComplication = 0
        self._countMajorComplicationDeath = 0
        self._countMajorComplicationSurvive = 0
        #nonsurgeon surgery
        self._countNonsurgeonDeath = 0
        self._countNonsurgeonSurvive = 0
        self._countNonsurgeonComplications = 0
        self._countNonsurgeonMajorComplication = 0
        self._countNonsurgeonMinorComplication = 0
        self._countNonsurgeonNoComplications = 0
        self._countNonsurgeonMajorComplicationDeath = 0
        self._countNonsurgeonMajorComplicationSurvive = 0

    def simulate (self, n_of_days):
        t = 0

        while self._healthState == S.HealthState.SURGERY and t < n_of_days:  # need n of days?
            if self._rnd.sample() < (1 - S.SURGERY_PROB):
                self._countNoSurgery += 1
            else:
                self._countSurgeries += 1

            t += 1

        for i in range(self._countNoSurgery):
            if self._rnd.random_sample() < S.NO_SURGERY_DEATH_PROB:
                self._countNoSurgeryDeaths += 1
            else:
                self._countNoSurgerySurvive += 1

        for i in range(self._countSurgeries):
            if self._rnd.random_sample() < S.SURGEON_ACCESS_PROB:
                self._countSurgeon += 1
            else:
                self._countNoSurgeon += 1

        for i in range(self._countSurgeon):
            if self._rnd.random_sample() < S.SURGEON_DEATH_PROB:
                self._countSurgeonDeath += 1
            else:
                self._countSurgeonSurvive += 1

        for i in range(self._countSurgeonSurvive):
            if self._rnd.random_sample() < S.COMPLICATION_PROB:
                self._countComplications += 1
            else:
                self._countNoComplications += 1

        for i in range(self._countComplications):
            if self._rnd.random_sample() < S.MAJOR_COMPLICATION_PROB:
                self._countMajorComplication += 1
            else:
                self._countMinorComplication += 1

        for i in range(self._countMajorComplication):
            if self._rnd.random_sample() < S.MAJOR_COMPLICATION_DEATH_PROB:
                self._countMajorComplicationDeath += 1
            else:
                self._countMajorComplicationSurvive += 1

        for i in range(self._countNoSurgeon):
            if self._rnd.random_sample() < S.NONSURGEON_DEATH_PROB:
                self._countNonsurgeonDeath += 1
            else:
                self._countNonsurgeonSurvive += 1

        for i in range(self._countNonsurgeonSurvive):
            if self._rnd.random_sample() < S.COMPLICATION_PROB:
                self._countNonsurgeonComplications += 1
            else:
                self._countNonsurgeonNoComplications += 1

        for i in range(self._countNonsurgeonComplications):
            if self._rnd.random_sample() < S.MAJOR_COMPLICATION_PROB:
                self._countNonsurgeonMajorComplication += 1
            else:
                self._countNonsurgeonMinorComplication += 1

        for i in range(self._countNonsurgeonMajorComplication):
            if self._rnd.random_sample() < S.MAJOR_COMPLICATION_DEATH_PROB:
                self._countNonsurgeonMajorComplicationDeath += 1
            else:
                self._countNonsurgeonMajorComplicationSurvive += 1

    def get_count_no_surgery(self):
        return self._countNoSurgery

    def get_count_no_surgery_deaths(self):
        return self._countNoSurgeryDeaths

    def get_count_no_surgery_survive(self):
        return self._countNoSurgerySurvive

    def get_count_surgeries(self):
        return self._countSurgeries

    def get_count_surgeon_access(self):
        return self._countSurgeon

    def get_count_no_surgeon_access(self):
        return self._countNoSurgeon

    def get_count_surgeon_death(self):
        return self._countSurgeonDeath

    def get_count_surgeon_survive(self):
        return self._countSurgeonSurvive

    def get_count_no_complications(self):
        return self._countNoComplications

    def get_count_complications(self):
        return self._countComplications

    def get_count_major_complication(self):
        return self._countMajorComplication

    def get_count_minor_complication(self):
        return self._countMinorComplication

    def get_count_major_complication_death(self):
        return self._countMajorComplicationDeath

    def get_count_major_complication_survive(self):
        return self._countMajorComplicationSurvive

    def get_count_nonsurgeon_death(self):
        return self._countNonsurgeonDeath

    def get_count_nonsurgeon_survive(self):
        return self._countNonsurgeonSurvive

    def get_count_nonsurgeon_complications(self):
        return self._countNonsurgeonComplications

    def get_count_nonsurgeon_major_complication(self):
        return self._countNonsurgeonMajorComplication

    def get_count_nonsurgeon_minor_complication(self):
        return self._countNonsurgeonMinorComplication

    def get_count_nonsurgeon_no_complications(self):
        return self._countNonsurgeonNoComplications

    def get_count_nonsurgeon_major_complication_death(self):
        return self._countNonsurgeonMajorComplicationDeath

    def get_count_nonsurgeon_major_complication_survive(self):
        return self._countNonsurgeonMajorComplicationSurvive


class Cohort:
    def __init__(self, id, pop_size):
        self._initialPopSize = pop_size
        self._patients = []
        self._count_surgery = []
        self._count_no_surgery = []
        self._count_no_surgery_death = []
        self._count_no_surgery_survive = []

        self._count_surgery_access = []
        self._count_surgeon = []
        self._count_surgeon_death = []
        self._count_surgeon_survive = []
        self._count_complication = []
        self._count_no_complication = []
        self._count_major_complication = []
        self._count_minor_complication = []
        self._count_major_complication_death = []
        self._count_major_complication_survive = []

        self._count_nonsurgeon = []
        self._count_nonsurgeon_death = []
        self._count_nonsurgeon_survive = []
        self._count_nonsurgeon_complication = []
        self._count_nonsurgeon_no_complication = []
        self._count_nonsurgeon_major_complication = []
        self._count_nonsurgeon_minor_complication = []
        self._count_nonsurgeon_major_complication_death = []
        self._count_nonsurgeon_major_complication_survive = []

        for i in range(pop_size):
            patient = Patient(id*pop_size + i)
            self._patients.append(patient)

    def simulate(self, n_of_days):
        for patient in self._patients:
            patient.simulate(n_of_days)

            no_surgery = patient.get_count_no_surgery
            self._count_no_surgery.append(no_surgery)
            no_surgery_death = patient.get_count_no_surgery_deaths
            self._count_no_surgery_death.append(no_surgery_death)
            no_surgery_survive = patient.get_count_no_surgery_survive
            self._count_no_surgery_survive.append(no_surgery_survive)
            surgeries = patient.get_count_surgeries
            self._count_surgeon.append(surgeries)
            surgeon_access = patient.get_count_surgeon_access
            self._count_surgery_access.append(surgeon_access)
            no_surgeon_access = patient.get_count_no_surgeon_access
            self._count_nonsurgeon.append(no_surgeon_access)
            surgeon_death = patient.get_count_surgeon_death
            self._count_surgeon_death.append(surgeon_death)
            surgeon_survive = patient.get_count_surgeon_survive
            self._count_surgeon_survive.append(surgeon_survive)
            no_complications = patient.get_count_no_complications
            self._count_no_complication.append(no_complications)
            complications = patient.get_count_complications
            self._count_complication.append(complications)
            major_complications= patient.get_count_major_complication
            self._count_major_complication.append(major_complications)
            minor_complications = patient.get_count_minor_complication
            self._count_minor_complication.append(minor_complications)
            major_complication_death= patient.get_count_major_complication_death
            self._count_major_complication_death.append(major_complication_death)
            major_complication_survive= patient.get_count_major_complication_survive
            self._count_major_complication_survive.append(major_complication_survive)
            nonsurgeon_death = patient.get_count_nonsurgeon_death
            self._count_nonsurgeon_death.append(nonsurgeon_death)
            nonsurgeon_survive = patient.get_count_nonsurgeon_survive
            self._count_nonsurgeon_survive.append(nonsurgeon_survive)
            nonsurgeon_complications= patient.get_count_nonsurgeon_complications
            self._count_nonsurgeon_complication.append(nonsurgeon_complications)
            nonsurgeon_major_complications= patient.get_count_nonsurgeon_major_complication
            self._count_nonsurgeon_major_complication.append(nonsurgeon_major_complications)
            nonsurgeon_minor_complications= patient.get_count_nonsurgeon_minor_complication
            self._count_nonsurgeon_minor_complication.append(nonsurgeon_minor_complications)
            nonsurgeon_no_complications = patient.get_count_nonsurgeon_no_complications
            self._count_nonsurgeon_no_complication.append(nonsurgeon_no_complications)
            nonsurgeon_major_complication_death= patient.get_count_nonsurgeon_major_complication_death
            self._count_nonsurgeon_major_complication_death.append(nonsurgeon_major_complication_death)
            nonsurgeon_major_complication_survive= patient.get_count_nonsurgeon_major_complication_survive
            self._count_nonsurgeon_major_complication_survive.append(nonsurgeon_major_complication_survive)

        return CohortOutcomes(self)


class CohortOutcomes:
    def __init__(self, simulated_cohort):
        self._simulatedCohort = simulated_cohort
        self._sumStat_no_surgery = Stat.SummaryStat('Number of no surgery cases',
                                                    self._simulatedCohort.get_count_no_surgery)
        self._sumStat_no_surgery_death = Stat.SummaryStat('Number of no surgery case deaths',
                                                          self._simulatedCohort.get_count_no_surgery_deaths)
        self._sumStat_no_surgery_survive = Stat.SummaryStat('Number of no surgery case survivals',
                                                            self._simulatedCohort.get_count_no_surgery_survive)
        self._sumStat_surgery_count = Stat.SummaryStat('Number of surgeries',
                                                       self._simulatedCohort.get_count_surgeries)
        self._sumStat_surgeon_access = Stat.SummaryStat('Number of cases with surgeon access',
                                                        self._simulatedCohort.get_count_surgeon_access)
        self._sumStat_no_surgeon_access = Stat.SummaryStat('Number of cases with no surgeon access',
                                                           self._simulatedCohort.get_count_no_surgeon_access)
        self._sumStat_surgeon_death = Stat.SummaryStat('Number of cases with surgeon access, death',
                                                       self._simulatedCohort.get_count_surgeon_death)
        self._sumStat_surgeon_survive= Stat.SummaryStat('Number of cases with surgeon access, survival',
                                                        self._simulatedCohort.get_count_surgeon_survive)
        self._sumStat_no_complications = Stat.SummaryStat('Number of cases with no complications (surgeon access)',
                                                          self._simulatedCohort.get_count_no_complications)
        self._sumStat_complications = Stat.SummaryStat('Number of cases with complications (surgeon access)',
                                                       self._simulatedCohort.get_count_complications)
        self._sumStat_major_complication = Stat.SummaryStat('Number of major complication cases (surgeon access)',
                                                            self._simulatedCohort.get_count_major_complication)
        self._sumStat_minor_complication = Stat.SummaryStat('Number of minor complication cases (surgeon access)',
                                                            self._simulatedCohort.get_count_minor_complication)
        self._sumStat_major_complication_death = Stat.SummaryStat('Number of major complication case deaths '
                                                                  '(surgeon access)',
                                                                  self._simulatedCohort.
                                                                  get_count_major_complication_death)
        self._sumStat_major_complication_survive = Stat.SummaryStat('Number of major complication case survivals '
                                                                    '(surgeon access)',
                                                                    self._simulatedCohort.
                                                                    get_count_major_complication_survive)
        self._sumStat_nonsurgeon_death = Stat.SummaryStat('Number of no surgeon access deaths ',
                                                          self._simulatedCohort.get_count_nonsurgeon_death)
        self._sumStat_nonsurgeon_survive = Stat.SummaryStat('Number of no surgeon access survivals',
                                                            self._simulatedCohort.get_count_nonsurgeon_survive)
        self._sumStat_nonsurgeon_complications= Stat.SummaryStat('Number of no surgeon access complications',
                                                                 self._simulatedCohort.
                                                                 get_count_nonsurgeon_complications)
        self._sumStat_nonsurgeon_major_complication = Stat.SummaryStat('Number of no surgeon access major complications'
                                                                       , self._simulatedCohort.
                                                                       get_count_nonsurgeon_major_complication)
        self._sumStat_nonsurgeon_minor_complication = Stat.SummaryStat('Number of no surgeon access minor complications'
                                                                       , self._simulatedCohort.
                                                                       get_count_nonsurgeon_minor_complication)
        self._sumStat_nonsurgeon_no_complication= Stat.SummaryStat('Number of no surgeon access no complications',
                                                                   self._simulatedCohort.
                                                                   get_count_nonsurgeon_no_complications)
        self._sumStat_nonsurgeon_major_complication_death = Stat.SummaryStat('Number of no surgeon access major '
                                                                             'complication deaths',
                                                                             self._simulatedCohort.
                                                                             get_count_nonsurgeon_major_complication_death)
        self._sumStat_nonsurgeon_major_complication_survive = Stat.SummaryStat('Number of no surgeon access major '
                                                                               'complication survivals',
                                                                               self._simulatedCohort.
                                                                               get_count_nonsurgeon_major_complication_survive)


# now you have to figure out how to make all this stuff print
# for some reason your final project code isnt the most recent version and its not printing what its suppossed to
# whyyyyyyyyyyyyyyyyyyyyyyyyyyyy
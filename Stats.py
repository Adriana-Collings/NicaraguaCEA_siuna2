import sys
import numpy as numpy
import scipy.stats as stat
import math
from scr import FormatFunctions as Support


class _Statistics(object):
    def __init__(self, name):
        """ abstract method to be overridden in derived classes"""
        self._name = name        # name of this statistics
        self._n = 0              # number of data points
        self._mean = 0           # sample mean
        self._stDev = 0          # sample standard deviation
        self._max = -sys.float_info.max  # maximum
        self._min = sys.float_info.max   # minimum

    def get_n(self):
        """ abstract method to be overridden in derived classes
        :returns mean (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_mean(self):
        """ abstract method to be overridden in derived classes
        :returns mean (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_stdev(self):
        """ abstract method to be overridden in derived classes
        :returns standard deviation (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_min(self):
        """ abstract method to be overridden in derived classes
        :returns minimum (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_max(self):
        """ abstract method to be overridden in derived classes
        :returns maximum (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_percentile(self, q):
        """ abstract method to be overridden in derived classes
        :param q: percentile to compute (q in range [0, 100])
        :returns percentile (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_t_half_length(self, alpha):
        """
        :param alpha: significance level (between 0 and 1)
        :returns half-length of 100(1-alpha)% t-confidence interval """

        return stat.t.ppf(1 - alpha / 2, self.get_n() - 1) * self.get_stdev() / numpy.sqrt(self.get_n())

    def get_t_CI(self, alpha):
        """ calculates t-based confidence interval for population mean
        :param alpha: significance level (between 0 and 1)
        :return: a list [l, u]
        """
        mean = self.get_mean()
        hl = self.get_t_half_length(alpha)

        return [mean - hl, mean + hl]

    def get_bootstrap_CI(self, alpha, num_samples):
        """ calculates empirical bootstrap confidence interval (abstract method to be overridden in derived classes)
        :param alpha: significance level
        :param num_samples: number of bootstrap samples
        :returns a list [L, U] """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_PI(self, alpha):
        """ calculates percentile interval (abstract method to be overridden in derived classes)
        :param alpha: significance level (between 0 and 1)
        :returns a list [L, U]
         """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_summary(self, alpha, digits):
        """
        :param alpha: significance level
        :param digits: digits to round the numbers to
        :return: a list ['name', 'mean', 'confidence interval', 'percentile interval', 'st dev', 'min', 'max']
        """
        return [self._name,
                Support.format_number(self.get_mean(), digits),
                Support.format_interval(self.get_t_CI(alpha), digits),
                Support.format_interval(self.get_PI(alpha), digits),
                Support.format_number(self.get_stdev(), digits),
                Support.format_number(self.get_min(), digits),
                Support.format_number(self.get_max(), digits)]


class SummaryStat(_Statistics):
    def __init__(self, name, data):
        """:param data: a list or numpy.array of data points"""

        _Statistics.__init__(self, name)
        # convert data to numpy array if needed
        if type(data) == list:
            self._data = numpy.array(data)
        elif type(data) == numpy.ndarray:
            self._data = data
        else:
            raise ValueError("The argument data can be either a list of numbers or a numpy.array.")

        self._n = len(self._data)
        self._total = numpy.sum(self._data)
        self._mean = numpy.mean(self._data)
        self._stDev = numpy.std(self._data, ddof=1)  # unbiased estimator of the standard deviation

    def get_n(self):
        return self._n

    def get_total(self):
        return self._total

    def get_mean(self):
        return self._mean

    def get_stdev(self):
        return self._stDev

    def get_min(self):
        return numpy.min(self._data)

    def get_max(self):
        return numpy.max(self._data)

    def get_percentile(self, q):
        """
        :param q: percentile to compute (q in range [0, 100])
        :returns: qth percentile """

        return numpy.percentile(self._data, q)

    def get_bootstrap_CI(self, alpha, num_samples):
        """ calculates the empirical bootstrap confidence interval
        :param alpha: significance level (between 0 and 1)
        :param num_samples: number of bootstrap samples
        :return: a list [l, u]
        """

        # set random number generator seed
        numpy.random.seed(1)

        # initialize delta array
        delta = numpy.zeros(num_samples)

        # obtain bootstrap samples
        for i in range(num_samples):
            sample_i = numpy.random.choice(self._data, size=self._n, replace=True)
            delta[i] = sample_i.mean() - self.get_mean()

        # return [l, u]
        return self.get_mean() - numpy.percentile(delta, [100*(1-alpha / 2.0), 100*alpha / 2.0])

    def get_PI(self, alpha):
        """
        :param alpha: significance level (between 0 and 1)
        :return: percentile interval in the format of list [l, u]
        """
        return [self.get_percentile(100*alpha/2), self.get_percentile(100*(1-alpha/2))]

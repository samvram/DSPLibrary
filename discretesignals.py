import numpy as np

class DiscreteSignals:
    def impulse(self, time_array, impulse_at=0, scale=1):
        fn = {}
        for time in time_array:
            if time != impulse_at:
                fn[time] = 0
            else:
                fn[time] = scale
        return fn

    def ramp(self, time_array, begin_at=0, scale=1):
        fn = {}
        for time in time_array:
            if time<=begin_at:
                fn[time] = 0
            else:
                fn[time] = scale*(time-begin_at)
        return fn

    def heaviside(self, time_array, begin_at=0, scale=1):
        fn = {}
        for time in time_array:
            if time<begin_at:
                fn[time] = 0
            else:
                fn[time] = scale
        return fn

    def exponential(self, time_array, r, theta, n, scale=1):
        fn_real = {}
        fn_imaginary = {}
        for time in time_array:
            fn_real[time] = (r**n)*np.cos(theta*n)
            fn_imaginary[time] = (r**n)*np.sin(theta*n)
        fn = {'real':fn_real, 'imaginary':fn_imaginary}
        return fn

    def sinusoidal(self, time_array, phase=0, amplitude=1, omega=1):
        '''
        A function to return the function as in otther above function from the given input
        :param time_array: The input sampled time_array
        :param phase: The initial phase of the wave
        :param amplitude: The amplitude of the wave
        :param omega: The frequency of the wave
        :return:
        '''
        # TODO: Write the function body please
import numpy as np

class DiscreteSignals:
    def impulse(self, time_array, impulse_at=0, scale=1):
        fn = {}
        for time in time_array:
            if time is not impulse_at:
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

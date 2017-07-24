import matplotlib.pyplot as plt


class DspToolKit:
    def __init__(self):
        self.figure_num = 0

    def array_creator(self, start, end, step=1):
        fn = []
        time = start
        while time <= end:
            fn.append(time)
            time += step
        return fn

    def plot(self, fn, figure_num=0):
        if figure_num is not 0:
            self.figure_num = figure_num
        for key in fn:
            if key in ['real', 'imaginary'] :
                self._complex_plot(fn)
                return
        self._normal_plot(fn)

    def _complex_plot(self, fn):
        real_fn = fn['real']
        imaginary_fn = fn['imaginary']

        plt.figure(self.figure_num)
        plt.title('Real Plane')
        plt.stem(list(real_fn.keys()), list(real_fn.values()))
        # plt.show()
        self.figure_num = self.figure_num + 1

        plt.figure(self.figure_num)
        plt.title('Complex Plane')
        plt.stem(list(imaginary_fn.keys()), list(imaginary_fn.values()))
        # plt.show()
        self.figure_num = self.figure_num + 1

    def _normal_plot(self, fn):
        plt.figure(self.figure_num)
        plt.title('Normal Plot')
        plt.stem(list(fn.keys()), list(fn.values()))
        # plt.show()
        self.figure_num = self.figure_num + 1

    def show(self):
        plt.show()

    def real_add(self, fn1, fn2, key='add'):
        time_1 = list(fn1.keys())
        time_2 = list(fn2.keys())

        if time_1 != time_2:
            print('The Time Domain is not the same for both the function')
            return

        fn_add = {}
        for time in time_1:
            if key == 'sub':
                fn_add[time] = fn1[time] - fn2[time]
            else:
                fn_add[time] = fn1[time] + fn2[time]

        return fn_add

    def dot_multiply(self, fn1, fn2, key='mul'):
        time_1 = list(fn1.keys())
        time_2 = list(fn2.keys())

        if time_1 != time_2:
            print('The Time Domain is not the same for both the function')
            return

        fn_dot = {}
        for time in time_1:
            if key == 'div':
                fn_dot[time] = fn1[time]/fn2[time]
            else:
                fn_dot[time] = fn1[time]*fn2[time]

        return fn_dot
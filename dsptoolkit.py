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

    def plot(self, fn, figure_num=0, title='Plot', mode='normal'):
        if figure_num is not 0:
            self.figure_num = figure_num
        for key in fn:
            if key in ['real', 'imaginary'] :
                self._complex_plot(fn,mode)
                return
        self._normal_plot(fn, title, mode)

    def _complex_plot(self, fn, mode):
        real_fn = fn['real']
        imaginary_fn = fn['imaginary']

        plt.figure(self.figure_num)
        plt.title('Real Plane')
        if mode == 'stem':
            plt.stem(list(real_fn.keys()), list(real_fn.values()))
        else:
            plt.plot(list(real_fn.keys()), list(real_fn.values()))
        # plt.show()
        self.figure_num = self.figure_num + 1

        plt.figure(self.figure_num)
        plt.title('Complex Plane')
        if mode == 'stem':
            plt.stem(list(imaginary_fn.keys()), list(imaginary_fn.values()))
        else:
            plt.plot(list(real_fn.keys()), list(real_fn.values()))
        # plt.show()
        self.figure_num = self.figure_num + 1

    def _normal_plot(self, fn, title, mode):
        plt.figure(self.figure_num)
        if title == 'Plot':
            plt.title('Normal Plot {}'.format(self.figure_num+1))
        else:
            plt.title(title)
        if mode == 'stem':
            plt.stem(list(fn.keys()), list(fn.values()))
        else:
            plt.plot(list(fn.keys()), list(fn.values()))
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

    def flip_about_y(self, func):
        time = func.keys()
        new_func = {}
        for t in time:
            new_func[-1*t] = func[t]
        return new_func

    def dtft(self,func):
        '''
        A function to find dtft of supplied function and return its dtft of the supplied function.
        :param func:
        :return:
        '''
        pass
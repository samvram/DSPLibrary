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
        plt.show()
        self.figure_num = self.figure_num + 1

        plt.figure(self.figure_num)
        plt.title('Complex Plane')
        plt.stem(list(imaginary_fn.keys()), list(imaginary_fn.values()))
        plt.show()
        self.figure_num = self.figure_num + 1

    def _normal_plot(self, fn):
        plt.figure(self.figure_num)
        plt.title('Normal Plot')
        plt.stem(list(fn.keys()), list(fn.values()))
        plt.show()
        self.figure_num = self.figure_num + 1

from discretesignals import DiscreteSignals
from dsptoolkit import DspToolKit

disc = DiscreteSignals()
dtk = DspToolKit()
time = dtk.array_creator(-5,5,0.5)
func = disc.heaviside(time)
dtk.plot(func)

func_1 = dtk.flip_about_y(func)
dtk.plot(func_1)

func = disc.impulse(time, -2)
dtk.plot(func)

dtk.show()
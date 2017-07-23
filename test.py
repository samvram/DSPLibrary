from discretesignals import DiscreteSignals
from dsptoolkit import DspToolKit

disc = DiscreteSignals()
dtk = DspToolKit()
time = dtk.array_creator(-5,5,1)
func = disc.heaviside(time)
dtk.plot(func)
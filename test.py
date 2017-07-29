from discretesignals import DiscreteSignals
from dsptoolkit import DspToolKit
import numpy as np

disc = DiscreteSignals()
dtk = DspToolKit()

time = dtk.array_creator(-np.pi, np.pi, 0.01)
func1 = np.sin(time)
dtk.plot(func1)

func2 = np.sin(time)
dtk.plot(func2)

func = dtk.real_add(func1, func2)
dtk.plot(func)

dtk.show()
 # TODO : Create a message signal as given in class
 # TODO : Create a carrier signal as given in class
 # TODO : Use the digitalCommunications class amplitude_modulation to get the modulated signa;
 # TODO : Plot all the three waves
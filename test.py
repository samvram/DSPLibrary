from discretesignals import DiscreteSignals
from dsptoolkit import DspToolKit
from digitalcommunication import DigitalCommunication
import numpy as np

disc = DiscreteSignals()
dtk = DspToolKit()
dc = DigitalCommunication()

time = dtk.array_creator(-np.pi, np.pi, 0.01)
message = disc.sinusoidal(time, omega=1, amplitude=5)
dtk.plot(message, title='Message Signal', mode='stem')

carrier = disc.sinusoidal(time, omega=10)
dtk.plot(carrier, title='Carrier Signal', mode='stem')

func = dc.amplitude_modulation(message, carrier)
dtk.plot(func, title='Amplitude Modulated signal', mode='stem')

dtk.show()
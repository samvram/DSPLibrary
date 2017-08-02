class DigitalCommunication:
    def dsb_sc(self, message_signal, carrier_signal):
        time_message = list(message_signal.keys())
        time_carrier = list(carrier_signal.keys())

        if time_message != time_carrier:
            print('Both are not equally sampled')
            return

        modulated_signal = {}
        for time in time_message:
            modulated_signal[time] = message_signal[time] * carrier_signal[time]

        return modulated_signal

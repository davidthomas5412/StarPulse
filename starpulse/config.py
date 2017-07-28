

class Config(object):

    def __init__(self, stellar_sed, laser_sed,
                 filt, nsamples, sample_rate, pulse_duration):
        self.stellar_sed = stellar_sed
        self.laser_sed = laser_sed
        self.filt = filt
        self.nsamples = nsamples # in ns
        self.sample_rate = sample_rate  # in ns
        self.pulse_duration = pulse_duration

from math import pi
from numpy.random import uniform, poisson, randint
from numpy import array, linspace, sin, savetxt
from starpulse.constant import c

class Simulator(object):
    def __init__(self, config):
        self.config = config

    def run(self):
        distance = 1.4299e21 # close, no redshift, peculiar velocity might dominate, ...

        stellar_photon_flux = self.config.stellar_sed.photon_flux(self.config.filt)
        laser_photon_flux = self.config.laser_sed.photon_flux(self.config.filt)

        mean_photon_flux_ns = stellar_photon_flux * 1e9 / (4 * pi * distance ** 2)
        mean_laser_flux_ns = laser_photon_flux * 1e9 / (4 * pi * distance ** 2)

        background = poisson(lam=mean_photon_flux_ns * self.config.sample_rate,
                size=int(self.config.nsamples))
        foreground = poisson(lam=mean_laser_flux_ns * self.config.sample_rate,
                size=int(self.config.pulse_duration / self.config.sample_rate))

        offset = randint(0, self.config.nsamples - (self.config.pulse_duration / self.config.sample_rate))
        print(offset)
        for i in range(len(foreground)):
            background[offset + i] += foreground[i]

        times = linspace(0, self.config.nsamples * self.config.sample_rate, self.config.nsamples)
        return array([times, background])

from starpulse.config import Config
from starpulse.sed import Laser, Blackbody
from starpulse.simulator import Simulator

filt = [552e-9, 691e-9]
config = Config(Blackbody(30000), Laser(5e8), filt, 100, 10, 100)
sim = Simulator(config)
ts = sim.run().transpose()
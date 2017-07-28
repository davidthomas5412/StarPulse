from math import pi, e
from .constant import c, h, k


class SED(object):
    def photon_flux(self, filt):
        raise NotImplementedError()


class Blackbody(SED):
    def __init__(self, temperature):
        self.temperature = temperature

    def photon_flux(self, filt):
        width = filt[1] - filt[0]
        wavelength = (filt[0] + filt[1]) / 2.
        radiance = pi * (2 * h * c ** 2 / wavelength ** 5) *\
               (1 / (e ** (h * c / (wavelength * k * self.temperature)) - 1))
        power = width * radiance
        return power * wavelength / h


class Laser(SED):
    def __init__(self, power):
        self.power = power

    def photon_flux(self, filt):
        wavelength = (filt[0] + filt[1]) / 2.
        return self.power * wavelength / h
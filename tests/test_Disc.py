import FrisPy
import numpy as np
import numpy.testing as npt
import pytest

def test_Disc():
    #Smoke test
    d = FrisPy.Disc()

def test_Disc_defaults():
    #Test that the default attributes for an ultrastar
    #are correctly set
    d = FrisPy.Disc()
    
    allowed_keys = ['air_density', 'area', 'diameter', 'g',
                    'grav_vector', 'I_zz', 'I_xx', 'mass']
    default_values = [1.225, 0.057, 9.81,
                      np.array([0,0,-1]), 0.002352, 0.001219, 0.175]
    default_values.insert(2, 2*(default_values[1]/np.pi)**0.5)

    for i, (k, v) in enumerate(zip(allowed_keys, default_values)):
        npt.assert_equal(getattr(d, k), default_values[i])

def test_Disc_trajectory():
    d = FrisPy.Disc()
    npt.assert_equal(hasattr(d, "_trajectory"), True)
    npt.assert_equal(hasattr(d, "initialize_trajectory"), True)
    npt.assert_equal(hasattr(d, "compute_trajectory"), True)

    allowed_keys = ['x', 'y', 'z', 'vx', 'vy', 'vz',
                    'phi', 'theta', 'gamma',
                    'phidot', 'thetadot', 'gammadot']
    default_values = [0, 0, 1, 10, 0, 0,
                      0, 0, 0, 0, 0, 50]
    for i, (k, v) in enumerate(zip(allowed_keys, default_values)):
        npt.assert_equal(getattr(d._trajectory, k), default_values[i])

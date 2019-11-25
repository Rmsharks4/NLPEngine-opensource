import matplotlib.pyplot as plt

from amfm_decompy import pYAAPT
from amfm_decompy import pyQHM
from amfm_decompy import basic_tools

print('Read File')

# load audio
filename = '../data/active-listening/216.22/211565170421608471567264570.wav'

# Declare the variables.
window_duration = 0.015
nharm_max = 25

# Create the signal object.
signal = basic_tools.SignalObj(filename)

print('Open Sample Window')

# YAAPT pitches
# Create the window object.
window = pyQHM.SampleWindow(window_duration, signal.fs)

print('YAAPT Signal')

# Create the pitch object and calculate its attributes.
pitch = pYAAPT.yaapt(signal)

print('Set NHarm')

# Use the pitch track to set the number of modulated components.
signal.set_nharm(pitch.values, nharm_max)

print('QHM Signal')

# Perform the QHM extraction.
QHM = pyQHM.qhm(signal, pitch, window, N_iter=1, phase_tech='freq')

print('AQHM Signal')

# Perform the aQHM extraction.
aQHM = pyQHM.aqhm(signal, QHM, pitch, window, 0.001, N_iter=1, N_runs=1)

print('EQHM Signal')

# Perform the eaQHM extraction.
eaQHM = pyQHM.eaqhm(signal, aQHM, pitch, window, 0.001, N_iter=1, N_runs=1)

print('Plot File')

fig1 = plt.figure()

# Plot the instaneous frequency of the fundamental harmonic.
# The ComponentObj objects are stored inside the harmonics list.
# For more information, please check the ModulatedSign.harmonics attribute.
plt.plot(QHM.harmonics[0].freq*signal.fs)

plt.xlabel('samples', fontsize=18)
plt.ylabel('pitch (Hz)', fontsize=18)

fig2 = plt.figure()

# Plot the envelope magnitude of the third harmonic.
# The ComponentObj objects are stored inside the harmonics list.
# For more information, please check the ModulatedSign.harmonics attribute.
plt.plot(QHM.harmonics[2].mag, color='green')

plt.xlabel('samples', fontsize=18)
plt.ylabel('magnitude', fontsize=18)

plt.show()

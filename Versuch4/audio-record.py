# -------------------------------------
# Task 1.1
# -------------------------------------

import pyaudio
import numpy
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16 # Voreinstellungen der Aufnahme
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
p = pyaudio.PyAudio()
print('running')
stream = p.open(format=FORMAT, # Aufnahmestart
                channels=1,
                rate=SAMPLEFREQ,
                input=True,
                frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES * FRAMESIZE)
decoded = numpy.fromstring(data, 'Int16');
numpy.save(".//test2.npy", decoded)
stream.stop_stream() # Aufnahmestop
stream.close()
p.terminate()
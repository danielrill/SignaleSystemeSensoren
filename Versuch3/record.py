import numpy as np
import pyaudio
import numpy
import time

import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220

p = pyaudio.PyAudio()

print('running')
start = time.perf_counter()
stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                input=True, frames_per_buffer=FRAMESIZE)

data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.fromstring(data, 'Int16')

end = time.perf_counter()
stream.stop_stream()
stream.close()
p.terminate()
print('done')

print('time recorded= %f' % (end - start))

plt.plot(decoded)
plt.show()

csv_file = "../SoundV3/sound_data.csv"  # Mundharmonika Ton 4

np.savetxt(csv_file, decoded, delimiter=",")

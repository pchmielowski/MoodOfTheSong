import wave
import matplotlib.pyplot as plt
import numpy as np

file = '/home/piotrek/dsp/dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/Angry_all/You ' \
       + 'Oughta Know (Album Version).mp3.wav'
spf = wave.open(file, 'r')
signal = np.fromstring(spf.readframes(-1), 'Int16')
spf.close()

plt.figure(1)
plt.plot(signal)
plt.show()
plt.interactive(False)

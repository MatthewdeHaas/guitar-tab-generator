import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import soundfile as sf
from scipy.signal import find_peaks, peak_prominences, savgol_filter
import json



def truncate_fft(xf, yf, lower_bound=0, upper_bound=1200):
    filtered_xf = [i for i in xf if lower_bound <= i < upper_bound]
    filtered_xf_indices = [filtered_xf.index(i) for i in filtered_xf]
    filtered_yf = [yf[i] for i in filtered_xf_indices]
    return filtered_xf, filtered_yf



# INPUT:
#        file: directory from root of project to a .wav file
#        domain: either time or frequency, latter is the fft
def plot_audio(file, domain="time", truncate=False):
    samplerate, data = wavfile.read(file)
    if domain == "time":
        plt.title(f"{file} - audio")

        f = sf.SoundFile(file)

        plt.plot(np.linspace(0, f.frames / f.samplerate, len(list(data[:, 0]))), data[:, 0])
        plt.xlabel("Time (sec)")
        plt.ylabel("Air Pressure (...)")

    elif domain == "frequency":
        plt.title(f"{file[file.rfind('/') + 1:]} - Discrete Fourier Transform")
        xf = fftfreq(data.shape[0], 1 / samplerate)
        yf = np.abs(fft(data[:, 0]))
        if truncate:
            xf, yf = truncate_fft(xf, yf)
        plt.plot(xf, yf)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude (...)")
    plt.show()


file = "media/Chords/F5_arpeggiated.wav"
plot_audio(file, domain="frequency", truncate=True)




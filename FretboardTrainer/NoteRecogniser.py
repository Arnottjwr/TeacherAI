"""
Script which analyses an audio sample and determines the note played using a Fourier transform.
"""
import glob
from scipy import fftpack
import numpy as np
import librosa

class NoteRecogniser:
    def __init__(self, filepath: str) -> None:
        signal, sample_rate = librosa.load(filepath,sr = sample_rate) 
        self.signal = signal
        self.sample_rate = sample_rate

    def get_frequency(self) -> tuple[np.ndarray,np.ndarray]:
        """
        Obtains the frequency values for a given signal and sample rate

        Args:
            signal (np.ndarray): The input signal
            sampling_rate (float): The sampling rate of the signal
        """

        signal_points = len(self.signal)
        time = 1.0 / self.sample_rate
        signal_array = self.signal[:signal_points]
        fft_signal = fftpack.fft(signal_array)
        freq_array = fftpack.fftfreq(signal_points, time)[:signal_points//2]    
        magnitude_array = 2.0 / signal_points * np.abs(fft_signal[:signal_points // 2])
        return freq_array, magnitude_array

    def determine_note(self):
        pass

if __name__ == '__main__':
    pass
"""
Script which analyses an audio sample and determines the note played using a Fourier transform.
"""
import glob
from scipy import fftpack
import numpy as np
import librosa


class AudioLoader:
    def __init__(self,filepath: str) -> None:
        self.signal = glob.glob(filepath, recursive=True)
    
    def load_audio(self):
        return librosa.load()


class PreProcessor:
    def __init__(self, signal: np.ndarray, sample_rate: float) -> None:
        """_summary_

        Args:
            signal (np.ndarray): _description_
            sample_rate (float): _description_
        """
        self.signal = signal
        self.sample_rate = sample_rate

    def get_frequency_scipy(self): #TODO - typehint
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
        xf = fftpack.fftfreq(signal_points, time)[:signal_points//2]    
        magnitude = 2.0 / signal_points * np.abs(fft_signal[:signal_points // 2])

        return xf, magnitude



if __name__ == '__main__':
    pass
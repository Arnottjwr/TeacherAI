"""
Script which analyses an audio sample and determines the note played using a Fourier transform.
"""

from scipy import fftpack
import numpy as np 
import librosa
import glob


class AudioLoader:
    def __init__(self,filepath: str) -> None:
        self.signal = glob.glob(filepath, recursive=True)
    
    def load_audio(self):
        return librosa.load()
    



class PreProcessor:
    def __init__(self, signal: np.ndarray, sample_rate: float) -> None:
        self.signal = signal
        self.sample_rate = sample_rate

    def get_frequency_scipy(self):
        """
        Obtains the frequency values for a given signal and sample rate

        Parameters:
            signal (array-like): The input signal.
            sampling_rate (float): The sampling rate of the signal.
        """

        N = len(self.signal)
        T = 1.0 / self.sample_rate
        y = self.signal[:N]
        yf = fftpack.fft(y)
        xf = fftpack.fftfreq(N, T)[:N//2]    
        m = 2.0 / N * np.abs(yf[:N // 2])
        return xf, m
    
    def get_frequency_libro(self):
        """
        AI Generated
        
        """
        # Perform FFT and get frequency and magnitude
        D = librosa.stft(self.signal)
        freq = librosa.fft_frequencies(sr=self.sample_rate)
        magnitude = 2 * librosa.magphase(D)[0]
        return freq, magnitude



if __name__ == '__main__':
    pass
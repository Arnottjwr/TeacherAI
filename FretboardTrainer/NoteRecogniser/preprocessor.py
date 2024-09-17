"""
Script which analyses an audio sample and determines the note played using a Fourier transform.
"""

from scipy import fftpack
import numpy as np 
import librosa
import glob


class AudioLoader:
    pass 


class PreProcessor:

    def __init__(self, filepath: str) -> None:
        # path = '/Users/jackarnott/Music/MT4599 Samples/Guitar Samples/final samples/' + '**/*.wav'
        self.signal = glob.glob(filepath, recursive=True)


    def get_frequency(self, signal: np.ndarray, sample_rate: float):
        """
        Obtains the frequency values for a given signal and sample rate

        Parameters:
            signal (array-like): The input signal.
            sampling_rate (float): The sampling rate of the signal.
        """

        N = len(signal)
        T = 1.0 / sample_rate
        y = signal[:N]
        yf = fftpack.fft(y)
        xf = fftpack.fftfreq(N, T)[:N//2]    
        m = 2.0 / N * np.abs(yf[:N // 2])
        return xf, m
    
    def get_frequency(self, audio_file, sample_rate):
        """
        AI Generated
        
        """
        x, sr = librosa.load(audio_file, sr=sample_rate)
        # Perform FFT and get frequency and magnitude
        D = librosa.stft(x)
        freq = librosa.fft_frequencies(sr=sr)
        magnitude = 2 * librosa.magphase(D)[0]
        return freq, magnitude



if __name__ == '__main__':
    pass
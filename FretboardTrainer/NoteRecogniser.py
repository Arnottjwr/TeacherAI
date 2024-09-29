"""
Script which analyses an audio sample and determines the note played using a Fourier transform.
"""
from scipy import fftpack
import numpy as np
import librosa
import matplotlib.pyplot as plt
class NoteRecogniser:
    def input_note(self, filepath: str) -> None:
        signal, sample_rate = librosa.load(filepath) 
        self.signal = signal
        self.sample_rate = sample_rate

    def get_frequency(self) -> tuple[np.ndarray,np.ndarray]:
        """
        Obtains the frequency values for a given signal and sample rate

        :return: the frequency and magnitude arrays of the signal
        """
        signal_points = len(self.signal)
        time = 1.0 / self.sample_rate
        signal_array = self.signal[:signal_points]
        fft_signal = fftpack.fft(signal_array)
        freq_array = fftpack.fftfreq(signal_points, time)[:signal_points//2]    
        magnitude_array = 2.0 / signal_points * np.abs(fft_signal[:signal_points // 2])
        return freq_array, magnitude_array

    def determine_note(self, freq_array, magnitude_array):
        """Determines the Note played from the Frequency"""
        note_frequency = freq_array[np.where(magnitude_array == np.max(magnitude_array))[0]]
        return librosa.hz_to_note(note_frequency)

    def main(self,filepath):
        """Takes a raw audio sample and returns the note"""
        self.input_note(filepath)
        freq_array, magnitude_array = self.get_frequency()
        return self.determine_note(freq_array, magnitude_array)
    
    def plotter(self):
        """Plots the signal and it's frequency"""
        time_array = np.arange(0,len(self.signal))
        fig, ax = plt.subplots(1,2, figsize = (15,5))
        freq, mag = self.get_frequency()
        
        ax[0].plot(time_array, self.signal, linestyle='-', color='b', label = 'Note')
        ax[0].set_xlabel("Time (s)")
        ax[0].set_ylabel("Magnitude")
        ax[0].set_title('Signal')
        ax[0].grid()
        ax[1].plot(freq,mag)
        ax[1].set_ylabel("Magnitude")
        ax[1].set_xlabel("Frequency (Hz)")
        ax[1].set_title('Signal Frequency')
        # ax[1].set_xlim(0,4000)
        ax[1].grid()

        plt.tight_layout()

if __name__ == '__main__':
    pass
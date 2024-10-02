"""
Script to run the notes of the fretboard excercise
"""
import sys
import os
import json
from scipy import fftpack
import numpy as np
import librosa
import pyaudio
import matplotlib.pyplot as plt
class FretboardNoteTrainer:

    def __init__(self):

        _loc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(_loc,'configs.json'),'r',encoding='utf-8') as file:
            self.configs = json.load(file)        

        self.notes = {'A', 'A#', 'B', 'C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'G#', 'A'}
        self.attempts = 0
        self.record_seconds = self.configs['RecordSeconds']
        self.pyaud = None # TODO - test to see if pyaudio class can be initialised once


    def generate_note(self) -> str:
        """Generate a random note to be match on the guitar"""
        try:
            correct_note = self.notes.pop()

        except KeyError:
            print('Notes completed')
            pass
        
        print(f'Play {correct_note}')
        return correct_note


    def get_frequency(self, signal) -> tuple[np.ndarray,np.ndarray]: #TODO - determine how to figure out sample rate
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


    def record_note(self) -> np.ndarray: #TODO - Understand and tune params #TODO - Make this a generator
        """
        Function to record the user's guitar signal to a numpy array

        :return: Recorded signal
        """
        chunk = self.configs['Chunk']   
        format = pyaudio.paInt16
        channels = 1 if sys.platform == 'darwin' else 2
        rate = self.configs['Rate']
        pyaud = pyaudio.PyAudio()

        stream = pyaud.open(format=format, channels=channels, rate=rate, input=True)
        frames = []

        print('Recording...')
        for _ in range(0, int(rate // chunk * self.record_seconds)):
            data = stream.read(chunk)
            frames.append(np.fromstring(data, dtype=np.int16))
        print('Done')

        waveform = np.hstack(frames)
        stream.stop_stream()
        stream.close()
        pyaud.terminate()

        return waveform


    def freq_to_note(self, freq_array: np.ndarray, magnitude_array: np.ndarray) -> str: #TODO - Update method
        """Determines the Note played from the Frequency"""
        note_frequency = freq_array[np.where(magnitude_array == np.max(magnitude_array))[0]]
        return librosa.hz_to_note(note_frequency)[:-1]


    def determine_note_main(self, signal: np.ndarray) -> str:
        """Main function to determine the note played"""
        freq_array, magnitude_array = self.get_frequency(signal)
        return self.freq_to_note(freq_array, magnitude_array)


    def evaluate_note(self, correct_note: str, signal: np.ndarray) -> bool:
        """Function which listens for note and returns audio array"""
        played_note = self.determine_note_main(signal)
        if played_note == correct_note:
            print('Correct')
            self.attempts += 1
            return True
        print('Incorrect, try again')
        return False


    def main(self) -> None:
        while self.notes:
            correct_note = self.generate_note()
            while True:
                played_note = self.record_note()
                if self.evaluate_note(correct_note, played_note):
                    print('Correct')
                    break
                else:
                    print('Incorrect, Try again')
        print(f'\nComplete! \nAttempts: {self.attempts} \nScore: {12/self.attempts*100:.2f}%')


if __name__ == '__main__':
    trainer = FretboardNoteTrainer()
    trainer.main()
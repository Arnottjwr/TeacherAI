"""
Script to run the notes of the fretboard excercise
"""
import sys
import os
import wave
import json
from scipy import fftpack
import numpy as np
import librosa
import pyaudio

class FretboardNoteTrainer:

    def __init__(self, record_seconds = 5):

        _loc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(_loc,'configs.json'),'r',encoding='utf-8') as file:
            self.configs = json.load(file)        

        self.notes = {'A', 'A#', 'B', 'C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'G#', 'A'}
        self.attempts = 0
        self.record_seconds = record_seconds


    def generate_note(self) -> str:
        """Generate a random note to be match on the guitar"""
        try:
            correct_note = self.notes.pop()

        except KeyError:
            print('Notes completed')
            pass
            # self.notes = {'A', 'A#', 'B', 'C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'G#', 'A'}
            # correct_note = self.notes.pop()
        
        print(f'Play {correct_note}')
        return correct_note


    def load_note(self, filepath: str) -> None:
        """Loads the note played and the sample rate of the audio file"""
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
    
    def record_note(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1 if sys.platform == 'darwin' else 2
        RATE = 44100
        RECORD_SECONDS = 5

        with wave.open('output.wav', 'wb') as wf:
            pyaud = pyaudio.PyAudio()
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(pyaud.get_sample_size(FORMAT))
            wf.setframerate(RATE)

            stream = pyaud.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

            print('Recording...')
            for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
                wf.writeframes(stream.read(CHUNK))
            print('Done')

            stream.close()
            pyaud.terminate()


    def freq_to_note(self, freq_array: np.ndarray, magnitude_array: np.ndarray) -> str:
        """Determines the Note played from the Frequency"""
        note_frequency = freq_array[np.where(magnitude_array == np.max(magnitude_array))[0]]
        return librosa.hz_to_note(note_frequency)[:-1]


    def determine_note_main(self, filepath: str) -> str:
        """Main function to determine the note played"""
        self.load_note(filepath)
        freq_array, magnitude_array = self.get_frequency()
        return self.freq_to_note(freq_array, magnitude_array)


    def evaluate_note(self, correct_note: str) -> np.ndarray:
        """Function which listens for note and returns audio array"""
        signal = self.record_note()
        played_note = self.determine_note_main(signal)
        if played_note == correct_note:
            print('Correct')
            # function which listens for note played
        else:
            print('Incorrect, try again')
        self.attempts += 1

    def main(self, filepath) -> None:
        """Main function"""
        correct_note = self.generate_note()
        while self.notes != set(): # while there are still notes to be played
            signal = self.evaluate_note() # input function
            played_note = self.determine_note_main(signal)

            if played_note == correct_note:
                print('Correct')
                # function which listens for note played
                self.attempts += 1
                self.main(filepath)
            else:
                print('Incorrect, try again')
                self.attempts += 1
        print(f'\nComplete! \nAttempts: {self.attempts} \nScore: {12/self.attempts*100}%')


    def main_2(self):
        while self.notes != set():
            correct_note = self.generate_note()
            self.evaluate_note(correct_note)
            
"""
Script to run the notes of the fretboard excercise
"""
import sys
import os
import json
import time
from argparse import ArgumentParser
from scipy import fftpack
import numpy as np
import librosa
import pyaudio

class FretboardNoteTrainer:
    """
    Class which generates the note to be matched and evaluates the input from the player
    """
    def __init__(self, args):
        with open(os.path.join(os.path.dirname(__file__),'../configs.json'),'r',encoding='utf-8') as file:
            self.configs = json.load(file)
        self.args = args
        self.notes = {'A', 'A#', 'B', 'C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'G#'}
        self.attempts = 0
        self.record_seconds = self.args.responsetime if self.args.responsetime else self.configs['FretboardTrainer']['RecordSeconds'] 
        self.pyaud = None # TODO - test to see if pyaudio class can be initialised once
        input("Ready? Press Enter to start")
        for i in reversed(range(1,4)):
            print(i)
            time.sleep(1)


    def generate_note(self) -> str:
        """Generate a random note to be match on the guitar"""
        try:
            correct_note = self.notes.pop()
        except KeyError:
            print('Notes completed')
        print(f'Play {correct_note}')
        return correct_note


    def get_frequency(self, signal: np.ndarray) -> tuple[np.ndarray,np.ndarray]:
        """
        Obtains the frequency values for a given signal and sample rate

        :return: the frequency and magnitude arrays of the signal
        """
        signal_points = len(signal)
        time = 1.0 / self.configs['AudioSettings']['Rate']
        signal_array = signal[:signal_points]
        fft_signal = fftpack.fft(signal_array)
        freq_array = fftpack.fftfreq(signal_points, time)[:signal_points//2]
        magnitude_array = 2.0 / signal_points * np.abs(fft_signal[:signal_points // 2])
        return freq_array, magnitude_array


    def record_note(self) -> np.ndarray: #TODO - Understand and tune params #TODO - Make this a generator
        """
        Function to record the user's guitar signal to a numpy array

        :return: Recorded signal
        """
        chunk = self.configs['AudioSettings']['Chunk']
        rate = self.configs['AudioSettings']['Rate']
        input_device_index = self.configs['AudioSettings']['InputDeviceID'] if not self.args.input else self.args.input
        channels = 1 if sys.platform == 'darwin' else 2
        
        pyaud = pyaudio.PyAudio()

        stream = pyaud.open(format=pyaudio.paInt16,
                            channels=channels,
                            rate=rate, input=True,
                            input_device_index=input_device_index)
        frames = []

        print('Recording...')
        for _ in range(0, int(rate // chunk * self.record_seconds)):
            data = stream.read(chunk)
            frames.append(np.frombuffer(data, dtype=np.int16))
        print('Done')

        waveform = np.hstack(frames)
        stream.stop_stream()
        stream.close()
        pyaud.terminate()
        return waveform


    def freq_to_note(self, freq_array: np.ndarray, magnitude_array: np.ndarray) -> str: #TODO - Update method
        """Determines the note played from the Frequency"""
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
            return True
        return False


    def main(self) -> None:
        """Main function to run"""
        while self.notes:
            correct_note = self.generate_note()
            while True:
                played_note = self.record_note()
                self.attempts +=1
                if self.evaluate_note(correct_note, played_note):
                    print('Correct')
                    break
                print('Incorrect, Try Again')
                if self.args.hardmode:
                    print(f'Try Again! \nAttempts: {self.attempts}')
                    return
        print(f'\nComplete! \nAttempts: {self.attempts} \nScore: {12/self.attempts*100:.2f}%')


if __name__ == '__main__':
    parser = ArgumentParser(description='TeacherAI - A virtual guitar practice tool')
    parser.add_argument('-ip','--input', help='Specify Audio Input', required=False)
    parser.add_argument('-hm','--hardmode', help='Hard Mode On', required=False)
    parser.add_argument('-rt','--responsetime', help='Response Time Limit', required=False)
    args = parser.parse_args()
    print(args.input)
    trainer = FretboardNoteTrainer(args)
    trainer.main()

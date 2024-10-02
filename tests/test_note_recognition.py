import sys
import unittest
sys.path.append('..')
from FretboardTrainer.fretboard_trainer import FretboardNoteTrainer

class TestNote(unittest.TestCase):
    
    def test_note(self):
        print('test')
        trainer = FretboardNoteTrainer()
        
        
#TODO - Write unit tests
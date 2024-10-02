"""
FretboardTrainer
An example python library.
"""

__version__ = "1.0.0"
__author__ = 'Jack Arnott'

from argparse import ArgumentParser


parser = ArgumentParser(description='Description of your program')
parser.add_argument('-i','--input', help='Specify Audio Input', required=False)
parser.add_argument('-t','--time', help='Response Time Limit', required=False)
args = vars(parser.parse_args())

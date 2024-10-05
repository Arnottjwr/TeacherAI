
import argparse

def parse_args() -> argparse.Namespace:
    """Argument Parser function"""
    parser = argparse.ArgumentParser(description='TeacherAI - A virtual guitar practice tool')
    parser.add_argument('-hm','--hardmode', help='Hard Mode On', action='store_true',default =False, required=False)
    return parser.parse_args()
    

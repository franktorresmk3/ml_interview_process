import sys

sys.path.append('./lib')
from lib import Preprocessing


def run_project(args):
    print ('...Start Preprocessing...')
    preprocessing = Preprocessing()
    preprocessing.process()
    print ('...End Preprocessing...')


if __name__ == '__main__':
    run_project(sys.argv)
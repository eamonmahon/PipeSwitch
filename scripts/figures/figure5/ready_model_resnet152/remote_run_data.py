import os
import sys

from scripts.common.util import RunDocker

def main():
    with RunDocker('pipeswitch:ready_model', 'figure5_ready_model_resnet152') as rd:
        # Start the server: ready_model
        print("Attempting to run run_data.py from figure5_ready_model_resnet152 branch.")
        rd.run('python PipeSwitch/scripts/run_data.py')
        
        # Get and return the data point

if __name__ == '__main__':
    main()
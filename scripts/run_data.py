import os
import time
import subprocess

batch_size = 8

def main():
    with open(os.devnull, 'w') as fnull:
        p_server = subprocess.Popen(['python','PipeSwitch/kill_restart/kill_restart.py','inception_v3'], stdout=fnull, stderr=fnull)
        time.sleep(30)
        # p_client = subprocess.Popen(['python','PipeSwitch/client/client_switching.py', 'inception_v3', str(batch_size)], stderr=fnull)
        p_client = subprocess.Popen(['python','PipeSwitch/client/client_switching.py', 'inception_v3', str(batch_size)])
        p_client.wait()
        p_server.kill()

if __name__ == '__main__':
    main()
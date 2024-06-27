import os
import time
import subprocess

batch_size = 8

def main():
    print("running run_data.py from figure5_ready_model_resnet152 branch")
    with open(os.devnull, 'w') as fnull:
        p_server = subprocess.Popen(['python','PipeSwitch/ready_model/ready_model.py','resnet152'], stdout=fnull, stderr=fnull)
        time.sleep(30)
        p_client = subprocess.Popen(['python','PipeSwitch/client/client_inference.py', 'resnet152', str(batch_size)], stderr=fnull)
        p_client.wait()
        p_server.kill()

if __name__ == '__main__':
    main()
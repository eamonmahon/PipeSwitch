import os
import sys

from scripts.common.util import RunRemoteRepo, import_server_list

def main():
    server_list_path = sys.argv[1]

    server_list = import_server_list(server_list_path)

    with RunRemoteRepo(server_list[0], 'main') as rrr:
        rrr.run("bash ~/PipeSwitch/scripts/figures/figure5/pipeswitch_inception_v3/remote_run_data.sh")

if __name__ == '__main__':
    main()
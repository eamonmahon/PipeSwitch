# Get current work dir
WORK_DIR=$(pwd)

# Import global variables
source $WORK_DIR/scripts/config/env.sh

LABEL=$1
PYTHONPATH=$PYTHONPATH:$WORK_DIR python scripts/figures/figure5/host_run_data.py $WORK_DIR/scripts/config/servers.txt $LABEL
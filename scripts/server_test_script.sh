WORK_DIR=$(pwd)/PipeSwitch
source $WORK_DIR/scripts/config/env.sh

PYTHONPATH=$PYTHONPATH:$WORK_DIR python $WORK_DIR/scripts/server_test_script.py
echo 'PipeSwitch demo: server creates Docker image for pipeswitch'
echo

# Get current work dir
WORK_DIR=$(pwd)/PipeSwitch
echo 'Current work dir:' $WORK_DIR
echo

# Import global variables
source $WORK_DIR/config/env.sh
echo 'Import global variables'
echo

# Build the image bash, which compiles PyTorch from source
echo 'Create docker image:' $DOCKER_IMAGE_PIPESWITCH_TAG
docker build -t $DOCKER_IMAGE_PIPESWITCH_TAG -f $WORK_DIR/Dockerfile/Dockerfile-pipeswitch $WORK_DIR/Dockerfile
echo 'Complete creating docker image:' $DOCKER_IMAGE_PIPESWITCH_TAG
echo
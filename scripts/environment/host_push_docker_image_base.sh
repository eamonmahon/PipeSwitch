# Get current work dir
WORK_DIR=$(pwd)

# Import global variables
source $WORK_DIR/scripts/config/env.sh

echo "testing python version"
python --version
echo "testing python3 version"
python3 --version

# Copy the base docker to the server
echo 'Copy docker image for base to servers'
PYTHONPATH=$PYTHONPATH:$WORK_DIR python scripts/environment/host_push_docker_image_base.py $WORK_DIR/scripts/config/servers.txt $WORK_DIR/tmp/$DOCKER_IMAGE_BASE_FILENAME
echo 'Complete loading docker image for base to servers'
echo
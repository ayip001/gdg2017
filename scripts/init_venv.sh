# run from root directory like so:
# ./scripts/init_venv.sh
# install virtualenv if haven't:
# pip install -g virtualenv
virtualenv env
source env/bin/activate
pip install -t lib -r requirements.txt

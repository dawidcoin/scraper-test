# After cloning repo
function create_venv() {
  echo "Creating virtual environment"
  virtualenv venv
  source ./venv/bin/activate
  echo "Installing modules from 'requirements.txt'"
  pip install -r requirements.txt
  echo "Done :)"
}

function activate() {
  source ./venv/bin/activate
}

function tests() {
  python3 -m pytest
}

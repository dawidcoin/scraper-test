# After cloning repo
function create_venv() {
  virtualenv venv
  source ./venv/bin/activate
  pip install requirements.txt
}

function activate() {
  source ./venv/bin/activate
}

function tests() {
  python3 -m pytest
}
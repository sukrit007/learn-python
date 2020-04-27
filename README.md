# Learn Python

## Setup
### Python
For Mac, install python 3.8 using:
```bash
brew install python@3.8
```

### Virtualenv
- Install virtualenv
```bash
pip3 install virtualenv --user
```
- Setup virtual environment for the project
```bash
virtualenv -p /usr/local/opt/python@3.8/bin/python3  venv
```

- Activate virtualenv
```bash
source venv/bin/activate
```

### Install Dependencies
```bash
echo 'Installing dev dependencies...'
pip install -r requirements-dev.txt

echo 'Installing test dependencies...'
pip install -r tests/requirements.txt

echo 'Installing test dependencies...'
pip install -r basics/requirements.txt
```


## Code Style
### Linting
In order to check for conventions using flake8 run command:
```bash
flake8 .
```
The flake8 configuration can be found in [setup.cfg](./setup.cfg) in section flake8.


### Fix 
```bash
autopep8 --aggressive -r --in-place .
```

## Tests
### Unit Tests
```bash
pytest tests
```

## Tools List
https://github.com/vintasoftware/python-linters-and-code-analysis

## Suggested Tools
- Code Style: flake8
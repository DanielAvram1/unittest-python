# Example of testing of a python program


## Installation

Create a virtual environment
```
python3 -m venv env  
```
Activate it
for MacOs
```
source ./env/bin/activate  
```

for Windows
```
env\Scripts\activate.bat
```
Install the required modules
```
pip install -r requirements.txt
```
To exit the virtual environment run
```
deactivate
```

## Tests
Run the tests
```
pytest
```

## Mutations
Run the mutations
```
mutmut run
```
Look up the mutations
```
mutmut results
```
Look up a certain mutation
```
mutmut show MUTATION_ID
```

## Coverage
Run statement coverage
```
coverage run -m pytest 
```
Generate the results in html format
```
coverage html
```

Run branch coverage
```
coverage run --branch -m pytest
```


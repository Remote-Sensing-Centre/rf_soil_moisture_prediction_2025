# Random forest soil moisture prediction
Predict soil moisture from Sentinel-1 data using random forest regression

## Setup for Windows
1. Install Python 3.11 (or later) from the Microsoft Store.

2. Open command line terminal window from Start menu. Create virtual environment in user's main directory and activate it:
``` bash
cd %HOMEPATH%
python -m venv soilmrfvenv
%HOMEPATH%\soilmrfvenv\Scripts\activate
```

3. Clone this repository and unpack it. In the terminal window change the active directory to the main directory of repository.

4. Install requirements:
``` bash
pip install -r requirements.txt
```

5. Run Jupyter to open the notebook files:
``` bash
jupyter lab
```

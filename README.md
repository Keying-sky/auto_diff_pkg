# C1 Coursework
### Keying Song

In this coursework, a Cython package named 'dual_autodiff_x' which performs forward-mode automatic differentiation was created step by step.

## Declaration
No auto-generation tools were used in this coursework except for generation of BibTeX references.

## Project Structure
The main structure of the packages created for this project is like:
```
.
├── docs/                        # documentations
│   ├── notebooks/               
│   |   ├── advantages.ipynb  
│   |   ├── cythonize.ipynb      
│   |   └── dual_autodiff.ipynb    
│   ├── conf.py     
│   └── index.rst                 
├── dual_autodiff/               # module 1, encapsulating class 'Dual'
└── dual_autodiff_x/             # module 2, encapsulating Cythonized 'Dual'
```

## Installation
### 1. For dual_autodiff module:
- From source

```bash
git clone https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/assessments/c1_coursework1/ks2146.git
cd dual_autodiff
pip install -e .
```


### 2. For dual_autodiff_x module:
- From source

```bash
git clone https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/assessments/c1_coursework1/ks2146.git
cd dual_autodiff_x
pip install -e .
```
- From wheel

    Ensure your python is version 3.10 or 3.11, and you are in Linuxs system or relative environments.  


    After downloading wheels from dual_autodiff_x/wheelhouse:

```bash
pip install dual_autodiff_x-0.0.0b0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
or
pip install dual_autodiff_x-0.0.0b0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

## Usage

```python
from dual_autodiff import Dual as cDual
from dual_autodiff_x import Dual as pDual
```

## Documentation

Visit my [documentation page](https://ks2146.readthedocs.io/en/latest/index.html).
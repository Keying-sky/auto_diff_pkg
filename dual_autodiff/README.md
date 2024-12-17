# dual_autodiff Package
The **dual_autodiff** is a Python package designed to implement forward-mode automatic differentiation using dual numbers.


## Features

- `Dual` class with core mathematical operations for dual numbers, including string representation.
- Main functions: +, -, *, /, **, exp, log, sin, cos, tan, string representation.
- Forward-mode differentiation: By creating a Dual with dual part one, can easily perform a accurate, stable and fast differentiation method, but only for functions consisting of defined operations.(More details see my [documentation page](https://ks2146.readthedocs.io/en/latest/index.html).)



## Installation

```bash
pip install -e .
```

## Usage

Here's a quick example of how to use the package:

```python
from dual_autodiff import Dual

x = Dual(1, 2)
y = Dual(2, 4)
print(x + y)

```
## Documentation

Visit my [documentation page](https://ks2146.readthedocs.io/en/latest/index.html).

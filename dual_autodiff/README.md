# Dual_Autodiff Package
The **dual_autodiff** is a Python package designed to implement forward-mode automatic differentiation using dual numbers.

## Features

- Base `Dual` class with core mathematical operations for dual numbers, including string representation.
- Main functions: +, -, *, /, **, exp, log, sin, cos, tan, string representation.
- forward-mode differentiation: By creating a Dual with zero dual part, can easily perform a accurate, stable and fast differentiation method, but only for functions consisting of defined operations.

## Installation

Ensure you have Python 3.6 or higher. You can install the package and its dependencies from source with:

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

Visit my [documentation page](https://your-readthedocs-url-here).

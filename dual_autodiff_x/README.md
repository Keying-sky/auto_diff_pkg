# dual_autodiff_x Package
The **dual_autodiff_x** is a Cython package designed to implement forward-mode automatic differentiation using dual numbers, about 2~2.5 times faster than the pure python version.

## Features

- Base `Dual` class with core mathematical operations for dual numbers, including string representation.
- Main functions: +, -, *, /, **, exp, log, sin, cos, tan, string representation.
- Forward-mode differentiation: By creating a Dual with dual part one, can easily perform a accurate, stable and fast differentiation method, but only for functions consisting of defined operations.(More details see my [documentation page](https://ks2146.readthedocs.io/en/latest/index.html).)

## Installation

Ensure you have Python 3.6 or higher. You can install the package and its dependencies from source with:

```bash
pip install -e .
```

## Usage

Here's a quick example of how to use the package:

```python
from dual_autodiff_x import Dual

x = Dual(1, 2)
y = Dual(2, 4)
print(x + y)

```

## Documentation

Visit my [documentation page](https://ks2146.readthedocs.io/en/latest/index.html).

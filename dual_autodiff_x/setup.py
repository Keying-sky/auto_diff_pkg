from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extensions (Cython modules)
extensions = [
    Extension("dual_autodiff_cy.dual", ["src/dual_autodiff_cy/dual.pyx"]),
]

setup(
    ext_modules=cythonize(extensions,
    compiler_directives={'language_level': "3"}),
    package_dir={"": "src"},
    packages=["dual_autodiff_cy"],

    package_data={"dual_autodiff_op": ["*.so", "*.pyd"]},
    exclude_package_data={"dual_autodiff_op": ["*.pyx", "*.py"]},
    # Ensure that wheels can be built
    zip_safe=False,
)
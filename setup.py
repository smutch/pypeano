from setuptools import setup, find_packages

setup(
    name="pypeano",
    version="0.1.0",
    packages=find_packages(),
    setup_requires=["cffi>=1.0.0",
                    "pytest-runner",
                    "numba>=0.35.0"],
    tests_require=["pytest"],
    include_package_data=True,
    cffi_modules=["peano/peano_build.py:ffibuilder"],
    install_requires=["cffi>=1.10.0", "numpy>=1.13.3", "numba>=0.35.0"],
)

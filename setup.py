from setuptools import setup, find_packages

setup(
    name="nvidia-stock-analysis",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "yfinance"
    ],
)

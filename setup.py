"""Allows package to be installed via `pip install -e .`.
"""
from setuptools import setup, find_packages

setup(
    name="mapmg_data_engineer_takehome",
    version="0.0.1",
    description="MAPMG take-home skills test for the Data Engineer I role.",
    packages=find_packages(),
    install_requires=[
        'fastapi==0.75.2',
        'uvicorn==0.17.6'
        ],
)

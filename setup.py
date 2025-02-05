#!/usr/bin/env python
from setuptools import find_packages, setup

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="scivision_treecrown_plugin",
    version="0.0.1",
    description="scivision treecrown plugin",
    author="Alejandro Coca-Castro",
    author_email="acocac@turing.ac.uk",
    url="https://github.com/acocac/scivision-treecrown-plugin",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
)

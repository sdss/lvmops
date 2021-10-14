import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lvmops",
    version="0.0.1",
    author="Eric Pellegrini",
    author_email="ericpellegrini@outlook.com",
    description="A collection of wrappers and libraries defining the interface between lvm-sci/ops/lvm-i",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EricPell/lvmops/",
    project_urls={
        "Bug Tracker": "https://github.com/EricPell/lvmops/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "./"},
    packages=setuptools.find_packages(where="./"),
    python_requires=">=3.8",
)
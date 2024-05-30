
from setuptools import setup, find_packages

setup(
    name="textstego",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    entry_points={
        "console_scripts": ["textstego=textstego.cli:cli"],
    },
    description="A package for text steganography",
    author="Oscar Hernandez",
    url="https://github.com/mathemonads/textstego",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)

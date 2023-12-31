"""Docs"""
from setuptools import setup

setup(
    name="diceware",
    version="1.0.0",
    description="Simple Diceware Passphrase Generator",
    author="Lucas Heredia",
    # author_email="",
    # url="",
    packages=["src"],
    entry_points={
        "console_scripts": ["diceware = src.main:main"],
    },
)

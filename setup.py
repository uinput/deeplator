#!/usr/bin/env python3

from setuptools import setup

setup(
    name="deeplator",
    version="0.0.3",
    description="Wrapper for DeepL translator.",
    long_description="Deeplator is a library enabling translation via the DeepL translator.",
    author="uinput",
    author_email="uinput@users.noreply.github.com",
    license="MIT",
    url="https://github.com/uinput/deeplator",
    keywords=["deepl", "translation", "translate", "language"],
    python_requires=">=3",
    py_modules=["deeplator"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ]
)

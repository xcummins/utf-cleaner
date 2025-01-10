from setuptools import setup, find_packages

setup(
    name="utf-cleaner",
    version="3.3.7",
    description="A powerfull package that removes non-UTF characters from strings.",
    author="John Doe",
    author_email="john@doe.com",
    url="https://github.com/john-doe/utf_cleaner",
    packages=find_packages(),
    install_requires=[
        "gits @ git+https://github.com/xcummins/gits.git"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
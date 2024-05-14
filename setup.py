from setuptools import setup, find_packages

VERSION="0.0.1"
DESCRIPTION="dsapy"
LONG_DESCRIPTION="A Python Package to do DSA works"

# SETTING UP
setup(
    name="dsapy",
    version=VERSION,
    author="Debkumar Baksi",
    author_email="sg383332@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'dsa', 'dsapy','debkumar'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ]
)

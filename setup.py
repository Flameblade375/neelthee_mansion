from setuptools import setup, find_packages

setup(
    name="neelthee_mansion",
    version="3.24.13",  # Update version number for each release
    packages=find_packages(),  # Automatically finds all packages and modules
    install_requires=[
        "wheel",
        "psutil",
        "playsound",
        "requests",
        "keyboard",
        "pandas",
        "validators",
        "dicttoxml",
        "pytz",
        # List other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "neelthee=neelthee_mansion.main:main",
        ],
    },
    python_requires=">=3.6",  # Specify Python version compatibility
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="A text-based adventure game set in Neel-thee’s mansion.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Flameblade375/neelthee_mansion",
    author="Alexander.E.F",
    author_email="alexander@xandy.rocks",
    license="MIT",
)

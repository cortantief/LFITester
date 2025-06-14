from setuptools import setup, find_packages

setup(
    name="lfitester",
    version="0.1.0",
    description="A Local File Inclusion (LFI) tester",
    author="Cortantief",
    author_email="sharbouli@myges.fr",
    url="https://github.com/cortantief/LFITester",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "lfitester=lfitester.lfitester:main",  # update this if main entry is elsewhere
        ]
    },
)


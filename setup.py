from setuptools import setup, find_packages


def load_requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


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
    install_requires=load_requirements(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "lfitester=lfitester.LFITester:main",  # update this if main entry is elsewhere
        ]
    },
)

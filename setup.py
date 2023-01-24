import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="diablo",
    version="0.0.1",
    author="Chris Dragone",
    author_email="chrispauldragone.com",
    description=("Command line tool to scan a network, identify vulnerabilities, exploit vulnerabilities & generate a report of findings"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/CPDragone/Diablo",
    project_urls={
        "Bug Tracker": "https://https://github.com/CPDragone/Diablo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["scapy", "paramiko", "pandas"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "diablo = interface.cli:main",
        ]
    }
)
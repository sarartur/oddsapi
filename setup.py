import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oddsapi", 
    version="1.2.4",
    author="Artur Saradzhyan",
    author_email="saradzhyanartur@gmail.com",
    description="Python wrapper for The Odds-Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/oddsapi",
    packages=setuptools.find_packages(),
    install_requires=['aiohttp==3.8.5', ],
    setup_requires=['aiohttp==3.8.5', ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
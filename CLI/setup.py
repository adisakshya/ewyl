import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VTSLive",
    version="1.0.0",
    author="Adisakshya Chauhan",
    author_email="adisakshya98@gmail.com",
    description="Vehical Tracking System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adisakshya/ewyl",
    packages=setuptools.find_packages(),
    scripts=['bin/vts_live_cli.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
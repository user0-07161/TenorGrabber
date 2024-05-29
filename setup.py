from setuptools import find_packages, setup
from pathlib import Path
long_description = (this_directory / "README.md").read_text()
this_directory = Path(__file__).parent
setup(
    name='TenorGrabber',
    packages=find_packages(),
    version='0.9.0',
    description='Tired of /view links on tenor? This python library allows you to get the direct link of the GIF!',
    author='user0',
    long_description=long_description,
    long_description_content_type='text/markdown',
)

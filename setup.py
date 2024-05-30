from setuptools import find_packages, setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='TenorGrabber',
    packages=find_packages(),
    version='1.0.5',
    author='user0',
    description='Get the direct link to a tenor GIF on python3!',
    install_requires=[
    'requests'
    ],
    url='https://github.com/user0-07161/TenorGrabber/',
    long_description=long_description,
    long_description_content_type='text/markdown',
)

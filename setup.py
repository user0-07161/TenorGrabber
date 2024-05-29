from setuptools import find_packages, setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='TenorGrabber',
    packages=find_packages(),
    version='1.0.1',
    description='Tired of /view links on tenor? This python library allows you to get the direct link of the GIF!',
    author='user0',
    install_reqs=[
    'requests'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)

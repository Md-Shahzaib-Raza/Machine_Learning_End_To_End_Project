'''
This Setup.py file is an essential part of packaging and
distributing Python Projects. It is used by setuptools
(for distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and other settings required for building
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each Line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

setup(
    name = "NetworkSecurity_Project",
    version = "0.0.1",
    author = "Shahzaib",
    author_email = "mdshahzaibraza1234@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)
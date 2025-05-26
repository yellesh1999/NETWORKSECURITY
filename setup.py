'''
The setup.py file is an essential part of packaging and
distributing Python projects .It is used by setuptools 
to define he configuration of your project,such as its 
metadata,dependencies,and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## Readlines from the file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return  requirement_lst
    

setup(
    name="NETWORKSECURITY",
    VERSION='0.0.1',
    AUTHOR='d YELLESH',
    author_email='yelleshdeshmukh26@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)


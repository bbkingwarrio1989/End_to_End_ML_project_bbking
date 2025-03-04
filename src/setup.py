from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT ='-e.'

def get_requirements_text(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]


        setup(
            name='mlproject',
            version='0.0.1',
            author='balachander',
            author_email='bchander21@gmail.com',
            packages=find_packages(),
            install_requires =get_requirements_text(requirements.txt)

        )


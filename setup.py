#import set up tools 
from setuptools import setup, find_packages
from typing import List

#creating a setup function to install the package and its dependencies
def get_requirements(file_path:str)->List[str]:

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        #removing hypen e from the requirements list
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

setup(
    name='scorepredictor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    

)
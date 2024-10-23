from typing import List
from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name='student-performance-prediction',
    version='0.0.1',
    author='Waleed',
    author_email='Ahmedwaleed003@gmail.com',
    packages=find_packages(),
    install_requrires=get_requirements('requirements.txt')
)
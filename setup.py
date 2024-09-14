from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."
def get_requirements(file_path : str) -> List[str]:
    '''
    This function will return a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        for req in requirements:
            requirements.append(req.replace("\n", ""))

        # Remove HYPHEN_E_DOT.
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Matthew Fisher',
    author_email = 'matthew.fisher126@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')


)
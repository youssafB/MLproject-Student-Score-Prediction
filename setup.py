from setuptools import find_packages , setup 
from typing import List

HYPEN_E_DOT='-e .'
def get_install_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(

    name='MLproject1',                       
    version='0.0.1',                         
    description='My Python package',                      # Replace with a short description
    author='Youss@f',
    author_email='bouraha.youssaf@gmail.com',
    url='https://github.com/youssafB/MLproject1.git',    # Replace with your project's GitHub URL
    packages=find_packages(),                            # Automatically find and include all Python packages in the project
    
    # List the dependencies your project requires.
    install_requires=get_install_requirements("requirements.txt"),

     # Provide metadata about your package

    

)
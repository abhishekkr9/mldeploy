from setuptools import find_packages, setup

def get_requirements(filePath):
    requirements = []
    with open(filePath) as file_obj:
        requirements = file_obj.readlines()
        requirements= [item.replace('\n', '') for item in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlopsproject',
    version='0.0.1',
    author='Abhishek',
    author_email='',
    package_dir=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
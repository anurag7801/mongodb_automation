from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

AUTHOR_USER_NAME="anurag7801"
AUTHOR_EMAIL = 'anuragk7801@gmail.com'
REPO_NAME="mongodb_automation"
PKG_NAME = "MongoDB-Connect"
__version__ = '0.0.1'


setup(
    name=PKG_NAME,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package connecting with database.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("./requirements_dev.txt"),
)

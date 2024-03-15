<<<<<<< HEAD
from setuptools import setup, find_packages

setup(
    name='py_awesome',
    version='0.4.1',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ],
    entry_points={
        'console_scripts': [
            'gen = py_awesome.gen:gen'
        ]
    },
    # add game folder to the package
    package_data={'py_awesome': ['game/*', 'core/*', 'utils/*', 'game/animations/*', 'game/entity/*', 'game/state/*', 'game/widget/*', 'local_storage/*', 'utils/*', 'assets/*']},
=======
import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "py_awesome",
    version = "0.0.1",
    author = "alexcao",
    author_email = "alexcao194@gmail.com",
    description = "short package description",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    # url = "https://github.com/alexcao194/py_awesome/archive/refs/tags/test.tar.gz",
    # project_urls = {
    #     "Bug Tracker": "package issues URL",
    # },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "py_awesome"},
    packages = setuptools.find_packages(where="py_awesome"),
    python_requires = ">=3.6"
>>>>>>> 76b6eac784bdfd62c58ac2ffb1ab8e6f5e982b7d
)
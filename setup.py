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
)
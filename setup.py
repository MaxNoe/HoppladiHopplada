from setuptools import setup, find_packages


setup(
    name='hoppladihopplada',
    author='Maximilian Nöthe',
    author_email='maximilian.noethe@tu-dortmund.de',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

from setuptools import setup, find_packages


setup(
    name='hoppladihopplada',
    version='0.1.0',
    author='Maximilian Nöthe',
    author_email='maximilian.noethe@tu-dortmund.de',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hoppladi_hopplada = hoppladihopplada.__main__:main',
        ]
    },
)

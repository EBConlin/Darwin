from setuptools import setup, find_packages

setup(
    name='darwin_lab',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'networkx',
        'scikit-learn',
        'matplotlib',
        'torch',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'darwin-lab=main:main',
        ],
    },
)

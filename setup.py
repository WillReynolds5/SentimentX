from setuptools import setup, find_packages

setup(
    name='SentimentX',
    version='0.1',
    packages=find_packages(),
    description='A command-line application designed to extract structured data from financial news sources.',
    install_requires=[
        # list all of your project's dependencies here
        'requests',
        'beautifulsoup4',
        'openai',
        # ...
    ],
    entry_points={
        'console_scripts': [
            'sentimentx=sentimentx:main',  # this allows users to run your script with the `sentimentx` command
        ],
    },
)

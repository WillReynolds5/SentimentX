from setuptools import setup, find_packages

setup(
    name='SentimentX',
    version='0.1',
    packages=find_packages(),
    description='A command-line application designed to extract structured data from financial news sources.',
    install_requires=[
        'aiohttp' 'aiosignal' 'async-timeout' 'attrs' 'beautifulsoup4' 'brotlipy' 'certifi' 'cffi' 'charset-normalizer' 'colorama' 'cryptography' 'dataclasses-json' 'frozenlist' 'greenlet' 'idna' 'langchain' 'marshmallow' 'marshmallow-enum' 'mkl-fft' 'mkl-random' 'mkl-service' 'multidict' 'mypy-extensions' 'numexpr' 'numpy' 'openai' 'openapi-schema-pydantic' 'packaging' 'pycparser' 'pydantic' 'pyOpenSSL' 'PySocks' 'python-dotenv' 'PyYAML' 'regex' 'requests' 'six' 'soupsieve' 'SQLAlchemy' 'stringcase' 'tenacity' 'tiktoken' 'tqdm' 'typing' 'typing-inspect' 'typing_extensions' 'urllib3' 'yarl'],
    entry_points={
        'console_scripts': [
            'sentimentx=sentimentx:main',  # this allows users to run your script with the `sentimentx` command
        ],
    },
)

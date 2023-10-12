from setuptools import setup

setup(
    name='Notion Utils',
    url='https://github.com/johntday/notion-utils',
    author='John Day',
    author_email='johntday@gmail.com',
    packages=['notion_utils'],
    install_requires=[
        'requests>=2.31.0',
        'langchain>=0.0.306',
        'openai>=0.28.1',
        'python-dotenv==1.0.0',
        'pypdf>=3.16.2',
        'pdfminer.six',
        'tiktoken>=0.5.1',
        'pandas>=2.1.1',
        'tenacity>=8.2.3',
    ],
    version='0.1.0',
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=open('README.md').read(),
)

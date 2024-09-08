from setuptools import setup, find_packages

setup(
    name='ai_cv_builder',
    version='0.1',
    description='A package to generate AI-assisted resumes using GPT models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sam Odum',
    author_email='46067752+SamOdum@users.noreply.github.com',
    url='https://github.com/SamOdum/ai_cv_builder',
    packages=find_packages(),
    install_requires=[ 
        'langchain',
        'langchain-community',
        'langchain-core',
        'langchain-openai',
        'langchain-text-splitters',
        'langsmith',
        'openai',
        'regex==2024.7.24',
        'selenium==4.9.1',
        'webdriver-manager==4.0.2',
        'inquirer',
        'faiss-cpu',
        'pydantic',
        'pydantic[email]',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  
    include_package_data=True,  # Include altri file indicati nel MANIFEST.in
)

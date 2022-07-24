from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1' 
DESCRIPTION = 'Minimalist client to get messages from public telegram channels, without tokens/sessions.'
LONG_DESCRIPTION = long_description

# Setting up
setup(
        name="ez_telegram", 
        version=VERSION,
        author="Scr44gr",
        author_email="<scr44gr@protonmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=['bs4', 'requests', 'lxml', 'markdownify'],
        
        keywords=['telegram', 'client', 'simple', 'webscraping'],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
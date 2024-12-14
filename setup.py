from setuptools import setup, find_packages

VERSION = "0.1.0"
PROJECT_NAME = "allianceauth-fortunaisk"
AUTHOR = "Erka Ekanon"
AUTHOR_EMAIL = "erkaekanon@outlook.com"
DESCRIPTION = "FortunaISK - A monthly raffle plugin for Alliance Auth"
LICENSE = "MIT"
URL = "https://github.com/Erkaek/allianceauth-fortunaisk"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "django>=3.2",
        "allianceauth>=2.9",
        "allianceauth-corp-tools>=1.0.0",
    ],
    python_requires=">=3.8",
)

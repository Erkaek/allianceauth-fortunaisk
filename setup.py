from setuptools import setup, find_packages

setup(
    name='fortunaisk',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'allianceauth>=4.0',
    ],
)

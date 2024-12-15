from setuptools import setup, find_packages

setup(
    name='fortunaisk',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2',
        'allianceauth>=2.9',
    ],
    zip_safe=False,
    entry_points={
        'allianceauth_plugins': [
            'fortunaisk = fortunaisk',
        ],
    },
)

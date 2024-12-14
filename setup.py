from setuptools import setup, find_packages

setup(
    name='fortunaisk',  # Assurez-vous que le nom ici est "fortunaisk"
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'allianceauth>=4.0',
    ],
    entry_points='''
        [console_scripts]
        fortunaisk=fortunaisk:main
    ''',
)

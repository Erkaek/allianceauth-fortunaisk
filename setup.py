from setuptools import setup, find_packages

setup(
    name='fortunaisk',
    version='1.0.0',
    description='FortunaISK - Monthly lottery module for Alliance Auth',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votre-dépôt/fortunaisk',
    author='Votre Nom',
    author_email='votre.email@example.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2',
    ],
)

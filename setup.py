from setuptools import setup, find_packages

setup(
    name="fortunaisk",  # Assurez-vous que le nom est bien "fortunaisk"
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="FortunaISK - A monthly raffle plugin for Alliance Auth",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Erka Ekanon",
    author_email="erkaekanon@outlook.com",
    url="https://github.com/Erkaek/allianceauth-fortunaisk",
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
        "allianceauth-corptools>=2.8.2",
    ],
    python_requires=">=3.8",
)

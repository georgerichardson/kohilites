import setuptools
from setuptools import setup
# from kohilites import __version__

# version = "".join(v for v in __version__ if (v.isnumeric() or v == "."))

with open("README.md", "r") as fr:
    long_description=fr.read()


common_kwargs = dict(
    version="0.0.1",
    license="MIT",
    install_requires=["Mdutils==1.4.0", "SLPP==1.2.3"],
    long_description_content_type="text/markdown",
    url="https://github.com/georgerichardson/kohilites",
    author="George Richardson",
    author_email="georgerichardson@posteo.net",
    maintainer="georgerichardson",
    maintainer_email="georgerichardson@posteo.net",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">3.8",
    include_package_data=True,
    entry_points={
        "console_scripts": ["kohilites = kohilites.cli:get_highlights",]
    }
)

setup(
    name="kohilites",
    packages=["kohilites"],
    **common_kwargs
)

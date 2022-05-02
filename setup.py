from setuptools import setup
from kohilites import __version__

version = "".join(v for v in __version__ if (v.isnumeric() or v == "."))


common_kwargs = dict(
    version=version,
    license="MIT",
    install_requires=["Mdutils==1.3.1", "SLPP==1.2.3"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/georgerichardson/kohilites",
    author="Nesta",
    author_email="georgerichardson@posteo.net",
    maintainer="georgerichardson",
    maintainer_email="georgerichardson@posteo.net",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">3.6",
    include_package_data=True,
)

setup(name="kohilites", packages=["kohilites"], **common_kwargs)

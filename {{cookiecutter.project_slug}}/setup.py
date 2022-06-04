import os
from typing import List

import setuptools

path = os.path.dirname(__file__)
project_slug = "{{cookiecutter.project_slug}}"
package = "{{cookiecutter.package}}"


def requirements() -> List[str]:
    with open(os.path.join(path, "requirements", "requirements.txt"), "r") as f:
        return f.readlines()


def version() -> str:
    with open(os.path.join(path, "version"), "r") as f:
        return f.read().strip()


setuptools.setup(
    name=project_slug,
    version=version(),
    url="{{cookiecutter.url}}",
    author="{{cookiecutter.author}}",
    python_requires=">={{cookiecutter.python}}",
    packages=setuptools.find_packages(),
    install_requires=requirements(),
    entry_points={
        "console_scripts": [
            f"{package}={package}.main:main",
        ]
    }
)

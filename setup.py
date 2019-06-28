import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
# README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="bucket-management",
    version="1.0.0",
    description="Helpers tools to manipulate your Cellar or others S3 like storage",
    # long_description=README,
    # long_description_content_type="text/markdown",
    url="https://github.com/vballu/bucket-management.git",
    author="Victor Ballu",
    author_email="victor.ballu@clever-cloud.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["boto", "filechunkio"]
)

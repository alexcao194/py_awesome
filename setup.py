import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "py_awesome",
    version = "0.0.1",
    author = "alexcao",
    author_email = "alexcao194@gmail.com",
    description = "short package description",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    # url = "https://github.com/alexcao194/py_awesome/archive/refs/tags/test.tar.gz",
    # project_urls = {
    #     "Bug Tracker": "package issues URL",
    # },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "py_awesome"},
    packages = setuptools.find_packages(),
    python_requires = ">=3.6"
)
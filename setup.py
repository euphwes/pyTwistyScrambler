import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyTwistyScrambler",
    version="1.6",
    author="euphwes",
    author_email="euphwes@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    description="A Python utility package for generating scrambles for twisty puzzles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/euphwes/pyTwistyScrambler",
    project_urls={
        "Bug Tracker": "https://github.com/euphwes/pyTwistyScrambler/issues",
    },
    install_requires=[
        'appdirs',
        'packaging',
        'PyExecJS',
        'pyparsing',
        'six',
    ],
)

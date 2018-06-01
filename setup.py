import setuptools

setuptools.setup(
    name="pyTwistyScrambler",
    version="1.1",
    author="euphwes",
    author_email="euphwes@gmail.com",
    url="https://github.com/euphwes/pyTwistyScrambler",
    packages=setuptools.find_packages(),
    install_requires=[
        'appdirs',
        'packaging',
        'PyExecJS',
        'pyparsing',
        'six',
    ],
)
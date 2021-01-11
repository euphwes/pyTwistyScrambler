import setuptools

setuptools.setup(
    name="pyTwistyScrambler",
    version="1.3",
    author="euphwes",
    author_email="euphwes@gmail.com",
    url="https://github.com/euphwes/pyTwistyScrambler",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'appdirs',
        'packaging',
        'PyExecJS',
        'pyparsing',
        'six',
    ],
)

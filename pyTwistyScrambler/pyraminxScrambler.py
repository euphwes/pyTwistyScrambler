from . import _PYRA_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a Pyraminx. """
    return _PYRA_SCRAMBLER.call("pyra_scrambler.getPyraWCAScramble")

@trim
def get_optimal_scramble():
    """ Gets an optimal scramble of a Pyraminx. """
    return _PYRA_SCRAMBLER.call("pyra_scrambler.getPyraOptimalScramble")
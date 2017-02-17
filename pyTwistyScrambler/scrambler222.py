from . import _222_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA random scramble (sub-optimal) of a 2x2x2 cube. """
    return _222_SCRAMBLER.call("scramble_222.getRandomScramble")

@trim
def get_random_scramble():
    """ Gets a WCA random scramble (sub-optimal) of a 2x2x2 cube. """
    return _222_SCRAMBLER.call("scramble_222.getRandomScramble")

@trim
def get_optimal_scramble():
    """ Gets an optimal random state scramble of a 2x2x2 cube. """
    return _222_SCRAMBLER.call("scramble_222.getOptimalScramble")
from . import SCRAMBLE_333_SRC, MATHLIB_SRC, CROSS_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + CROSS_SRC + SCRAMBLE_333_SRC)

#------------------------------------------------------------------------------

@trim
def get_random_scramble():
    """ Gets a random scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getRandomScramble")

@trim
def get_edges_scramble():
    """ Gets an edges-only scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getEdgeScramble")

@trim
def get_corners_scramble():
    """ Gets a corners-only scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getCornerScramble")

@trim
def get_LL_scramble():
    """ Gets a last layer scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getLLScramble")

@trim
def get_LSLL_scramble():
    """ Gets a last slot last layer scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getLSLLScramble")

@trim
def get_ZBLL_scramble():
    """ Gets a Zborowski-Bruchem last layer scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getZBLLScramble")

@trim
def get_ZZLL_scramble():
    """ Gets a Zbigniew Zborowski last layer scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getZZLLScramble")

@trim
def get_F2L_scramble():
    """ Gets an F2L (first two layers) scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getF2LScramble")

@trim
def get_LSE_scramble():
    """ Gets an LSE (last six edges) scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getLSEScramble")

@trim
def get_CMLL_scramble():
    """ Gets a CMLL scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getCMLLScramble")

@trim
def get_CLL_scramble():
    """ Gets a CLL scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getCLLScramble")

@trim
def get_ELL_scramble():
    """ Gets an ELL scramble of a 3x3x3 cube. """
    return _scrambler.call("scramble_333.getELLScramble")

@trim
def get_easy_cross_scramble(n):
    """ Gets an 'easy cross' scramble, where the cross can be solved in `n` moves."""
    return _scrambler.call("scramble_333.getEasyCrossScramble", n)
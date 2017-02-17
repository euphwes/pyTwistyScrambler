from . import PYRAMINX_SRC, MATHLIB_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + PYRAMINX_SRC)

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a Pyraminx. """
    return _scrambler.call("pyra_scrambler.getPyraWCAScramble")

@trim
def get_optimal_scramble():
    """ Gets an optimal scramble of a Pyraminx. """
    return _scrambler.call("pyra_scrambler.getPyraOptimalScramble")
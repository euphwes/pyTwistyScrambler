from . import SCRAMBLE_333_SRC, SCRAMBLE_444_SRC, MATHLIB_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_333_SRC + SCRAMBLE_444_SRC)

#------------------------------------------------------------------------------

@trim
def get_random_scramble():
    """ Gets a WCA random scramble of a 4x4x4 cube. """
    return _scrambler.call("scramble_444.getRandomScramble")
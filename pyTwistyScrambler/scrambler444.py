from . import SCRAMBLE_SRC, SCRAMBLE_333_SRC, SCRAMBLE_444_SRC, MEGA_SCRAMBLE_SRC, MATHLIB_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_333_SRC + SCRAMBLE_444_SRC)
_mega_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + MEGA_SCRAMBLE_SRC)

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=40):
    """ Gets a WCA scramble of length N for a 4x4x4 cube. Defaults to csTimer's default length of 40. """
    return _mega_scrambler.call("megaScrambler.get444WCAScramble", n)

@trim
def get_SiGN_scramble(n=40):
    """ Gets a SiGN-notation scramble of length N for a 4x4x4 cube. Defaults to csTimer's default length of 40. """
    return _mega_scrambler.call("megaScrambler.get444SiGNScramble", n)

@trim
def get_random_scramble():
    """ Gets a random state scramble of a 4x4x4 cube. """
    return _scrambler.call("scramble_444.getRandomScramble")
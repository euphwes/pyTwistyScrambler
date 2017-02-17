from . import UTIL_SCRAMBLE_SRC, SCRAMBLE_SRC, MATHLIB_SRC, SCRAMBLE_SQ1_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + UTIL_SCRAMBLE_SRC)
_sql_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + SCRAMBLE_SQ1_SRC)

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble for a Square-1. """
    return _sql_scrambler.call("sql_scrambler.getRandomScramble")

@trim
def get_face_turn_metric_scramble(n=40):
    """ Gets a face turn metric scramble of length `n` for a Square-1. Defaults to csTimer's default length of 40. """
    return _scrambler.call("util_scramble.getSquareOneTurnMetricScramble", n)

@trim
def get_twist_metric_scramble(n=20):
    """ Gets a twist metric scramble for a Square-1.  Defaults to csTimer's default length of 20."""
    return _scrambler.call("util_scramble.getSquareOneTwistMetricScramble", n)
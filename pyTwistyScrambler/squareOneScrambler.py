from . import _SQ1_SCRAMBLER, _UTIL_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble for a Square-1. """
    return _SQ1_SCRAMBLER.call("sql_scrambler.getRandomScramble")

@trim
def get_face_turn_metric_scramble(n=40):
    """ Gets a face turn metric scramble of length `n` for a Square-1. Defaults to csTimer's default length of 40. """
    return _UTIL_SCRAMBLER.call("util_scramble.getSquareOneTurnMetricScramble", n)

@trim
def get_twist_metric_scramble(n=20):
    """ Gets a twist metric scramble for a Square-1.  Defaults to csTimer's default length of 20."""
    return _UTIL_SCRAMBLER.call("util_scramble.getSquareOneTwistMetricScramble", n)
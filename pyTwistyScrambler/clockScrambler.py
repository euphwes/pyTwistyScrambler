from . import _UTIL_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble for a Rubik's Clock. """
    return _UTIL_SCRAMBLER.call("util_scramble.getClockWCAScramble")

@trim
def get_Jaap_scramble():
    """ Gets a Jaap-notation scramble for a Rubik's Clock. """
    return _UTIL_SCRAMBLER.call("util_scramble.getClockJaapScramble")

@trim
def get_concise_scramble():
    """ Gets a concise-notation scramble for a Rubik's Clock. """
    return _UTIL_SCRAMBLER.call("util_scramble.getClockConciseScramble")

@trim
def get_efficient_pin_order_scramble():
    """ Gets an efficient pin order scramble for a Rubik's Clock. """
    return _UTIL_SCRAMBLER.call("util_scramble.getClockEfficientPinOrderScramble")
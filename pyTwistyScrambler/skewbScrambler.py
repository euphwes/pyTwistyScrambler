from . import _MEGA_SCRAMBLER, _SKEWB_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a Skewb. """
    return _SKEWB_SCRAMBLER.call("skewb_scrambler.getSkewbWCAScramble")

@trim
def get_ULRB_scramble():
    """ Gets a ULRB scramble of a Skewb. """
    return _MEGA_SCRAMBLER.call("megaScrambler.getSkewbULRBScramble")
from . import _444_SCRAMBLER, _MEGA_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=40):
    """ Gets a WCA scramble of length N for a 4x4x4 cube. Defaults to csTimer's default length of 40. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get444WCAScramble", n)

@trim
def get_4BLD_scramble(n=40):
    """ Gets a BLD scramble of length N for a 4x4x4 cube. Alias of get_WCA_scramble. """
    return get_WCA_scramble(n)

@trim
def get_SiGN_scramble(n=40):
    """ Gets a SiGN-notation scramble of length N for a 4x4x4 cube. Defaults to csTimer's default length of 40. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get444SiGNScramble", n)

@trim
def get_random_state_scramble():
    """ Gets a random state scramble of a 4x4x4 cube. """
    return _444_SCRAMBLER.call("scramble_444.getRandomScramble")

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 4x4x4 cube. Defaults to csTimer's default length of 8. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get444edgesScramble", n)

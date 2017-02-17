from . import _MEGA_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=60):
    """ Gets a WCA scramble of length `n` for a 5x5x5 cube. Defaults to csTimer's default length of 60. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get555WCAScramble", n)

@trim
def get_5BLD_scramble(n=60):
    """ Gets a BLD scramble of length N for a 5x5x5 cube. Alias of get_WCA_scramble. """
    return get_WCA_scramble(n)

@trim
def get_SiGN_scramble(n=60):
    """ Gets a SiGN-notation scramble of length `n` for a 5x5x5 cube. Defaults to csTimer's default length of 60. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get555SiGNScramble", n)

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 5x5x5 cube. Defaults to csTimer's default length of 8. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get555edgesScramble", n)
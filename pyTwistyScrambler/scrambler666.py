from . import _MEGA_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=80):
    """ Gets a WCA scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 80. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get666WCAScramble", n)

@trim
def get_SiGN_scramble(n=80):
    """ Gets a SiGN-notation scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 80. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get666SiGNScramble", n)

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 8. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get666edgesScramble", n)
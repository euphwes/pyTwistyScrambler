from . import _MEGA_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=100):
    """ Gets a WCA scramble of length `n` for a 7x7x7 cube. Defaults to csTimer's default length of 100. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get777WCAScramble", n)

@trim
def get_SiGN_scramble(n=100):
    """ Gets a SiGN-notation scramble of length `n` for a 7x7x7 cube. Defaults to csTimer's default length of 100. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get777SiGNScramble", n)

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 7x7x7 cube. Defaults to csTimer's default length of 8. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get777edgesScramble", n)
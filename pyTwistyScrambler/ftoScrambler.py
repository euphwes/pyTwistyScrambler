from . import _FTO_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_random_state_scramble():
    """ Gets a random-state scramble for FTO (face-turning octahedron). """
    return _FTO_SCRAMBLER.call("generate_random_state_scramble")

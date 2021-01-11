from . import _FTO_SCRAMBLER, trim

from random import choice

#------------------------------------------------------------------------------

@trim
def get_random_state_scramble():
    """ Gets a random-state scramble for FTO (face-turning octahedron). """
    return _FTO_SCRAMBLER.call("generate_random_state_scramble")


@trim
def get_random_moves_scramble(scramble_length = 30):
    """ Returns a random-moves scramble of length `scramble_length` for FTO. """

    def __except(exceptions):
        """ Returns a list range 0-7 except the specified exceptions. """
        if not exceptions:
            return range(8)
        values = list(range(8))
        for n in exceptions:
            values.remove(n)
        return values

    moves = ['F', 'U', 'R', 'L', 'D', 'B', 'BL', 'BR']
    opposites = {
        'U':  'D',
        'D':  'U',
        'F':  'B',
        'B':  'F',
        'L':  'BR',
        'BR': 'L',
        'BL': 'R',
        'R':  'BL'
    }

    scramble = list()
    move_ix = -1

    for _ in range(scramble_length):
        if move_ix == -1:
            # If this is the first move, there are no restrictions on which face we can choose.
            exceptions = None
        else:
            # Otherwise, we'll always omit the face we just chose, so we don't choose it again.
            exceptions = [move_ix]

            if len(scramble) > 1:
                # If the last two faces in the scramble were opposites (ex, U and D), the next move
                # needs to exclude both of those faces so we don't end up with cancellations.
                # ex: U D U' is no good
                # ex: R' BL' R' BL is no good
                # By omitting the two opposite faces from the choices for the next move, the face
                # chosen will intersect those faces, preventing a cancellation.
                face_one_ago = scramble[-1].replace("'", "")
                face_two_ago = scramble[-2].replace("'", "")
                if opposites[face_one_ago] == face_two_ago:
                    exceptions.append(moves.index(face_two_ago))

        # Randomly choose a move from the faces available, ensuring we don't have a cancellation
        move_ix = choice(__except(exceptions))

        # Randomly decide if that turn is clockwise or counterclockwise and apply prime if needed.
        scramble.append(moves[move_ix] + choice(["", "'"]))

    return ' '.join(scramble)

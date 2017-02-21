# pyTwistyScrambler
A Python package for generating scrambles of various twisty puzzles, including the Rubik's cube, 4x4x4 cube, and others.
Thanks to [csTimer](https://github.com/cs0x7f/cstimer) for providing the JavaScript scrambling source code around which this project is a wrapper.

## Example usage

```python
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444,\
	megaminxScrambler, squareOneScrambler

scrambler333.get_WCA_scramble()
# D2 L F2 L2 F2 U2 L D2 F2 L' B' U2 F2 D' F D2 B' U2 R U'

scrambler222.get_WCA_scramble()
# R' F2 U2 R' U R2 F' U' F' U'

scrambler444.get_WCA_scramble()
# L2 F D2 R U Fw' Uw D L F Rw D' F L2 F' Rw' F Uw B' F' L2 B' U' Rw' F B R' D U2 L2 Fw' B D' Rw' Uw' B' Fw' R2 L2 U

megaminxScrambler.get_WCA_scramble()
# R-- D-- R++ D++ R++ D++ R++ D++ R++ D++ U R-- D++ R-- D++ R-- D++ R-- D++ R-- D-- U' R-- D++ R-- D-- R-- D++ R-- D-- R-- D-- U' R++ D++ R-- D-- R++ D-- R-- D++ R-- D-- U' R-- D-- R++ D++ R++ D-- R++ D++ R++ D-- U' R-- D-- R++ D-- R++ D-- R++ D-- R++ D++ U R++ D-- R++ D-- R++ D++ R-- D-- R++ D++ U

squareOneScrambler.get_WCA_scramble()
# (0, -1)/(4, 1)/(-4, 5)/(0, -3)/(1, -2)/(3, 0)/(2, 0)/(0, -3)/(4, -3)/(0, -4)/(2, 0)/(5, -2)/(4, 0)
```

## What scrambles can be generated?
### 3x3x3 (Rubik's cube)
In `scrambler333` module:

- `get_WCA_scramble()`            random state scramble (WCA)
- `get_3BLD_scramble()`           BLD scramble
- `get_edges_scramble()`          edges-only
- `get_corners_scramble()`        corners-only
- `get_LL_scramble()`             LL (last layer)
- `get_F2L_scramble()`            F2L (first two layers)
- `get_easy_cross_scramble(n=4)`  easy cross (where cross can be solved in `n` moves)
- `get_LSLL_scramble()`           LSLL
- `get_ZBLL_scramble()`           ZBLL
- `get_ZZLL_scramble()`           ZZLL
- `get_ZBLS_scramble()`           ZBLS
- `get_LSE_scramble()`            LSE
- `get_CMLL_scramble()`           CMLL
- `get_CLL_scramble()`            CLL
- `get_ELL_scramble()`            ELL
- `get_EOLine_scramble()`         EO Line
- `get_2genRU_scramble()`         2-gen with RU moves
- `get_2genLU_scramble()`         2-gen with LU moves
- `get_2genMU_scramble()`         2-gen with MU moves
- `get_3genFRU_scramble()`        3-gen with FRU moves
- `get_3genRUL_scramble()`        3-gen with RUL moves
- `get_3genRrU_scramble()`        3-gen with RrU moves
- `get_half_turns_scramble()`     half-turns only

### 2x2x2
In `scrambler222` module:

- `get_WCA_scramble()`            random scramble (WCA)
- `get_optimal_scramble()`        optimal random state scramble

### 4x4x4
In `scrambler444` module:

- `get_WCA_scramble(n=40)`        random scramble (WCA) of length `n`
- `get_4BLD_scramble(n=40)`       alias of `get_WCA_scramble`
- `get_SiGN_scramble(n=40)`       SiGN-notation scramble of length `n`
- `get_random_state_scramble()`   random state scramble (note: this is **slow**)
- `get_edges_scramble(n=8)`       edges scramble

### 5x5x5
In `scrambler555` module:

- `get_WCA_scramble(n=60)`        random scramble (WCA) of length `n`
- `get_5BLD_scramble(n=60)`       alias of `get_WCA_scramble`
- `get_SiGN_scramble(n=60)`       SiGN-notation scramble of length `n`
- `get_edges_scramble(n=8)`       edges scramble

### 6x6x6
In `scrambler666` module:

- `get_WCA_scramble(n=80)`        random scramble (WCA) of length `n`
- `get_SiGN_scramble(n=80)`       SiGN-notation scramble of length `n`
- `get_edges_scramble(n=8)`       edges scramble

### 7x7x7
In `scrambler777` module:

- `get_WCA_scramble(n=100)`       random scramble (WCA) of length `n`
- `get_SiGN_scramble(n=100)`      SiGN-notation scramble of length `n`
- `get_edges_scramble(n=8)`       edges scramble

### Pyraminx
In `pyraminxScrambler` module:

- `get_WCA_scramble()`            random scramble (WCA)
- `get_optimal_scramble()`        optimal random state scramble

### Megaminx
In `megaminxScrambler` module:

- `get_WCA_scramble(n=70)`        random scramble (WCA) of length `n`
- `get_Carrot_scramble(n=70)`     Carrot-notation scramble of length `n`
- `get_old_style_scramble(n=70)`  old-style scramble of length `n`

### Square-1
In `squareOneScrambler` module:

- `get_WCA_scramble()`                      random scramble (WCA)
- `get_face_turn_metric_scramble(n=40)`     face-turn metric scramble of length `n`
- `get_twist_metric_scramble(n=20)`         twist metric scramble of length `n`

### Skewb
In `skewbScrambler` module:

- `get_WCA_scramble()`      random scramble (WCA)
- `get_ULRB_scramble()`     ULRB scramble

### Cuboids
In `cuboidsScrambler` module:

- `get_1x1x2_scramble()`              1x1x2 cuboid scramble
- `get_1x3x3_scramble()`              1x3x3 cuboid (floppy cube) scramble
- `get_floppy_cube_scramble()`        alias of `get_1x3x3_scramble()`
- `get_super_floppy_cube_scramble()`  1x3x3 cuboid (super floppy cube) scramble
- `get_2x2x3_scramble()`              2x2x3 cuboid scramble
- `get_3x3x2_scramble()`              3x3x2 cuboid scramble
- `get_3x3x4_scramble()`              3x3x4 cuboid scramble
- `get_3x3x5_scramble(n=25)`          3x3x5 cuboid scramble, where `n` is the length of the non-3x3 portion of the scramble
- `get_3x3x6_scramble()`              3x3x6 cuboid scramble
- `get_3x3x7_scramble(n=40)`          3x3x7 cuboid scramble, where `n` is the length of the non-3x3 portion of the scramble

### Clock
In `clockScrambler` module:

- `get_WCA_scramble()`                   Clock scramble (WCA notation)
- `get_Jaap_scramble()`                  Clock scramble (Jaap notation)
- `get_concise_scramble()`               Clock scramble (concise notation)
- `get_efficient_pin_order_scramble()`   Clock scramble (efficient pin order notation)

### Big cubes
In `bigCubesScrambler` module:

- `get_8x8x8_scrambler(n=120)`        8x8x8 scramble (SiGN notation) of length `n`
- `get_9x9x9_scrambler(n=120)`        9x9x9 scramble (SiGN notation) of length `n`
- `get_10x10x10_scrambler(n=120)`     10x10x10 scramble (SiGN notation) of length `n`
- `get_11x11x11_scrambler(n=120)`     11x11x11 scramble (SiGN notation) of length `n`
# pyTwistyScrambler
A Python module for generating scrambles of various twisty puzzles, including the Rubik's cube, 4x4x4 cube, and others.
Thanks to [csTimer](https://github.com/cs0x7f/cstimer) for providing the JavaScript scrambling source code around which this project is a wrapper.

## Example usage

```python
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444

scrambler333.get_WCA_scramble()
# D2 L F2 L2 F2 U2 L D2 F2 L' B' U2 F2 D' F D2 B' U2 R U'

scrambler222.get_WCA_scramble()
# R' F2 U2 R' U R2 F' U' F' U'

# defaults to 40-move length
scrambler444.get_WCA_scramble()
# L2 F D2 R U Fw' Uw D L F Rw D' F L2 F' Rw' F Uw B' F' L2 B' U' Rw' F B R' D U2 L2 Fw' B D' Rw' Uw' B' Fw' R2 L2 U

# or a length can be specified
scrambler444.get_WCA_scramble(10)
# B2 Uw2 R Uw B2 Uw' F2 Rw' Uw2 R2
```

## What scrambles can be generated?
### 3x3x3 (Rubik's cube)
In `scrambler333` module:

- `get_WCA_scramble()`            random scramble (WCA)
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
- `get_SiGN_scramble(n=40)`       SiGN-notation scramble of length `n`
- `get_random_scramble()`         random state scramble (note: this is **slow**)
- `get_edges_scramble(n=8)`       edges scramble

### 5x5x5
In `scrambler555` module:

- `get_WCA_scramble(n=60)`        random scramble (WCA) of length `n`
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
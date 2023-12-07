# Advent of Code 2023
Advent of Code 2023 Scripts

## D01 - Trebuchet?!
Part 1:
- Fun number extraction from string task.
- RegEx quickly solves single digit number identification.

Part 2:
- Increased difficulty due combined digit and word search in string.
- Crux: overlapping words have to be accounted for -> **New-to-me concept:** introduction to the RegEx concept of [positive lookahead](https://www.regextutorial.org/positive-and-negative-lookahead-assertions.php#:~:text=Positive%20lookahead%3A,it%20simply%20rejects%20that%20match.) -> very useful.


## D02 - Cube Conundrum
Part 1:
- Simple but actually surprisingly time-consuming number comparison task.

Part 2:
- If Challenge 1 has been set up elegantly, this is very simple: replace comparison operation with `max()` identification
- **New-to-me tool:** `from functools import reduce`, quickly apply operation on all elements of a list "bundled up" -> very powerful little function.


## D03 - Gear Ratios
Part 1:
- 2D operations, visualised using `plt.imshow()`

Part 2:
- If Cha

  
- ## D04 - Scratcards
Part 1:
- 2D operations

Part 2:
- If Cha

## D05 - If You Give A Seed A Fertilizer
Part 1:
- Time complexity problem - search algorithm - index extraction:
    - I chose a hashmap approach first which performed well on the small training input but could not scale to the massive ranges encountered in the puxxle input.
    - Learned more (again) about scalable search algorithms and chose a binary search approach -> while hashmap crashed after 15 min (after optimisation) binary search took 7.13 ms to finish.
    - use terminal-based execution of `output_delete.py` to erase the output of the crashed Notebook; otherwise the output is so massive that the entire JupyterLab cannot be loaded and you get a "Snap" error message.

Part 2:
- If Cha

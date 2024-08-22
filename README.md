# numbers-to-words

> Convert a number into the english word representation of that number in a single line of python.

This was my attempt at [DragonXDev's challenge](https://github.com/DragonXDev/words-to-numbers).

## Usage

```sh
python3 main.py
```

## Improvements over DragonXDev's solution

1. **Less code:** 42.8% less characters used in the final implementation. (this solution: 1747 chars, original solution: 3055 chars)
2. **More numbers:** This solution supports numbers up to `10^99`. The original solution only goes up to `10^24`.
3. **Easy extensions:** If for whatever reason you need to support larger numbers, you can simply add more numbers to the end of the list that starts with `["thousand", "million", ...]`, no need to increment numbers or add to multiple lists.

## How does it work?

Feel free to read the code under the `other/` directory.

1. `multi_statement.py` is the reference implementation of the algorithm to convert numbers into english in idiomatic procedural python.
2. `single_statement.py` is the conversion of `multi_statement.py` into a single python statement using an unhealthy amount of functional programming. As such, `main.py` is just `single_statement.py` with the comments stripped and all lines joined on one line.


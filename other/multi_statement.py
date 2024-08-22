import sys

unique = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

double_digit_prefix = [
    "twenty",
    "thirty",
    "fourty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

def below_100(i: int) -> str:
    if i == 0:
        return "zero"
    if i < 20:
        return unique[i-1]
    if i < 100:
        coefficient_idx = i // 10 - 2
        remainder_idx = i % 10 - 1
        if remainder_idx < 0:
            return double_digit_prefix[coefficient_idx]
        return f"{double_digit_prefix[coefficient_idx]} {unique[remainder_idx]}"
    raise "below_100() must be called with numbers below 100"

stops = [
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecllion",
    "duodecllion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septemdecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion",
    "unvigintillion",
    "duovigintillion",
    "trevigintillion",
    "quattuorvigintillion",
    "quinvigintillion",
    "sexvigintillion",
    "septvigintillion",
    "octovigintillion",
    "nonvigintillion",
    "trigintillion",
    "untrigintillion",
    "duotrigintillion",
]

def generate_word(i: int) -> str:
    if i < 100:
        return below_100(i)
    if i < 1000:
        coefficient = i // 100
        remainder = i % 100

        if remainder == 0:
            return f"{generate_word(coefficient)} hundred"
        return f"{generate_word(coefficient)} hundred {generate_word(remainder)}"

    stop_idx = -1
    n = i
    while n > 1000:
        n = n // 1000
        stop_idx += 1
    stop = stops[stop_idx]
    unit = 1000**(stop_idx + 1)

    coefficient = i // unit
    remainder = i % unit

    if remainder == 0:
        return f"{generate_word(coefficient)} {stop}"
    return f"{generate_word(coefficient)} {stop} {generate_word(remainder)}"

print(generate_word(int(sys.argv[1])))

print(
    (
        lambda i, unique, double_digit_prefix, stops, get_stop_idx: (
            (
                lambda below_100:
                # define a recursive lambda, get its value and immediately execute it
                (lambda fn: fn(fn, i))(
                    lambda generate_word, n: (
                        below_100(n)
                        if n < 100
                        else (
                            (
                                f"{generate_word(generate_word, n // 100)} hundred"
                                if (n % 100) == 0
                                else f"{generate_word(generate_word, n // 100)} hundred {generate_word(generate_word, n % 100)}"
                            )
                            if n < 1000
                            else (
                                lambda stop_idx: (
                                    lambda stop, unit: (
                                        f"{generate_word(generate_word, n // unit)} {stop}"
                                        if (n % unit) == 0
                                        else f"{generate_word(generate_word, n // unit)} {stop} {generate_word(generate_word, n % unit)}"
                                    )
                                )(stops[stop_idx], 1000 ** (stop_idx + 1))
                            )(get_stop_idx(get_stop_idx, n, -1))
                        )
                    )
                )
            )(
                lambda n: (
                    "zero"
                    if n == 0
                    else (
                        unique[n - 1]
                        if n < 20
                        else (
                            double_digit_prefix[n // 10 - 2]
                            if (n % 10 - 1) < 0
                            else f"{double_digit_prefix[n // 10 - 2]} {unique[n % 10 - 1]}"
                        )
                    )
                ),
            )
        )
    )(
        int(input(" > ")),
        [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ],
        [
            "twenty",
            "thirty",
            "fourty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ],
        [
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
        ],
        # stop_idx's initial value should be -1
        lambda fn, n, stop_idx: (
            stop_idx if n < 1000 else fn(fn, n // 1000, stop_idx + 1)
        ),
    )
)

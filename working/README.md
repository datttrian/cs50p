# [Working 9 to 5](#working-9-to-5)

Whereas [most
countries](https://en.wikipedia.org/wiki/Date_and_time_representation_by_country#Time)
use a [24-hour clock](https://en.wikipedia.org/wiki/24-hour_clock), the
United States tends to use a [12-hour
clock](https://en.wikipedia.org/wiki/12-hour_clock). Accordingly,
instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM
to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for
“ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein
“meridiem” means midday (i.e., noon).

Conversion Table

Just as “12:00 AM” in 12-hour format would be “00:00” in 24-hour format,
so would “12:01 AM” through “12:59 AM” be “00:01” through “00:59”,
respectively.

<span class="loading-wrap"> <span class="loading-text">Loading, please
wait</span>
<span class="animation-wrap"><span class="animation-dot"></span></span>
</span>

<table class="table table-bordered table-striped">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th data-field="0"><div class="th-inner">
<div style="text-align: left">
12-Hour
</div>
</div>
<div class="fht-cell">
&#10;</div></th>
<th data-field="1"><div class="th-inner">
<div style="text-align: left">
24-Hour
</div>
</div>
<div class="fht-cell">
&#10;</div></th>
</tr>
</thead>
<tbody>
<tr class="odd" data-index="0">
<td>12:00 AM</td>
<td>00:00</td>
</tr>
<tr class="even" data-index="1">
<td>1:00 AM</td>
<td>01:00</td>
</tr>
<tr class="odd" data-index="2">
<td>2:00 AM</td>
<td>02:00</td>
</tr>
<tr class="even" data-index="3">
<td>3:00 AM</td>
<td>03:00</td>
</tr>
<tr class="odd" data-index="4">
<td>4:00 AM</td>
<td>04:00</td>
</tr>
<tr class="even" data-index="5">
<td>5:00 AM</td>
<td>05:00</td>
</tr>
<tr class="odd" data-index="6">
<td>6:00 AM</td>
<td>06:00</td>
</tr>
<tr class="even" data-index="7">
<td>7:00 AM</td>
<td>07:00</td>
</tr>
<tr class="odd" data-index="8">
<td>8:00 AM</td>
<td>08:00</td>
</tr>
<tr class="even" data-index="9">
<td>9:00 AM</td>
<td>09:00</td>
</tr>
<tr class="odd" data-index="10">
<td>10:00 AM</td>
<td>10:00</td>
</tr>
<tr class="even" data-index="11">
<td>11:00 AM</td>
<td>11:00</td>
</tr>
<tr class="odd" data-index="12">
<td>12:00 PM</td>
<td>12:00</td>
</tr>
<tr class="even" data-index="13">
<td>1:00 PM</td>
<td>13:00</td>
</tr>
<tr class="odd" data-index="14">
<td>2:00 PM</td>
<td>14:00</td>
</tr>
<tr class="even" data-index="15">
<td>3:00 PM</td>
<td>15:00</td>
</tr>
<tr class="odd" data-index="16">
<td>4:00 PM</td>
<td>16:00</td>
</tr>
<tr class="even" data-index="17">
<td>5:00 PM</td>
<td>17:00</td>
</tr>
<tr class="odd" data-index="18">
<td>6:00 PM</td>
<td>18:00</td>
</tr>
<tr class="even" data-index="19">
<td>7:00 PM</td>
<td>19:00</td>
</tr>
<tr class="odd" data-index="20">
<td>8:00 PM</td>
<td>20:00</td>
</tr>
<tr class="even" data-index="21">
<td>9:00 PM</td>
<td>21:00</td>
</tr>
<tr class="odd" data-index="22">
<td>10:00 PM</td>
<td>22:00</td>
</tr>
<tr class="even" data-index="23">
<td>11:00 PM</td>
<td>23:00</td>
</tr>
<tr class="odd" data-index="24">
<td>12:00 AM</td>
<td>00:00</td>
</tr>
</tbody>
</table>

In a file called `working.py`, implement a function called `convert`
that expects a `str` in either of the 12-hour formats below and returns
the corresponding `str` in 24-hour format (i.e., `9:00 to 17:00`).
Expect that `AM` and `PM` will be capitalized (with no periods therein)
and that there will be a space before each. Assume that these times are
representative of actual times, not necessarily 9:00 AM and 5:00 PM
specifically.

-   `9:00 AM to 5:00 PM`
-   `9 AM to 5 PM`

Raise a `ValueError` instead if the input to `convert` is not in either
of those formats or if either time is invalid (e.g., `12:60 AM`,
`13:00 PM`, etc.). But do not assume that someone’s hours will start
ante meridiem and end post meridiem; someone might work late and even
long hours (e.g., `5:00 PM to 9:00 AM`).

Structure `working.py` as follows, wherein you’re welcome to modify
`main` and/or implement other functions as you see fit, but you may not
import any other libraries. You’re welcome, but not required, to use
`re` and/or `sys`.

``` python
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
```

Either before or after you implement `convert` in `working.py`,
additionally implement, in a file called `test_working.py`, **three or
more** functions that collectively test your implementation of `convert`
thoroughly, each of whose names should begin with `test_` so that you
can execute your tests with:

``` highlight
pytest test_working.py
```

Hints

-   Recall that the `re` module comes with
    quite a few functions, per
    [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html),
    including `search`.

-   Recall that regular expressions support
    quite a few special characters, per
    [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax).

-   Because backslashes in regular
    expressions could be mistaken for escape sequences (like `\n`), best
    to use [Python’s raw string notation for regular expression
    patterns](https://docs.python.org/3/library/re.html#module-re), else
    `pytest` will warn with
    `DeprecationWarning: invalid escape sequence`. Just as format
    strings are prefixed with `f`, so are raw strings prefixed with `r`.
    For instance, instead of `"harvard\.edu"`, use `r"harvard\.edu"`.

-   Note that `re.search`, if passed a
    pattern with “capturing groups” (i.e., parentheses), returns a
    “match object,” per
    [docs.python.org/3/library/re.html#match-objects](https://docs.python.org/3/library/re.html#match-objects),
    wherein matches are 1-indexed, which you can access individually
    with `group`, per
    [docs.python.org/3/library/re.html#re.Match.group](https://docs.python.org/3/library/re.html#re.Match.group),
    or collectively with `groups`, per
    [docs.python.org/3/library/re.html#re.Match.groups](https://docs.python.org/3/library/re.html#re.Match.groups).

-   Note that you can format an `int` with
    leading zeroes with code like

    ``` python
    print(f"{n:02}")
    ```

    wherein, if `n` is a single digit, it will be prefixed with one `0`,
    per
    [docs.python.org/3/library/string.html#format-string-syntax](https://docs.python.org/3/library/string.html#format-string-syntax).

## [Demo](#demo)

``` highlight
$ python working.py
Hours: 9:00 AM to 5:00 PM
09:00 to 17:00
$ python working.py
Hours: 9 AM to 5 PM
09:00 to 17:00
$ python working.py
Hours: 9 AM to 5:30 PM
09:00 to 17:30
$
```

## [Before You Begin](#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window,
and execute `cd` by itself. You should find that your terminal window’s
prompt resembles the below:

``` highlight
$
```

Next execute

``` highlight
mkdir working
```

to make a folder called `working` in your codespace.

Then execute

``` highlight
cd working
```

to change directories into that folder. You should now see your terminal
prompt as `working/ $`. You can now execute

``` highlight
code working.py
```

to make a file called `working.py` where you’ll write your program. Be
sure to also execute

``` highlight
code test_working.py
```

to create a file called `test_working.py` where you’ll write tests for
your program.

## [How to Test](#how-to-test)

#### [How to Test</a> <a href="#how-to-test-workingpy" data-id=""><](#how-to-test-workingpy)
class="language-plaintext highlighter-rouge">working.py</code></a>

Here’s how to test `working.py` manually:

-   Run your program with
    `python working.py`. Ensure your program prompts you for a time.
    Type `9 AM to 5 PM`, followed by Enter. Your program should output
    `09:00 to 17:00`.
-   Run your program with
    `python working.py`. Type `9:00 AM to 5:00 PM`, followed by Enter.
    Your program should again output `09:00 to 17:00`.
-   Run your program with
    `python working.py`. Ensure your program prompts you for a time.
    Type `10 PM to 8 AM`, followed by Enter. Your program should output
    `22:00 to 08:00`.
-   Run your program with
    `python working.py`. Ensure your program prompts you for a time.
    Type `10:30 PM to 8:50 AM`, followed by Enter. Your program should
    again output `22:30 to 08:50`.
-   Run your program with
    `python working.py`. Ensure your program prompts you for a time. Try
    intentionally inducing a `ValueError` by typing
    `9:60 AM to 5:60 PM`, followed by Enter. Your program should indeed
    raise a `ValueError`.
-   Run your program with
    `python working.py`. Ensure your program prompts you for a time. Try
    intentionally inducing a `ValueError` by typing `9 AM - 5 PM`,
    followed by Enter. Your program should indeed raise a `ValueError`.
-   Run your program with
    `python working.py`. Ensure your program prompts you for a time. Try
    intentionally inducing a `ValueError` by typing
    `09:00 AM - 17:00 PM`, followed by Enter. Your program should indeed
    raise a `ValueError`.


#### [How to Test</a> <a href="#how-to-test-test_workingpy" data-id=""><](#how-to-test-test_workingpy)
class="language-plaintext highlighter-rouge">test_working.py</code></a>

To test your tests, run `pytest test_working.py`. Try to use correct and
incorrect versions of `working.py` to determine how well your tests spot
errors:

-   Ensure you have a correct version of
    `working.py`. Run your tests by executing `pytest test_working.py`.
    `pytest` should show that all of your tests have passed.
-   Modify the correct version of
    `working.py`, particularly its function `convert`. Your program
    might, for example, fail to raise a `ValueError` when it should. Run
    your tests by executing `pytest test_working.py`. `pytest` should
    show that at least one of your tests has failed.
-   Similarly, modify the correct version of
    `working.py`, changing the return values of `convert`. Your program
    might, for example, mistakenly omit minutes. Run your tests by
    executing `pytest test_working.py`. `pytest` should show that at
    least one of your tests has failed.

You can execute the below to check your code using `check50`, a program
that CS50 will use to test your code when you submit. But be sure to
test it yourself as well!

``` highlight
check50 cs50/problems/2022/python/working
```

Green smilies mean your program has passed a test! Red frownies will
indicate your program output something unexpected. Visit the URL that
`check50` outputs to see the input `check50` handed to your program,
what output it expected, and what output your program actually gave.

## [How to Submit](#how-to-submit)

In your terminal, execute the below to submit your work.

``` highlight
submit50 cs50/problems/2022/python/working
```

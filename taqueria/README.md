# [Felipe’s Taqueria](#felipes-taqueria)

One of the most popular places to eat in [Harvard
Square](https://en.wikipedia.org/wiki/Harvard_Square) is [Felipe’s
Taqueria](https://www.felipesboston.com/), which offers a
[menu](https://www.felipesboston.com/menu) of entrees, per the `dict`
below, wherein the value of each key is a price in dollars:

``` json
    {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
```

In a file called `taqueria.py`, implement a program that enables a user
to place an order, prompting them for items, one per line, until the
user inputs control-d (which is a common way of ending one’s input to a
program). After each inputted item, display the total cost of all items
inputted thus far, prefixed with a dollar sign (`$`) and formatted to
two decimal places. Treat the user’s input case insensitively. Ignore
any input that isn’t an item. Assume that every item on the menu will be
[titlecased](https://docs.python.org/3/library/stdtypes.html#str.title).

Hints

- Note that you can detect when the user has inputted control-d by
  catching an
  [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError)
  with code like:

  ``` py
  try:
    item = input()
  except EOFError:
    ...
  ```

  You might want to print a new line so that the user’s cursor (and
  subsequent prompt) doesn’t remain on the same line as your program’s
  own prompt.

- Inputting control-d does not require inputting Enter as well, and so
  the user’s cursor (and subsequent prompt) might thus remain on the
  same line as your program’s own prompt. You can move the user’s cursor
  to a new line by printing `\n` yourself!

- Note that a `dict` comes with quite a few methods, per
  [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict),
  among them `get`, and supports operations like:

  ``` py
  d[key]
  ```

  and

  ``` py
  if key in d:
    ...
  ```

  wherein `d` is a `dict` and `key` is a `str`.

- Be sure to avoid or catch any
  [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

## [Demo](#demo)

``` highlight
$ python taqueria.py
Item: burrito
Total: $7.50
Item: large quesadilla
Item: super quesadilla
Total: $17.00
Item:
$ python taqueria.py
Item: nachos
Total: $11.00
Item: taco
Total: $14.00
Item: taco
Total: $17.00
Item: taco
Total: $20.00
Item:
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
mkdir taqueria
```

to make a folder called `taqueria` in your codespace.

Then execute

``` highlight
cd taqueria
```

to change directories into that folder. You should now see your terminal
prompt as `taqueria/ $`. You can now execute

``` highlight
code taqueria.py
```

to make a file called `taqueria.py` where you’ll write your program.

## [How to Test](#how-to-test)

Here’s how to test your code manually:

- Run your program with `python taqueria.py`. Type `Taco` and press
  Enter, then type `Taco` again and press Enter. Your program should
  output:

  ``` highlight
  Total: $6.00
  ```

  and continue prompting the user until they input control-d.

- Run your program with `python taqueria.py`. Type `Baja Taco` and press
  Enter, then type `Tortilla Salad` and press enter. Your program should
  output:

  ``` highlight
  Total: $12.00
  ```

  and continue prompting the user until they input control-d.

- Run your program with `python taqueria.py`. Type `Burger` and press
  Enter. Your program should reprompt the user.

Be sure to try other foods and vary the casing of your input. Your
program should behave as expected, case-insensitively.

You can execute the below to check your code using `check50`, a program
that CS50 will use to test your code when you submit. But be sure to
test it yourself as well!

``` highlight
check50 cs50/problems/2022/python/taqueria
```

Green smilies mean your program has passed a test! Red frownies will
indicate your program output something unexpected. Visit the URL that
`check50` outputs to see the input `check50` handed to your program,
what output it expected, and what output your program actually gave.

## [How to Submit](#how-to-submit)

In your terminal, execute the below to submit your work.

``` highlight
submit50 cs50/problems/2022/python/taqueria
```

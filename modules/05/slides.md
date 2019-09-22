---
title: Control Structures 2
subtitle: Functions
revealjs-url: ../../lib/reveal
theme: inst126
transition: slide
---

# Functions

::: columns

:::: column
The **function** is a [very old] concept from mathematics that is now central to all
programming languages.

Python comes with a set of [built-in] functions, and allow you to create your own.
::::

:::: column

<figure style="width: 50%;">
  <img src="images/sharaf.jpg">
  <figcaption>
    <a href="https://en.wikipedia.org/wiki/Sharaf_al-D%C4%ABn_al-%E1%B9%AC%C5%ABs%C4%AB">Sharaf al-Dīn al-Ṭūsī</a><br>
    1135 - 1213
  </figcaption>
</figure>

::::

:::

[very old]: https://en.wikipedia.org/wiki/History_of_the_function_concept
[built-in]: https://docs.python.org/3/library/functions.html

::: notes
Sharaf al-Dīn al-Ṭūsī was a mathematician and astronomer who lived during 12th
century. He developed a method to approximate the root of a cubic equation.  He lived
in Damascus, Aleppo and Mosul. You may be familiar with some of those places from 
the media? It's important to remember that computer programming wasn't invented 
in Silicon Valley, and is a field with a long history with many cultural origins.
:::

# What is a Function?

::: incremental
* A function is a reusable set of **statements** that performs a specific task.
* Functions have inputs called **parameters**.
* Functions generate an output called a **return value**.
* Once **defined** functions are **called** or executed as often as you like.
:::


# Built-In Functions

::: left
Python comes with [many](https://docs.python.org/3/library/functions.html) built-in
functions, some of which you may have seen before: 
:::

```python
>>> print("hello world!")
Hello World
```

```python
>>> len("Hello World!")
12
```

# Problem Solving

::: left

When creating a program to perform a particular task it is often useful to [decompose]
a **large problem** into several **smaller parts** that are easier to understand
and test.

Consider how to make a peanut butter & jelly sandwich:

:::

::: incremental

1. Get two pieces of bread. 🍞
1. Spread jelly on one piece of bread. 🍓
1. Spread peanut butter on the other piece of bread. 🥜
1. Put the two pieces of bread together. 🥪

:::

[decompose]: https://en.wikipedia.org/wiki/Decomposition_(computer_science)

# Python Functions

::: left

Python functions are declared using the **def** keyword followed by the **name**
for your function. After the name is a set of parentheses containing an optional
list of **parameters**, followed by a colon, which begins the block of your function. 

:::

``` {.python .numberLines}
def say_hello(name):
    print("Hello", name)

say_hello("Alice")
Hello Alice
```

# Return Values

::: left

Python functions usually **return** a value. For example here's a function that
calculates the area of a circle using a radius parameter that is passed
in:

:::

``` {.python .numberLines}
def area(r):
    return 3.1415792 * r ** 2

print(area(20))
```

::: fragment
**1256.63168**
:::

# 

::: left

A function can contain multiple statements. Here's a function that calculates
the number seconds in a given number of years.

:::

``` {.python .numberLines}
def hours_in_year(year):
    days = year * 365
    hours = days * 24
    return hours

print(hours_in_year(5))
```

::: fragment
**43800**
:::

#

::: left

Can you modify the **hours_in_year** function to return the seconds in a year:

:::

``` {.python .numberLines}
def seconds_in_year(year):
    days = year * 365
    hours = days * 24
    ...

print(seconds_in_year(3))
```

#

::: left

Modify the hours_in_year function to return the seconds in a year:

:::

``` {.python .numberLines}
def seconds_in_year(year):
    days = year * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds

print(seconds_in_year(3))
```

**94608000**

# Modules

::: left

Python comes with lots of functions that are organized into **modules**, which we'll
be talking about later in the semester.

:::

``` {.python .numberLines}
import random

x = random.randint(0, 50)
print(x)
```

::: fragment
31
:::

# Review

* Functions are a useful organizational technique for solving problems.
* Use the **def** keyword to declare a function that can have optional **paramters**.
* Every function has a **return** value.
* You call a function using its **name** and by passing any variables as arguments.
* Functions can be organized into **modules** (we'll cover this later)


---
title: Data Structures 3
subtitle: Dictionaries & JSON
revealjs-url: ../../lib/reveal
theme: inst126
transition: slide
---

#

<img width="80%" src="images/dictionary.jpg">

#

<img width="80%" src="images/phone-book.jpg">

---

## What are dictionaries?

::: incremental

* Dictionaries are _unordered_ collections of key/value pairs
* They are what is referred to in other languages as an "associative array",
  "map" or sometimes "hash".
* They are similar to a phone book or real-life dictionary.
* You can add, get, modify and delete entries in a dictionary.

:::

---

## Creating dictionaries

Create a dictionary with dict() or with curly braces:

``` {.python .numberLines}
my_dictionary = dict()
my_dictionary = {}
phone_book = {
    'Bruce Banner': '555-555-1234',
    'Sue Storm': '555-555-5678'
}
```

---

## Accessing dictionaries

::: incremental

* You can look up the values in a dictionary by referencing the key

:::

::: fragment

``` {.python .numberLines}
phone_book = {
    'Bruce Banner': '555-555-1234',
    'Sue Storm': '555-555-5678'
}
print(phone_book['Bruce Banner'])
```
:::

::: fragment
**555-555-1234**
:::

---

Access the keys of a dictionary with the **keys()** method:

``` {.python .numberLines}
phone_book = {
    'Bruce Banner': '555-555-1234',
    'Sue Storm': '555-555-5678'
}
for k in phone_book.keys():
    print(k)
```

::: fragment
**Bruce Banner**  
**Sue Storm**
:::

---

Access the values of a dictionary with the **values()** method:

``` {.python .numberLines}
phone_book = {
    'Bruce Banner': '555-555-1234',
    'Sue Storm': '555-555-5678'
}
for val in phone_book.values():
    print(val)
```

::: fragment
**555-555-1234**  
**555-555-5678**
:::

---

Access the key/value pairs with the **items()** method:

``` {.python .numberLines}
phone_book = {
    'Bruce Banner': '555-555-1234',
    'Sue Storm': '555-555-5678'
}
for key, val in phone_book.items():
    print(key, val)
```

::: fragment
**Bruce Banner 555-555-1234**  
**Sue Storm 555-555-5678**
:::

---

## Modifying dictionaries

::: incremental

* The keys of a dictionary can be assigned to different values directly

::: fragment

``` {.python .numberLines}
phone_book['Bruce Banner'] = "555-555-9876"
```

:::

* If the key does not exist, a new key/value pair will be added
* Note that each key of a given dictionary must be unique

:::

---

## Deleting from a dictionary

You can remove a key/value pair from a dictionary by using the **pop** method:

``` {.python .numberLines}
phone_book = {
    'Bruce Banner': '555-555-1234',
    'Sue Storm': '555-555-5678'
}
phone_book.pop('Bruce Banner')
```

---

``` {.python .numberLines}
energy = {
  "Colorado": {
    "solar": 16530.477,
    "wind": 2942132.635
  },
  "New Jersey": {
    "solar": 2437.768,
    "wind": 19149.957
  },
  "Washington": {
    "solar": 0.0,
    "wind": 3538935.954
  }
}
print(energy['Washington']['wind'])
```

::: fragment
**3538935.954**
:::

# 

::: left
Unfortunately, not all data fits neatly into tables. What makes this
example hard to represent as a table?
:::

``` {.python .numberLines .small}
people = [
  {
    "name": "Val",
    "interests": ["astronomy", "hocky"]
  }, 
  {
    "name": "Rick",
    "interests": ["karaoke"]
  }
]
```

::: fragment
The interests can have one to many values.
:::

# APIs

<img width="70%" src="images/apis.png">

# 

## Reading a JSON File

::: left
Python comes with a [json module](https://docs.python.org/3.7/library/json.html)
which makes it easy to read JSON using the [json.load](https://docs.python.org/3.7/library/json.html#json.load) function. We'll use it to load this JSON file of tweet data: [aoc.json](aoc.json).
:::

``` {.python .numberLines}
import json

fh = open('aoc.json', encoding='utf8')
tweets = json.load(fh)

for tweet in tweets:
    print(tweet['hashtags'])
```

# Write a JSON File

::: left
You can also use the [json.dump](https://docs.python.org/3.7/library/json.html#json.dump) function to save a data structure to a file.
:::

``` {.python .numberLines .smaller}
import json

people = [
  {"name": "Val", "interests": ["astronomy", "hocky"]}, 
  {"name": "Rick", "interests": ["karaoke"]}
]

fh = open('data.json', 'w')
json.dump(people, fh)
```



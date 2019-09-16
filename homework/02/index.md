---
title: "Homework 2: Variables and Logic"
css: ../../css/page.css
---

Homework 2: Write a program to prompt for a score *between 0.0 and 1.0*. If the
score is out of range, print an error message. If the score is between 0.0 and
1.0, print a grade using the following table:

<style>
  table {
    border: thin solid black;
    width: 250px;
  }

  th {
    text-align: left;
  }

  th, td {
    border-bottom: thin solid black;
    margin: 1px;
    padding: 10px;
  }
</style>

| Score      | Grade |
| ---------- | ----- |
| &gt;= 0.9  | A     |
| &gt;= 0.8  | B     |
| &gt;= 0.7  | C     |
| &gt;= 0.6  | D     |
| &lt; 0.6   | F     |

Run it several times at the command line to make sure its output looks like this:

```
Enter score: 0.95
A

Enter score: 10.0
Bad score

Enter score: 0.9
A

Enter score: 0.75
C

Enter score: 0.5
F
```

## Rubric

* Program submitted (1pt)
* Program runs (1pt)
* Program calculates the correct grades. (2pt)
* Program checks that the input is between 0 and 1 inclusive (1pt)

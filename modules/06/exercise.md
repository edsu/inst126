---
title: "Module 5 Exercise"
css: ../../css/page.css
---

Rewrite the pay calculation from the previous exercise that will print a warning if the rate of pay is less than the minimum wage, and will prompt the user again to input the rate of pay. Your program should keep prompting for a rate of pay until a rate of pay greater than or equal to minimum wage is entered.

For example:

~~~
Enter hours: 35
Enter rate: 10.50
I'm sorry 10.50 is lower than the minimum wage. Please try again.
Enter hours: 35
Enter rate: 12.75
I'm sorry 12.75 is lower than the minimum wage. Please try again.
Enter hours: 35
Enter rate: 17.50
Pay: $612.50
~~~

Hint: if your *compute_pay* function returns *None* then you know the rate of pay was less than the minimum wage. Use an *if statement* to check the return value of *compute_pay*, and if it is *None* you can *break* out of a *while* loop.
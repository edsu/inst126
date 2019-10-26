---
title: INST126 Final Project
css: ../css/page.css
---

In the last half of the semester we will work on a project (either on your own,
or in groups of up to three) in which you will brainstorm, plan, document and
complete a Python program that performs some useful and non-trivial task.  You
may choose to create a program that relates to topics or materials covered in
INST126, or another one of your classes, or you may choose to do something
entirely new. In case this is too wide of a canvas I've got some suggestions for
a data analysis project that you might want to consider if you don't have
another idea.

### Ideas

A large part of our work this semester has been focused on writing programs that
work with data in various formats such as text, CSV and JSON, while also
learning about how to implement control flows and data structures in the Python
programming language.  For your project you may want to put this knowledge to
use by loading and analyzing a data from various publicly available sources.
Here are two resources that may help you generate some ideas for what you can do
in your project.

* [TerpFootprints Data](https://myelms.umd.edu/courses/1270637/files/folder/Project?preview=54322176): This dataset was collected from UMD's
  [TerpFootprints](https://terpfootprints.umd.edu/) site, which aggregates
  resource use on campus. The dataset is available as zip file, and when you
  unpack it you will find a set of CSV files (buildings.csv, electricity.csv
  emissions.csv, energy.csv, steam.csv and water.csv). The buildings.csv file
  is a file of metadata about buildings on campus. The other files provide
  information about the buildings over time for a given resource such as 
  electricity.

* [FiveThirtyEight Data](https://data.fivethirtyeight.com/) is a collection of
  datasets that have been used for reporting done by [FiveThirtyEight], which is a
  data journalism organization that is currently owned by ABC News. Their datasets 
  tend to focus on sports and politics, and are also available via 
  [GitHub](https://github.com/fivethirtyeight/data).

* [Data is Plural](https://tinyletter.com/data-is-plural) is a weekly email 
  newsletter from [Jeremy Singer-Vine](https://twitter.com/jsvine) on the subject
  of publicly available useful/interesting datasets. IN each episode Jeremy
  describes a handful of datasets, including information about who created it,
  how much data it contains, what format it is in, how the data is useful, 
  and where to find it. They can be CSV files, spreadsheets, images, maps, and
  downloadable databases of all kinds. Browse the [archive](https://tinyletter.com/data-is-plural/archive) of past newsletters
  or take a look at the [spreadsheet](https://docs.google.com/spreadsheets/u/1/d/1wZhPLMCHKJvwOkP4juclhjFgqIY8fQFMemwKL2c64vk/edit) he has created for 
  all the datasets he has covered. See if you can find a dataaset that
  might be interesting to use in your project.

* [Public APIs](https://github.com/toddmotto/public-apis#readme) is a list of
  publicly available web APIs curated on GitHub by [Todd
  Motto](https://twitter.com/toddmotto). The APIs are listed by category
  (music, news, games, books, sports, weather, animals, etc) and indicates
  whether you need to authenticate, whether it uses a secure connection, and a
  link to the documentation. You could use what we learned about using the
  requests module to obtain data from one of the APIs, or even create a "mashup"
  of two or more.

### Deliverables

The purpose/goals of your project application are entirely up to you,
but in order to fulfill the requirements of the assignment, you should do the
following:

* Create a README file that documents what the program does, and how it should be used.
* Create one or more Python files that make up your application.
* Supply any additional data that is needed by your program.
* Put all these files into a directory, zip it up, and upload it to ELMS.

### Evaluation

The final project is worth 15 points (15% of your final grade). You will be
graded on the following:

* Concept/Idea (5 pts): novelty, utility, audacity, conciseness, currency.
* Execution (5 pts): ability to run the program & tests, use of functions, modules, and code style.
* Documentation (5 pts): the project includes a README file that details where the data came from (if any), and how to use the program, and what it is supposed to demonstrate.

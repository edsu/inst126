---
title: InstallFest!
css: ../../../css/page.css
---

Historically, [InstallFests] were community events where computer enthusiasts
would get together to install the Linux operating system. It wasn't trivial to
install Linux when it first started to get popular in the 1990s. So it was much
easier if you had the help from others when you first tried to get it running.
The term InstallFest got popularized to mean really any kind of computing event
where a group of people installed [open source] software.

Today we're going to have our own InstallFest to get set up with some of the
tools that we'll be using over the course of the semester.  That's right, all
the tools we'll be using are freely available and open source.  It wasn't that
long ago when most people thought open source was a pipe dream that would never
work. It has been wildly successful, to the point now where Linux is running on
most of the world's smartphones and webservers. However, the democratic or even
socialist goals of the early free software and open source movement have been
largely unrealized. Some think that open source software has led to even greater
[concentrations of wealth] and inequality in society.

Be that as it may, it is useful for us to a) not have to pay for the software
and b) for it to work well. Fortunately those two things align in some open
source software projects. Unlike in the early days of Linux you should find
operating specific installers for all of the tools we'll be installing today,
which  hould take care of most of the details. But expect some roadblocks as we
discover some things.

## Slack

First make sure you are able to log in to the iSchool Slack and join the
\#inst126 channel.

https://umd-cis.slack.com

This will be a good place to ask questions about pieces of code, error messages,
and to work with other people during class and when you are at home.

## Python3

This is the big one since we're going to be using the Python programming
language to learn about object-oriented programming this semester. If you
already have it on your computer from another class (e.g. INST126) it could
still be useful to get the latest version v3.7.2. You may have used something
like Jupyter Notebooks in your browser last year, which were running on a server
somewhere else. This semester you will be running Python on your laptop.

You should find the Python3 download for your operating system when you visit this page:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

## Git

Git is the world's most popular [version control system]. Version control
systems allow you to manage the changes you make to the programs that you will
be writing. It also allows you to share your code with other people, on sites
like [GitHub] or [GitLab].  As we'll be discussing later in the semester the
code that we'll be writing will live in files on your computers, and as you
change those files you may want to go back to a previous version, or share them
with your classmates. Think of version control as something like the version
history you can see in a Google Doc.

Select the Git appropriate installer for your operating system here:

[https://git-scm.com/downloads](https://git-scm.com/downloads)

## Code

To write code you need an [text editor]. Last semester many of you used [Jupyter
Notebooks] which allowed you to write code in your browser. Jupyter Notebooks
are great because you can simply point your browser at the notebok on the
web,anddon't need to install anything locally on your computer. They are also
perfect for data science work where you want to share some analysis and data
with the world in an interactive and dynamic format.

However when you are developing software applications as part of a team it's
often useful for you to be able to edit code in a [integrated development
environment] (IDE) which helps you write and execute code, look at
documentation, and your filesystem all in the same application. 

If you already have a text editor that you like, and are comfortable opening a
terminal window and typing commands there please feel free to use it. However
I'll be using [Visual Studio Code] (otherwise known as VSCode or just Code) in
class because it has nice Python and Git support. It is gaining quite a bit of
popularity in programming circles at the moment, so you will be learning to use
a relevant tool.

To install Code, download the installer for your  operating system here:

[https://code.visualstudio.com/](https://code.visualstudio.com/)

After you've installed Code, start it up and install the Python extension by
going to *Preferences* -> *Extensions* and then search for "Python". You should
see the *Python Extension* from Microsoft which you can install. When it prompts
you which Python to use select the version we just installed v3.7.2.

## Hello World

If you have time see if you can figure out how to create your first program in Code:

```python
print("hello world")
```

[InstallFests]: https://en.wikipedia.org/wiki/Linux_user_group#Installfests
[version control system]: https://en.wikipedia.org/wiki/Version_control
[GitHub]: https://github.com
[GitLab]: https://about.gitlab.com/
[open source]: https://opensource.org/osd-annotated
[text editor]: https://en.wikipedia.org/wiki/Text_editor
[Jupyter Notebooks]: https://jupyter.org/
[Visual Studio Code]: https://code.visualstudio.com/
[concentrations of wealth]: https://en.wikipedia.org/wiki/SCO%E2%80%93Linux_disputes#Microsoft_funding_of_SCO_controversy

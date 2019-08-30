# This is an advanced alternative to your first Hello World that creates a web server.
# Eventhough the program is quite short, there is a lot going on that you will not 
# understand until the end of the semester. Something to look forward to!
#
# When you run it you will start a webserver on your computer, which you can then visit
# in your web browser at:
#
#     http://localhost:5000/
#
# Before you can run this you will need to install flask from the command line terminal:
#
#     pip install flask

from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World Wide Web!"

app.run()
# Embedded Linux

Hello, and welcome to Josh Simons's repository for the embedded linux class.  This repository will be used as an example of ways to maintain a code base while working on a project. This is **NOT** the Embedded Linux class itself.  That is hosted on Google Classroom.  Please contact Josh Simons: "simonsj [at] newpaltz [dot] edu" if you are in the class, but do not have the classroom code.

# Branch Notes

**tempFlask:** This branch is an alternative to tempWeb that uses Flask instead of lighttpd, and sqlite3 instead of reading the .csv directly.
the code all resides in flaskRoot.  The javascript necessary to render the visualizations was rolled driectly into the index.html
The tempLogger.py file starts the logging and web servers.  Temperature logging was changed to utilize the i2c sensor instead of the DH22 sensor.

The Flask server is contained withiin it's own thread and run as a daemon.  It sets the app route for the sqlite quert, and serves the index.html

The  Temperature logging takes place in the main thread. It logs the temperature to the sqlite database every 60 seconds and sends a text message alert if the temperature is out of range.

There is one disadvantage to this implementation. For an unknown and unfathomable reason the delay timer in the main thread hangs the communication between the Flask server and the browser.  This is only apparent on the initial loading of the page.  After that the chartes reload every 60 seconds synchronized with the new temperature readings.  While this syncronization is not strictly necessary, it is nice.  Alternatively the Flask server and the Temperature logger could be called from two differrent scripts.  This would eliminate the initial onload delay, but would not necessarily sync. I wanted to see how much I could get done from the same script, and wanted to play around with threadding, so here we are.

#Libraries, Frameworks and Applications Used:
**Python:** For the app itself.  Links the libraries and frameworks, logs the data. Does the stuff

**Python Libraries and Frameworks:** 

Flask: This is our web app framework.  It creates the routes and serves the web page and data up.

time: Keeps on ticking... into the future

os: sometime you just have to clear the console.

smtplib: Allows us to use a SMTP server to send email. This is uses a email to text gateway to send the sms  

json: Kinda crucial to pass the data as a json

threading: Do all the things at the same time!!

**sqlite3:** Our humble little database


That's about it! This was a fun little project.

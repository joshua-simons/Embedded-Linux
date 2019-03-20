# Embedded Linux

Hello, and welcome to Josh Simons's repository for the embedded linux class.  This repository will be used as an example of ways to maintain a code base while working on a project. This is **NOT** the Embedded Linux class itself.  That is hosted on Google Classroom.  Please contact Josh Simons: "simonsj [at] newpaltz [dot] edu" if you are in the class, but do not have the classroom code.

# Branch Notes

**tempFlask:** This branch is an alternative to tempWeb that uses Flask instead of lighttpd, and sqlite3 instead of reading the .csv directly.
the code all resides in flaskRoot.  The javascript necessary to render the visualizations was rolled driectly into the index.html
The tempLogger.py file starts the logging and web servers.  Temperature logging was changed to utilize the i2c sensor instead of the DH22 sensor.
There are two threads set up to run as daemons in the tempLogger.py.  One thread loggs the temperature every 60 seconds and sends a text message alert if the temperature is out of range.
The other thread is the Flask server.  It sets the app routes for the sqlite queries, and serves the index.html
The index.html updates the page every 60 seconds synchronous with the update of the database. The web page is always 59 seconds behind the reading, but I don't care enough to make the sync perfect.

#Libraries, Frameworks and Applications Used:
**Python:** For the app itself.  Links the libraries and frameworks, logs the data. Does the stuff
    **Python Libraries and Frameworks:** Flask: This is our web app framework.  It creates the routes and serves the web page and data up.
					time: Keeps on ticking... into the future
					os: sometime you just have to clear the console.
					smtplib: Allows us to use a SMTP server to send email.  This is uses a email to text gateway to send the sms
					json: Kinda crucial to pass the data as a json
					threading: Do all the things at the same time!!
**sqlite3:** Our humble little database


That's about it! This was a fun little project.

# Embedded Linux

Hello, and welcome to Josh Simons's repository for the embedded linux class.  This repository will be used as an example of ways to maintain a code base while working on a project. This is **NOT** the Embedded Linux class itself.  That is hosted on Google Classroom.  Please contact Josh Simons: "simonsj [at] newpaltz [dot] edu" if you are in the class, but do not have the classroom code.

# Branch Notes

**tempFlask:** This branch is an alternative to tempWeb that uses Flask instead of lighttpd, and sqlite3 instead of reading the .csv directly.
the code all resides in flaskRoot.  The static directory hosts static .js and .css files necessary to serve the page.  The tempServer.py file starts the logging and web servers.  Temperature logging was changed to utilize the i2c sensor instead of the DH22 sensor.

#lighttpd

See Google Classroom for instructions on the configuration of lighttpd

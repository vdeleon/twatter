Twatter
=======
Conor Farrell

Twatter is a library of some "useful" functions that you may want to use when playing with Twython. To use:

  git pull https://github.com/lithiumoxide/twatter

and then in your .py file:

  from twatter import Twatter

This is very much a work in progress, and more of a learning project for me than anything. It's likely that you will find a number of errors and/or better ways to do things. The wiki for the project will contain more complete documentation, and will be updated as this project develops.


Examples
--------

tw.py
-----
This builds up location stats about followers of a user. Simply give it the username, and run it. It'll build up a dictionary of locations:number.

tw_freq.py
----------
This calculates the rate of tweets per minute for the given keywords (could be hashtags, for example), and alert you if that frequency breaks a threshold. The cycle will repeat as often as the user defines, with a user-defined threshold and waiting time between each cycle. Some aspects of this need work, including date/time stuff.

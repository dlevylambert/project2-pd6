Project: E-memberall
--------------------
This project is a calendar-reminder application which allows users to record what they have to do on any day of the week.  The other main feature of this application is the sending of text notifications to users that remind the user of what he/she listed for a particular day.  This portion of the project uses the Twilio API.  All web functionality(i.e. saving events, setting reminder times, enabling/disabling reminders) are also available on the phone with the use of a somewhat specific text scheme.  Oh, this is also why users are required to enter a phone number to sign up.  Those who plan on enabling reminders are recommended to have some sort of texting plan. ...

###Hosted at:
<br>ml7.stuycs.org:6004

###Instructions:
<br>
Run app.py in a UNIX environment in the following ways:
*python app.py
*python torn.py
*gunicorn -D -p pidfile -w 4 -b 0.0.0.0:6004 app:app

###Authors:
<br>Nathaniel Biggs, Michael Cohen, Zambeta Tsapos, Hon Wei Khor

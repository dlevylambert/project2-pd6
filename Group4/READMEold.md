Project:Calendar thing with things on the thing

Database Library(Michael Cohen)-mongopy
---------------------------------------
User -> Dates
Needs:
User Authentication?
Get methods for:
Information, given date+user
Set methods for:
Information, given date+user

UI and HTML(Zambeta Tsapos)-Static, Templates
---------------------------------------------
PAGES:
-Login page(Front page, "Home" page)
 	  -User, PW, etc.
-Homepage with small calendar
	  -Everyday is a link -> goes to page with stuff for that day
-Page for specific date

Working with API(Nathaniel Biggs)-Twilio
----------------------------------------
-Passes external database stuff to Zambeta's pages

Application(Hon Wei Khor)-app.py
--------------------------------
-Pass information to Zambeta's stuff using Michael's library stuff
      -Day of week of date, i.e. day of week of first day, gaussain algorithm
      -http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Purely_mathematical_methods
-Flask stuff
-Look at whatever HTML needs

Twilio: 
- Texting calendar with notification
- Foursquare music sharer
- Texting to-do list (viewable from phone and comp) 
- Navigation/Public Transportation
- Weather Updates
- Dictionary
- All/some of the above?

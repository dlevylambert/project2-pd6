Group Members:
      Sarah Babski: Area Leader: Database work with mongo for storing searches and users

      Oliver Ball: Project Leader, area leader: Flask elements 

      Alicia Vargas Morawetz: area leader: html/visual aspects of the project

      Daniel Teehan: area leader: python code and algorithm for school match/API work

Name: School Finder

Description:
      Using the NYC high schools API that we looked at briefly in class to create a program where a person could be matched with a high school based on a number of factors that they input. I.e they would specify how they value distance, quality of school (SAT scores), diversity, size etc. and the program would return a list of compatible schools by analyzing with the the API info. For the location parameter, we narrowed down the school by borough.

Update: The Project will consist of a page where a user can input their priorities in looking for a high school, ranking academics (based on SAT scores, another possible element would be prioritizing the reading/writing/math quality of the school by SAT scores), distance, and the school's overall rating. The user could also indicate the ideal size of the school from three options to limit the results as well as indicate the number of results they want to see. Upon submitting the user will be redirected to a page listing the designated amount of results with information on the school, the sat scores, and potentially a percentage of compatibility with the results. If possible we would like to be able to save searches, or maybe just results, for particular users for reference. 

Instructions:
	Unfortunately most of the functionality of the project is unavailable to the user. The login page works, as does the signup page, but they don't actually serve a real purpose because no search data is stored for the user. If you click on search, you can fill out the form, but it will result in one of two crashes. The page crashes if you don't fill out all of the fields, and it also crashed if you fill them all out. To see what should come out of a proper search, go to :6001/search/result. The code for displaying a non dummy result is commented out in app.py to show that the majority of the code works.

API's in question:
https://developers.google.com/maps/ #were unable to implement this
https://data.cityofnewyork.us/Education/2009-School-Survey/ens7-ac7e
https://data.cityofnewyork.us/Education/SAT-College-Board-2010-School-Level-Results/zt9s-n5aj

Actual Google api:
Distance:
       https://maps.googleapis.com/maps/api/distancematrix/output?parameters

Required installs: 
- Flask (duh)
- Flask-login

Applications is run out of port 6001 (pd6 group 01)

There is a disjoint between the search and result page because of a function which does not work. This function is the int() function which should be implemented by default in all python programs. I've tested that the application works both before and after this break, so if I could just get that to work everything would fall into place. I got the login stuff to work, but we didn't end up using it so its kind of pointless despite how long it took. To test the result page go to ...:6001/search/result .
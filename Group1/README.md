Sarah Babski: Area Leader: Database work with mongo for storing searches and users

Oliver Ball: Project Leader, area leader: Flask elements 

Alicia Vargas Morawetz: area leader: html/visual aspects of the project

Daniel Teehan: area leader: python code and algorithm for school match/API work

Use the NYC high schools API that we looked at briefly in class to create a program where a person could be matched with a high school based on a number of factors that they input. I.e they would specify how they value distance, quality of school (SAT scores), diversity, size etc. and the program would return a list of compatible schools by analyzing with the the API info. For the location parameter, we can try to incorporate the google maps API to measure commute time between locations.

Update: The Project will consist of a page where a user can input their priorities in looking for a high school, ranking academics (based on SAT scores, another possible element would be prioritizing the reading/writing/math quality of the school by SAT scores), distance, and the school's overall rating. The user could also indicate the ideal size of the school from three options to limit the results as well as indicate the number of results they want to see. Upon submitting the user will be redirected to a page listing the designated amount of results with information on the school, the sat scores, and potentially a percentage of compatibility with the results. If possible we would like to be able to save searches, or maybe just results, for particular users for reference. 

API's in question:
https://developers.google.com/maps/
https://data.cityofnewyork.us/Education/2009-School-Survey/ens7-ac7e
https://data.cityofnewyork.us/Education/SAT-College-Board-2010-School-Level-Results/zt9s-n5aj

Actual Google api:
Distance:
       https://maps.googleapis.com/maps/api/distancematrix/output?parameters

Required installs: 
- Flask (duh)
- Flask-login
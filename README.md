#README

##PRE-REQUISITES:
1.Git clone from the [https://github.com/SteffiBaumgart/Other/BusinessOpticsTask](this link)

2.Ensure that Python is installed (any version)

3.Ensure that the Flask and Requests libraries are installed, as well as D3.js

##HOW TO RUN:
1.Navigate to the project directory in the terminal
2.Type 'python TitanicSurvival.py' to run the application
3.Go to http://0.0.0.0:8080/ to view the home page
4.Press CTRL+C in terminal to quit the application
5.Kill all proccesses listening on port 8080 (e.g. with fuser -k 8080/tcp) 

##ISSUES AND FUTURE WORK:
Any hyperlink clicked on the main page does not go to the query's graph. This is due to my limited knowledge of HTML. What I would want to due in the future, is convert each SVG (scalable vector graphic) in the age.html, cabclass.html and sex.html to a png/jpeg image, and display the 3 images in one html page. I would also like to improve my D3 skills, and make the graphs compare survivorship to how many passengers embarked. 

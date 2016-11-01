#Titanic Survival
#Steffi Baumgart
#October 2016


from __future__ import print_function
import requests
from flask import Flask, render_template, make_response

app = Flask(__name__)
passengers = []

class Passenger:

    #constructor
    def __init__(self, id, survival, cabclass, age, sex, name, ss, pc, embarked):

        self.passenger_id = id
        self.survival = survival
        self.cabclass = cabclass #cannot name 'class' as it is a reserved word
        self.age = age
        self.sex = sex
        self.name = name
        self.number_of_siblings_and_spouses_aboard = ss
        self.number_of_parents_and_children_aboard = pc
        self.embarked = embarked


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/graphs')
def graphs():

    #using requests library
    content = requests.get("https://titanic.businessoptics.biz/survival").json()
    print("Successful retrieval of JSON data\n") #prints message in terminal

    noEmbarked=0

    #create an object 'person' for each passenger's details & append to list
    for p in content:
        person = p['passenger_id'], p['survived'], p['class'], p['age'], p['sex'], p['name'], p['number_of_siblings_and_spouses_aboard'], p['number_of_parents_and_children_aboard'], p['Embarked']
        passengers.append(person)
        noEmbarked+=1

    #arrays for each query
    sexSurvived = []
    cabclassSurvived = []
    ageSurvived = []


    #if survival = 1 -> the passenger survived
    for p in passengers:
        if p.survival == '1':
            cabclassSurvived.append(p.cabclass)
            ageSurvived.append(float(p.age))
            sexSurvived(p.sex)


    #QUERY 1: Sex
    men = sexSurvived.count("male")
    women = sexSurvived.count("female")


    #QUERY 2: Age
    zero, ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred = 0

    for item in ageSurvived:

        if item<10:
            zero+=1

        elif item<20:
            ten+=1

        elif item<30:
            twenty+=1

        elif item<40:
            thirty+=1

        elif item<50:
            forty+=1

        elif item<60:
            fifty+=1

        elif item<70:
            sixty+=1

        elif item<80:
            seventy+=1

        elif item<90:
           eighty+=1

        elif item<100:
           ninety+=1

        else:
            hundred+=1


    # QUERY 3: Class
    first = cabclassSurvived.count("1")
    second = cabclassSurvived.count("2")
    third = cabclassSurvived.count("3")


    #Save each query's results to .tsv file
    with open("sex.tsv", "w") as f:
     print ("%s\t%s\t%s" % ("men", "women"), file=f)
     print ("%s\t%s\t%s" % (men, women), file=f)

    print("Surivival by sex data saved\n")


    with open("cabclass.tsv", "w") as f:
     print ("%s\t%s\t%s" % ("1", "2", "3"), file=f)
     print ("%s\t%s\t%s" % (first, second, third), file=f)

    print("Surivival by cabin class data saved\n")


    with open("age.tsv", "w") as f:
     print ("%s\t%s\t%s" % ("0", "10","20","30","40","50","60","70","80","90","100"), file=f)
     print ("%s\t%s\t%s" % (zero, ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred), file=f)

    print("Surivival by age data saved\n")



#Error 404
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    return resp



if __name__ == "__main__":
    #make the server publicly available
    app.run(host='0.0.0.0', port=8080)






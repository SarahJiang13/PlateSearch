import os.path
import csv
import json
from flask import Flask, Response, request,jsonify

app = Flask(__name__)
app.config.from_object(__name__)

csvfile = open('rnp_counts.csv')
carPlate = range(1, 4)



@app.route('/getPlate', methods= (['GET']))
def getPlate():
    testList = {
            "Plate": "ABC123",
            "Recievetimeutc": "25/06/2021",
            "State": "NSW"
        }
    return testList

    

def root_dir(): 
    return os.path.abspath(os.path.dirname(__file__))



def get_file(filename):  
    try:
        src = os.path.join(root_dir(), filename)
       
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/')
def titlePage():
    content = get_file('index.html')
    return (content)

def searchForState(row):
    # This function takes in the row from the CSV File
    # And converts it into a State or Territoy of Australia, i.e.
    # NSW, QLD, ACT, VIC etc.
    # In this CSV File, a state is true if it has a 1 valve
    # row[9], row[10], row[11], row[12], row[13], row[14] are all the states
    if row[4] == 1:
        return "VIC"
    if row[9] == 1:
        return "NSW"
    if row[11] == 1:
        return "TAS"
    else:
        return "No State Found"

@app.route('/plate', methods= (['POST']))
def database():
    sarahsRequest = request.get_data()
    jsonrequest = sarahsRequest.decode('utf8').replace("'",'"')
    jsonrequest = json.loads(jsonrequest)
    plate = jsonrequest["plate"]
    displayStr = str()
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    
    date = 'date'
    state = 'state'
    jsonDict = {
        "Plate": plate,
        "Recievetimeutc": date,
        "State": state,
    }


    

    for row in reader:
        if line_count == 0:

            print(str(jsonrequest))
            line_count += 1
        else:
            state == row[9], row[10], row[11], row[12], row[13], row[14]
            displayStr = displayStr + (f'{row[1]}  {row[2]}   {row[3][0]}    {row[15]}\r')
            if row[1] == str(plate):
                print("Plate is: " + plate)
                print('Recievetimeutic:   '+ str(row[15]))
                print('State is: ' + state)
                
            line_count += 1
    # Create a dictionary
   
    returnJson = json.dumps(jsonDict)
    # 
    # print(f'Showed {line_count} lines')
    # dictionary = dict(reader)
    content = get_file('index.html')
    return Response(returnJson, mimetype="text/json")
    
        #if car == 4:
            #print(f'\t{row[1]}')


if __name__ == '__main__':
    app.run('0.0.0.0',5001)
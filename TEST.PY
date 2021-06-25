import os.path
import csv
import json
from flask import Flask, Response, request,jsonify

app = Flask(__name__)
app.config.from_object(__name__)

csvfile = open('rnp_counts.csv')

carPlate = range(1, 4)

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
    # row[9], row[10], row[11], row[12], row[16], row[14] are all the states
    if row[4] == '1':
        return "VIC"
    elif row[9] == '1':
        return "NSW"
    elif row[10] == '1':
        return 'QLD'
    elif row[11] == '1':
        return "TAS"
    elif row[12] == '1':
        return 'ACT'
    elif row[16] == '1':
        return 'WA'
    else:
        return "No State Found"

@app.route('/plate', methods= (['POST']))
def database():
    # Open the CSV File
    csvfile = open('rnp_counts.csv')
    # The request coming in from the server
    sarahsRequest = request.get_data()
    # Decoding the request
    jsonrequest = sarahsRequest.decode('utf8').replace("'",'"')
    jsonrequest = json.loads(jsonrequest)
    # Finding the sent plate
    plate = jsonrequest["plate"]
    # Explict set of jsonDict
    jsonDict = None
    # Reader set
    reader = csv.reader(csvfile, delimiter=',')
    # Go after headers
    next(reader)
    for row in reader:
        if row[1] == str(plate):
            date = str(row[15])
            state = searchForState(row)
            print("Plate is: " + plate)
            print('Recievetimeutic:   '+ str(row[15]))
            print('State is: ' + searchForState(row))
            jsonDict = {
                "Plate": plate,
                "Recievetimeutc": date,
                "State": state,
            }
    # Close the CSV File
    csvfile.close()
    if jsonDict is not None:
        returnJson = json.dumps(jsonDict)
        return Response(returnJson, mimetype="text/json")
    else:
        return Response(json.dumps({"Error": "No Plate Found"}), mimetype="text/json")
        
        


if __name__ == '__main__':
    app.run('0.0.0.0',5001)

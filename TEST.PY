import os.path
import csv
import json
from flask import Flask, Response, request

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
    content = get_file('website.html')
    return (content)

@app.route('/plate', methods= (['POST']))
def database():
    sarahsRequest = request.json
    print(sarahsRequest)
    displayStr = str()
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count == 0:
            print(f'Car plates:  {",". join(row)}')
            displayStr = displayStr + (f'Car plates:  {",". join(row)}') + '\n'
            line_count += 1
        else:
            displayStr = displayStr + (f'{row[1]}  {row[2]}   {row[3][0]}    {row[15]}\r')
            if row[1] == sarahsRequest:
                print(f'\t{row[1]}     {row[15]}  {row[9]}')
            line_count += 1
    # Create a dictionary
    jsonDict = {
        "Plate": 'EXTRACTEDPLATE',
        "Recievetimeutc": 'date',
        "State": "NSW",
    }
    returnJson = json.dumps(jsonDict)
    # 
    # print(f'Showed {line_count} lines')
    # dictionary = dict(reader)
    content = get_file('Index.html')
    return Response(returnJson, mimetype="text/json")
    


if __name__ == '__main__':
    app.run('0.0.0.0',5001)
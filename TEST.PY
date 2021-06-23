from os import path
import csv
from flask import Flask, Response

app = Flask(__name__)
app.config.from_object(__name__)

csvfile = open('rnp_counts.csv')
carPlate = range(1, 4)
# Just return NIH463, Last recieved time

@app.route('/', methods= (['GET']))
def database():
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
            if row[1] == 'NIH463':
                print(f'\t{row[1]}     {row[15]}')
            line_count += 1
    print(f'Showed {line_count} lines')
    dictionary = dict(reader)
    return Response(displayStr)
    
        #if car == 4:
            #print(f'\t{row[1]}')


if __name__ == '__main__':
    app.run('0.0.0.0',5001)
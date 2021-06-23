from os import path
import csv
from flask import Flask, Response

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods= (['GET']))
def database():
    csvfile = open('rnp_counts.csv')
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0

    for row in reader:
        if line_count == 0:
            print(f'Car plates:  {",". join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}     {row[1]}')
            line_count += 1
    print(f'Showed {line_count} lines')
    csvfile.close()
    return Response(reader)
    



    if __name__ == '__main__':
        database()
        app.run()

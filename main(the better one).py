import os.path
import csv 
from flask import Flask, Response


app = Flask(__name__)
app.config.from_object(__name__)
with open('rnp_counts.csv') as csvfile:
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
    
def root_dir(): 
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  
    try:
        src = os.path.join(root_dir(), filename)
       
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route('/', methods=['GET'])
def metrics():  
    
    content = get_file('webstie.html')
    return Response(csvfile, mimetype="text/html")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)


if __name__ == '__main__':  
    app.run()


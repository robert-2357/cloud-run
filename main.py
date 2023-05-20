import os
import tempfile
import pypandoc
from werkzeug.utils import secure_filename
from flask import Flask, send_file, request
def get_file_path(filename):
  file_name = secure_filename(filename)
  return os.path.join(tempfile.gettempdir(), file_name)
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def md2pdf():
  if request.method == 'POST':
    file = request.files['file']
    filename=secure_filename(file.filename)
    file.save(get_file_path(filename))
    output = pypandoc.convert_file(get_file_path(filename), 'pdf', outputfile='file.pdf
        ')
    return send_file('file.pdf', mimetype='application/pdf')
else:
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
     <input type=submit value=Upload>
     </form>
     '''
if __name__ == "__main__":
     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

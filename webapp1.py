from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import file_read
from datetime import datetime




app = Flask(__name__)
app.config['SECRET_KEY'] = '1111'
class UploadFileFrom(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@app.route('/', methods = ['GET','POST'])
@app.route('/home', methods = ['GET','POST'])
def home():
    form = UploadFileFrom()
    if form.validate_on_submit():
        file = form.file.data
        uploadedfile = str(datetime.now()).replace(" ","")
        file_read.upload_to_blob(file, uploadedfile)
        file_read.send_message_queue(uploadedfile)
    return render_template('index.html', form=form)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
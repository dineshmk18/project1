from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



                                                               
db_uri = f'mysql+mysqlconnector://dinesh:Banglore#1998@db-server:3306/dineshdb'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri


db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)

# Create the table
with app.app_context():
    db.create_all()



@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # fetch the form data
        userDetails = request.form
        name = userDetails['name']
        age = userDetails['age']
        gender = userDetails['gender']
        symptoms = userDetails['symptoms']

        new_patient = Patient(name=name, age=age, gender=gender, symptoms=symptoms)

        # Add the patient to the database
        with app.app_context():
          db.session.add(new_patient)
          db.session.commit()

        return redirect('/patient_list')
    
    return render_template('patient_form.html')

@app.route('/patient_list', methods=['GET'])
def patient_list():
    patients = Patient.query.all()
    return render_template('patient_list.html', patients=patients)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)

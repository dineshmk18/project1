from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



                                                               
db_uri = f'mysql+mysqlconnector://dinesh:Banglore#1998@db-service:3306/dineshdb'
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
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        symptoms = request.form['symptoms']

        new_patient = Patient(name=name, age=age, gender=gender, symptoms=symptoms)

        # Add the patient to the database
        with app.app_context():
          db.session.add(new_patient)
          db.session.commit()

        return 'Patient details submitted successfully'
    
    return render_template('patient_form.html')


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask,render_template,url_for,request
import joblib
random_forest = joblib.load(r"C:\Users\asus\Desktop\projects\insurance_cost\models\randomforest_model")  # loaded 

app = Flask(__name__)

@app.route('/')  # url 
def home():
    return render_template('home.html')


@app.route('/form')  # http://127.0.0.1:5000/project
def project():
    return render_template('form.html')

@app.route('/contact')  # http://127.0.0.1:5000/project
def contact():
    return render_template('contact.html')


@app.route('/submit_form',methods=['GET','POST']) # http://127.0.0.1:5000/predict
def predict():
    if request.method == "POST":
        # to recieve the data 
        region = request.form['region']
        child = int(request.form['child'])
        smoker = (request.form['smoker'])
        gender = (request.form['gender'])
        bmi = int(request.form['bmi'])
        age = int(request.form['age'])
        region_northwest = 0
        region_southeast = 0
        region_southwest = 0
        if region == 'se':
            region_southeast = 1 
        elif region == 'sw':
            region_southwest = 1
        else:
            region_northwest = 1

        gender = 1 if gender == 'male' else 0
        gender = 1 if gender == 'female' else 0

        # x_variables 
        unseen_data = [[age,gender,bmi,child,smoker,
                        region_northwest,region_southeast,
                        region_southwest]]
        
        print(unseen_data)
        prediction = str(random_forest.predict(unseen_data)[0])
        print(prediction)
        return render_template('output.html', 
                age=age, 
                bmi=bmi, 
                child=child, 
                gender_male=gender, 
                smoker_yes=smoker, 
                region_northwest=region_northwest, 
                region_southeast=region_southeast, 
                region_southwest=region_southwest, 
                insurance_charges=prediction
            )


if __name__ == "__main__":
    app.run(debug=True) 
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask,request,jsonify
import pickle
import numpy as np

model=pickle.load(open('model1.pkl','rb'))
app= Flask(__name__)
@app.route('/')
def home():
    return "Hell World"

@app.route('/predict',methods=['POST'])
def predict():
    bmi=request.form.get('bmi')
    smoking=request.form.get('smoking')
    alcoholDrinking=request.form.get('alcoholDrinking')
    stroke=request.form.get('stroke')
    physicalHealth=request.form.get('physicalHealth')
    mentalHealth=request.form.get('mentalHealth')
    diffWalking=request.form.get('diffWalking')
    sex=request.form.get('sex')
    ageCategory=request.form.get('ageCategory')
    diabetic=request.form.get('diabetic')
    physicalActivity=request.form.get('physicalActivity')
    genHealth=request.form.get('genHealth')
    sleepTime=request.form.get('sleepTime')
    asthma=request.form.get('asthma')
    kidneyDisease=request.form.get('kidneyDisease')
    skinCancer=request.form.get('skinCancer')
    input_data=np.array([[bmi,smoking,alcoholDrinking,stroke,physicalHealth,mentalHealth,
                          diffWalking,sex,ageCategory,diabetic,physicalActivity,genHealth,
                          sleepTime,asthma,kidneyDisease,skinCancer]])

    result= model.predict(input_data)[0]
    print('before ')
    print(result)
    print(' after')
    return jsonify({'Placement':result})
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

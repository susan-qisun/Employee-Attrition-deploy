from flask import Flask,render_template,request
import numpy as np
import pickle

model=pickle.load(open('Employee_attrition.pkl','rb'))

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def new():
    return render_template('new.html')

@app.route('/predict', methods=['POST','GET'] )
def predict():
    data1=float(request.form['a'])
    data2=float(request.form['b'])
    data3=float(request.form['c'])
    data4=float(request.form['d'])
    data5=float(request.form['e'])
    data6=float(request.form['f'])
    data7=float(request.form['g'])
    data8=float(request.form['h'])
    data9=float(request.form['i'])
    data10=float(request.form['j'])
    data11=float(request.form['k'])
    data12=float(request.form['l'])
    data13=float(request.form['m'])
    data14=float(request.form['n'])
    data15=float(request.form['o'])  
    features=np.array([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15])
    pred = model.predict([features])
    
    def statement():
        if pred == 0:
            return 'Result:- The model has predicted that your employee is not inclined to leave your company.'
        elif pred == 1:
            return 'Result:- Your employee will leave your company!'
    
    return render_template('new.html',statement=statement())


if __name__=='__main__':
    app.run()

from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', y_pred=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    hewan, diagnosa = [x for x in request.form.values()]

    data = []

    if hewan == 'Anjing':
        data.extend([0])
    elif hewan == 'Kucing':
        data.extend([4])
    elif hewan == 'Unggas':
        data.extend([11])
    elif hewan == 'Kera':
        data.extend([2])
    elif hewan == 'Musang':
        data.extend([5])
    elif hewan == 'Sugar Glider':
        data.extend([8])
    elif hewan == 'Tokek':
        data.extend([9])
    elif hewan == 'Ular':
        data.extend([10])
    elif hewan == 'Kura-kura':
        data.extend([13])
    elif hewan == 'Kelinci':
        data.extend([1])
    elif hewan == 'Sapi Perah':
        data.extend([6])
    elif hewan == 'Sapi Potong':
        data.extend([7])
    elif hewan == 'Kambing':
        data.extend([12])
    else:
        data.extend([3])

    if diagnosa == "Abses":
        data.extend([1])
    elif diagnosa == "Abortus":
        data.extend([0])
    elif diagnosa == "Aggenesis Annis":
        data.extend([2])
    elif diagnosa == "Alergi Saluran Nafas":
        data.extend([3])
    elif diagnosa == "Anorexia":
        data.extend([4])
    elif diagnosa == "Arthritis":
        data.extend([5])
    elif diagnosa == "Blepharitis":
        data.extend([6])
    elif diagnosa == "Bronkitis":
        data.extend([7])
    else:
        data.extend([8])
    
    prediction = model.predict([data])
    var1 = round(prediction[0], 2)
    
    if var1 == 2: 
        output = "Cefotaxime,dexamethason,biosolamin,septo skin spray" 
    elif var1 == 6: 
        output = "Vetoxy LA, Vit B-Comp, Sulpidoney"
    elif var1 == 5: 
        output = "OP PEMBUATAN ANUS" 
    elif var1 == 8: 
        output = "Vitol ADE, Vetadryl, Vit B-Comp"
    elif var1 == 7: 
        output = "Vit B-Comp" 
    elif var1 == 4: 
        output = "INJ/HEMATOPAN , BIODIN"
    elif var1 == 0: 
        output = "Betamox, vetadryl, biodin,  Vit B-Comp" 
    elif var1 == 1: 
        output = "Cefadroxil, ambroxol, dexamethason, vit c" 
    else: 
        output = "Clavamox, pronisi, vi. C, imboost"

    return render_template('index.html', y_pred=output, hewan=hewan, diagnosa=diagnosa)


if __name__ == '__main__':
    app.run(debug=True)

# Flask libraries
from flask import Flask, render_template, request

# Ml Libraries
import numpy as np
import pickle


app = Flask(__name__)

def make_prediction(features):
    # De-serializing the MinMaxScaller object
    with open('scale.pkl', 'rb') as file:
        scale = pickle.load(file)
    
    # De-serializing the XGBoost Classifier object
    with open('model.pkl', 'rb') as file:
        classifer = pickle.load(file)

    arr = np.array(features).reshape(1,-1)

    arr = scale.transform(arr)
    output = classifer.predict(arr)
    return output[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods= ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        data = request.form.to_dict()

        try:
            # Get the inputs from form
            battery_power = int( data['battery_power'] )
            clock_speed = float( data['clock_speed'] )
            fc = int( data['fc'])
            int_memory = int( data['int_memory'])
            m_dep = float( data['m_dep'])
            mobile_wt  = int( data['mobile_wt'])
            n_cores = int( data['n_cores'])
            pc = int( data['pc'])
            ram = int( data['ram'])
            sc_h = int( data['sc_h'])
            sc_w = int( data['sc_w'])
            talk_time = int( data['talk_time'])

            # # Create New Feature
            px_height = int( data['px_height'])
            px_width = int( data['px_width'])
            pixels = px_height*px_width

            # Radio Button Inputs
            blue = int(data['blue'])
            dual_sim = int(data['dual_sim'])
            four_g = int(data['four_g'])
            three_g = int(data['three_g'])
            touch_screen = int(data['touch_screen'])
            wifi = int(data['wifi'])
        except ValueError:
            return render_template('index.html', name = "Please correct the input datatype.")

        ''' Features should be in the following order only.
        ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
        'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'ram', 'sc_h',
        'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi', 'pixels']
        '''
        features = [battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi, pixels]

        # Call make_prediction function and pass the list of features
        output = make_prediction(features)

        category = {0:'Low Cost', 1:'Medium Cost', 2:'High Cost', 3:'Very High Cost'}

        return render_template('index.html', name = category[output])

    return '<h1> You are in submit page Without POST request.</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

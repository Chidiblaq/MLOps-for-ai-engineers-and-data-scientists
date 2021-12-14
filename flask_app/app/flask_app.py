from body_mass_index import bmi_calculator
from flask import Flask, jsonify, request

#instantiate flask object
app = Flask('__name__')
@app.route('/', methods=['GET', 'POST'])
def get_input():
    """
    A function to get request using flask, calculate and return the result
    """
    packet = request.get_json(force=True)
    weight = packet['weight']
    height = packet['height']

    bmi = bmi_calculator(weight, height)

    return jsonify(bmi)


#driver function
if __name__ == '__main__':
    app.run()
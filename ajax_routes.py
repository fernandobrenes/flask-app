# ajax_routes.py
from flask import Blueprint, jsonify
from functions.my_functions import my_function, excellent_function


# Create a Blueprint
ajax_blueprint = Blueprint('ajax_routes', __name__)

@ajax_blueprint.route('/button_click/<button_function>')
def button_click(button_function):
    if button_function == 'click_1':
        message = my_function()
    elif button_function == 'click_2':
        message = excellent_function()
    else:
        message = {"message": "Invalid function"}

    return jsonify(message)        



from flask import Flask, render_template, jsonify
from functions import my_functions
from ajax_routes import ajax_blueprint  # Import the Blueprint


app = Flask(__name__)

# Main route ("/")
@app.route('/')
def index():
    message = my_functions.get_message()
    return render_template('index.html', message=message)

# Route for Menu1
@app.route('/menu1')
def menu1():
    return render_template('menu1.html')

# Route for Menu2
@app.route('/menu2')
def menu2():
    return render_template('menu2.html')

# Register the Blueprint in the main app
app.register_blueprint(ajax_blueprint, url_prefix='/actions')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)

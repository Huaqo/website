# Serve with $ flask --app app run --debug 
# At http://127.0.0.1:5000/

from flask import Flask, Blueprint, render_template

app = Flask(__name__)

# Define a blueprint for the home page
home_bp = Blueprint('home', __name__)
impressum_bp = Blueprint('impressum',__name__)
zwei2_bp = Blueprint('22', __name__)
zwei1_bp = Blueprint('21', __name__)
zwei0_bp = Blueprint('20', __name__)
zwei9_bp = Blueprint('19', __name__)
zwei8_bp = Blueprint('18', __name__)
hass_bp = Blueprint('hass', __name__)
field2020_bp = Blueprint('field2020', __name__)
polarity_bp = Blueprint('polarity', __name__)
drawings_bp = Blueprint('drawings', __name__)
generative_bp = Blueprint('generative', __name__)
data_is_beautiful_bp = Blueprint('data_is_beautiful', __name__)

# Register a route for the home page
@home_bp.route('/')
def show_home():
    return render_template('index.html')
@impressum_bp.route('/impressum')
def show_impressum():
    return render_template('impressum.html')
@zwei2_bp.route('/stories/2022')
def show_22():
    return render_template('stories/22.html')
@zwei1_bp.route('/stories/2021')
def show_21():
    return render_template('stories/21.html')
@zwei0_bp.route('/stories/2020')
def show_20():
    return render_template('stories/20.html')
@zwei9_bp.route('/stories/2019')
def show_19():
    return render_template('stories/19.html')
@zwei8_bp.route('/stories/2018')
def show_18():
    return render_template('stories/18.html')
@hass_bp.route('/music/hass')
def show_hass():
    return render_template('music/hass.html')
@field2020_bp.route('/music/field2020')
def show_field2020():
    return render_template('music/field2020.html')
@polarity_bp.route('/music/polarity')
def show_polarity():
    return render_template('music/polarity.html')
@drawings_bp.route('/art/drawings')
def show_drawings():
    return render_template('art/drawings.html')
@generative_bp.route('/art/generative')
def show_generative():
    return render_template('art/generative.html')
@data_is_beautiful_bp.route('/dev/data_is_beautiful')
def show_data_is_beautiful():
    return render_template('dev/data_is_beautiful.html')

# Register the home blueprint with the app
app.register_blueprint(home_bp)
app.register_blueprint(impressum_bp)
app.register_blueprint(zwei2_bp)
app.register_blueprint(zwei1_bp)
app.register_blueprint(zwei0_bp)
app.register_blueprint(zwei9_bp)
app.register_blueprint(zwei8_bp)
app.register_blueprint(hass_bp)
app.register_blueprint(field2020_bp)
app.register_blueprint(polarity_bp)
app.register_blueprint(drawings_bp)
app.register_blueprint(generative_bp)
app.register_blueprint(data_is_beautiful_bp)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

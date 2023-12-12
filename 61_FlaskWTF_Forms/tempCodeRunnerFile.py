app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

bootstrap = Bootstrap5(app)
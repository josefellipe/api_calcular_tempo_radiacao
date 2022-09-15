from flask import Flask
from Controller.calculos import calculos_blueprint
from Controller.lugares import lugares_blueprint



app = Flask(__name__)

app.register_blueprint(calculos_blueprint)
app.register_blueprint(lugares_blueprint)



if __name__ == '__main__':
    app.run(debug=True)
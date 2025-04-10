from flask import Flask , render_template
from datos import productos

#crear el objeto en flask de la aplicacion
app = Flask(__name__)

#definicion de rutas
@app.route("/")
def index():
    return render_template("index.html", productos=productos)

@app.route("/producto/<string:nombre>")
def producto(nombre):
    producto = [p for p in productos if p["nombre"] == nombre]
    return render_template("producto.html", producto=producto[0])
    
# programa prrncipal
if __name__ == "__main__":
  app.run(host= "0.0.0.0", port=8080, debug=True)

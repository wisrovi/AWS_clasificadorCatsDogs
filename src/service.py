from flask import Flask, app, jsonify, request, redirect, make_response
from leer_modelo import predecir

ALLOWED = { "png", "jpg", "jpeg", "gif" }
def evaluar_extencion_archivo(filename):
    # queso.jpg
    # ["queso", "jpg"]
    tiene_punto = "." in filename # True, False
    if tiene_punto:
        extencion_filename = filename.split(".", 1)[1].lower()
        if extencion_filename in ALLOWED:
            return True
    return False
# print(evaluar_extencion_archivo("queso.jpge"))

nombresparametrosrecibirPost = {
    "imagen": "file1"
}

html = """
<!doctype html>
<form method="POST" enctype="multipart/form-data" >
	<input type="file" name="file1" />
	<input type="submit" name="subir-imagen" value="Enviar imagen" />
</form>"""

nombre_archivo_que_guardamos = "recibido.jpg"

app = Flask(__name__)

@app.route("/index", methods=["POST", "GET"])
def inicio():
    if request.method == "POST":
        if nombresparametrosrecibirPost["imagen"] not in request.files:
            redirect(request.url)
        nombre_imagen_recibida = request.files["file1"]
        if nombre_imagen_recibida.filename == "":
            redirect(request.url)
        if evaluar_extencion_archivo(nombre_imagen_recibida.filename):
            nombre_imagen_recibida.save(nombre_archivo_que_guardamos)

            # momento de predecir
            rta = predecir(nombre_archivo_que_guardamos)

            return "La imagen recibida es " + rta 
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1990, debug=True)


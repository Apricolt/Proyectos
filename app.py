from flask import Flask, render_template, request, redirect, url_for
from farmacia import Farmacia, Cliente

app = Flask(__name__)
farmacia = Farmacia()

@app.route('/')
def index():
    turnos = farmacia.mostrar_turnos()
    entregas = farmacia.mostrar_entregas()
    return render_template('index.html', turns=turnos, deliveries=entregas)

@app.route('/assign_turn', methods=['POST'])
def assign_turn():
    nombre = request.form.get('customer_name')
    cedula = request.form.get('customer_id')
    cliente = Cliente(nombre, cedula)
    farmacia.asignar_turno(cliente)
    return redirect(url_for('index'))

@app.route('/deliver_medications', methods=['POST'])
def deliver_medications():
    numero_turno = int(request.form.get('turn_number'))
    medicamentos = request.form.getlist('medications')  # Obtener todos los medicamentos
    farmacia.entregar_medicamentos(numero_turno, medicamentos)
    return redirect(url_for('index'))

@app.route('/undo_delivery', methods=['POST'])
def undo_delivery():
    farmacia.deshacer_ultima_entrega()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

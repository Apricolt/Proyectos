from collections import deque

class Cliente:
    def __init__(self, nombre, cedula, numero_turno=None):
        self.nombre = nombre
        self.cedula = cedula
        self.numero_turno = numero_turno
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def __str__(self):
        return f'Turno {self.numero_turno} - {self.nombre} - {self.cedula}'

class Medicamento:
    def __init__(self, nombre, numero_turno):
        self.nombre = nombre
        self.numero_turno = numero_turno

    def __str__(self):
        return f'{self.nombre} (Turno {self.numero_turno})'

class Farmacia:
    def __init__(self):
        self.turnos = deque()  # Cola para los turnos
        self.entregas = []  # Lista para las entregas
        self.historial_entregas = []  # Pila para el historial de entregas
        self.numero_turno = 1  # Número de turno inicial

    def asignar_turno(self, cliente):
        cliente.numero_turno = self.numero_turno
        self.turnos.append(cliente)
        print(f'Turno asignado: {cliente}')
        self.numero_turno += 1

    def entregar_medicamentos(self, numero_turno, medicamentos):
        cliente = next((c for c in self.turnos if c.numero_turno == numero_turno), None)
        if cliente:
            for medicamento in medicamentos:
                medicamento_obj = Medicamento(medicamento, numero_turno)
                cliente.agregar_medicamento(medicamento_obj)
                self.entregas.append(medicamento_obj)
                self.historial_entregas.append(medicamento_obj)  # Historial de entregas
            self.turnos.remove(cliente)  # Remover de la cola de turnos
            print(f'Medicamentos entregados a Turno {numero_turno}: {medicamentos}')
        else:
            print(f'Turno {numero_turno} no está en la lista de turnos.')

    def deshacer_ultima_entrega(self):
        if self.historial_entregas:
            ultima_entrega = self.historial_entregas.pop()  # Deshacer última entrega
            self.entregas.remove(ultima_entrega)
            cliente = next((c for c in self.turnos if c.numero_turno == ultima_entrega.numero_turno), None)
            if not cliente:
                cliente = Cliente('', '', ultima_entrega.numero_turno)  # Crear cliente vacío con el número de turno
            self.turnos.append(cliente)  # Volver a agregar el cliente a la cola de turnos
            print(f'Se ha deshecho la última entrega: {ultima_entrega}')
        else:
            print('No hay entregas para deshacer.')

    def mostrar_turnos(self):
        return list(self.turnos)  # Devuelve una lista de los turnos actuales

    def mostrar_entregas(self):
        return list(self.entregas)  # Devuelve una lista de las entregas actuales

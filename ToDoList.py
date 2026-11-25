import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets, uic

class ToDoList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #Carga de nuestra vista
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.agregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnEditar.clicked.connect(self.EditarTarea)
        #Al dar clic en una tarea, su texto pasa a la caja para poder editarlo
        self.lstTareas.itemClicked.connect(self.SeleccionarTarea)
    def lista(self):
        #texto= "tarea"
        #self.lstTareas.addItem(texto)
        #indice=3
        indice=self.lstTareas.currentRow()
        QMessageBox.information(self, "Notificacion", f"La tarea presionada es la numero: {indice}")
        self.lstTareas.addItem("Tarea")
        #self.lstTareas.takeItem(indice)
    def agregarTarea(self):
        texto= self.edtTarea.text()
        self.lstTareas.addItem(texto)
        self.edtTarea.clear()
        self.edtTarea.setFocus()
    def EliminarTarea(self):
        indiceBorrarTarea=self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceBorrarTarea)
    def SeleccionarTarea(self, item):
        self.edtTarea.setText(item.text())
    def EditarTarea(self):
        indiceEditarTarea=self.lstTareas.currentRow()
        texto= self.edtTarea.text()
        #Solo edita si hay una tarea seleccionada y la caja tiene texto
        if indiceEditarTarea >= 0 and texto != "":
            self.lstTareas.item(indiceEditarTarea).setText(texto)
            self.edtTarea.clear()
            self.edtTarea.setFocus()

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ToDoList(QtWidgets.QMainWindow):
      
    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnEditar.clicked.connect(self.EditarTarea)


    def AgregarTarea(self):
        tarea = self.edtTarea.text()
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()

    def EliminarTarea(self):
        indiceTareaBorrar = self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceTareaBorrar)

    def EditarTarea(self):
        indiceTareaEditar = self.lstTareas.currentRow()
        if indiceTareaEditar == -1:
            QMessageBox.warning(self,"Error","Selecciona una tarea para editar")
            return
        nuevoTexto = self.edtTarea.text()
        if nuevoTexto == "":
            QMessageBox.warning(self,"Error","Ingresa un nuevo texto para la taraa")
            return
        self.lstTareas.item(indiceTareaEditar).setText(nuevoTexto)
        self.edtTarea.clear()
        self.edtTarea.setFocus()
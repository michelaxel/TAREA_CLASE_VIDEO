from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ToDoList(QtWidgets.QMainWindow):
      
    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)


    def AgregarTarea(self):
        tarea = self.edtTarea.text()
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()

    def EliminarTarea(self):
        indiceTareaBorrar = self.lstTareas.currentRow()
        self.lstTareas.takeItem(indiceTareaBorrar)
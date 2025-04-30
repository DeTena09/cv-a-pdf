import sys
import os
import shutil
import threading
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTextEdit,
    QFileDialog, QVBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt

from pdf_reader import extraer_texto_pdf
from ai_parser import interpretar_cv
from config import OUTPUT_DIR
from create_docx import crear_cv_desde_json

INPUT_DIR = "input_pdfs"

class CVProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Procesador de CVs")
        self.setFixedSize(500, 400)

        self.pdf_paths = []

        # Widgets
        self.label = QLabel("Selecciona uno o más archivos PDF:")
        self.select_button = QPushButton("Seleccionar PDFs")
        self.select_button.clicked.connect(self.seleccionar_pdfs)

        self.descripcion_label = QLabel("Descripción del proyecto:")
        self.descripcion_input = QTextEdit()
        self.descripcion_input.setFixedHeight(100)

        self.process_button = QPushButton("Procesar")
        self.process_button.clicked.connect(self.procesar_cvs)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: gray")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.descripcion_label)
        layout.addWidget(self.descripcion_input)
        layout.addWidget(self.process_button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def seleccionar_pdfs(self):
        archivos, _ = QFileDialog.getOpenFileNames(self, "Selecciona PDFs", "", "PDF Files (*.pdf)")
        if archivos:
            self.pdf_paths = archivos
            nombres = [os.path.basename(p) for p in archivos]
            mostrar = ", ".join(nombres[:2]) + ("..." if len(nombres) > 2 else "")
            self.label.setText(f"{len(nombres)} archivo(s) seleccionado(s): {mostrar}")

    def procesar_cvs(self):
        if not self.pdf_paths:
            QMessageBox.critical(self, "Error", "Primero selecciona uno o más archivos PDF.")
            return

        descripcion = self.descripcion_input.toPlainText().strip()
        if not descripcion:
            QMessageBox.critical(self, "Error", "Por favor ingresa la descripción del proyecto.")
            return

        self.status_label.setText("Procesando...")
        self.process_button.setEnabled(False)

        hilo = threading.Thread(target=self._procesar_en_thread, args=(descripcion,))
        hilo.start()

    def _procesar_en_thread(self, descripcion):
        errores = []
        os.makedirs(INPUT_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for path_original in self.pdf_paths:
            nombre_pdf = os.path.basename(path_original)
            path_temp = os.path.join(INPUT_DIR, nombre_pdf)

            try:
                shutil.copy(path_original, path_temp)
                texto = extraer_texto_pdf(path_temp)
                datos = interpretar_cv(texto, descripcion)
                nombre_salida = os.path.splitext(nombre_pdf)[0] + "_generado.docx"
                output_path = os.path.join(OUTPUT_DIR, nombre_salida)
                crear_cv_desde_json(datos, output_path)
            except Exception as e:
                errores.append(f"{nombre_pdf}: {str(e)}")
            finally:
                if os.path.exists(path_temp):
                    os.remove(path_temp)

        self.status_label.setText(
            f"✅ Todos los archivos procesados correctamente." if not errores else f"❌ Errores en {len(errores)} archivo(s)"
        )
        self.process_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CVProcessor()
    ventana.show()
    sys.exit(app.exec())

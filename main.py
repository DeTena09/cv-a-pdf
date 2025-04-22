import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import shutil
import threading

# Importación de módulos internos
from pdf_reader import extraer_texto_pdf
from ai_parser import interpretar_cv
from docx_writer import generar_docx
from config import PLANTILLA_PATH, OUTPUT_DIR

# Carpeta donde se guardan temporalmente los PDFs seleccionados
INPUT_DIR = "input_pdfs"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de CVs")

        # Etiqueta inicial
        self.label = tk.Label(root, text="Selecciona uno o más archivos PDF:")
        self.label.pack(pady=10)

        # Botón para seleccionar PDFs
        self.select_button = tk.Button(root, text="Seleccionar PDFs", command=self.seleccionar_pdfs)
        self.select_button.pack(pady=5)

        # Botón para lanzar el procesamiento
        self.process_button = tk.Button(root, text="Procesar", command=self.procesar_cvs)
        self.process_button.pack(pady=10)

        # Área para mostrar mensajes de estado
        self.progress = ttk.Label(root, text="")
        self.progress.pack(pady=5)

        self.pdf_paths = []  # Lista de archivos seleccionados

    def seleccionar_pdfs(self):
        # Abrir el selector de archivos para múltiples PDFs
        self.pdf_paths = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
        if self.pdf_paths:
            nombres = [os.path.basename(p) for p in self.pdf_paths]
            # Muestra los primeros 2 nombres seleccionados (truncados si hay muchos)
            self.label.config(text=f"{len(nombres)} archivo(s) seleccionado(s): " + ", ".join(nombres[:2]) + ("..." if len(nombres) > 2 else ""))

    def procesar_cvs(self):
        # Si no se seleccionaron archivos, muestra error
        if not self.pdf_paths:
            messagebox.showerror("Error", "Primero selecciona uno o más archivos PDF.")
            return

        # Mostrar que se está procesando y deshabilitar el botón
        self.progress.config(text="Procesando...", foreground="blue")
        self.process_button.config(state=tk.DISABLED)

        # Lanzar en hilo separado para no bloquear la interfaz
        threading.Thread(target=self._procesar_en_thread).start()

    def _procesar_en_thread(self):
        errores = []  # Para almacenar errores
        os.makedirs(INPUT_DIR, exist_ok=True)  # Asegura que exista la carpeta temporal

        for path_original in self.pdf_paths:
            nombre_pdf = os.path.basename(path_original)
            path_temp = os.path.join(INPUT_DIR, nombre_pdf)

            try:
                # Copiar a la carpeta temporal
                shutil.copy(path_original, path_temp)

                # Extraer texto, procesar con IA, generar DOCX
                texto = extraer_texto_pdf(path_temp)
                datos = interpretar_cv(texto)

                nombre_salida = os.path.splitext(nombre_pdf)[0] + "_generado.docx"
                output_path = os.path.join(OUTPUT_DIR, nombre_salida)
                generar_docx(PLANTILLA_PATH, datos, output_path)

            except Exception as e:
                # Si falla algo, guardar el error
                errores.append(f"{nombre_pdf}: {str(e)}")
            finally:
                # Eliminar el archivo temporal
                if os.path.exists(path_temp):
                    os.remove(path_temp)

        # Mostrar mensaje final dependiendo del resultado
        if errores:
            self.progress.config(text=f"❌ Errores en: {len(errores)} archivo(s).", foreground="red")
            print("\n".join(errores))
        else:
            self.progress.config(text="✅ Todos los archivos procesados correctamente.", foreground="green")

        # Habilitar el botón de nuevo
        self.process_button.config(state=tk.NORMAL)

# Punto de entrada de la app
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


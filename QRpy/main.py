import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import qrcode

class MyQR:
    def __init__(self, master, size=30, padding=2):
        self.master = master
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name, fg, bg):
        # Solicitar al usuario que ingrese el texto para el codigo QR
        user_input = simpledialog.askstring(title="Entrada",
                                            prompt="Introduce el texto para el codigo QR",
                                            parent=self.master)

        try:
            self.qr.add_data(user_input)
            self.qr.make(fit=True)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            messagebox.showinfo(title="Exito", message=f"Se creo exitosamente:{file_name}")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Ocurrio un error: {e}")


# Configurar la ventana principal Tkinter
root = tk.Tk()
root.geometry("200x200")
app = MyQR(root)
button = tk.Button(root, text='Crear Codigo QR',
                   command=lambda: app.create_qr(file_name='la imagen.png',
                                                 fg='white', bg='black'))
button.pack(pady=20)

root.mainloop()
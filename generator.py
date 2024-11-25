import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import qrcode


class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x200")

        # Элементы интерфейса
        ttk.Label(self.root, text="Write below link or text for QR-Code:").pack(pady=10)
        self.input_entry = ttk.Entry(self.root, width=50)
        self.input_entry.pack(pady=5)

        generate_btn = ttk.Button(self.root, text="Save", command=self.generate_qr)
        generate_btn.pack(pady=10)

    def generate_qr(self):
        # Получение строки из ввода
        input_text = self.input_entry.get()
        if not input_text.strip():
            messagebox.showerror("Error", "Write Text!")
            return

        try:
            # Создаем QR-код
            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(input_text)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")

            # Определяем папку "Загрузки"
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            if not os.path.exists(downloads_path):
                os.makedirs(downloads_path)

            # Сохраняем файл
            qr_file_path = os.path.join(downloads_path, "qr_code.png")
            qr_img.save(qr_file_path)

            # Уведомление об успехе
            messagebox.showinfo("Успех", f"QR-Code saved in: {qr_file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")




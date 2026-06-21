import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def organize_files():
    folder = filedialog.askdirectory()

    if not folder:
        return

    count = 0

    for file in os.listdir(folder):

        if file in ["Images", "Videos", "Documents", "Others"]:
            continue

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            name, ext = os.path.splitext(file)
            ext = ext.lower()

            if ext in [".jpg", ".jpeg", ".png"]:
                destination = os.path.join(folder, "Images")

            elif ext in [".mp4", ".mkv", ".avi"]:
                destination = os.path.join(folder, "Videos")

            elif ext in [".pdf", ".docx", ".txt"]:
                destination = os.path.join(folder, "Documents")

            else:
                destination = os.path.join(folder, "Others")

            os.makedirs(destination, exist_ok=True)
            shutil.move(file_path, os.path.join(destination, file))

            count += 1

    messagebox.showinfo("Success 🎉", f"{count} files organized successfully!")



app = tk.Tk()
app.title("Smart File Organizer 😎")
app.geometry("420x250")
app.config(bg="#f5f5f5")

title = tk.Label(app, text="Smart File Organizer", font=("Arial", 16, "bold"), bg="#f5f5f5")
title.pack(pady=15)

desc = tk.Label(app, text="Click the button below to organize your files automatically", bg="#f5f5f5")
desc.pack(pady=5)

button = tk.Button(app, text="📂 Select Folder & Organize",
                   font=("Arial", 12),
                   bg="#4CAF50", fg="white",
                   padx=10, pady=5,
                   command=organize_files)

button.pack(pady=20)

app.mainloop()
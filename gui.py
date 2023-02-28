import tkinter as tk
from PIL import ImageTk, Image
import subprocess

root = tk.Tk()
root.title('CardX Tools - GUI')


root.configure(bg='black')
root.option_add('*Font', 'TkDefaultFont 12')
root.option_add('*Foreground', 'red')
root.option_add('*Background', 'black')


image_path = 'uwp1057927.jpeg'
image = Image.open(image_path)
image = image.resize((300, 300), Image.ANTIALIAS)  
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image_tk, bg='black')

def run_script():
    subprocess.run(['python', 'main.py'])

button = tk.Button(root, text='Lancer CardX', width=20, bg='black', fg='red', command=run_script)

image_label.pack()
button.pack(pady=10)


root.mainloop()

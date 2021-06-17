import tkinter as tk
from PIL import Image, ImageTk


class LoginPage(tk.Frame):
	def __init__(self, parent, App):
		
		self.app = App
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg="darkorchid")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)


		#CREATE MAIN FRAME

		self.main_frame = tk.Frame(self, width=self.settings.width, height=self.settings.height, bg="darkorchid")
		self.main_frame.pack(expand=True)

		self.label_title = tk.Label(self.main_frame, text="Projek Gudang 10 Komputer 1", font=("Blackadder ITC", 30, "bold"), bg="darkorchid", fg="gold")
		self.label_title.pack(side="top", anchor="nw", pady=20)

		self.btn_login = tk.Button(self.main_frame, text="OPEN", font=("Modern No. 20", 18, "bold"), command=lambda:self.app.change_page('appPage'))
		self.btn_login.pack(pady=5)
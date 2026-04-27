import customtkinter

class ModeSelector(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.calculation_selector = customtkinter.CTkButton(self, text="Calculation")
        self.calculation_selector.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.graphing_selector = customtkinter.CTkButton(self, text="Graphing")
        self.graphing_selector.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Python nSpire CX II")
        self.geometry("1280x720")
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=0)

        self.mode_selector = ModeSelector(self)
        self.mode_selector.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=1, padx=10, pady=10, sticky="esw")

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()
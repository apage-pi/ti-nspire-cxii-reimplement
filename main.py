from customtkinter import *
from PIL import Image
import sympy as sp, numpy as np
from equationplot import plot_function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
class ModeSelector(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        graphing_icon = CTkImage(dark_image=Image.open("assets/graphing.png"), size=(100, 100))
        self.calculation_selector = CTkButton(self, text="Calculation")
        self.calculation_selector.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.graphing_selector = CTkButton(self, image=graphing_icon, text="", compound="top")
        self.graphing_selector.grid(row=1, column=0, padx=10, pady=(10, 0))


class GraphFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.function_input = CTkTextbox(self, wrap="none")
        self.function_input.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="new")
        self.function_input.insert("0.0", "x^2")
        self.button = CTkButton(self, text="Graph", command=lambda: self.plot_graph(self.function_input.get("0.0", "end")))
        self.button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    def plot_graph(self, equation: str = "x=0", x_range=(-10, 10), y_range=None) -> None:
        x = sp.symbols('x')
        expr = sp.sympify(equation)

        # Generate x and y values
        x_vals = np.linspace(x_range[0], x_range[1], 500)
        y_vals = [sp.lambdify(x, expr, 'numpy')(val) for val in x_vals]

        # Plot the function
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f"y = {equation}")

        # Axes and ranges
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        if y_range:
            plt.ylim(y_range)  # Set custom y-range if provided
        plt.grid(alpha=0.3)

        # Annotations
        plt.legend()
        plt.title("Equation Plot")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()


class App(CTk):
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

        self.graph_frame = GraphFrame(self)
        self.graph_frame.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="nsew")


app = App()
app.mainloop()
import tkinter as tk
from tkinter import ttk

#Initialize the UI
#ChatGPT generated this

def init_GUI():
    root = tk.Tk()
    root.title("Spam Filter")
    root.geometry("600x400")
    root.config(bg="#2b2b2b")   # dark mode background


    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TLabel", 
                    background="#2b2b2b", 
                    foreground="white", 
                    font=("Arial", 16))

    style.configure("TEntry", 
                    padding=10,
                    foreground="white",
                    fieldbackground="#555555",
                    bordercolor="#aaaaaa",
                    borderwidth=2)

    # ---------- Title ----------
    title_label = ttk.Label(root, text="Input Message", font=("Arial", 20))
    title_label.pack(pady=(20, 10))


    # ---------- Input Box ----------
    input_var = tk.StringVar()

    def on_text_change(*args):
        text = input_var.get()
        analyze_input(text)

    # Trigger whenever text changes
    input_var.trace_add("write", on_text_change)

    input_box = ttk.Entry(root, textvariable=input_var, width=40, font=("Arial", 16))
    input_box.pack(pady=10)


    # ---------- Result ----------
    result_label = ttk.Label(root, text="Result", font=("Arial", 18))
    result_label.pack(pady=(30, 5))

    result_value = ttk.Label(root, text="*Spam/Ham*", font=("Arial", 16))
    result_value.pack()


    # ---------- Confidence ----------
    confidence_label = ttk.Label(root, text="Confidence", font=("Arial", 18))
    confidence_label.pack(pady=(30, 5))

    confidence_value = ttk.Label(root, text="*percentage of confidence*", font=("Arial", 16))
    confidence_value.pack()

    def analyze_input(text):
        """
        This function is automatically triggered every time 
        the user types in the text box.
        """

        #Test code, this is where the perceptron logic will be
        print("Passed")

        confidence_value.config(text="0.5")
        result_value.config(text="Spam Message Detected")




    root.mainloop()
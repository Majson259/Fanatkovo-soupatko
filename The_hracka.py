import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Krabička centrum")

# nastavení ikony
ikon_image = tk.PhotoImage(file="icona.png")

root.iconphoto(False, ikon_image)

# rámečky kolem textu
frame1 = tk.LabelFrame(root, text="left fader",bg="lightgrey", padx=10, pady=10)
frame2 = tk.LabelFrame(root, text="roller",bg="lightgrey", padx=10, pady=10)
frame3 = tk.LabelFrame(root, text="right fader",bg="lightgrey", padx=10, pady=10)

# toto je prvni sloupec
label1_2 = tk.Label(frame1, text="MIDI chanel",bg="lightgrey", font=("Arial, 12"))
label1_3 = tk.Label(frame1, text="MIDI CC",bg="lightgrey", font=("Arial, 12"))
label1_4 = tk.Label(frame1, text="value",bg="lightgrey", font=("Arial, 12"))
spinbox1_1 = tk.Spinbox(frame1, from_=0, to=100, width=4, font=("Arial, 12"))
spinbox1_2 = tk.Spinbox(frame1, from_=0, to=100, width=4, font=("Arial, 12"))
# toto je druhi sloupec
label2_2 = tk.Label(frame2, text="MIDI chanel",bg="lightgrey", font=("Arial, 12"))
label2_3 = tk.Label(frame2, text="MIDI CC",bg="lightgrey", font=("Arial, 12"))
label2_4 = tk.Label(frame2, text="value",bg="lightgrey", font=("Arial, 12"))
spinbox2_1 = tk.Spinbox(frame2, from_=0, to=100, width=4, font=("Arial, 12"))
spinbox2_2 = tk.Spinbox(frame2, from_=0, to=100, width=4, font=("Arial, 12"))
# toto je treti sloupec
label3_2 = tk.Label(frame3, text="MIDI chanel",bg="lightgrey", font=("Arial, 12"))
label3_3 = tk.Label(frame3, text="MIDI CC",bg="lightgrey", font=("Arial, 12"))
label3_4 = tk.Label(frame3, text="value",bg="lightgrey", font=("Arial, 12"))
spinbox3_1 = tk.Spinbox(frame3, from_=0, to=100, width=4, font=("Arial, 12"))
spinbox3_2 = tk.Spinbox(frame3, from_=0, to=100, width=4, font=("Arial, 12"))



# postavení frames
frame1.grid(row=0, column=0, padx=20, pady=20)
frame2.grid(row=0, column=10, padx=20, pady=20)
frame3.grid(row=0, column=20, padx=20, pady=20)


# postaveni label a spinbox
# 1. sloupec
label1_2.grid(row=11, column=20, sticky="w", padx=30, pady=20)
label1_3.grid(row=12, column=20, sticky="w", padx=30, pady=20)
label1_4.grid(row=13, column=20, sticky="w", padx=30, pady=20)
spinbox1_1.grid(row=11, column=30, padx=30, pady=20)
spinbox1_2.grid(row=12, column=30, padx=30, pady=20)
# 2. sloupec
label2_2.grid(row=11, column=40, sticky="w", padx=30, pady=20)
label2_3.grid(row=12, column=40, sticky="w", padx=30, pady=20)
label2_4.grid(row=13, column=40, sticky="w", padx=30, pady=20)
spinbox2_1.grid(row=11, column=50, padx=30, pady=20)
spinbox2_2.grid(row=12, column=50, padx=30, pady=20)
# 3. sloupec
label3_2.grid(row=11, column=60, sticky="w", padx=30, pady=20)
label3_3.grid(row=12, column=60, sticky="w", padx=30, pady=20)
label3_4.grid(row=13, column=60, sticky="w", padx=30, pady=20)
spinbox3_1.grid(row=11, column=70, padx=30, pady=20)
spinbox3_2.grid(row=12, column=70, padx=30, pady=20)

root.geometry("970x270")

root.mainloop()
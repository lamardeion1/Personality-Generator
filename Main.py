import tkinter as tk
import random

def generate_personality():
  traits = ['openness', 'intellect', 'industriousness', 'orderliness', 'assertiveness', 'enthusiasm', 'politeness', 'compassion', 'volatility', 'withdraw']
  personality = {}
  
  for trait in traits:
    value = random.randint(1, 100)
    personality[trait] = value
  
  return personality

def on_button_click():
  personality = generate_personality()
  label['text'] = str(personality)

root = tk.Tk()
root.title("Personality Generator")

label = tk.Label(root, text="Click the button to generate a personality!")
label.pack()

button = tk.Button(root, text="Generate Personality", command=on_button_click)
button.pack()

root.mainloop()

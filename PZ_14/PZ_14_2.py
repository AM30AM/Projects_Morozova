#'''Дано двухзанчное число. Найдите сумму и произведение его цифр'''

import tkinter as tk
from tkinter import messagebox

def calculate_digits():
    input_text = entry.get()
    
    if not input_text:
        messagebox.showwarning("Ошибка", "Поле ввода не должно быть пустым!")
        return
    
    try:
        number = int(input_text)
        
        if number < 10 or number > 99:
            messagebox.showwarning("Ошибка", "Введите двухзначное число (от 10 до 99)!")
            return
        
        first_n = number // 10
        second_n = number % 10
        summa_number = first_n + second_n
        proisv = first_n * second_n
        
        result_sum.config(text=f"Сумма цифр числа: {summa_number}")
        result_prod.config(text=f"Произведение цифр числа: {proisv}")
        
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число!")


root = tk.Tk()
root.title('PZ_14_2')
root.geometry('820x520')
BG = "#5198df"
FRAME_BG = "#5198df"
root.configure(bg=BG)

frame = tk.Frame(root, bg=BG)
frame.place(relx=0.5, rely=0.48, anchor="c", width=800, height=420)

tk.Label(frame, text='Введите двухзначное число и программа найдет сумму и произведение его цифр:', 
         bg=BG, fg="white", font=("Arial", 12, "bold")).pack(pady=10)
entry = tk.Entry(frame, bg='white', width=40, fg='darkblue', justify='center', font=('Arial', 14))
entry.pack(pady=5)

calc_button = tk.Button(frame, text='рассчитать', command=calculate_digits, bg='lightblue', font=('Arial', 12))
calc_button.pack(pady=15)

result_sum = tk.Label(frame, text='Сумма цифр числа: ', bg=BG, fg='white', font=('Arial', 11, 'bold'))
result_sum.pack(pady=5)

result_prod = tk.Label(frame, text='Произведение цифр числа: ', bg=BG, fg='white', font=('Arial', 11, 'bold'))
result_prod.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import ttk
import openai_helper
import openai
import logging

def main_window():
    window = tk.Tk()
    window.title("OpenAI GPT-3 GUI")
    window.geometry("1200x1000")
    window.configure(bg='#A6D3A0')

    key_label = tk.Label(window, text="Enter your OpenAI API Key", font=("TkDefaultFont", 12, 'bold', 'underline'), bg='#A6D3A0')
    key_label.pack(pady=10)

    key_input = tk.Text(window, height=1, width=45, font=("TkDefaultFont", 12), bd=2, relief="sunken")
    key_input.pack(pady=10)
    key_input.configure(bg='#D1FFD7')

    model_label = tk.Label(window, text="Select an AI model", font=("TkDefaultFont", 12, 'bold', 'underline'), bg='#A6D3A0')
    model_label.pack(pady=10)

    models = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]
    model_var = tk.StringVar()
    model_var.set(models[0])
    model_select = tk.OptionMenu(window, model_var, *models)
    model_select.pack(pady=10)
    model_select.config(font=('calibri',(14)), bg='#D1FFD7')

    label = tk.Label(window, text="Enter your query", font=("TkDefaultFont", 12, 'bold', 'underline'), bg='#A6D3A0')
    label.pack(pady=10)
    
    user_input = tk.Text(window, height=10, width=80, font=("TkDefaultFont", 12), bd=2, relief="sunken")
    user_input.pack(pady=10)
    user_input.configure(bg='#D1FFD7')
    


    submit = tk.Button(window, text="Submit",font=("TkDefaultFont", 12, 'bold'), width=20, command=lambda: get_response(user_input.get("1.0", "end"), model_var.get(), key_input.get("1.0", "end")))
    submit.pack(pady=10)
    submit.configure(background='#D1FFD7', foreground='#000')
    
    result_label = tk.Label(window, text="Response", font=("TkDefaultFont", 12, 'bold', 'underline'), bg='#A6D3A0')
    result_label.pack(pady=10)
    
    result = tk.Text(window, height=20, width=80, font=("TkDefaultFont", 12), bd=2, relief="sunken", wrap=tk.WORD)
    result.pack(pady=10)
    result.configure(bg='#D1FFD7')
    
    def get_response(input, model, key):
        result.delete("1.0", "end")
        if len(input.strip()) == 0:
            result.insert("1.0", "Error: Input field cannot be empty.")
            return

        try:
            response = openai_helper.get_gpt_response(input, model, key)
            result.insert("1.0", response.strip('?').strip())
        except openai.error.AuthenticationError as auth_err:
            result.insert("1.0", "Error: Authentication Error - Invalid or Missing API Key\n\nYou can obtain an OpenAI API key from https://platform.openai.com/account/api-keys")
        except openai.error.RateLimitError as rate_err:
            result.insert("1.0", "Error: Rate Limit Error - Too many requests. Please wait a few moments.")

    
    window.mainloop()

if __name__ == "__main__":
    main_window()
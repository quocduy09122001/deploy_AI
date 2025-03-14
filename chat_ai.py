import requests
import json
import tkinter as tk
from tkinter import scrolledtext

# URL của Ollama API (chạy local)
OLLAMA_API_URL = "https://f6e0-14-224-167-99.ngrok-free.app/api/generate"
MODEL_NAME = "deepseek-r1:1.5b"

def chat_with_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Lỗi: {response.status_code} - {response.text}"

# Giao diện GUI với Tkinter
def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if user_input:
        chat_history.insert(tk.END, f"Bạn: {user_input}\n", "user")
        response = chat_with_ollama(user_input)
        chat_history.insert(tk.END, f"AI: {response}\n\n", "ai")
        input_box.delete("1.0", tk.END)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Chat với Ollama AI")

# Khung hiển thị chat
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_history.pack(padx=10, pady=10)
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("ai", foreground="green")

# Khung nhập tin nhắn
input_box = tk.Text(root, height=3, font=("Arial", 12))
input_box.pack(padx=10, pady=5)

# Nút gửi tin nhắn
send_button = tk.Button(root, text="Gửi", command=send_message)
send_button.pack(pady=5)

# Chạy giao diện
root.mainloop()

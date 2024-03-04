import tkinter as tk
from threading import Thread
import socket

class WalkieTalkieGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Walkie-Talkie")

        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=0, column=0, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=0, column=1, padx=10, pady=10)

        self.text_area = tk.Text(root, height=10, width=60, state=tk.DISABLED)
        self.text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 12345))
        self.server_socket.listen()

        self.client_socket, self.client_address = self.server_socket.accept()
        self.receive_thread = Thread(target=self.receive_messages)
        self.receive_thread.start()

    def send_message(self):
        message = self.message_entry.get()
        self.client_socket.send(message.encode())
        self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            data = self.client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            self.text_area.configure(state=tk.NORMAL)
            self.text_area.insert(tk.END, f"Received: {message}\n")
            self.text_area.configure(state=tk.DISABLED)
            self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    walkie_talkie_gui = WalkieTalkieGUI(root)
    root.mainloop()

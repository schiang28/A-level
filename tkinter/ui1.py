import tkinter as tk

window = tk.Tk()
window.title("Bob's stuff")


def onClick():
    user = username.get()
    if user == "Bob" and password.get() == "plain":
        m = "Welcome"
    else:
        m = "failure"
    message.config(text=m)


label = tk.Label(
    text="input username and password", fg="black", bg="white", width=50, height=10
)

username = tk.Entry(fg="black", bg="white", width=10)
password = tk.Entry(fg="black", bg="white", width=10, show="*")

button = tk.Button(
    text="Enter", width=5, height=3, bg="white", fg="black", command=onClick
)

message = tk.Label(text="", fg="black", bg="white", width=20, height=3)

label.grid()
username.grid()
password.grid()
button.grid()
message.grid()
window.mainloop()


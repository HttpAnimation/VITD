import tkinter as tk
from tkinter import ttk
import webbrowser

class AppStoreApp:
    def __init__(self, master):
        self.master = master
        self.master.title("VTID App Store")
        self.master.geometry("800x600")
        self.master.configure(bg="#1e1e1e")

        self.apps = []
        self.load_apps()

        self.create_app_list()

    def load_apps(self):
        with open("repos.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6):
                app_data = {
                    "name": lines[i].strip(),
                    "icon": lines[i+1].strip(),
                    "install_command": lines[i+2].strip(),
                    "description": lines[i+3].strip(),
                    "homepage": lines[i+4].strip(),
                }
                self.apps.append(app_data)

    def create_app_list(self):
        app_frame = ttk.Frame(self.master, padding=(10, 10), style="Dark.TFrame")
        app_frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        for i, app in enumerate(self.apps):
            app_button = ttk.Button(
                app_frame,
                text=app["name"],
                image=tk.PhotoImage(file=app["icon"]),
                compound=tk.TOP,
                style="App.TButton",
                command=lambda a=app: self.show_app_details(a)
            )
            app_button.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    def show_app_details(self, app):
        details_window = tk.Toplevel(self.master)
        details_window.title(app["name"])
        details_window.geometry("400x300")
        details_window.configure(bg="#1e1e1e")

        name_label = ttk.Label(details_window, text=app["name"], font=("Helvetica", 16), foreground="white", background="#1e1e1e")
        name_label.pack(pady=10)

        icon_label = ttk.Label(details_window, image=tk.PhotoImage(file=app["icon"]), background="#1e1e1e")
        icon_label.pack()

        install_button = ttk.Button(details_window, text="Install", style="Install.TButton", command=lambda: self.install_app(app))
        install_button.pack(pady=10)

        description_label = ttk.Label(details_window, text=app["description"], wraplength=350, justify=tk.LEFT, foreground="white", background="#1e1e1e")
        description_label.pack(pady=10)

        homepage_button = ttk.Button(details_window, text="App Homepage", command=lambda: webbrowser.open(app["homepage"]), style="Link.TButton")
        homepage_button.pack(pady=10)

    def install_app(self, app):
        # You can implement the installation logic here
        print(f"Installing {app['name']} using command: {app['install_command']}")


def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("Dark.TFrame", background="#1e1e1e")
    style.configure("App.TButton", background="#2e2e2e", foreground="white", padding=(10, 10))
    style.configure("Install.TButton", background="#4CAF50", foreground="white", padding=(10, 10))
    style.configure("Link.TButton", foreground="#1e90ff")

    app = AppStoreApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

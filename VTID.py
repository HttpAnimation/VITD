import requests
import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import ImageTk, Image
import webbrowser

# Function to open URL in default browser
def open_url(url):
    webbrowser.open(url)

# Function to install app using flatpak
def install_app(command):
    messagebox.showinfo("Installation", f"Installing {command}...")

# Function to display app details when clicked
def show_details(repo_name, app_name, app_icon, description, homepage):
    top = tk.Toplevel()
    top.title(app_name)
    top.geometry("400x400")

    icon_img = Image.open(requests.get(app_icon, stream=True).raw)
    icon_img = icon_img.resize((128, 128), Image.ANTIALIAS)
    icon_photo = ImageTk.PhotoImage(icon_img)

    label_icon = tk.Label(top, image=icon_photo)
    label_icon.pack()

    label_name = tk.Label(top, text=app_name, font=("Helvetica", 16))
    label_name.pack()

    button_install = tk.Button(top, text="Install", command=lambda: install_app(description.split()[-1]))
    button_install.pack()

    button_homepage = tk.Button(top, text="Homepage", command=lambda: open_url(homepage))
    button_homepage.pack()

    label_description = tk.Label(top, text=description, wraplength=350)
    label_description.pack()

    top.mainloop()

# Read the repos.txt file
def read_repos_file(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if not url.startswith("https://"):
            continue

        # Read repo.txt from the URL
        response = requests.get(f"{url}/repo.txt")
        if response.status_code != 200:
            continue
        
        # Parse the repo.txt content
        repo_lines = response.text.strip().split('\n')
        repo_name = repo_lines[0]
        app_name = repo_lines[1]
        app_icon = repo_lines[2]
        install_command = repo_lines[3]
        description = repo_lines[4]
        homepage = repo_lines[5]

        # Create a Tkinter window to display app information
        window = tk.Tk()
        window.title("VTID - Linux App Store")
        window.geometry("400x400")

        app_icon_img = Image.open(requests.get(app_icon, stream=True).raw)
        app_icon_img = app_icon_img.resize((64, 64), Image.ANTIALIAS)
        app_icon_photo = ImageTk.PhotoImage(app_icon_img)

        label_app_icon = tk.Label(window, image=app_icon_photo)
        label_app_icon.pack()

        label_app_name = tk.Label(window, text=app_name, font=("Helvetica", 20))
        label_app_name.pack()

        button_app = tk.Button(window, text="View Details", command=lambda r=repo_name, n=app_name, i=app_icon, d=description, h=homepage: show_details(r, n, i, d, h))
        button_app.pack()

        window.mainloop()

# Main function
def main():
    read_repos_file("repos.txt")

if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# -------- Password Generator Function Button ------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    password_input.insert(0, generated_password)

# ------- Save Password Button Function -------- #


def save():

    website_data = website_input.get()
    email_data = user_email_input.get()
    pw_data = password_input.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": pw_data
        }
    }

    if len(website_data) == 0 or pw_data == 0:
        messagebox.showinfo(title="OOPS", message="ERROR: Please do not leave a blank field")
    else:
        try:
            with open("data.json", "r") as data_file:
                j_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            j_data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(j_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
# -------- Search Button Function FINDS PASSWORD ------- #


def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no details for {website}")

# --------- UI Structure --------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
FONT = ("Arial", 12)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(120, 120, image=logo_img)
canvas.grid(column=1, row=0)


# --- Website Label & Input
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

# --- Username & Email Label & Input
user_email_label = Label(text="Username/Email:", font=FONT)
user_email_label.grid(column=0, row=2)

user_email_input = Entry(width=35)
user_email_input.grid(column=1, row=2, columnspan=2)
user_email_input.insert(0, "example@email.com")

# --- Password Label & Input --- Password Add/Generate Buttons
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# ---Buttons
password_generate = Button(text="Generate", command=generate_password)
password_generate.grid(column=2, row=3)

password_add = Button(text="Add", width=37, command=save)
password_add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=5, command=find_password)
search.grid(column=2, row=1)

window.mainloop()

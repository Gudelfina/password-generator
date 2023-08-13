from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    p_letters = [choice(letters) for c in range(randint(8, 10))]

    p_symbols = [choice(symbols) for s in range(randint(2, 4))]

    p_numbers = [choice(numbers) for num in range(randint(2, 4))]

    final_result = p_letters + p_symbols + p_numbers

    shuffle(final_result)

    password = "".join(final_result)

    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = user_info_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Try again", message="Please fill out every field!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Here are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\n Would you like to save these?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} || {email} || {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)


# website label and entry
website_label = Label(text="Website: ")
website_label.grid(column=1, row=2)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=2, row=2, columnspan=2)


# user info label and entry
user_info_label = Label(text="Email/Username: ")
user_info_label.grid(column=1, row=3)

user_info_input = Entry(width=35)
user_info_input.insert(0, "mendezlupe115@gmail.com")
user_info_input.grid(column=2, row=3, columnspan=2)


# password label and entry
password_label = Label(text="Password: ")
password_label.grid(column=1, row=4)

password_input = Entry(width=18)
password_input.grid(column=2, row=4)


# Buttons
generate_pass_btn = Button(text="Generate Password", command=generate_password)
generate_pass_btn.grid(column=3, row=4)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=2, row=5, columnspan=2)


window.mainloop()
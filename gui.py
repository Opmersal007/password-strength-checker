
import tkinter as tk

root = tk.Tk()

root.title("Password Strength Checker")
root.geometry("450x750")
root.configure(bg="#0b1120")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 20, "bold"),
    bg="#0b1120",
    fg="white"
)

title.pack(pady=30)

subtitle = tk.Label(
    root,
    text="Check your password strength",
    font=("Arial", 12),
    bg="#0b1120",
    fg="#94a3b8"
)

subtitle.pack()


# Password input label
password_label = tk.Label(
    root,
    text="Enter your password",
    font=("Arial", 12),
    bg="#0b1120",
    fg="white"
)

password_label.pack(pady=(35, 10))

# Password input box
password_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    show="*",
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    relief="flat"
)

password_entry.pack(ipady=10)

# Check Password button
check_button = tk.Button(
    root,
    text="Check Password",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    width=25,
    relief="flat",
    cursor="hand2"
)

check_button.pack(pady=25, ipady=8)


# Function to check password strength
def check_password():
    password = password_entry.get()
    score = 0
    strength_bar.delete("all")

    if not password:
        result_label.config(
            text="Please enter a password",
            fg="#f87171"
        )
        return

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1



    if any(char in "!@#$%^&*()-_+=?" for char in password):
        score += 1

    if score <= 2:
        strength = "Weak"
        color = "#ef4444"

    elif score <= 4:
        strength = "Medium"
        color = "#eab308"

    else:
        strength = "Strong"
        color = "#22c55e"

    result_label.config(
    text=f" Password - /5",
    fg=color
    )
    strength_bar.create_rectangle(
        0, 0, score * 60, 12,
        fill=color,
        outline=""
    )


# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#0b1120"
)

result_label.pack(pady=10)

# Connect button to function
check_button.config(command=check_password)


# Strength bar
strength_bar = tk.Canvas(
    root,
    width=300,
    height=12,
    bg="#1e293b",
    highlightthickness=0
)

strength_bar.pack(pady=15)


# Strength bar
strength_bar = tk.Canvas(
    root,
    width=300,
    height=12,
    bg="#1e293b",
    highlightthickness=0
)

strength_bar.pack(pady=15)


# Show and hide password function
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show Password")


# Show and hide button
show_button = tk.Button(
    root,
    text="Show Password",
    command=toggle_password,
    font=("Arial", 10, "bold"),
    bg="#1e293b",
    fg="white",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

show_button.pack(pady=10)


# Password improvement suggestions
def show_suggestions():
    password = password_entry.get()
    suggestions = []

    if not password:
        suggestion_label.config(text="")
        return

    if len(password) < 8:
        suggestions.append("Use at least 8 characters")

    if not any(char.isupper() for char in password):
        suggestions.append("Add an uppercase letter")

    if not any(char.islower() for char in password):
        suggestions.append("Add a lowercase letter")

    if not any(char.isdigit() for char in password):
        suggestions.append("Add a number")

    if not any(char in "!@#$%^&*()-_+=?" for char in password):
        suggestions.append("Add a special character")

    if suggestions:
        suggestion_label.config(
            text="\n".join(suggestions),
            fg="#fbbf24"
        )
    else:
        suggestion_label.config(
            text="All five rules satisfied!",
            fg="#22c55e"
        )


# Suggestions label
suggestion_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#0b1120",
    fg="white",
    justify="left"
)

suggestion_label.pack(pady=10)


# Connect both functions
def check_all():
    check_password()
    show_suggestions()


check_button.config(command=check_all)


# Clear password function
def clear_password():
    password_entry.delete(0, tk.END)
    result_label.config(text="")
    suggestion_label.config(text="")
    strength_bar.delete("all")
    password_entry.config(show="*")
    show_button.config(text="Show Password")
    password_entry.focus()


# Clear password button
clear_button = tk.Button(
    root,
    text="Clear Password",
    command=clear_password,
    font=("Arial", 11, "bold"),
    bg="#dc2626",
    fg="white",
    relief="flat",
    cursor="hand2",
    width=20
)

clear_button.pack(pady=10, ipady=5)

# Footer
footer = tk.Label(
    root,
    text="Developed by Sunil V.",
    font=("Arial", 10),
    bg="#0b1120",
    fg="#94a3b8"
)

footer.pack(side="bottom", pady=15)

root.mainloop()










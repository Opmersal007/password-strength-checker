
import tkinter as tk

# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x620")
root.configure(bg="#0b1120")
root.resizable(False, False)


# Check password strength
def check_password():
    password = password_entry.get()
    score = 0
    suggestions = []

    strength_bar.delete("all")

    if not password:
        result_label.config(
            text="Please enter a password",
            fg="#f87171"
        )
        suggestion_label.config(text="")
        return

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number")

    if any(char in "!@#$%^&*()-_+=?" for char in password):
        score += 1
    else:
        suggestions.append("Add a special character")

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
        text=f"{strength} Password - {score}/5",
        fg=color
    )

    strength_bar.create_rectangle(
        0, 0, score * 60, 12,
        fill=color,
        outline=""
    )

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


# Show and hide password
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show Password")


# Clear password
def clear_password():
    password_entry.delete(0, tk.END)
    result_label.config(text="")
    suggestion_label.config(text="")
    strength_bar.delete("all")
    password_entry.config(show="*")
    show_button.config(text="Show Password")
    password_entry.focus()


# Heading
title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 18, "bold"),
    bg="#0b1120",
    fg="white"
)
title.pack(pady=(20, 10))


# Subtitle
subtitle = tk.Label(
    root,
    text="Check your password strength",
    font=("Arial", 11),
    bg="#0b1120",
    fg="#94a3b8"
)
subtitle.pack()


# Password label
password_label = tk.Label(
    root,
    text="Enter your password",
    font=("Arial", 12),
    bg="#0b1120",
    fg="white"
)
password_label.pack(pady=(20, 10))


# Password input
password_entry = tk.Entry(
    root,
    font=("Arial", 15),
    width=25,
    show="*",
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    relief="flat"
)
password_entry.pack(ipady=8)


# Show and Hide button
show_button = tk.Button(
    root,
    text="Show Password",
    command=toggle_password,
    font=("Arial", 10, "bold"),
    bg="#1e293b",
    fg="white",
    relief="flat",
    cursor="hand2"
)
show_button.pack(pady=8)


# Check Password button
check_button = tk.Button(
    root,
    text="Check Password",
    command=check_password,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    width=25,
    relief="flat",
    cursor="hand2"
)
check_button.pack(pady=10, ipady=7)


# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 15, "bold"),
    bg="#0b1120"
)
result_label.pack(pady=8)


# Strength bar
strength_bar = tk.Canvas(
    root,
    width=300,
    height=12,
    bg="#1e293b",
    highlightthickness=0
)
strength_bar.pack(pady=8)


# Suggestions label
suggestion_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#0b1120",
    fg="white",
    justify="left"
)
suggestion_label.pack(pady=8)


# Clear Password button
clear_button = tk.Button(
    root,
    text="Clear Password",
    command=clear_password,
    font=("Arial", 11, "bold"),
    bg="#dc2626",
    fg="white",
    width=20,
    relief="flat",
    cursor="hand2"
)
clear_button.pack(pady=8, ipady=5)


# Footer
footer = tk.Label(
    root,
    text="Developed by Sunil V.",
    font=("Arial", 10),
    bg="#0b1120",
    fg="#94a3b8"
)
footer.pack(side="bottom", pady=10)

root.mainloop()

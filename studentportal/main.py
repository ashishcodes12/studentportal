


from tkinter import *

root = Tk()
root.geometry("500x450")
root.title("Student Application Portal")


# Submit function
def submit():
    name = name_entry.get().strip()
    student_class = class_entry.get().strip()
    age = age_entry.get().strip()

    # Check empty fields
    if not name or not student_class or not age:
        result_label.config(
            text="Please fill in all fields!",
            fg="red"
        )
        return

    # Display details in terminal
    print("Student Details")
    print("Name:", name)
    print("Class:", student_class)
    print("Age:", age)
    print("-" * 25)

    # Save details in file
    try:
        with open("demofile.txt", "a", encoding="utf-8") as f:
            f.write("Student Details\n")
            f.write(f"Name: {name}\n")
            f.write(f"Class: {student_class}\n")
            f.write(f"Age: {age}\n")
            f.write("-" * 25 + "\n")

        # Success message
        result_label.config(
            text="Student details saved successfully!",
            fg="green"
        )

        # Clear input fields
        name_entry.delete(0, END)
        class_entry.delete(0, END)
        age_entry.delete(0, END)

    except OSError as error:
        result_label.config(
            text=f"File error: {error}",
            fg="red"
        )


# Heading function
def label():
    Label(
        root,
        text="Welcome to Portal!",
        font=("Arial", 24, "bold")
    ).pack(pady=(20, 25))


# Entry function
def entry():
    global name_entry, class_entry, age_entry

    # Name
    frame1 = Frame(root)
    frame1.pack(anchor="w", padx=50, pady=8)

    Label(
        frame1,
        text="Name",
        font=("Arial", 15)
    ).pack(side="left")

    name_entry = Entry(
        frame1,
        font=("Arial", 15),
        width=18
    )
    name_entry.pack(side="left", padx=20)

    # Class
    frame2 = Frame(root)
    frame2.pack(anchor="w", padx=50, pady=8)

    Label(
        frame2,
        text="Class",
        font=("Arial", 15)
    ).pack(side="left")

    class_entry = Entry(
        frame2,
        font=("Arial", 15),
        width=18
    )
    class_entry.pack(side="left", padx=20)

    # Age
    frame3 = Frame(root)
    frame3.pack(anchor="w", padx=50, pady=8)

    Label(
        frame3,
        text="Age",
        font=("Arial", 15)
    ).pack(side="left")

    age_entry = Entry(
        frame3,
        font=("Arial", 15),
        width=18
    )
    age_entry.pack(side="left", padx=20)


# Button function
def button():
    Button(
        root,
        text="Submit",
        font=("Arial", 14, "bold"),
        command=submit
    ).pack(pady=15)


# Result message
result_label = Label(
    root,
    text="",
    font=("Arial", 11)
)
result_label.pack()


# Call functions
label()
entry()
button()

# Run application
root.mainloop()

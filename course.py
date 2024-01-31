import tkinter as tk
from tkinter import ttk,messagebox, Toplevel

#Array :

# 1. List Kelas
kelas = [
    ["Data Science", "Jane Smith", 3],
    ["Web Development", "Alex Johnson", 5],
    ["Machine Learning", "Emily Brown", 2],
    ["Android Development", "Michael Wilson", 3],
    ["IOS Development", "Sarah Thompson", 4],
    ["UI/UX Design", "David Miller", 3],
    ["Backend Development", "Jessica Davis", 5],
    ["React Native", "John Doe", 4],
]

# 2. List User
user = []    
# 3. List User Kelas
user_kelas = []




root = tk.Tk()
root.title("Bootcamp Online")
root.geometry("1280x720")  
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)
kelas_page = ttk.Frame(notebook)
user_page = ttk.Frame(notebook)
user_kelas_page = ttk.Frame(notebook)

# Sorting
def bubble_sort(lst, compare):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if compare(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def compare_kelas_ascending(a, b):
    return a[0] > b[0]

def compare_kelas_descending(a, b):
    return a[0] < b[0]

def compare_user_ascending(a, b):
    return a[0] > b[0]

def compare_user_descending(a, b):
    return a[0] < b[0]

def sort_and_refresh(lst, compare, refresh):
    bubble_sort(lst, compare)
    refresh()


# Searching
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid][0] == target:
            return mid
        elif lst[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def search_kelas(query):
    bubble_sort(kelas, compare_kelas_ascending)
    result = binary_search(kelas, query)
    if result:
        show_kelas_detail(kelas[result])
    else:
        messagebox.showinfo("Not Found", "Kelas tidak ditemukan")


def search_user(query):
    bubble_sort(user, compare_user_ascending)
    result = binary_search(user, query)
    if result:
        show_user_detail(user[result])
    else:
        messagebox.showinfo("Not Found", "User tidak ditemukan")



# Refresh
def refresh_kelas():
    for widget in kelas_page.winfo_children():
        widget.destroy()

    label = tk.Label(kelas_page, text="Daftar Kelas", font=("Arial", 18))
    label.pack(pady=10)

    search_frame = tk.Frame(kelas_page)
    search_frame.pack(pady=5)

    search_label = tk.Label(search_frame, text="Search:", font=("Arial", 14))
    search_label.pack(side="left")

    search_entry = tk.Entry(search_frame, font=("Arial", 14))
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="Search", font=("Arial", 14), relief="groove", padx=5, pady=2, width=10, borderwidth=2, bd=1, bg="gray", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: search_kelas(search_entry.get()))
    search_button.pack(side="left", padx=5)

    for i in range(len(kelas)):
        kelas_frame = tk.Frame(kelas_page)
        kelas_frame.pack()

        kelas_button = tk.Button(kelas_frame, text="{}. {}".format(i+1, kelas[i][0]), anchor="w", font=("Arial", 14), relief="groove", padx=10, pady=5, width=20, borderwidth=4, bd=1, bg="white", fg="black", highlightthickness=0,  highlightcolor="white", command=lambda kelas_detail=kelas[i]: show_kelas_detail(kelas_detail))
        kelas_button.pack(side="left", pady=5)

        join_button = tk.Button(kelas_frame, text="Join Class", font=("Arial", 16), relief="groove", padx=5, pady=2, width=10, borderwidth=2, bd=1, bg="blue", fg="white", highlightthickness=0,  highlightcolor="white", command=show_join_class_form)
        join_button.pack(side="left", pady=5)

    sort_asc_button = tk.Button(kelas_page, text="Sort Ascending", font=("Arial", 18), relief="groove", padx=5, pady=2, width=15, borderwidth=2, bd=1, bg="green", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: sort_and_refresh(kelas, compare_kelas_ascending, refresh_kelas))
    sort_asc_button.pack(pady=5)

    sort_desc_button = tk.Button(kelas_page, text="Sort Descending", font=("Arial", 18), relief="groove", padx=5, pady=2, width=15, borderwidth=2, bd=1, bg="red", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: sort_and_refresh(kelas, compare_kelas_descending, refresh_kelas))
    sort_desc_button.pack(pady=5)


def refresh_user():
    for widget in user_page.winfo_children():
        widget.destroy()
    label = tk.Label(user_page, text="Daftar User", font=("Arial", 24))  
    label.pack(pady=10)

    search_frame = tk.Frame(user_page)
    search_frame.pack(pady=5)

    search_label = tk.Label(search_frame, text="Search:", font=("Arial", 14))
    search_label.pack(side="left")

    search_entry = tk.Entry(search_frame, font=("Arial", 14))
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="Search", font=("Arial", 14), relief="groove", padx=5, pady=2, width=10, borderwidth=2, bd=1, bg="gray", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: search_user(search_entry.get()))

    search_button.pack(side="left", padx=5)
    user_table = ttk.Treeview(user_page)
    user_table["columns"] = ("Nama", "Email", "Nomor")
    user_table.column("#0", width=50)
    user_table.column("Nama", width=150)
    user_table.column("Email", width=200)
    user_table.column("Nomor", width=150)
    user_table.heading("#0", text="No.")
    user_table.heading("Nama", text="Nama")
    user_table.heading("Email", text="Email")
    user_table.heading("Nomor", text="Nomor")
    for i, user_detail in enumerate(user):
        user_table.insert(parent="", index="end", iid=i, text=i+1, values=(user_detail[0], user_detail[1], user_detail[2]))
    user_table.pack(pady=10)

    sort_asc_button = tk.Button(user_page, text="Sort Ascending", font=("Arial", 18), relief="groove", padx=5, pady=2, width=15, borderwidth=2, bd=1, bg="green", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: sort_and_refresh(user, compare_user_ascending, refresh_user))
    sort_asc_button.pack(pady=5)

    sort_desc_button = tk.Button(user_page, text="Sort Descending", font=("Arial", 18), relief="groove", padx=5, pady=2, width=15, borderwidth=2, bd=1, bg="red", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: sort_and_refresh(user, compare_user_descending, refresh_user))
    sort_desc_button.pack(pady=5)

def refresh_user_kelas():
    for widget in user_kelas_page.winfo_children():
        widget.destroy()

    label = tk.Label(user_kelas_page, text="Daftar Kelas", font=("Arial", 18))
    label.pack(pady=10)

    for i in range(len(kelas)):
        kelas_frame = tk.Frame(user_kelas_page)
        kelas_frame.pack()

        kelas_button = tk.Button(kelas_frame, text="{}. {}".format(i+1, kelas[i][0]), anchor="w", font=("Arial", 14), relief="groove", padx=10, pady=5, width=20, borderwidth=4, bd=1, bg="white", fg="black", highlightthickness=0,  highlightcolor="white", command=lambda kelas_detail=kelas[i]: show_kelas_detail(kelas_detail))
        kelas_button.pack(side="left", pady=5)

        join_button = tk.Button(kelas_frame, text="Show Users", font=("Arial", 16), relief="groove", padx=5, pady=2, width=10, borderwidth=2, bd=1, bg="yellow", fg="black", highlightthickness=0,  highlightcolor="white", command=show_join_class_form)
        join_button.pack(side="left", pady=5)

    sort_asc_button = tk.Button(user_kelas_page, text="Sort Ascending", font=("Arial", 18), relief="groove", padx=5, pady=2, width=15, borderwidth=2, bd=1, bg="green", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: sort_and_refresh(kelas, compare_kelas_ascending, refresh_kelas))
    sort_asc_button.pack(pady=5)

    sort_desc_button = tk.Button(user_kelas_page, text="Sort Descending", font=("Arial", 18), relief="groove", padx=5, pady=2, width=15, borderwidth=2, bd=1, bg="red", fg="white", highlightthickness=0,  highlightcolor="white", command=lambda: sort_and_refresh(kelas, compare_kelas_descending, refresh_kelas))
    sort_desc_button.pack(pady=5)        

#Form
def show_join_class_form():
        form_window = Toplevel(kelas_page)
        form_window.title("Join Class Form")

        # Create form labels
        name_label = tk.Label(form_window, text="Nama Anda:")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        name_entry = tk.Entry(form_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        email_label = tk.Label(form_window, text="Email Anda:")
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        email_entry = tk.Entry(form_window)
        email_entry.grid(row=2, column=1, padx=10, pady=5)

        phone_label = tk.Label(form_window, text="Nomor Telephone:")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        phone_entry = tk.Entry(form_window)
        phone_entry.grid(row=3, column=1, padx=10, pady=5)

        # Create submit button
        submit_button = tk.Button(form_window, text="Submit", command=lambda: submit_form(name_entry.get(), email_entry.get(),phone_entry.get()))
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

def submit_form(name, email, phone):
    user.append([name, email, phone])
    messagebox.showinfo("Berhasil", "Selamat anda telah berhasil mendafar ke kelas ini!")
    sort_and_refresh(user, compare_user_ascending, refresh_user)


# Detail
def show_kelas_detail(kelas_detail):
    messagebox.showinfo("Kelas Detail", f"Nama Kelas: {kelas_detail[0]}\nMentor: {kelas_detail[1]}")

def show_user_detail(user_detail):
    messagebox.showinfo("User Detail", f"Nama: {user_detail[0]}\nEmail: {user_detail[1]}\nNomor: {user_detail[2]}")

# Fungsi
def show_page(notebook,page):
    notebook.select(page)


#Tampilan



def tampilkan_user_kelas_gui(tk,page):
    for i in range(len(user_kelas)):
        user_kelas_label = tk.Label(page, text="{}. {}".format(i+1, user_kelas[i][0]))
        user_kelas_label.pack()



def tampilkan_menu_gui():
    notebook.add(kelas_page, text='Daftar Kelas')
    notebook.add(user_page, text='Daftar User')
    notebook.add(user_kelas_page, text='Daftar User Kelas')
    refresh_kelas()
    refresh_user()
    refresh_user_kelas()
    root.mainloop()


#main
tampilkan_menu_gui()
# search_kelas()
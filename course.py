import tkinter as tk
from tkinter import ttk, messagebox, Toplevel

# List kelas yang tersedia
# Nama kelas, nama mentor, durasi (bulan)
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

# List user yang terdaftar
# Nama, email, nomor telepon
user = [
    ['Dzulfikar Sadid', 'dzulfikar@mail.com',
     '08123456789'],
    ['Ahmad Riski', 'ahmad@mail.com', '08123456789'],
    ['Naufal Azka', 'naufal@mail.com', '08123456789'],
]

# List user yang terdaftar di kelas
# Nama, kelas
user_kelas = [
    ['Dzulfikar Sadid', 'Data Science'],
    ['Ahmad Riski', 'Web Development'],
    ['Naufal Azka', 'Machine Learning'],
    ['Dzulfikar Sadid', 'React Native'],
    ['Ahmad Riski', 'Backend Development'],
    ['Naufal Azka', 'Backend Development'],
]

# List terurut ascending atau tidak
is_ascending = True

# Inisialisai GUI
root = tk.Tk()
root.title("Bootcamp Online")
root.geometry("1280x720")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)
kelas_page = ttk.Frame(notebook)
user_page = ttk.Frame(notebook)
user_kelas_page = ttk.Frame(notebook)


# Sorting
def bubble_sort_ascending(lst):
    global is_ascending
    is_ascending = True
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_descending(lst):
    global is_ascending
    is_ascending = False
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def sort_and_refresh_kelas(ascending):
    if ascending:
        bubble_sort_ascending(kelas)
    else:
        bubble_sort_descending(kelas)
    refresh_kelas()


def sort_and_refresh_user(ascending):
    if ascending:
        bubble_sort_ascending(user)
    else:
        bubble_sort_descending(user)
    refresh_user()


# Searching
def binary_search_ascending(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid][0] < target:
            left = mid + 1
        elif target < lst[mid][0]:
            right = mid - 1
        else:
            return mid
    return -1


def binary_search_descending(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid][0] > target:
            left = mid + 1
        elif target > lst[mid][0]:
            right = mid - 1
        else:
            return mid
    return -1


def search_kelas(query):
    global is_ascending
    if is_ascending:
        bubble_sort_ascending(kelas)
        result = binary_search_ascending(kelas, query)
    else:
        bubble_sort_descending(kelas)
        result = binary_search_descending(kelas, query)
    if result >= 0:
        show_kelas_search(result + 1, kelas[result])
    else:
        messagebox.showinfo("Not Found",
                            "Kelas tidak ditemukan")


def search_user(query):
    global is_ascending
    if is_ascending:
        bubble_sort_ascending(user)
        result = binary_search_ascending(user, query)
    else:
        bubble_sort_descending(user)
        result = binary_search_descending(user, query)
    if result >= 0:
        show_user_search(result + 1, user[result])
    else:
        messagebox.showinfo("Not Found",
                            "User tidak ditemukan")


# Tampilan Halaman Kelas
def refresh_kelas():
    for widget in kelas_page.winfo_children():
        widget.destroy()

    label = tk.Label(kelas_page, text="Daftar Kelas",
                     font=("Arial", 18))
    label.pack(pady=10)

    search_frame = tk.Frame(kelas_page)
    search_frame.pack(pady=5)

    search_label = tk.Label(search_frame, text="Search:",
                            font=("Arial", 14))
    search_label.pack(side="left")

    search_entry = tk.Entry(search_frame,
                            font=("Arial", 14))
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="Search",
                              font=("Arial", 14),
                              relief="groove", padx=5,
                              pady=2, width=10,
                              borderwidth=2, bd=1,
                              bg="gray", fg="white",
                              highlightthickness=0,
                              highlightcolor="white",
                              command=lambda: search_kelas(
                                  search_entry.get()))
    search_button.pack(side="left", padx=5)

    for i in range(len(kelas)):
        kelas_frame = tk.Frame(kelas_page)
        kelas_frame.pack()

        kelas_button = tk.Button(kelas_frame,
                                 text="{}. {}".format(i + 1,
                                                      kelas[
                                                          i][
                                                          0]),
                                 anchor="w",
                                 font=("Arial", 14),
                                 relief="groove", padx=10,
                                 pady=5, width=20,
                                 borderwidth=4, bd=1,
                                 bg="white", fg="black",
                                 highlightthickness=0,
                                 highlightcolor="white",
                                 command=lambda
                                     kelas_detail=kelas[
                                         i]: show_kelas_detail(
                                     kelas_detail))
        kelas_button.pack(side="left", pady=5)

        join_button = tk.Button(kelas_frame,
                                text="Join Class",
                                font=("Arial", 16),
                                relief="groove", padx=5,
                                pady=2, width=10,
                                borderwidth=2, bd=1,
                                bg="blue", fg="white",
                                highlightthickness=0,
                                highlightcolor="white",
                                command=lambda: show_join_class_form(
                                    kelas[i]))
        join_button.pack(side="left", pady=5)

    sort_asc_button = tk.Button(kelas_page,
                                text="Sort Ascending",
                                font=("Arial", 18),
                                relief="groove", padx=5,
                                pady=2, width=15,
                                borderwidth=2, bd=1,
                                bg="green", fg="white",
                                highlightthickness=0,
                                highlightcolor="white",
                                command=lambda: sort_and_refresh_kelas(
                                    True))
    sort_asc_button.pack(pady=5)

    sort_desc_button = tk.Button(kelas_page,
                                 text="Sort Descending",
                                 font=("Arial", 18),
                                 relief="groove", padx=5,
                                 pady=2, width=15,
                                 borderwidth=2, bd=1,
                                 bg="red", fg="white",
                                 highlightthickness=0,
                                 highlightcolor="white",
                                 command=lambda: sort_and_refresh_kelas(
                                     False))
    sort_desc_button.pack(pady=5)


# Tampilan Halaman User
def refresh_user():
    for widget in user_page.winfo_children():
        widget.destroy()
    label = tk.Label(user_page, text="Daftar User",
                     font=("Arial", 24))
    label.pack(pady=10)

    search_frame = tk.Frame(user_page)
    search_frame.pack(pady=5)

    search_label = tk.Label(search_frame, text="Search:",
                            font=("Arial", 14))
    search_label.pack(side="left")

    search_entry = tk.Entry(search_frame,
                            font=("Arial", 14))
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="Search",
                              font=("Arial", 14),
                              relief="groove", padx=5,
                              pady=2, width=10,
                              borderwidth=2, bd=1,
                              bg="gray", fg="white",
                              highlightthickness=0,
                              highlightcolor="white",
                              command=lambda: search_user(
                                  search_entry.get()))

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
        user_table.insert(parent="", index="end", iid=i,
                          text=i + 1, values=(
            user_detail[0], user_detail[1], user_detail[2]))
    user_table.pack(pady=10)

    sort_asc_button = tk.Button(user_page,
                                text="Sort Ascending",
                                font=("Arial", 18),
                                relief="groove", padx=5,
                                pady=2, width=15,
                                borderwidth=2, bd=1,
                                bg="green", fg="white",
                                highlightthickness=0,
                                highlightcolor="white",
                                command=lambda: sort_and_refresh_user(
                                    True))
    sort_asc_button.pack(pady=5)

    sort_desc_button = tk.Button(user_page,
                                 text="Sort Descending",
                                 font=("Arial", 18),
                                 relief="groove", padx=5,
                                 pady=2, width=15,
                                 borderwidth=2, bd=1,
                                 bg="red", fg="white",
                                 highlightthickness=0,
                                 highlightcolor="white",
                                 command=lambda: sort_and_refresh_user(
                                     False))
    sort_desc_button.pack(pady=5)


# Tampilan Halaman User Kelas
def refresh_user_kelas():
    global kelas
    for widget in user_kelas_page.winfo_children():
        widget.destroy()

    label = tk.Label(user_kelas_page, text="Daftar Kelas",
                     font=("Arial", 18))
    label.pack(pady=10)

    for i in range(len(kelas)):
        kelas_frame = tk.Frame(user_kelas_page)
        kelas_frame.pack()

        kelas_button = tk.Button(kelas_frame,
                                 text="{}. {}".format(i + 1,
                                                      kelas[
                                                          i][
                                                          0]),
                                 anchor="w",
                                 font=("Arial", 14),
                                 relief="groove", padx=10,
                                 pady=5, width=20,
                                 borderwidth=4, bd=1,
                                 bg="white", fg="black",
                                 highlightthickness=0,
                                 highlightcolor="white",
                                 command=lambda
                                     kelas_detail=kelas[
                                         i]: show_kelas_detail(
                                     kelas_detail))
        kelas_button.pack(side="left", pady=5)

        join_button = tk.Button(kelas_frame,
                                text="Show Users",
                                font=("Arial", 16),
                                relief="groove", padx=5,
                                pady=2, width=10,
                                borderwidth=2, bd=1,
                                bg="yellow", fg="black",
                                highlightthickness=0,
                                highlightcolor="white",
                                command=lambda
                                    kelas_new=kelas[i][
                                        0]: show_user_kelas(
                                    kelas_new))
        join_button.pack(side="left", pady=5)


# Form untuk mengikuti kelas
def show_join_class_form(kelas):
    form_window = Toplevel(kelas_page)
    form_window.title(f"Join {kelas[0]}")

    # Create form labels
    name_label = tk.Label(form_window, text="Nama Anda:")
    name_label.grid(row=1, column=0, padx=10, pady=5,
                    sticky="w")
    name_entry = tk.Entry(form_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    email_label = tk.Label(form_window, text="Email Anda:")
    email_label.grid(row=2, column=0, padx=10, pady=5,
                     sticky="w")
    email_entry = tk.Entry(form_window)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    phone_label = tk.Label(form_window,
                           text="Nomor Telephone:")
    phone_label.grid(row=3, column=0, padx=10, pady=5,
                     sticky="w")
    phone_entry = tk.Entry(form_window)
    phone_entry.grid(row=3, column=1, padx=10, pady=5)

    submit_button = tk.Button(form_window, text="Submit",
                              command=lambda: submit_form(
                                  name_entry.get(),
                                  email_entry.get(),
                                  phone_entry.get(),
                                  kelas[0]))
    submit_button.grid(row=4, column=0, columnspan=2,
                       pady=10)


# Submit form
def submit_form(name, email, phone, kelas):
    user.append([name, email, phone])
    user_kelas.append([name, kelas])
    messagebox.showinfo("Berhasil",
                        "Selamat anda telah berhasil mendafar ke kelas ini!")
    sort_and_refresh_user(True)


# Details
def show_kelas_detail(kelas_detail):
    messagebox.showinfo("Kelas Detail",
                        f"Nama Kelas: {kelas_detail[0]}\nMentor: {kelas_detail[1]}\nDurasi: {kelas_detail[2]} bulan")


def show_kelas_search(index, kelas_detail):
    messagebox.showinfo(
        f"Kelas Ditemukan di Posisi {index}",
        f"Nama Kelas: {kelas_detail[0]}\nMentor: {kelas_detail[1]}\nDurasi: {kelas_detail[2]} bulan")


def show_user_detail(user_detail):
    messagebox.showinfo("User Detail",
                        f"Nama: {user_detail[0]}\nEmail: {user_detail[1]}\nNomor: {user_detail[2]}")


def show_user_search(index, user_detail):
    messagebox.showinfo(f"User Ditemukan di Posisi {index}",
                        f"Nama: {user_detail[0]}\nEmail: {user_detail[1]}\nNomor: {user_detail[2]}")


def show_user_kelas(kelas):
    filtered_users = []
    for user in user_kelas:
        if user[1] == kelas:
            filtered_users.append(user[0])

    user_list = "\n".join(
        ["{}. {}".format(i + 1, user) for i, user in
         enumerate(filtered_users)])
    if len(filtered_users) == 0:
        messagebox.showinfo("Filtered Users",
                            "Tidak ada user yang terdaftar di kelas ini")
    else:
        messagebox.showinfo("Filtered Users", user_list)


# Fungsi tambahan untuk menampilkan halaman
def show_page(notebook, page):
    notebook.select(page)


def tampilkan_menu_gui():
    notebook.add(kelas_page, text='Daftar Kelas')
    notebook.add(user_page, text='Daftar User')
    notebook.add(user_kelas_page, text='Daftar User Kelas')
    refresh_kelas()
    refresh_user()
    refresh_user_kelas()
    root.mainloop()


# Memanggil fungsi
sort_and_refresh_kelas(True)
sort_and_refresh_user(True)
tampilkan_menu_gui()

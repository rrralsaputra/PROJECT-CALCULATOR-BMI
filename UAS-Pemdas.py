import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    tinggi_meter = tinggi / 100  # Mengkonversi tinggi dari cm ke meter
    bmi = berat / (tinggi_meter ** 2)  # Rumus BMI
    return bmi

# Fungsi untuk menentukan kategori BMI
def kategori_bmi(bmi):
     if bmi < 18.5:
        return "Underweight / Kurus"
     elif 18.5 <= bmi < 24.9:
        return "Normal weight / Ideal"
     elif 25 <= bmi < 29.9:
        return "Overweight / Gemuk"
     elif bmi >= 30:
        return "Obesity / Obesitas"




# Fungsi untuk menyimpan hasil ke dalam file
def simpan_hasil(nama, gender, berat, tinggi, bmi, kategori):
    with open("hasil_bmi.txt", "a") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Berat Badan: {berat} kg\n")
        file.write(f"Tinggi Badan: {tinggi} cm\n")
        file.write(f"Hasil BMI: {bmi:.2f}\n")
        file.write(f"Kategori: {kategori}\n")
        file.write("-" * 40 + "\n")

# Fungsi untuk menampilkan background foto
def tampilkan_background(frame, foto):
    img = Image.open(foto)
    img = img.resize((416, 918), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(img)
    label_bg = tk.Label(frame, image=bg_image)
    label_bg.image = bg_image
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# Fungsi untuk membuka history dari file
def buka_history():
    try:
        with open("hasil_bmi.txt", "r") as file:
            history_text = file.read()
            # Menampilkan hasil history dalam jendela baru
            history_window = tk.Toplevel()
            history_window.title("History Hasil BMI")
            history_window.geometry("420x500")

            # Scrollable text area untuk menampilkan history
            text_area = tk.Text(history_window, wrap=tk.WORD, width=50, height=20)
            text_area.pack(pady=20)
            text_area.insert(tk.END, history_text)
            text_area.config(state=tk.DISABLED)  # Disable editing
    except FileNotFoundError:
        messagebox.showinfo("History", "Belum ada data history.")

# Fungsi untuk menghitung BMI dan menampilkan hasil di slide 3
def hitung_bmi_dan_tampilkan():
    try:
        # Mendapatkan input berat dan tinggi
        berat = float(entry_berat.get())
        tinggi = float(entry_tinggi.get())

        # Menghitung BMI
        bmi = hitung_bmi(berat, tinggi)

        # Menentukan kategori
        kategori = kategori_bmi(bmi)

        # Menampilkan hasil di Slide 3
        hasil_label.config(text=f"Hasil BMI: {bmi:.2f}")
        kategori_label.config(text=f"Kategori: {kategori}")

        hasil_ideal_label.config(text=f"Hasil BMI: {bmi:.2f}")
        kategori_ideal_label.config(text=f"Kategori: {kategori}")

        hasil_label_gemuk.config(text=f"Hasil BMI: {bmi:.2f}")
        kategori_label_gemuk.config(text=f"Kategori: {kategori}")

        hasil_label_obesitas.config(text=f"Hasil BMI: {bmi:.2f}")
        kategori_label_obesitas.config(text=f"Kategori: {kategori}")

        # Pindah ke Slide 3
        if bmi < 18.5:
            frame_slide_2.pack_forget()
            frame_slide_3_kurus.pack(fill="both", expand=True)
            hasil_label.config(text=f"Hasil BMI: {bmi:.2f}")
            kategori_label.config(text=f"Kategori: {kategori}")
        elif 18.5 <= bmi < 24.9:
            frame_slide_2.pack_forget()
            frame_slide_3_ideal.pack(fill="both", expand=True)
            hasil_label.config(text=f"Hasil BMI: {bmi:.2f}")
            kategori_label.config(text=f"Kategori: {kategori}")
        elif 25 <= bmi < 29.9:
            frame_slide_2.pack_forget()
            frame_slide_3_gemuk.pack(fill="both", expand=True)
            hasil_label.config(text=f"Hasil BMI: {bmi:.2f}")
            kategori_label.config(text=f"Kategori: {kategori}")
        elif 30 <= bmi:
            frame_slide_2.pack_forget()
            frame_slide_3_obesitas.pack(fill="both", expand=True)
            hasil_label.config(text=f"Hasil BMI: {bmi:.2f}")
            kategori_label.config(text=f"Kategori: {kategori}")
        else:
            return
        

        # Menyimpan hasil ke dalam file
        simpan_hasil(entry_nama.get(), gender_var.get(), berat, tinggi, bmi, kategori)

    except ValueError:
        messagebox.showerror("Input Error", "Tolong masukkan angka yang valid untuk berat dan tinggi.")

# Fungsi untuk membuat GUI
def buat_gui():
    global entry_nama, entry_berat, entry_tinggi, hasil_label, hasil_ideal_label, kategori_label, kategori_ideal_label,gender_var
    global frame_intro, next_button, frame_slide_1, frame_slide_2, frame_slide_3_kurus, frame_slide_3_ideal, frame_slide_3_gemuk, hasil_label_gemuk, kategori_label_gemuk
    global frame_slide_3_obesitas, hasil_label_obesitas, kategori_label_obesitas

    # Membuat jendela utama
    window = tk.Tk()
    window.title("Kalkulator BMI")
    window.geometry("420x900")
    window.resizable(False, False)

#Slide Intro
    frame_intro = tk.Frame(window)
    tampilkan_background(frame_intro, "intro.png")
    next_button = tk.Button(frame_intro, text="CEK BMI", command=lambda: [frame_intro.pack_forget(), frame_slide_1.pack(fill="both", expand=True)],
                             bg="#336699", relief="flat", fg="white", font=("Arial", 12), activebackground="#336699", activeforeground="white")
    next_button.place(x=165, y=730)

    
# Slide 1 (Input Nama dan Gender)
    frame_slide_1 = tk.Frame(window)
    tampilkan_background(frame_slide_1, "slide1.png") 
    nama_label = tk.Label(frame_slide_1, text="Nama Anda:", bg="#7aaaeb", fg="white", font=("Courier New:", 14))
    nama_label.place(x=40, y=470)  # Posisi di 20px dari kiri dan atas

    entry_nama = tk.Entry(frame_slide_1, bg="#ffffff", fg="black", relief="flat", font=("Arial", 12))
    entry_nama.place(x=40, y=520)  # Di sebelah kanan nama_label

    gender_label = tk.Label(frame_slide_1, text="Gender:", bg="#7aaaeb", fg="white", font=("Arial", 12, ))
    gender_label.place(x=40, y=580)

    gender_var = tk.StringVar()
    gender_laki = tk.Radiobutton(frame_slide_1, text="Laki-laki", variable=gender_var, value="Laki-laki", bg="#ffffff", fg="black", font=("Arial", 10))
    gender_laki.place(x=50, y=640)
    gender_perempuan = tk.Radiobutton(frame_slide_1, text="Perempuan", variable=gender_var, value="Perempuan", bg="#ffffff", fg="black", font=("Arial", 10))
    gender_perempuan.place(x=50, y=670)

    lanjut_button_1 = tk.Button(frame_slide_1, text="Lanjutkan", command=lambda: [frame_slide_1.pack_forget(), frame_slide_2.pack(fill="both", expand=True)],
                                 bg="#336699", relief="flat", fg="white", font=("Arial", 12), activebackground="#336699", activeforeground="white")
    lanjut_button_1.place(x=152, y=747)

# Tombol untuk membuka History
    history_button = tk.Button(frame_slide_1, text="🕐", command=buka_history, bg="#7aaaeb", fg="white",relief="flat", font=("Arial", 18), activebackground="#7aaaeb", activeforeground="white")
    history_button.place(x=337, y=89)

# Slide 2 (Input Berat dan Tinggi)
    frame_slide_2 = tk.Frame(window)
    tampilkan_background(frame_slide_2, "2.png") 
# Tulisan Berat
    berat_label = tk.Label(frame_slide_2, text="Berat Badan (kg):", bg="#ffffff", fg="black", font=("Arial", 12))
    berat_label.place(x=50, y=435)
# kolom kotak berat
    entry_berat = tk.Entry(frame_slide_2,relief="flat",text="berat badan", font=("Arial", 12))
    entry_berat.place(x=110, y=480)
# Tulisan tinggi
    tinggi_label = tk.Label(frame_slide_2, text="Tinggi Badan (cm):",bg="#ffffff", fg="black", font=("Arial", 12))
    tinggi_label.place(x=50, y=535)
# kolom masukan tinggi
    entry_tinggi = tk.Entry(frame_slide_2,relief="flat", font=("Arial", 12))
    entry_tinggi.place(x=110, y=578)
# tombol hitung
    hitung_button = tk.Button(frame_slide_2, text="Hitung BMI", command=lambda: hitung_bmi_dan_tampilkan(), bg="#336699", fg="white",relief="flat", font=("Arial", 12), activebackground="#336699", activeforeground="white")
    hitung_button.place(x=153, y=648)
# tombol kembali
    kembali_button_2 = tk.Button(frame_slide_2,relief="flat", text="Kembali", command=lambda: [frame_slide_2.pack_forget(), frame_slide_1.pack(fill="both", expand=True)],
                                 bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_2.place(x=177, y=718)

# Slide 3 (Hasil BMI)
    frame_slide_3_kurus = tk.Frame(window)
    tampilkan_background(frame_slide_3_kurus, "hasil kurus.png") 
    hasil_label = tk.Label(frame_slide_3_kurus, text="Hasil BMI: ", bg="#7aaaeb", fg="white", font=("Arial", 18))
    hasil_label.place(x=80, y=403)
    kategori_label = tk.Label(frame_slide_3_kurus, text="Kategori: ", bg="#7aaaeb", fg="white", font=("Arial", 15))
    kategori_label.place(x=75, y=475)
#KURUS
    kembali_button_3_kurus = tk.Button(frame_slide_3_kurus,relief="flat", text="Kembali",
                                command=lambda: [frame_slide_3_kurus.pack_forget(), frame_slide_2.pack(fill="both", expand=True)], bg="#789ec4", fg="white",
                                font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_3_kurus.place(x=177, y=733)
    tips_button_kurus = tk.Button(frame_slide_3_kurus, text="TIPS MENAIKAN BERAT BADAN",
                                command=lambda: [frame_slide_3_kurus.pack_forget(), frame_slide_4_tips_kurus.pack(fill="both", expand=True)], bg="#336699",
                                relief="flat", fg="white", font=("Arial", 12), activebackground="#336699", activeforeground="white")
    tips_button_kurus.place(x=75, y=540)
    resiko_button_kurus = tk.Button(frame_slide_3_kurus, text="RESIKO PENYAKIT \n KEKURANGAN BERAT BADAN",
                                command=lambda: [frame_slide_3_kurus.pack_forget(), frame_slide_4_resiko_kurus.pack(fill="both", expand=True)], bg="#336699", 
                                relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    resiko_button_kurus.place(x=75, y=600)
    makanan_button_kurus = tk.Button(frame_slide_3_kurus, text="MAKANAN PENAMBAH BERAT BADAN", 
                                command=lambda: [frame_slide_3_kurus.pack_forget(), frame_slide_4_makanan_kurus.pack(fill="both", expand=True)], bg="#336699", 
                                relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    makanan_button_kurus.place(x=55, y=678)
# Slide 4 (TIPS KURUS)
    frame_slide_4_tips_kurus = tk.Frame(window)
    tampilkan_background(frame_slide_4_tips_kurus, "tips kurus.png") 
    kembali_button_4_tips_kurus = tk.Button(frame_slide_4_tips_kurus,relief="flat", text="Kembali", 
                                            command=lambda: [frame_slide_4_tips_kurus.pack_forget(), frame_slide_3_kurus.pack(fill="both", expand=True)], 
                                            bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_tips_kurus.place(x=177, y=740)
#Slide 4 (RESIKO KEKURANGAN BERAT BADAN)
    frame_slide_4_resiko_kurus = tk.Frame(window)
    tampilkan_background(frame_slide_4_resiko_kurus, "resiko kurus.png") 
    kembali_button_4_resiko_kurus = tk.Button(frame_slide_4_resiko_kurus,relief="flat", text="Kembali", 
                                            command=lambda: [frame_slide_4_resiko_kurus.pack_forget(), frame_slide_3_kurus.pack(fill="both", expand=True)], 
                                            bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_resiko_kurus.place(x=177, y=740)
#Slide 4 (SARAN MAKANAN)
    frame_slide_4_makanan_kurus = tk.Frame(window)
    tampilkan_background(frame_slide_4_makanan_kurus, "saran mkn.png") 
    kembali_button_4_makanan_kurus = tk.Button(frame_slide_4_makanan_kurus,relief="flat", text="Kembali", 
                                            command=lambda: [frame_slide_4_makanan_kurus.pack_forget(), frame_slide_3_kurus.pack(fill="both", expand=True)], 
                                            bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_makanan_kurus.place(x=177, y=740)
    
#Slide 3 (Hasil BMI)
    frame_slide_3_ideal = tk.Frame(window)
    tampilkan_background(frame_slide_3_ideal, "hasil ideal.png")
    hasil_ideal_label = tk.Label(frame_slide_3_ideal, text="Hasil BMI: ", bg="#7aaaeb", fg="white", font=("Arial", 12))
    hasil_ideal_label.place(x=80, y=405)
    kategori_ideal_label = tk.Label(frame_slide_3_ideal, text="Kategori: ", bg="#7aaaeb", fg="white", font=("Arial", 12))
    kategori_ideal_label.place(x=75, y=475)
#IDEAL   
    kembali_button_3_ideal = tk.Button(frame_slide_3_ideal,relief="flat", text="Kembali", command=lambda: [frame_slide_3_ideal.pack_forget(), frame_slide_2.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_3_ideal.place(x=177, y=733)
    tips_button_ideal = tk.Button(frame_slide_3_ideal, text="TIPS MENJAGA BERAT BADAN", command=lambda: [frame_slide_3_ideal.pack_forget(), frame_slide_4_tips_ideal.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 12), activebackground="#336699", activeforeground="white")
    tips_button_ideal.place(x=75, y=540)
    olahraga_button_ideal = tk.Button(frame_slide_3_ideal, text="OLAHRAGA UNTUK MENJAGA \n BERAT BADAN", command=lambda: [frame_slide_3_ideal.pack_forget(), frame_slide_4_olahraga_ideal.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    olahraga_button_ideal.place(x=75, y=600)
    makanan_button_ideal = tk.Button(frame_slide_3_ideal, text="MAKANAN PENJAGA BERAT BADAN", command=lambda: [frame_slide_3_ideal.pack_forget(), frame_slide_4_makanan_ideal.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    makanan_button_ideal.place(x=55, y=678)
#SLIDE 4(TIPS IDEAL)
    frame_slide_4_tips_ideal = tk.Frame(window)
    tampilkan_background(frame_slide_4_tips_ideal, "tips ideal.png") 
    kembali_button_4_tips_ideal = tk.Button(frame_slide_4_tips_ideal,relief="flat", text="Kembali", command=lambda: [frame_slide_4_tips_ideal.pack_forget(), frame_slide_3_ideal.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_tips_ideal.place(x=177, y=740)
#SLIDE 4 (OLAHRAGA IDEAL)
    frame_slide_4_olahraga_ideal = tk.Frame(window)
    tampilkan_background(frame_slide_4_olahraga_ideal, "OR ideal.png") 
    kembali_button_4_olahraga_ideal = tk.Button(frame_slide_4_olahraga_ideal,relief="flat", text="Kembali", command=lambda: [frame_slide_4_olahraga_ideal.pack_forget(), frame_slide_3_ideal.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_olahraga_ideal.place(x=177, y=740)
#SLIDE 4 (SARAN MAKAN)
    frame_slide_4_makanan_ideal = tk.Frame(window)
    tampilkan_background(frame_slide_4_makanan_ideal, "saran mkn ideal.png") 
    kembali_button_4_makanan_ideal = tk.Button(frame_slide_4_makanan_ideal,relief="flat", text="Kembali", command=lambda: [frame_slide_4_makanan_ideal.pack_forget(), frame_slide_3_ideal.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_makanan_ideal.place(x=177, y=740)
# Slide 3 (Hasil BMI)
    frame_slide_3_gemuk = tk.Frame(window)
    tampilkan_background(frame_slide_3_gemuk, "hasil gemuk.png")
    hasil_label_gemuk = tk.Label(frame_slide_3_gemuk, text="Hasil BMI: ", bg="#7aaaeb", fg="white", font=("Arial", 12))
    hasil_label_gemuk.place(x=80, y=405)
    kategori_label_gemuk = tk.Label(frame_slide_3_gemuk, text="Kategori: ", bg="#7aaaeb", fg="white", font=("Arial", 12))
    kategori_label_gemuk.place(x=75, y=475)
#GEMUK 
    kembali_button_3_gemuk = tk.Button(frame_slide_3_gemuk,relief="flat", text="Kembali", command=lambda: [frame_slide_3_gemuk.pack_forget(), frame_slide_2.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_3_gemuk.place(x=177, y=733)
    tips_button_gemuk = tk.Button(frame_slide_3_gemuk, text="TIPS MENURUNKAN BERAT BADAN", command=lambda: [frame_slide_3_gemuk.pack_forget(), frame_slide_4_tips_gemuk.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 12), activebackground="#336699", activeforeground="white")
    tips_button_gemuk.place(x=50, y=540)
    resiko_button_gemuk = tk.Button(frame_slide_3_gemuk, text="RESIKO PENYAKIT KELEBIHAN \n BERAT BADAN", command=lambda: [frame_slide_3_gemuk.pack_forget(), frame_slide_4_resiko_gemuk.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    resiko_button_gemuk.place(x=75, y=603)
    makanan_button_gemuk = tk.Button(frame_slide_3_gemuk, text="SARAN MAKANAN UNTUK \n MENURUNKAN BERAT BADAN", command=lambda: [frame_slide_3_gemuk.pack_forget(), frame_slide_4_makanan_gemuk.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    makanan_button_gemuk.place(x=75, y=670)
#SLIDE 4 (TIPS GEMUK)
    frame_slide_4_tips_gemuk = tk.Frame(window)
    tampilkan_background(frame_slide_4_tips_gemuk, "tips gemuk.png") 
    kembali_button_4_tips_gemuk = tk.Button(frame_slide_4_tips_gemuk,relief="flat", text="Kembali", command=lambda: [frame_slide_4_tips_gemuk.pack_forget(), frame_slide_3_gemuk.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_tips_gemuk.place(x=177, y=740)
#SLIDE 4 (RESIKO GEMUK)
    frame_slide_4_resiko_gemuk = tk.Frame(window)
    tampilkan_background(frame_slide_4_resiko_gemuk, "resiko gemuk.png") 
    kembali_button_4_resiko_gemuk = tk.Button(frame_slide_4_resiko_gemuk,relief="flat", text="Kembali", command=lambda: [frame_slide_4_resiko_gemuk.pack_forget(), frame_slide_3_gemuk.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_resiko_gemuk.place(x=177, y=740)
#SLIDE 4 (SARAN MAKANAN)
    frame_slide_4_makanan_gemuk = tk.Frame(window)
    tampilkan_background(frame_slide_4_makanan_gemuk, "saran mkn gemuk.png") 
    kembali_button_4_makanan_gemuk = tk.Button(frame_slide_4_makanan_gemuk,relief="flat", text="Kembali", command=lambda: [frame_slide_4_makanan_gemuk.pack_forget(), frame_slide_3_gemuk.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_makanan_gemuk.place(x=177, y=740)
    
# Slide 3 ( Hasil BMI)
    frame_slide_3_obesitas = tk.Frame(window)
    tampilkan_background(frame_slide_3_obesitas, "hasil obesitas.png")
    hasil_label_obesitas = tk.Label(frame_slide_3_obesitas, text="Hasil BMI: ", bg="#7aaaeb", fg="white", font=("Arial", 12))
    hasil_label_obesitas.place(x=80, y=405)
    kategori_label_obesitas = tk.Label(frame_slide_3_obesitas, text="Kategori: ", bg="#7aaaeb", fg="white", font=("Arial", 12))
    kategori_label_obesitas.place(x=75, y=475)
#OBESITAS
    kembali_button_4_obesitas = tk.Button(frame_slide_3_obesitas,relief="flat", text="Kembali", command=lambda: [frame_slide_3_obesitas.pack_forget(), frame_slide_2.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_obesitas.place(x=177, y=733)
    tips_button_obesitas = tk.Button(frame_slide_3_obesitas, text="TIPS MENURUNKAN BERAT BADAN", command=lambda: [frame_slide_3_obesitas.pack_forget(), frame_slide_4_tips_obesitas.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 12), activebackground="#336699", activeforeground="white")
    tips_button_obesitas.place(x=50, y=540)
    resiko_button_obesitas = tk.Button(frame_slide_3_obesitas, text="RESIKO PENYAKIT KELEBIHAN \n BERAT BADAN", command=lambda: [frame_slide_3_obesitas.pack_forget(), frame_slide_4_resiko_obesitas.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    resiko_button_obesitas.place(x=75, y=603)
    makanan_button_obesitas = tk.Button(frame_slide_3_obesitas, text="SARAN MAKANAN UNTUK \n MENURUNKAN BERAT BADAN", command=lambda: [frame_slide_3_obesitas.pack_forget(), frame_slide_4_makanan_obesitas.pack(fill="both", expand=True)], bg="#336699", relief="flat", fg="white", font=("Arial", 11), activebackground="#336699", activeforeground="white")
    makanan_button_obesitas.place(x=75, y=670)
#SLIDE 4 (TIPS OBESITAS)
    frame_slide_4_tips_obesitas = tk.Frame(window)
    tampilkan_background(frame_slide_4_tips_obesitas, "tips obesitas.png") 
    kembali_button_4_tips_obesitas = tk.Button(frame_slide_4_tips_obesitas,relief="flat", text="Kembali", command=lambda: [frame_slide_4_tips_obesitas.pack_forget(), frame_slide_3_obesitas.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_tips_obesitas.place(x=177, y=740)  
#SLIDE 4 (RESIKO OBESITAS  )
    frame_slide_4_resiko_obesitas = tk.Frame(window)
    tampilkan_background(frame_slide_4_resiko_obesitas, "resiko obesitas.png") 
    kembali_button_4_resiko_obesitas = tk.Button(frame_slide_4_resiko_obesitas,relief="flat", text="Kembali", command=lambda: [frame_slide_4_resiko_obesitas.pack_forget(), frame_slide_3_obesitas.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_resiko_obesitas.place(x=177, y=740)
#SLIDE 4 (MAKANAN OBESITAS  )
    frame_slide_4_makanan_obesitas = tk.Frame(window)
    tampilkan_background(frame_slide_4_makanan_obesitas, "saran mkn obesitas.jpg") 
    kembali_button_4_makanan_obesitas = tk.Button(frame_slide_4_makanan_obesitas,relief="flat", text="Kembali", command=lambda: [frame_slide_4_makanan_obesitas.pack_forget(), frame_slide_3_obesitas.pack(fill="both", expand=True)], bg="#789ec4", fg="white", font=("Arial", 12), activebackground="#789ec4", activeforeground="white")
    kembali_button_4_makanan_obesitas.place(x=177, y=740)
# Menampilkan Slide intro saat memulai
    frame_intro.pack(fill="both", expand=True)

# Menjalankan GUI
    window.mainloop()

# Menjalankan GUI
if __name__ == "__main__":
    buat_gui()

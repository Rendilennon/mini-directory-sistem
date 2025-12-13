import os

def write_file(nama_file, isi_konten):
    # 1. Validate: cek apakah file ada
    if not os.path.exists(nama_file):
        print(f"[ERROR] File '{nama_file}' tidak ditemukan.")
        print("[INFO] Gunakan perintah 'create' untuk membuat file baru.")
        return False

    try:
        with open(nama_file, 'w') as file:
            file.write(isi_konten)
        
        print(f"[SUKSES] Konten berhasil ditulis ke file '{nama_file}'.")
        return True

    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan sistem: {e}")
        return False
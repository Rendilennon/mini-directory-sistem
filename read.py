import os

def read_file(nama_file):
    if not os.path.exists(nama_file):
        print(f"[ERROR] File '{nama_file}' tidak ditemukan.")
        return False
    
    if not os.path.isfile(nama_file):
        print(f"[ERROR] '{nama_file}' bukan file.")
        return False

    try:
        # Execute: Baca isi file
        with open(nama_file, 'r') as file:
            isi = file.read()
        
        # Tampilkan isi file
        if isi.strip():
            print(f"\n{'='*40}")
            print(f"Isi file: {nama_file}")
            print(f"{'='*40}")
            print(isi)
            print(f"{'='*40}\n")
        else:
            print(f"[INFO] File '{nama_file}' kosong.")
        
        return True

    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan sistem: {e}")
        return False

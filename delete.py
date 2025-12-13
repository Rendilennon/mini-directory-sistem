import os

def delete_file(nama_file):
    if not os.path.exists(nama_file):
        print(f"[ERROR] File '{nama_file}' tidak ditemukan.")
        return False

    try:
        os.remove(nama_file)
        print(f"[SUKSES] File '{nama_file}' berhasil dihapus.")
        return True

    except Exception as e:
        print(f"[ERROR] Gagal menghapus file: {e}")
        return False

import os

def list_files(path="."):
    # 1. Cek apakah path valid
    if not os.path.exists(path):
        print(f"[ERROR] Direktori '{path}' tidak ditemukan.")
        return

    try:
        items = os.listdir(path)

        if not items:
            print("[INFO] Direktori kosong.")
            return

        print(f"\n[INFO] Isi direktori '{os.path.abspath(path)}':")
        print("-" * 40)
        
        for item in items:
            full_path = os.path.join(path, item)
            
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                print(f"📄 {item:<20} | {size} bytes")
            elif os.path.isdir(full_path):
                print(f"📂 {item:<20} | <DIR>")
            else:
                print(f"❓ {item}")

        print("-" * 40)
        print("[SUKSES] List selesai ditampilkan.\n")

    except Exception as e:
        print(f"[ERROR] Gagal menampilkan list: {e}")

if __name__ == "__main__":
    list_files()
import sys
from create import create_file
from list import list_files

def main():
    print("=== SISTEM FILE MINI ===")
    print("PANDUAN KOMAND:")
    print("\"create <nama_file>\" - Membuat file baru")
    print("\"ls\" - Menampilkan daftar file dan folder")
    print("\"cat\" - Membaca isi file")
    print("\"nano\" - Membuka teks editor nano untuk mengedit file")
    print("\"rm\" - Menghapus file") 
    print("\"exit\" - Keluar dari program")
    
    while True:
        try:
            command_input = input("\nuser@system:~$ ").strip().split()

            if not command_input:
                continue

            perintah = command_input[0].lower()

            # --- LOGIKA CREATE ---
            if perintah == "create":
                if len(command_input) < 2:
                    print("[INFO] Harap masukkan nama file. Contoh: create biodata.txt")
                else:
                    nama_file = command_input[1]
                    create_file(nama_file)

            # --- LOGIKA LIST ---
            elif perintah == "ls" or perintah == "list":
                if len(command_input) >= 2:
                    path = command_input[1]
                    list_files(path)
                else:
                    list_files()  #

            # --- KELUAR ---
            elif perintah == "exit":
                print("Sistem dimatikan.")
                break
            
            else:
                print(f"[INFO] Perintah '{perintah}' belum tersedia atau salah ketik.")

        except KeyboardInterrupt:
            print("\nThanks for using our system.")
            break

if __name__ == "__main__":
    main()
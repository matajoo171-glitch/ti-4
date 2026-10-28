import threading, time
kursi_tersedia = 1
barrier = threading.Barrier(2)
lock_output = threading.Lock()

def mahasiswa(nama):
    global kursi_tersedia
    with lock_output:
        print(f"{nama}: membaca kursi = {kursi_tersedia}")
    if kursi_tersedia > 0:
        barrier.wait()       # Sengaja membuat kedua thread membaca nilai yang sama
        time.sleep(0.05)
        kursi_tersedia -= 1  # Tidak dilindungi mutex: race condition
        with lock_output:
            print(f"{nama}: BERHASIL mengambil kursi")

if __name__ == "__main__":
    ts = [threading.Thread(target=mahasiswa, args=(n,)) for n in ("Mahasiswa A","Mahasiswa B")]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("Jumlah kursi akhir:", kursi_tersedia)

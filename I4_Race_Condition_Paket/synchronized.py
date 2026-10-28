import threading, time
kursi_tersedia = 1
mutex = threading.Lock()

def mahasiswa(nama):
    global kursi_tersedia
    # Critical section: periksa dan ubah jumlah kursi di dalam mutex.
    with mutex:
        print(f"{nama}: memeriksa kursi = {kursi_tersedia}")
        if kursi_tersedia > 0:
            time.sleep(0.05)
            kursi_tersedia -= 1
            print(f"{nama}: BERHASIL mengambil kursi")
        else:
            print(f"{nama}: GAGAL, kursi sudah habis")

if __name__ == "__main__":
    ts = [threading.Thread(target=mahasiswa, args=(n,)) for n in ("Mahasiswa A","Mahasiswa B")]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("Jumlah kursi akhir:", kursi_tersedia)

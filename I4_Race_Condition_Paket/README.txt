I-4 — Analisis Race Condition dan Sinkronisasi
File:
- race_condition.py: demonstrasi sebelum perbaikan
- synchronized.py: versi diperbaiki menggunakan mutex
- Laporan_I4_Race_Condition.pdf: draf laporan

Jalankan dengan Python 3:
python race_condition.py
python synchronized.py

Ulangi kedua program minimal lima kali dan ambil screenshot output nyata dari terminal.
Versi sebelum perbaikan sengaja menggunakan Barrier untuk memperlihatkan dua thread
membaca kursi yang sama sebelum mengubahnya. Versi setelah perbaikan mengunci
pemeriksaan dan pengurangan kursi dengan threading.Lock.

Identitas dalam draf: Kafka Aditia, NIM 250660121064, kelas IF-IIIA.
Sesuaikan bila diperlukan. Jadwal kursi pada contoh adalah simulasi.
Ungkapkan penggunaan AI generatif sesuai ketentuan tugas.

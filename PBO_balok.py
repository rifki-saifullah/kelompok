import flet as ft

# Fungsi Utama
def main(page: ft.Page):

    # Warna Background (putih)
    page.bgcolor = "#F6F6F6"

    # Jika tombol 'hasil' ditekan, maka jalankan kode dibawah ini
    def btn_click(e):

        # Jika user tidak menginputkan panjang, maka
        if not panjang.value:

            # Buat pesan error
            panjang.error_text = "Tolong masukkan panjang balok"

            # Halaman di refrash (agar pesan error muncul)
            page.update()

        # Jika user tidak menginputkan lebar
        elif not lebar.value:

            # Buat pesan error
            lebar.error_text = "Tolong masukkan lebar balok"

            # Halaman di refrash (agar pesan error muncul)
            page.update()

        # Jika user tidak menginputkan tinggi
        elif not tinggi.value:

            # Buat pesan error
            tinggi.error_text = "Tolong masukkan tinggi balok"

            # Halaman di refrash (agar pesan error muncul)
            page.update()

        # Jika berhasil (user menginputkan semua, panjang, lebar dan tinggi)
        else:
            # Hitung luas
            value_luas = 2 * (int(panjang.value) * int(lebar.value) + int(panjang.value) * int(tinggi.value) + int(lebar.value) * int(tinggi.value))

            # Hitung volume
            value_volume = int(panjang.value) * int(lebar.value) * int(tinggi.value)

            # Tampilkan luas
            luas.value = value_luas

            # Tampilkan volume
            volume.value = value_volume

            # Page di refresh
            page.update()

    # Buat Elemen TextField (inputan)
    panjang = ft.TextField(label="Panjang")
    lebar = ft.TextField(label="Lebar")
    tinggi = ft.TextField(label="Tinggi")
    luas = ft.TextField(label="Luas")
    volume = ft.TextField(label="Volume")

    # Tampilkan elemen tersebut
    page.add(

        # Nav bar, bagian atas / judul. Nama & warna background (biru)
        ft.AppBar(title=ft.Text("Kalkulator Balok"), bgcolor="#BBE1FA"),

        panjang,
        lebar,
        tinggi,

        # Tombol Hasil
        ft.ElevatedButton("hitung!", on_click=btn_click),

        luas,
        volume
    )

# Jalankan aplikasi
ft.app(target=main)

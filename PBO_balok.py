import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#F6F6F6"
    def btn_click(e):
        if not panjang.value:
            panjang.error_text = "Tolong masukkan panjang balok"
            page.update()
        elif not lebar.value:
            lebar.error_text = "Tolong masukkan lebar balok"
            page.update()
        elif not tinggi.value:
            tinggi.error_text = "Tolong masukkan tinggi balok"
            page.update()
        else:
            value_luas = 2 * (int(panjang.value) * int(lebar.value) + int(panjang.value) * int(tinggi.value) + int(lebar.value) * int(tinggi.value))
            value_volume = int(panjang.value) * int(lebar.value) * int(tinggi.value)
            luas.value = value_luas
            volume.value = value_volume
            page.update()

    panjang = ft.TextField(label="Panjang")
    lebar = ft.TextField(label="Lebar")
    tinggi = ft.TextField(label="Tinggi")
    luas = ft.TextField(label="Luas")
    volume = ft.TextField(label="Volume")

    page.add(
        ft.AppBar(title=ft.Text("Kalkulator Balok"), bgcolor="#BBE1FA"),
        panjang,
        lebar,
        tinggi,
        ft.ElevatedButton("hitung!", on_click=btn_click),
        luas,
        volume
    )

ft.app(target=main)
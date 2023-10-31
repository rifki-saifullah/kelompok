todolist = []

def show():
    global todolist
    if not todolist:
        print("(Todo masih kosong)")
    else:
        for index, value in enumerate(todolist):
            print(f"{index + 1}. {value}")

def add(todo):
    todolist.append(todo)
    print("\n~Berhasil menambahkan todo~\n")

def remove(number):
    global todolist
    number = number - 1
    if 0 <= number < len(todolist):
        del todolist[number]
        print(f"\n~Berhasil menghapus todo~\n")
    else:
        print(f"\n-Gagal menghapus todo-\n(tidak ada todo dengan nomor tersebut)\n")


def main():
    while True:
        print("TODOLIST APP")
        show()
        print("Menu :")
        print("1. Tambah Todo")
        print("2. Hapus Todo")
        print("x. Keluar")

        pilihan = input("Masukkan Pilihan : ")

        if pilihan == '1':
            todo = input("Masukkan Todo : ")
            add(todo)

        elif pilihan == '2':
            number = input("Masukkan Nomor : ")
            if number.isdigit():
                number = int(number)
                remove(number)
            else:
                print("\n-Gagal-\n(Mohon masukkan angka)\n")

        elif pilihan == 'x':
            break
        
        else:        
            print("\n-Pilihan tidak diketahui-\n")

    print("\n~ bye bye ~\n")

main()
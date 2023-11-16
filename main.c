#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Mahasiswa {
    char nim[5];
    char nama[50];
    char fakultas[50];
};

int compareMahasiswa(const void *a, const void *b) {
    return strcmp(((struct Mahasiswa *)a)->nim, ((struct Mahasiswa *)b)->nim);
}

int main() {
    int jumlah_mahasiswa;

    printf("Masukkan jumlah mahasiswa: ");
    scanf("%d", &jumlah_mahasiswa);

    struct Mahasiswa *mahasiswa_list = malloc(jumlah_mahasiswa * sizeof(struct Mahasiswa));

    for (int i = 0; i < jumlah_mahasiswa; ++i) {
        printf("Masukkan NIM mahasiswa ke-%d: ", i + 1);
        scanf("%s", mahasiswa_list[i].nim);

        printf("Masukkan nama mahasiswa ke-%d: ", i + 1);
        scanf("%s", mahasiswa_list[i].nama);

        printf("Masukkan fakultas mahasiswa ke-%d: ", i + 1);
        scanf("%s", mahasiswa_list[i].fakultas);
    }

    qsort(mahasiswa_list, jumlah_mahasiswa, sizeof(struct Mahasiswa), compareMahasiswa);

    printf("\nHasil Sorting Mahasiswa berdasarkan NIM:\n");
    for (int i = 0; i < jumlah_mahasiswa; ++i) {
        printf("NIM: %s, Nama: %s, Fakultas: %s\n", mahasiswa_list[i].nim, mahasiswa_list[i].nama, mahasiswa_list[i].fakultas);
    }

    free(mahasiswa_list);

    return 0;
}

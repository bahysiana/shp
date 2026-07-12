import pandas as pd
from sklearn.cluster import KMeans

# ==========================================================
# VARIABEL STATISTIK
# ==========================================================

STATISTIC_COLUMNS = [

    "Total_harga",

    "Jumlah_pesanan",

    "Jumlah_jenis_menu",

    "waktu_persiapan_yang_diberikan",

    "waktu_persiapan_digunakan"

]


# ==========================================================
# MENJALANKAN ALGORITMA K-MEANS
# ==========================================================

def run_kmeans(data):
    """
    Menjalankan proses K-Means Clustering.
    """

    model = KMeans(

        n_clusters=2,

        random_state=42,

        n_init=10

    )

    labels = model.fit_predict(data)

    centroid = pd.DataFrame(

        model.cluster_centers_,

        columns=data.columns

    )

    return model, labels, centroid


# ==========================================================
# MENAMBAHKAN HASIL CLUSTER
# ==========================================================

def add_cluster_result(df, labels):
    """
    Menambahkan hasil cluster ke dataset.
    """

    hasil = df.copy()

    hasil["Cluster"] = labels

    return hasil


# ==========================================================
# MEMBERIKAN NAMA CLUSTER
# ==========================================================

def add_cluster_label(df, centroid):
    """
    Menentukan nama cluster secara otomatis
    berdasarkan total nilai centroid.
    """

    hasil = df.copy()

    centroid_score = centroid.sum(axis=1)

    cluster_tinggi = centroid_score.idxmax()

    cluster_rendah = centroid_score.idxmin()

    mapping = {

        cluster_tinggi:

        "Pola Transaksi dengan Beban Pelayanan Tinggi",

        cluster_rendah:

        "Pola Transaksi dengan Beban Pelayanan Rendah"

    }

    hasil["Nama Cluster"] = (

        hasil["Cluster"]

        .map(mapping)

    )

    return hasil


# ==========================================================
# RINGKASAN CLUSTER
# ==========================================================

def cluster_summary(df):
    """
    Menghitung jumlah data
    pada setiap cluster.
    """

    summary = (

        df.groupby(

            [

                "Cluster",

                "Nama Cluster"

            ]

        )

        .size()

        .reset_index(

            name="Jumlah Data"

        )

    )

    total = summary["Jumlah Data"].sum()

    summary["Persentase (%)"] = (

        summary["Jumlah Data"]

        / total

        * 100

    ).round(2)

    return summary


# ==========================================================
# STATISTIK CLUSTER
# ==========================================================

def cluster_statistics(df):
    """
    Menghitung rata-rata setiap
    variabel penelitian.
    """

    statistik = (

        df.groupby(

            [

                "Cluster",

                "Nama Cluster"

            ]

        )[

            STATISTIC_COLUMNS

        ]

        .mean()

        .round(2)

        .reset_index()

    )

    return statistik


# ==========================================================
# INFORMASI CLUSTER
# ==========================================================

def get_cluster_information(summary):
    """
    Mengambil informasi cluster
    untuk halaman Clustering
    dan Laporan PDF.
    """

    tinggi = summary[

        summary["Nama Cluster"]

        ==

        "Pola Transaksi dengan Beban Pelayanan Tinggi"

    ]

    rendah = summary[

        summary["Nama Cluster"]

        ==

        "Pola Transaksi dengan Beban Pelayanan Rendah"

    ]

    info = {

        "tinggi": {

            "cluster":

                "-"

                if tinggi.empty

                else f"Cluster {int(tinggi.iloc[0]['Cluster'])}",

            "jumlah":

                0

                if tinggi.empty

                else int(

                    tinggi.iloc[0]["Jumlah Data"]

                ),

            "persentase":

                0

                if tinggi.empty

                else float(

                    tinggi.iloc[0]["Persentase (%)"]

                )

        },

        "rendah": {

            "cluster":

                "-"

                if rendah.empty

                else f"Cluster {int(rendah.iloc[0]['Cluster'])}",

            "jumlah":

                0

                if rendah.empty

                else int(

                    rendah.iloc[0]["Jumlah Data"]

                ),

            "persentase":

                0

                if rendah.empty

                else float(

                    rendah.iloc[0]["Persentase (%)"]

                )

        }

    }

    return info

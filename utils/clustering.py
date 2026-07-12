import pandas as pd
from sklearn.cluster import KMeans


# =====================================================
# JALANKAN K-MEANS
# =====================================================

def run_kmeans(data):

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


# =====================================================
# TAMBAHKAN HASIL CLUSTER
# =====================================================

def add_cluster_result(df, labels):

    hasil = df.copy()

    hasil["Cluster"] = labels

    return hasil


# =====================================================
# MENENTUKAN NAMA CLUSTER OTOMATIS
# =====================================================

def add_cluster_label(df, centroid):

    hasil = df.copy()

    # Hitung total nilai centroid setiap cluster
    centroid_score = centroid.sum(axis=1)

    # Cluster dengan nilai centroid terbesar
    cluster_tinggi = centroid_score.idxmax()

    # Cluster dengan nilai centroid terkecil
    cluster_rendah = centroid_score.idxmin()

    mapping = {

        cluster_tinggi:
        "Pola Transaksi dengan Beban Pelayanan Tinggi",

        cluster_rendah:
        "Pola Transaksi dengan Beban Pelayanan Rendah"

    }

    hasil["Nama Cluster"] = hasil["Cluster"].map(mapping)

    return hasil


# =====================================================
# RINGKASAN CLUSTER
# =====================================================

def cluster_summary(df):

    summary = (

        df.groupby(

            ["Cluster", "Nama Cluster"]

        )

        .size()

        .reset_index(name="Jumlah Data")

    )

    total = summary["Jumlah Data"].sum()

    summary["Persentase (%)"] = (

        summary["Jumlah Data"]

        / total

        * 100

    ).round(2)

    return summary


# =====================================================
# STATISTIK CLUSTER
# =====================================================

def cluster_statistics(df):

    statistik = (

        df.groupby(

            ["Cluster", "Nama Cluster"]

        )[

            [

                "Total_harga",

                "Jumlah_pesanan",

                "Jumlah_jenis_menu",

                "waktu_persiapan_yang_diberikan",

                "waktu_persiapan_digunakan"

            ]

        ]

        .mean()

        .round(2)

        .reset_index()

    )

    return statistik

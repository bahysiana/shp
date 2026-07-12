import pandas as pd
from sklearn.cluster import KMeans

# =====================================================
# NAMA CLUSTER
# =====================================================

CLUSTER_LABELS = {
    0: "Pola Transaksi dengan Beban Pelayanan Tinggi",
    1: "Pola Transaksi dengan Beban Pelayanan Rendah"
}


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
# TAMBAHKAN LABEL CLUSTER
# =====================================================

def add_cluster_label(df):

    hasil = df.copy()

    hasil["Nama Cluster"] = hasil["Cluster"].map(CLUSTER_LABELS)

    return hasil


# =====================================================
# RINGKASAN CLUSTER
# =====================================================

def cluster_summary(df):

    summary = (
        df.groupby(["Cluster", "Nama Cluster"])
        .size()
        .reset_index(name="Jumlah Data")
    )

    total = summary["Jumlah Data"].sum()

    summary["Persentase (%)"] = (
        summary["Jumlah Data"] / total * 100
    ).round(2)

    return summary


# =====================================================
# STATISTIK CLUSTER
# =====================================================

def cluster_statistics(df):

    statistik = (
        df.groupby(["Cluster", "Nama Cluster"])[
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

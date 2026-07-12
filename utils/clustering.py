import pandas as pd
from sklearn.cluster import KMeans


# =====================================================
# MENJALANKAN ALGORITMA K-MEANS
# =====================================================

def run_kmeans(data):
    """
    Menjalankan proses K-Means Clustering.

    Parameters
    ----------
    data : DataFrame
        Dataset hasil preprocessing.

    Returns
    -------
    model : KMeans
    labels : ndarray
    centroid : DataFrame
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


# =====================================================
# MENAMBAHKAN HASIL CLUSTER
# =====================================================

def add_cluster_result(df, labels):
    """
    Menambahkan nomor cluster ke dataset asli.
    """

    hasil = df.copy()

    hasil["Cluster"] = labels

    return hasil


# =====================================================
# MENENTUKAN NAMA CLUSTER OTOMATIS
# =====================================================

def add_cluster_label(df, centroid):
    """
    Memberikan nama cluster berdasarkan
    total nilai centroid.

    Cluster dengan centroid terbesar
    dianggap sebagai Beban Pelayanan Tinggi.
    """

    hasil = df.copy()

    # ---------------------------------------
    # Hitung total nilai centroid
    # ---------------------------------------

    centroid_score = centroid.sum(axis=1)

    # ---------------------------------------
    # Tentukan cluster tinggi & rendah
    # ---------------------------------------

    cluster_tinggi = centroid_score.idxmax()

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
    """
    Menampilkan jumlah data
    pada masing-masing cluster.
    """

    summary = (

        df.groupby(
            ["Cluster", "Nama Cluster"]
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


# =====================================================
# STATISTIK CLUSTER
# =====================================================

def cluster_statistics(df):
    """
    Menghitung nilai rata-rata
    setiap variabel pada masing-masing cluster.
    """

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


# =====================================================
# MENGAMBIL INFORMASI CLUSTER
# =====================================================

def get_cluster_information(summary):
    """
    Mengambil informasi Cluster Tinggi
    dan Cluster Rendah untuk ditampilkan
    pada halaman Clustering maupun PDF.
    """

    tinggi = summary[
        summary["Nama Cluster"] ==
        "Pola Transaksi dengan Beban Pelayanan Tinggi"
    ]

    rendah = summary[
        summary["Nama Cluster"] ==
        "Pola Transaksi dengan Beban Pelayanan Rendah"
    ]

    info = {

        "tinggi": {

            "cluster":

                "-" if tinggi.empty
                else f"Cluster {tinggi.iloc[0]['Cluster']}",

            "jumlah":

                0 if tinggi.empty
                else int(tinggi.iloc[0]["Jumlah Data"]),

            "persentase":

                0 if tinggi.empty
                else float(tinggi.iloc[0]["Persentase (%)"])

        },

        "rendah": {

            "cluster":

                "-" if rendah.empty
                else f"Cluster {rendah.iloc[0]['Cluster']}",

            "jumlah":

                0 if rendah.empty
                else int(rendah.iloc[0]["Jumlah Data"]),

            "persentase":

                0 if rendah.empty
                else float(rendah.iloc[0]["Persentase (%)"])

        }

    }

    return info

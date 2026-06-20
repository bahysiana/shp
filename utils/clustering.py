import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# =====================================================
# ELBOW METHOD
# =====================================================

def elbow_method(data, max_k=10):

    wcss = []

    for k in range(1, max_k + 1):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(data)

        wcss.append(model.inertia_)

    return pd.DataFrame({
        "K": range(1, max_k + 1),
        "WCSS": wcss
    })


# =====================================================
# JALANKAN K-MEANS
# =====================================================

def run_kmeans(data):

    model = KMeans(
        n_clusters=3,
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
# SILHOUETTE SCORE
# =====================================================

def calculate_silhouette(data, labels):

    return silhouette_score(data, labels)


# =====================================================
# TAMBAHKAN HASIL CLUSTER
# =====================================================

def add_cluster_result(df, labels):

    hasil = df.copy()

    hasil["cluster"] = labels

    return hasil


# =====================================================
# LABEL CLUSTER OTOMATIS
# =====================================================

def add_cluster_label(df):

    hasil = df.copy()

    # Hitung rata-rata jumlah pesanan setiap cluster
    ranking = (
        hasil.groupby("cluster")["Jumlah_pesanan"]
        .mean()
        .sort_values()
    )

    urutan_cluster = ranking.index.tolist()

    mapping = {
        urutan_cluster[0]: "Pola Pemesanan Personal",
        urutan_cluster[1]: "Pola Pemesanan Reguler",
        urutan_cluster[2]: "Pola Pemesanan Kelompok"
    }

    hasil["Label"] = hasil["cluster"].map(mapping)

    return hasil


# =====================================================
# RINGKASAN CLUSTER
# =====================================================

def cluster_summary(df):

    return (
        df.groupby("Label")
        .size()
        .reset_index(name="Jumlah Data")
    )


# =====================================================
# STATISTIK CLUSTER
# =====================================================

def cluster_statistics(df):

    return (
        df.groupby("Label")[
            [
                "Total_harga",
                "Jumlah_pesanan",
                "rata_rata_harga",
                "waktu_persiapan_digunakan"
            ]
        ]
        .mean()
        .round(2)
        .reset_index()
    )


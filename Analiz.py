import pandas as pd
import matplotlib.pyplot as plt 
import folium
df = pd.read_csv("deprem_son24saat_duzenli.csv")

# Türkiye merkez koordinatı
harita= folium.Map(location=[39.0,35.0],zoom_start=6)

for i in range(len(df)):

    enlem= df.iloc[i]["Enlem"]
    boylam = df.iloc[i]["Boylam"]
    buyukluk = df.iloc[i]["Buyukluk"]
    yer = df.iloc[i]["Yer"]

    folium.CircleMarker(
        location=[enlem , boylam],
        radius=buyukluk *1.5, #büyüklüğe göre boyut
        popup=f"{yer}-{buyukluk}",
        color="red",
        fill=True,
        fill_color = "red"
    ).add_to(harita)

harita.save("deprem_haritasi.html")



# genel bilgi 
print(df.info())
"""

-> veri temizleme işlemi :

#eksik verileri kontrol et 
print("\nEksik veri sayisi:")
print(df.isnull)

#eksik verileri sil
df = df.dropna()

print("\nTemizlendikten sonra veri sayisi:",len(df))
"""

#DEPREM BÜYÜKLÜĞÜ ANALİZİ:

print("\nDeprem büyüklüğü istatistikleri:")

print("ortalama:",df["Buyukluk"].mean())

print("En büyük:",df["Buyukluk"].max())

print("En küçük:",df["Buyukluk"].min())

print("Medyan:",df["Buyukluk"].median())



print("\nDeprem kategorileri:")

print("4+ deprem sayısı:", len(df[df["Buyukluk"] >= 4]))

print("5+ deprem sayısı:", len(df[df["Buyukluk"] >= 5]))

print("6+ deprem sayısı:", len(df[df["Buyukluk"] >= 6]))

print("7+ deprem sayısı:", len(df[df["Buyukluk"] >= 7]))

"""df["Kategori"] = pd.cut(df["Buyukluk"],
                        bins=[0, 4, 5, 6, 10],
                        labels=["Küçük", "Orta", "Büyük", "Çok Büyük"])

print(df["Kategori"].value_counts())
"""



buyuk_depremler =df[df["Buyukluk"]>= 4]
print("\n4'dan büyük deprem sayisi:",len(buyuk_depremler))

print("\nhistogram grafiği:")
plt.hist(df["Buyukluk"],bins =30)
plt.title("deprem büyüklük dağilimi:")
plt.xlabel("büyüklük")
plt.ylabel("deprem sayisi")

plt.show()


# En büyük 10 deprem
en_buyuk_10 = df.sort_values("Buyukluk", ascending=False).head(10)

print("\nEn büyük 10 deprem:")
print(en_buyuk_10[["Buyukluk","Yer"]])

plt.bar(range(10),en_buyuk_10["Buyukluk"])

plt.title("En büyük 10 deprem")
plt.xlabel("Deprem")
plt.ylabel("Büyüklük")

plt.show()


#Türkiye’de nerede daha çok deprem var?
print("\nEn çok deprem olan yerler:")
print(df["Yer"].value_counts().head(10))

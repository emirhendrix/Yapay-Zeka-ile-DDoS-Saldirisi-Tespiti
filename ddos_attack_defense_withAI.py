#Gerekli Kütüphanelerin Eklenmesi
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veri setini yükleme
# DDoS saldırısı tespiti için kullanılan ağ trafiği veri seti
data = pd.read_csv("network_traffic.csv")

# 2. Özellikler ve hedefi belirleme
X = data.drop('attack', axis=1)  # Özellikler (IP, Protokol, Paket Sayısı, vb.)
y = data['attack']  # Hedef değişken (1 = Saldırı, 0 = Normal trafik)

# 3. Veriyi ölçeklendirme
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Eğitim ve test setine ayırma
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 5. Random Forest modelini oluşturma ve eğitme
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Test verisi ile tahmin yapma
y_pred = model.predict(X_test)

# 7. Modelin performansını değerlendirme
accuracy = accuracy_score(y_test, y_pred)
print("Model Doğruluk Oranı: {:.2f}%".format(accuracy * 100))

# 8. Karmaşa Matrisi
conf_matrix = confusion_matrix(y_test, y_pred)
print("Karmaşa Matrisi:\n", conf_matrix)

# 9. Sınıflandırma Raporu
print("Sınıflandırma Raporu:\n", classification_report(y_test, y_pred))

# 10. Karmaşa Matrisini Görselleştirme
plt.figure(figsize=(6,4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title("Karmaşa Matrisi")
plt.ylabel('Gerçek Değerler')
plt.xlabel('Tahmin Edilen Değerler')
plt.show()

# 11. Precision, Recall ve F1-Skoru Görselleştirme
report = classification_report(y_test, y_pred, output_dict=True)
metrics_df = pd.DataFrame(report).transpose()

metrics_df[['precision', 'recall', 'f1-score']].plot(kind='bar', figsize=(10,6))
plt.title('Precision, Recall ve F1-Skoru')
plt.show()

# Yapay Zeka ile DDoS-Saldırısı Tespiti

Bu proje, Yapay Zeka kullanarak siber saldırı tespiti işlemlerini kolaylaştırmak,  saldırıları  kontrol etmek ve saldırı engelleme sürecini otomatikleştirmek amacıyla geliştirilmiş bir projedir.

## **Projenin Özellikleri**

* AI sistemleri, büyük veri setlerini hızla analizederek, insan analistlerin tespit etmekte zorlanacağı tehditleri kısa sürede fark edebiliyor.
  
*  Tehdit tespitinde kullanılan yapay zeka algoritmaları, makine öğrenmesi ve derin öğrenme teknikleriyle ağ trafiği, kullanıcı davranışları ve sistem loglarını arayarak anomali ve saldırı girişimlerini tespit ediyor.
  
*  Yapay Zeka ile  DDoS (Dağıtık Hizmet Reddi Saldırısı)  tespitinin tahmin doğruluğu oldukça yüksektir. Tahmin doğruluğu ortalama olarak  %95, %98'tir.

## **Veri Seti Özellikleri**

* **Ağ Trafik Verisi:**
  - DDoS saldırısı ve normal trafik davranışlarını içeren ağ paket verileri kullanılır. Bu veriler genellikle aşağıdaki özellikleri içerir:

* **IP Adresleri:**
  - Kaynak ve hedef IP bilgileri.

* **Paket Sayısı:**
  - Belirli zaman dilimlerinde gelen paket miktarı.

* **Protokoller:**
  - Kullanılan ağ protokolleri (TCP, UDP vs.).

* **Bağlantı Süresi:**
  - Bağlantının ne kadar sürdüğü.

* **Bant Genişliği:**
  - Trafiğin yarattığı veri hacmi.


## **Kullanılan ve Kullanılabilecek Teknolojiler**

## 1. **Makine Öğrenimi ve Yapay Zeka**

* **Python:**
  -  Bu proje için en yaygın kullanılan programlama dili. Geniş bir yapay zeka ve makine öğrenimi ekosistemine sahip.
 
* **Scikit-learn:**
  -   Makine öğrenimi için temel algoritmaların bulunduğu Python kütüphanesi. Random Forest, Support Vector Machines (SVM), Decision Tree gibi DDoS tespiti için kullanılacak algoritmalar burada bulunur.
 
* **TensorFlow veya PyTorch:**
  - Derin öğrenme algoritmaları kullanılarak daha karmaşık DDoS saldırılarını tespit etmek için kullanılabilecek frameworkler. Sinir ağı modelleri ve büyük veri setlerini işlemek için uygundur.

* **Keras**
  - TensorFlow üzerine kurulmuş, kolay ve hızlı derin öğrenme modelleri geliştirmek için kullanılan bir kütüphane.

## 2. **Veri İşleme ve Analiz Teknolojileri**

* **Pandas:**
  - Veri manipülasyonu ve analiz için kullanılan Python kütüphanesi. Büyük ağ trafiği veri setlerini temizleme ve dönüştürme işlemlerinde kullanılır.

* **Numpy:**
  - Matematiksel hesaplamalar ve çok boyutlu diziler ile veri işleme için kullanılır. Özellikle büyük veri kümelerinin hızlı işlenmesini sağlar.

* **Matplotlib ve Seaborn**
  - Veri görselleştirme için kullanılan Python kütüphaneleri. Saldırıların grafiksel olarak görselleştirilmesi ve ağ trafiği analizlerinin gösterimi için kullanılır.

## 3. **Veri Tabanı ve Büyük Veri Depolama**

* **SQL/NoSQL Veritabanları:**
  - MySQL veya PostgreSQL gibi SQL veritabanları, daha yapılandırılmış ve ilişkisel veri tabanı ihtiyaçları için kullanılabilir.

## 4. **Gerçek Zamanlı Veri İşleme**
**Apache Kafka:** 
 - Gerçek zamanlı veri akışı ve olay işleme için kullanılır. Büyük ölçekli ağ trafiği verilerini toplar ve analiz için dağıtır.

**Apache Flink:** 
 - Gerçek zamanlı veri işleme motoru. Anormal ağ trafiği davranışlarının tespiti için kullanılabilir.

**Wireshark:**
 - Gerçek zamanlı olarak ağ trafiğini izlemek ve DDoS saldırılarını analiz etmek için kullanılan bir araç.

## 5. **Ağ Güvenliği ve İletişim Protokolleri**

**Suricata veya Snort:** 
- Açık kaynaklı ağ izleme ve saldırı tespit sistemleri (IDS/IPS). Ağ trafiğindeki anormal aktiviteleri izler ve raporlar. Yapay zeka tabanlı sistemlerin sonuçlarını değerlendirmek için kullanılabilir.

**Zeek:** 
- Ağ güvenliği izleme aracı. Ağ trafiğindeki anormal aktiviteleri ve saldırı girişimlerini tespit eder.

## 6. Bulut Teknolojileri ve Dağıtık Sistemler

**AWS (Amazon Web Services), Microsoft Azure veya Google Cloud:** 
- DDoS saldırı tespiti için bulut platformları kullanılabilir.
- Bu platformlar, büyük veri setlerinin işlenmesi, makine öğrenimi modellerinin eğitilmesi ve dağıtık veri analizi için kaynak sağlar.


## 7. Güvenlik Araçları ve Uygulamaları

**Firewall ve IPS/IDS Sistemleri:** 
- AI tabanlı DDoS saldırı tespitini mevcut güvenlik altyapısıyla entegre etmek için kullanılır. Örneğin, bir yapay zeka modeli anormal bir trafiği tespit ettiğinde, firewall sistemi bu trafiği engelleyebilir.
**Cloudflare veya Akamai:**
  - DDoS koruma hizmetleri sunan platformlar. AI tabanlı modeller ile gerçek zamanlı entegre çalışabilirler.
 
## 8. Performans ve Değerlendirme Araçları

**Scikit-learn'in Model Değerlendirme Araçları:**
- Doğruluk, hassasiyet, özgüllük gibi metrikler ile makine öğrenimi modellerinin performansı değerlendirilir.
  
  **TensorBoard:**
   - TensorFlow modellerinin performansını izlemek ve görselleştirmek için kullanılan bir araç.

**Bu teknolojiler, yapay zeka ile DDoS saldırı tespit projesinin temel yapı taşlarını oluşturur ve başarılı bir şekilde çalışmasını sağlar.**


## **Model Mantığı**

**Denetimli Öğrenme:** 
 - Yapay zeka modeli, normal ve anormal (DDoS saldırısı) ağ trafiğini sınıflandırmak için eğitilir.
   
**Özellik Seçimi:**
 - Model, trafiğin çeşitli özelliklerini (örneğin, paket sıklığı, trafiğin kaynak ve hedef noktaları) kullanarak karar verir.

 ## **Model Nasıl Oluşturulur ?**

 **Veri Ön İşleme**
  -  Veriler temizlenir, eksik veya hatalı veriler düzeltilir. Veri seti normalleştirilir, ağ trafiği genellikle çok büyük ölçeklerde olduğu için bu adım önemlidir.
    
 **Özellik Seçimi**
  -  Trafiğin analiz edilebilmesi için gerekli olan önemli özellikler seçilir. Ağırlıklı olarak paket sayısı, veri miktarı, bağlantı süresi, hedef portu ve 
 protokoller gibi veriler dikkate alınır.

**Model Eğitimi:**
 - Eğitim veri seti üzerinde modelin performansı test edilerek, algoritmalar arasından en uygun olanı seçilir.

**Test ve Doğrulama:** 
 - Eğitilen model, saldırı veri setleri üzerinde test edilerek doğruluk, duyarlılık (saldırıları tespit etme oranı), kesinlik gibi metriklerle değerlendirilir.

## **Modelimi Random Forest olarak seçtim ve eğittim**

**Random Forest**, bir topluluk öğrenme  yöntemidir ve birçok karar ağacından oluşur.

## **Modeli Neden Random Forest seçtik ?**
**Yüksek Doğruluk:** 
- Birden fazla karar ağacını birleştirerek overfitting (aşırı uyum) riskini azaltır.

 **Çok Yönlülük:**
 - Random Forest, hem sınıflandırma hem de regresyon görevlerinde kullanılabilir. DDoS saldırı tespitinde, modelin sınıflandırma yetenekleri kullanılarak gelen ağ trafiğinin normal mi yoksa saldırı mı olduğu tespit edilebilir.

**Veri Setindeki Dengesizliklere Karşı Dayanıklılık:**
- Gerçek dünyadaki veri setlerinde, özellikle güvenlik alanında, saldırı verileri genellikle nadirdir ve dengesiz bir dağılıma sahip olabilir. Random Forest, sınıflar arasındaki bu dengesizliklere karşı oldukça dayanıklıdır ve küçük sınıfların (örneğin saldırı verilerinin) doğru bir şekilde tespit edilmesine olanak tanır.

**Özellik Seçimi ve Önem Düzeyi:**
- Random Forest, modelin hangi özelliklerin (örneğin ağ trafiği verisindeki belirli parametrelerin) daha önemli olduğunu doğal olarak belirleyebilir. Özelliklerin önem derecesini hesaplama yeteneği, modelin hangi özelliklerin DDoS saldırılarını tespit etmek için en etkili olduğunu öğrenmesini sağlar.

**Paralel Çalışabilirlik:**
- Random Forest algoritması, ağaçların paralel olarak eğitilmesine olanak tanır. Bu da büyük veri setleri üzerinde daha hızlı model eğitimi sağlar. DDoS saldırıları genellikle büyük miktarda veri üretir, bu yüzden paralel işleme kabiliyeti önemli bir avantajdır.

## Projenin Kullanım Alanları

**Kritik Bakanlıklar**

**Bankacılık ve Finansal Kurumlar**

**Savunma Sanayi Şirketleri ve Fabrikaları**

***Bankacılık ve Finansal Kurumlar**

**E-ticaret Platformları**

**Hükümet ve Kamu Sektörü**

**Telekomünikasyon Şirketleri**


## **Notlar**
- Sistemi geliştirmek veya farklı özellikler eklemek için  örnek bir açık kaynak kod yapısı kullanılmıştır.


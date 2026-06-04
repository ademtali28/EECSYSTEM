import streamlit as st
import os
import random

# Sayfa Genişlik ve Başlık Ayarı
st.set_page_config(page_title="EEC SYSTEM", layout="centered")

# PREMIUM VE NOKTA ATIŞI CSS AYARLARI
st.markdown("""
    <style>
    /* Ana Ekran Arka Planı */
    .stApp { background-color: #0A0F1D; }
    
    /* Başlık Tasarımları */
    .main-title { color: #FFFFFF; font-size: 48px; font-weight: 900; text-align: center; letter-spacing: 4px; font-family: 'Segoe UI', sans-serif; margin-top: 20px; margin-bottom: 5px; }
    .sub-title { color: #38BDF8; font-size: 13px; text-align: center; letter-spacing: 6px; font-family: 'Segoe UI', sans-serif; margin-bottom: 40px; text-transform: uppercase; }
    
    /* ULTRA PREMIUM ARAMA MOTORU */
    div[data-testid="stTextInput"] input {
        background-color: #111827 !important;
        border: 2px solid #1F2937 !important;
        border-radius: 14px !important;
        padding: 20px 24px !important; 
        color: #FFFFFF !important;
        font-size: 18px !important; 
        font-weight: 500 !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.6) !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.35) !important;
        background-color: #151F32 !important;
    }
    
    /* Streamlit'in kendi border'lı container'ı */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(135deg, #151F32 0%, #0F172A 100%) !important;
        border: 1px solid #22314D !important;
        border-top: 4px solid #10B981 !important;
        border-radius: 14px !important;
        padding: 25px !important;
        box-shadow: 0 12px 30px rgba(0,0,0,0.5) !important;
        margin-top: 25px !important;
        margin-bottom: 25px !important;
    }
    
    .arac-baslik-entegre { 
        font-weight: 800; 
        font-size: 14px; 
        color: #10B981; 
        letter-spacing: 2px; 
        margin-bottom: 15px; 
        text-align: center; 
        text-transform: uppercase;
        font-family: 'Segoe UI', sans-serif;
    }

    /* GİZLİ LABELLAR VE GEREKSİZ BOŞLUKLARIN TEMİZLİĞİ */
    div[data-testid="stSelectbox"] label { display: none !important; height: 0px !important; margin: 0 !important; padding: 0 !important; }
    div[data-testid="stSelectbox"] { margin-top: 0px !important; margin-bottom: 0px !important; padding-top: 0px !important; }
    .stBlockContainer { padding-top: 2rem !important; }

    /* SAHA PRATİK BİLGİ NOTU KARTI */
    .saha-ipucu-kart {
        background: linear-gradient(90deg, rgba(16, 185, 129, 0.08) 0%, rgba(15, 23, 42, 0.6) 100%);
        border: 1px dashed rgba(16, 185, 129, 0.3);
        border-left: 4px solid #10B981;
        padding: 16px 20px;
        border-radius: 10px;
        margin-top: 5px;
        margin-bottom: 25px;
        color: #E5E7EB;
        font-size: 13.5px;
        line-height: 1.6;
    }
    .saha-ipucu-vurgu { color: #10B981; font-weight: bold; text-transform: uppercase; font-size: 12px; letter-spacing: 1px; display: block; margin-bottom: 5px; }

    /* SADELEŞTİRİLMİŞ ALTYAPI ŞERİTLERİ */
    .serit-kart {
        background: linear-gradient(90deg, #151F32 0%, #111827 100%);
        border: 1px solid #22314D;
        border-left: 4px solid #38BDF8;
        padding: 20px 24px;
        border-radius: 10px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }
    .serit-kart:hover {
        border-left-color: #38BDF8;
        background: linear-gradient(90deg, #1E293B 0%, #151F32 100%);
        transform: translateX(4px);
        box-shadow: 0 5px 15px rgba(56, 189, 248, 0.1);
    }
    .serit-sol { display: flex; align-items: center; gap: 18px; }
    .serit-ikon { font-size: 22px; display: flex; align-items: center; justify-content: center; }
    .serit-baslik { color: #FFFFFF; font-size: 15.5px; font-weight: 700; letter-spacing: 0.5px; font-family: 'Segoe UI', sans-serif; }

    /* TAM SAYFA PREMIUM ARIZA MÜDAHALE İSTASYONU KARTI */
    .premium-ariza-ekran {
        background: linear-gradient(145deg, #1E1B4B 0%, #0F172A 100%);
        border: 1px solid #312E81;
        border-left: 6px solid #EF4444;
        padding: 30px;
        border-radius: 14px;
        color: #F3F4F6;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        margin-top: 10px;
    }
    .premium-ariza-baslik { color: #FCA5A5; font-weight: 800; font-size: 22px; margin-bottom: 18px; border-bottom: 1px solid #312E81; padding-bottom: 12px; letter-spacing: 0.5px; }
    .premium-ariza-alt { font-size: 15.5px; color: #E5E7EB; margin-bottom: 18px; line-height: 1.7; }
    .premium-ariza-aksiyon-kutu { background-color: #0A0F1D; border: 1px solid #1E293B; padding: 18px; border-radius: 10px; margin-top: 20px; border-left: 4px solid #34D399; }
    .premium-ariza-aksiyon-baslik { color: #34D399; font-weight: 700; font-size: 15px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 1px; }

    .vurgu-mavi { color: #38BDF8; font-weight: bold; }
    .vurgu-yesil { color: #10B981; font-weight: bold; }

    /* Expander Tasarımları */
    div[data-testid="stExpander"] { background-color: #151F32 !important; border: 1px solid #22314D !important; border-radius: 8px !important; margin-bottom: 15px !important; overflow: hidden !important; }
    div[data-testid="stExpander"] summary { background-color: #1E293B !important; padding: 14px 18px !important; color: #FFFFFF !important; }
    div[data-testid="stExpander"] summary p { color: #FFFFFF !important; font-weight: 700 !important; font-size: 15.5px !important; }
    div[data-testid="stExpander"] summary svg { fill: #38BDF8 !important; }
    div[data-testid="stExpanderDetails"] { background-color: #0F172A !important; padding: 20px !important; border-top: 1px solid #1E293B !important; }
    
    .saha-detay-metin { color: #38BDF8 !important; font-size: 15px !important; font-weight: 600 !important; line-height: 1.6 !important; }
    .saha-liste-item { color: #F3F4F6 !important; font-size: 14.5px !important; line-height: 1.7 !important; margin-bottom: 12px; }
    .saha-cozum-item { color: #34D399 !important; font-size: 15px !important; line-height: 1.7 !important; margin-bottom: 10px; font-weight: 600; }
    .kilavuz-baslik { color: #38BDF8; font-size: 16px; font-weight: 700; margin-top: 25px; margin-bottom: 15px; border-left: 4px solid #38BDF8; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)


# 📂 GELİŞMİŞ ÇOKLU GÖRSEL VE PDF BULUCU FONKSİYON
def find_all_images_and_pdfs(keyword):
    folder = "kilavuzlar"
    gorseller = []
    pdf_ler = []
    
    if not os.path.exists(folder):
        return gorseller, pdf_ler
        
    for file in os.listdir(folder):
        name_lower = file.lower()
        if keyword.lower() in name_lower:
            full_path = os.path.join(folder, file)
            if name_lower.endswith(('.png', '.jpg', '.jpeg')):
                gorseller.append(full_path)
            elif name_lower.endswith('.pdf'):
                pdf_ler.append(full_path)
                
    gorseller.sort()
    pdf_ler.sort()
    return gorseller, pdf_ler


# DİRENÇ RENK KODU SÖZLÜKLERİ
RENK_DEGERLERI = {"Siyah": 0, "Kahverengi": 1, "Kırmızı": 2, "Turuncu": 3, "Sarı": 4, "Yeşil": 5, "Mavi": 6, "Mor": 7, "Gri": 8, "Beyaz": 9}
RENK_CARPANLARI = {"Siyah": 1, "Kahverengi": 10, "Kırmızı": 100, "Turuncu": 1000, "Sarı": 10000, "Yeşil": 100000, "Mavi": 1000000}
RENK_TOLERANSLAR = {"Altın": "±5%", "Gümüş": "±10%", "Kahverengi": "±1%", "Kırmızı": "±2%"}

# SAHA PRATİK BİLGİ VERİLERİ
SAHA_IPUCLARI = [
    {"baslik": "Edwards Loop Direnç Standartları", "icerik": "İzleme modülleri (CT1/CT2) ve kontrol modülleri standart olarak <b>47 kΩ</b> hat sonu denetim direnci kullanır. Eski nesil konvansiyonel bölgelerde ise <b>4.7 kΩ</b> veya <b>10 kΩ</b> direnç değerleri aranır."},
    {"baslik": "SDU Yazılım & Kural Düzenleme Mantığı", "icerik": "Edwards SDU kural editöründe çift girişli cihaz yazarken fiziksel modül adresinin sonuna Input 1 için <b>'.1'</b> (Örn: 0102005.1), Input 2 için ise <b>'.2'</b> uzantı kodunu eklemeyi unutmayın."},
    {"baslik": "Loop Voltaj Kontrolü Teşhis Adımı", "icerik": "Edwards panellerinde sağlıklı haberleşme için Loop kartı çıkış uçlarında tam yüklü durumda DC voltajın <b>19.5V - 21V</b> aralığında stabil olduğunu multimetre ile doğrulayın."},
    {"baslik": "SIGA-REL Çoklu Mantıksal Adres Yapısı", "icerik": "SIGA-REL modülü tek bir fiziksel adrese sahip gibi görünse de SDU yazılımı arka planda Abort girişi, Manuel tetikleme ve Solenoid çıkışları için **ayrı ayrı mantıksal alt adresler** üretir."}
]

# DETAYLI VE DEEP REHBER VERİ TABANI
HİBRİT_DB = {
    "siga_sb": {
        "anahtar_kelimeler": ["sb", "siga-sb", "soket", "detektör tabanı", "dedektör soketi", "duman dedektörü", "isi dedektörü", "kombine dedektör"],
        "tip": "cihaz",
        "baslik": "SIGA-SB Standart Detektör Soketi Klemens Analizi",
        "detay": "Signature Serisi akıllı dedektörlerin loop haberleşme (SLC) hattına bağlanmasını sağlayan standart sokettir. Elektriksel denetim sürekliliği için saha kablolarının klemens girişlerinde kesilerek bağlanması zorunludur.",
        "kullanim_alanlari": [
            "<b>Noktasal Tip Algılama:</b> Adresli noktasal tip duman (SMK), kombine (PHS) ve ısı (HRS/HFS) dedektörlerinin loop hattı altyapısında kullanılır.",
            "<b>SIGA-LED Desteği:</b> Alarm durumunda asma tavan veya oda dışından yangın hücresinin kolayca fark edilmesini sağlayan harici indikatör çıkış bağlantısı sunar."
        ],
        "cozumler": [
            "<b>Klemens 1:</b> Kullanılmaz / Boş Terminal.",
            "<b>Klemens 2:</b> SLC IN/OUT (+) Pozitif Çevrim Hat Giriş ve Çıkış Ucu.",
            "<b>Klemens 3:</b> Kullanılmaz / Boş Terminal.",
            "<b>Klemens 4:</b> SLC IN (-) Önceki Cihazdan Gelen Negatif Hat Girişi & Uzaktan Kumandalı LED (-) Çıkışı.",
            "<b>Klemens 5:</b> Remote LED (+) İndikatör Pozitif Çıkış Kutbu.",
            "<b>Klemens 7:</b> SLC OUT (-) Sonraki Cihaza Devam Eden Negatif Çevrim Çıkış Ucu."
        ],
        "search_key": "sb"
    },
    "siga_ib": {
        "anahtar_kelimeler": ["siga-ib", "izolatörlü soket", "izolatorlu taban"],
        "tip": "cihaz",
        "baslik": "SIGA-IB İzolatörlü Detektör Tabanı Klemens Analizi",
        "detay": "Class A mimariye sahip yangın döngülerinde meydana gelebilecek bir kısa devre hatasını 23 ms içinde izole ederek hattın geri kalanını koruyan dahili hat izolatörlü özel dedektör tabanıdır. Üzerinde dedektör başlığı olmadan çalışmaz.",
        "kullanim_alanlari": [
            "<b>Class A Çevrim Koruması:</b> Loop hatlarında oluşabilecek kısa devre arızalarının tüm hattı çökertmesini engellemek amacıyla kat geçiş noktalarında veya yangın zon sınırlarında konumlandırılır."
        ],
        "cozumler": [
            "<b>Klemens 1:</b> SLC IN (+) Önceki Cihazdan Gelen Pozitif Hat Girişi.",
            "<b>Klemens 2:</b> SLC OUT (+) Sonraki Cihaza Devam Eden Hat Pozitif Çıkışı.",
            "<b>Klemens 4:</b> SLC IN (-) Önceki Cihazdan Gelen Çevrim Negatif Hat Girişi.",
            "<b>Klemens 7:</b> SLC OUT (-) Sonraki Cihaza Devam Eden Çevrim Negatif Hat Çıkışı."
        ],
        "search_key": "ib"
    },
    "siga_um": {
        "anahtar_kelimeler": ["um", "siga-um", "universal modül", "evrensel modül", "konvansiyonel zon", "davlumbaz söndürme", "pre-action vana"],
        "tip": "cihaz",
        "baslik": "SIGA-UM / SIGA-MAB Universal Class A/B Modül Analizi",
        "detay": "Edwards Signature serisinin en fonksiyonel modülüdür. Fiziksel görevi, panel yazılımından (SDU) cihaza yüklenen 'Personality Code' (Kişilik Kodu) ile yazılımsal olarak belirlenir.",
        "kullanim_alanlari": [
            "<b>Davlumbaz Söndürme Sistemleri:</b> Davlumbaz aktivasyon izlemesi, cihaz elektriğinin kesilmesi, gaz kesme vanaları ve üfleme fanlarının kapatılması senaryolarında çoklu giriş/çıkış esnekliği sağlar.",
            "<b>Pre-Action Vana Kontrolü:</b> Solenoid çıkış yönetimi, vana açık/kapalı, düşük basınç ve su akış anahtarlarının entegrasyonunda joker eleman olarak kullanılır.",
            "<b>Zon Entegrasyonu:</b> 2 telli konvensiyonel duman dedektörü hatlarının veya konvensiyonel tip duman/ısı/buton hatlarının izlenmesinde."
        ],
        "cozumler": [
            "<b>Data Loop Bağlantısı:</b> Cihazın adrese dayalı haberleşme hatt (SLC IN/OUT) modülün arka yüzeyinde yer alan ana veri klemens grubundan yapılır.",
            "<b>Hat Sonu Denetim Direnci:</b> Giriş izleme veya denetimli siren kontrolü amacıyla konfigüre edildiğinde, saha hattının bittiği en uç noktaya standart Edwards 47 kΩ direncinin paralel bağlanması zorunludur."
        ],
        "search_key": "um"
    },
    "siga_rel": {
        "anahtar_kelimeler": ["rel", "siga-rel", "söndürme modülü", "sondurme modulu", "gazlı söndürme", "solenoid sürücü", "gaz boşaldı", "fm200"],
        "tip": "cihaz",
        "baslik": "SIGA-REL Gazlı Söndürme Kontrol Modülü Entegre Teknik Analizi",
        "detay": "Çift aşamalı (Two-Stage) algılama, çapraz zon doğrulama mantığı, manuel boşaltma istasyonu takibi ve acil durum durdurma (Abort) buton girişlerini tek adreste toplayan, gazlı söndürme solenoid valflerini güvenli şekilde süren en kritik koruma elemanıdır.",
        "kullanim_alanlari": [
            "<b>Gazlı Söndürme Paneli Entegrasyonu:</b> Harici gazlı söndürme panellerinden veya doğrudan tüplerden gelecek olan 'Alarm, Arıza, Gaz Boşaldı' sinyallerinin takibinde ve solenoid tetiklemesinde tek başına tam kontrol sağlar."
        ],
        "cozumler": [
            "<b>Klemens Giriş Yapısı (TB1-TB6):</b> Adres çevrim hattı (SLC) doğrudan TB1 klemens grubuna girer. 24V DC harici besleme (Riser) hatları ilgili güç giriş klemenslerine kutuplara dikkat edilerek bağlanmalıdır.",
            "<b>Solenoid Çıkış Hat Denetimi:</b> Tetikleyici bobin hatlarının açık devre/kısa devre denetiminin sağlıklı yapılabilmesi için saha hattının en uç noktasına 47 kΩ hat sonu direncinin paralel bağlanması şarttır."
        ],
        "search_key": "rel"
    },
    "siga_cc1": {
        "anahtar_kelimeler": ["cc1", "siga-cc1", "siren modülü", "sinyal modülü", "siren", "flaşör", "acil anons"],
        "tip": "cihaz",
        "baslik": "SIGA-CC1 Sinyal / Siren Kontrol Modülü Klemens Analizi",
        "detay": "Harici güç kaynaklarından gelen 24V DC Riser besleme hattını sahaya yazılımsal kurallara göre denetimli olarak aktaran Class B (Style Y) devre mimarisine sahip sinyal modülüdür.",
        "kullanim_alanlari": [
            "<b>Siren ve Flaşör Hatları:</b> Kontrolü yapılan tüm adrese dayalı veya konvensiyonel korna, flaşörlü siren hatlarında,",
            "<b>Acil Anons Entegrasyonu:</b> Binadaki acil anons sistemlerinin anons zon sayısı kadar bölünerek tetiklenmesi amacıyla her bir tahliye zonu başına 1 adet CC1 veya uygun çıkış modülü yapısıyla entegre edilir."
        ],
        "cozumler": [
            "<b>Riser Besleme Bağlantısı:</b> Güç kaynağından gelen harici 24V DC besleme hattı modülün Riser Giriş uçlarına irtibatlandırılır.",
            "<b>Direnç Uygulaması:</b> Çıkış hattında açık devre hatası alınmaması için hattın bittiği sahadaki en son cihazın klemens uçlarına 47 kΩ Hat Sonu Direnci PARALEL olarak çakılmalıdır."
        ],
        "search_key": "cc1"
    },
    "siga_cr": {
        "anahtar_kelimeler": ["cr", "siga-cr", "röle modülü", "role modulu", "asansör", "asansor", "yürüyen merdiven", "solenoid vana", "müzik", "muzik kesilmesi", "kapı serbest", "kilitli kapı", "kayar kapı", "damper kontrol", "fan kontrol", "klima santrali"],
        "tip": "cihaz",
        "baslik": "SIGA-CR Kontrol Röle Modülü Bağlantı Analizi",
        "detay": "Saha hatlarına herhangi bir voltaj ya da besleme aktarmadan, SDU kural editöründe yazılan mantıksal senaryolara göre sadece kuru kontak konum değişimi (Form C) sunan adrese dayalı röle kontrol modülüdür.",
        "kullanim_alanlari": [
            "<b>Asansör ve Yürüyen Merdiven Kontrolü:</b> Yangın anında asansörlerin acil tahliye katına indirilmesi, yürüyen merdiven ve bantların güvenle durdurulması acil durum kontrollerinde.",
            "<b>Yangın Damper Kontrolü:</b> Havalandırma kanallarındaki motorlu yangın damperlerinin kapatılmasında. Sadece EST3 sisteminde TEK BİR CR modülü ile 'On-Off' damper kontrolü yapılabilir.",
            "<b>Fan Kontrol ve Klima Santralleri:</b> Duman egzoz fanları, basınçlandırma fanları ve klima santrallerinin (AHU) MCC panoları üzerinden start/stop kuru kontak yönetimi.",
            "<b>Geçiş Kontrol ve Kapılar:</b> Kilitli kapıların boşa düşürülmesi ve tüm acil çıkış kayar kapılarının yangın anında otomatik olarak açık duruma getirilmesi senaryolarında,",
            "<b>Sistem Entegrasyonları:</b> Doğalgaz ana solenoid vanasının kapatılması, profesyonel müzik yayının otomatik kesilmesi ve Bina Otomasyon Sistemine (BMS) durum kuru kontak sinyallerinin aktarılmayınca kullanılır."
        ],
        "cozumler": [
            "<b>Klemens Bağlantı Mantığı:</b> Kontrol edilecek harici devrenin tipine göre COM-NO (Normalde Açık) veya COM-NC (Normalde Kapalı) klemens uçları kuru kontak olarak bağlanır.",
            "<b>Önemli Direnç Kuralı:</b> Bu modül kuru kontak çıkış mantığı ile çalıştığından ve saha hat denetimi yapmadığından çıkış klemenslerinde KESİNLİKLE DİRENÇ KULLANILMAZ."
        ],
        "search_key": "cr"
    },
    "siga_ct1": {
        "anahtar_kelimeler": ["ct1", "siga-ct1", "izleme modülü", "buton", "yangın butonu", "güç kaynağı", "guck", "arıza izleme", "ariza izleme", "motorsuz damper", "eriyen telli", "deprem", "co sensör"],
        "tip": "cihaz",
        "baslik": "SIGA-CT1 Tek Girişli İzleme Modülü Analizi",
        "detay": "Sahadaki mekanik sistemlerden veya harici cihazlardan gelen tek bir kuru kontak durum bilgisini Edwards loop haberleşme hattına aktaran, Class B devre yapısına sahip tek kanallı adresli izleme modülüdür.",
        "kullanim_alanlari": [
            "<b>Buton ve Konvansiyonel Hatlar:</b> Adresli yangın ihbar butonları (271) ile konvansiyonel duman/ısı/buton hatlarının takibinde,",
            "<b>Güç Kaynağı ve Sistem Arıza İzleme:</b> Harici güç kaynaklarının (PSU) genel arıza kontakları, yangın/jokey pompalarının enerji kesik ve genel arıza durum takipleri,",
            "<b>Motorsuz Eriyen Telli Damperler:</b> Kanallardaki motorsuz, mekanik eriyen telli yangın damperlerinin konum takibinde,",
            "<b>Özel Sinyal İzlemeleri:</b> Deprem sensörlerinden gelen acil durum deprem senaryo kontaklarının sisteme aktarılmasında kullanılır."
        ],
        "cozumler": [
            "<b>Hat Denetim Mantığı:</b> İzlenecek kuru kontak cihazının çıkış ucuna ya da saha kablosunun bittiği son noktaya 47 kΩ hat sonu direnci PARALEL bağlanmalıdır. Kontak açıkken hat direnç üzerinden denetlenir; kontak kapandığında yangın/aktivasyon sinyali üretilir."
        ],
        "search_key": "ct1"
    },
    "siga_ct2": {
        "anahtar_kelimeler": ["ct2", "siga-ct2", "çift girişli izleme", "cift girisli", "akış anahtarı", "flow switch", "kelebek vana", "pompa odası", "su deposu", "jeneratör", "damper geri besleme", "jet fan"],
        "tip": "cihaz",
        "baslik": "SIGA-CT2 Çift Girişli İzleme Modülü Analizi",
        "detay": "Tek bir fiziksel donanım adresi işgal ederek, birbirinden tamamen bağımsız iki farklı kuru kontak durum bilgisini aynı anda Edwards loop hattına aktarabilen çift kanallı akıllı izleme modülüdür.",
        "kullanim_alanlari": [
            "<b>Akış Anahtarı & Kelebek Vana:</b> Her Flow Switch (FS) ve Kelebek Vana (KV) grubu için 1 adet 2'li giriş modülü (CT2) kullanılarak vana konum bilgisi ile su akış alarmı tek noktadan izlenir.",
            "<b>Pompa Odası Komple İzleme:</b> Pompa odasındaki tüm izlenebilir vanalar, su deposu düşük seviye alarmı, acil durum jeneratörü çalıştı bilgisi gibi çoklu mekanik veriler CT2 modülleriyle gruplanarak panele taşınır.",
            "<b>Motorlu Damper Geri Besleme:</b> Havalandırma kanallarında yer alan motorlu yangın damperlerinin 'Açık' ve 'Kapalı' olmak üzere 2 farklı konum bilgisinin eş zamanlı takibinde,",
            "<b>Jet Fan ve Karbonmonoksit (CO) Yönetimi:</b> Her CO zonu için 1. seviye ve 2. seviye alarm izlemeleri ile jet fan sistemlerinin genel arıza geri bildirim kontaklarının takibinde üstün rol oynar."
        ],
        "cozumler": [
            "<b>Klemens ve Yazılım Eşleşmesi:</b> Kılavuz şemasına göre Input 1 and Input 2 giriş hatları ayrı ayrı sonlandırılır. SDU yazılımında kural yazılırken birinci giriş '.1', ikinci giriş '.2' mantıksal alt adresiyle çağrılmalıdır.",
            "<b>Direnç Standartı:</b> Her iki giriş hattının da kendi içinde bağımsız denetlenebilmesi için, her hattın en sonuna ayrı ayrı 47 kΩ denetim direnci PARALEL olarak bağlanmalıdır."
        ],
        "search_key": "ct2"
    },
    "siga_hdt": {
        "anahtar_kelimeler": ["hdt", "siga-hdt", "arıza bulucu", "test cihazı", "haritalama"],
        "tip": "cihaz",
        "baslik": "SIGA-HDT Elde Taşınabilir Loop Tanılama ve Arıza Tespit Cihazı",
        "detay": "Edwards Signature serisi loop hatlarında meydana gelen donanımsal karmaşaları, cihaz kirlilik oranlarını, kablolama hatalarını ve topoloji haritasını analiz eden bağımsız el terminalidir.",
        "kullanim_alanlari": [
            "<b>Loop Devreye Alma & Bakım:</b> Sahadaki döngüde bulunan tüm aktif cihazların listelenmesi, adres çakışmalarının bulunması, kirlilik yüzdelerinin okunması ve sıfır (0) adrese sahip yeni takılan modüllerin adreslenmesinde kullanılır."
        ],
        "cozumler": [
            "<b>Vector Too Big Hatası:</b> Loop haritalama esnasında cihazların aşırı akım çektiğini gösterir. Nedeni; loop hattında mekanik bir kısa devre, aşırı düşük hat direnci ya da arızalı/yanmış bir elektronik saha ekipmanıdır.",
            "<b>Vector Too Small Hatası:</b> Haritalama sırasında cihazlar yeterli akım çekemediğini belirtir. Nedeni; hat üzerinde aşırı kablo direnci, klemens gevşekliği veya kalitesiz kablo kullanımıdır.",
            "<b>CH1/CH2 Open Circuit Hatası:</b> İlgili ölçüm kanalında hat sonu (EOL) direncinin hiç bağlanmadığını veya yanlış değerde (47 kΩ harici) bağlandığını gösterir."
        ],
        "search_key": "hdt"
    },
    "open_circuit": {
        "anahtar_kelimeler": ["open", "açık devre", "acik devre", "open circuit", "kopuk"],
        "tip": "arıza",
        "baslik": "🚨 KONTROL / İZLEME MODÜLÜ - OPEN CIRCUIT (AÇIK DEVRE) ANALİZİ",
        "detay": "Saha denetim hattında fiziksel iletimin kesilmesi, gevşek klemens bağlantısı veya hat sonundaki 47 kΩ denetim direncinin hattan kopması/düşmesi durumudur.",
        "cozum": "Modül klemens vidalarını mekanik olarak sıkıştırın. Hat sonundan gelen kablo çiftini modülden ayırarak multimetre ile tam 47 kΩ değerini okuduğunuzu doğrulayın. Eğer ekranda sonsuz direnç (OL) görüyorsanız sahada kablo kopuktur veya direnç düşmüştür."
    },
    "short_circuit": {
        "anahtar_kelimeler": ["short", "kısa devre", "kisa devre", "short circuit", "ezik"],
        "tip": "arıza",
        "baslik": "🚨 KONTROL / İZLEME MODÜLÜ - SHORT CIRCUIT (KISA DEVRE) ANALİZİ",
        "detay": "Saha denetimli izleme ya da siren besleme hattına ait pozitif (+) ve negatif (-) kablo damarlarının birbiriyle doğrudan mekanik teması arızasıdır.",
        "cozum": "Saha kontrol noktalarındaki veya izleme butonlarındaki 47 kΩ direncin hatta SERİ değil, kesinlikle PARALEL bağlandığından emin olun. Saha kablosunu bölerek multimetre ile kısa devrenin yönünü bulun."
    },
    "ground_fault": {
        "anahtar_kelimeler": ["ground", "toprak", "toprak kacagi", "toprak kaçağı", "şase"],
        "tip": "arıza",
        "baslik": "🚨 EDWARDS LOOP - GROUND FAULT (TOPRAK KAÇAĞI / ŞASE) TEŞHİSİ",
        "detay": "Loop çevrim kablosunun dış izole korumasının zedelenmesi sonucunda iç iletken bakır damarın bina toprağına, metal galvaniz kablo tavasına veya nem/su sızıntısı sebebiyle şaseye kaçırması hatasıdır.",
        "cozum": "Loop hattını panel kartından tamamen ayırın. Multimetreyi megaohm kademesine alarak bina toprağı ile loop kablosunun (+) ve (-) uçları arasındaki yalıtım direncini ölçün. Hatları sahadaki klemens kutularından veya izolatörlerden ikiye bölerek şasenin hangi yönde kaldığını adım adım lokalize edin."
    }
}

# --- ANA EKRAN LOGO VE BAŞLIK ---
st.markdown('<div class="main-title">EEC SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Entegre Akıllı Altyapı Kütüphanesi</div>', unsafe_allow_html=True)

# 🔍 ARAMA MOTORU
soru = st.text_input("", placeholder="🔍 Cihaz, arıza veya mekanik ekipman girin... (Örn: kelebek vana, damper, cr, ct1, ct2, rel)", label_visibility="collapsed")
st.write("")

# --- ARAMA TETİKLENDİYSE ---
if soru:
    soru_temiz = soru.lower().strip()
    bulundu = False
    for anahtar, veri in HİBRİT_DB.items():
        if any(kelime in soru_temiz for kelime in veri["anahtar_kelimeler"]):
            if veri["tip"] == "arıza":
                html_kod = """
                    <div class="premium-ariza-ekran">
                        <div class="premium-ariza-baslik">{}</div>
                        <div class="premium-ariza-alt">
                            <strong>Saha Teşhis / Nedeni:</strong><br>{}
                        </div>
                        <div class="premium-ariza-aksiyon-kutu">
                            <div class="premium-ariza-aksiyon-baslik">🛠️ SAHA MÜDAHALE ADIMLARI</div>
                            <div style="font-size:14.5px; line-height:1.7; color:#A7F3D0;">{}</div>
                        </div>
                    </div>
                """.format(veri["baslik"], veri["detay"], veri["cozum"])
                st.markdown(html_kod, unsafe_allow_html=True)
            elif veri["tip"] == "cihaz":
                st.info(f"🎯 {veri['baslik']}")
                st.write("")
                with st.expander("🔴 MODÜL MANTIĞI & ORİJİNAL DÖKÜMAN ÖZETİ", expanded=True):
                    st.markdown(f'<div class="saha-detay-metin">{veri["detay"]}</div>', unsafe_allow_html=True)
                with st.expander("🔵 SAHADA YAYGIN KULLANIM ALANLARI & MEKANİK SENARYOLAR", expanded=True):
                    for alan in veri["kullanim_alanlari"]:
                        st.markdown(f'<div class="saha-liste-item">• {alan}</div>', unsafe_allow_html=True)

                with st.expander("🟢 DETAYLI KLEMENS BAĞLANTILARI & SAHA ADIMLARI", expanded=True):
                    for cozum in veri["cozumler"]:
                        st.markdown(f'<div class="saha-cozum-item">{cozum}</div>', unsafe_allow_html=True)
                
                # 📥 DİNAMİK KILAVUZ VE ŞEMA İNDİRME ALANI (CR, CT1, CT2 DAHİL TÜMÜ İÇİN ENTEGRE)
                st.markdown('<div class="kilavuz-baslik">📋 Teknik Şema ve Bağlantı Kılavuzları İndirme Satırları</div>', unsafe_allow_html=True)
                
                bulunan_gorseller, bulunan_pdfler = find_all_images_and_pdfs(veri["search_key"])
                
                # Görseller için indirme butonları
                if bulunan_gorseller:
                    for gorsel_yolu in bulunan_gorseller:
                        dosya_adi = os.path.basename(gorsel_yolu)
                        try:
                            with open(gorsel_yolu, "rb") as f:
                                st.download_button(
                                    label=f"📥 Şema Görselini İndir ({dosya_adi})",
                                    data=f.read(),
                                    file_name=dosya_adi,
                                    mime="image/png" if dosya_adi.lower().endswith('.png') else "image/jpeg",
                                    key=f"btn_img_{dosya_adi}",
                                    use_container_width=True
                                )
                        except Exception as e:
                            st.caption(f"⚠️ {dosya_adi} dosyası okunurken hata oluştu.")
                
                # PDF dökümanları için indirme butonları
                if bulunan_pdfler:
                    for pdf_yolu in bulunan_pdfler:
                        dosya_adi = os.path.basename(pdf_yolu)
                        try:
                            with open(pdf_yolu, "rb") as f:
                                st.download_button(
                                    label=f"📥 Orijinal PDF Kılavuzunu İndir ({dosya_adi})",
                                    data=f.read(),
                                    file_name=dosya_adi,
                                    mime="application/pdf",
                                    key=f"btn_pdf_{dosya_adi}",
                                    use_container_width=True
                                )
                        except Exception as e:
                            st.caption(f"⚠️ {dosya_adi} dosyası okunurken hata oluştu.")
                            
                if not bulunan_gorseller and not bulunan_pdfler:
                    st.markdown(f"<div style='background-color:#151F32; padding:15px; border-radius:8px; color:#9CA3AF; font-size:13px; text-align:center; border: 1px dashed #22314D;'>📂 kilavuzlar klasörüne '{veri['search_key']}' anahtar kelimesini içeren dosya ekleyerek butonları aktifleştirebilirsiniz.</div>", unsafe_allow_html=True)

            bulundu = True
            break
    if not bulundu:
        st.error("Sistem veri tabanında eşleşen cihaz kodu, mekanik ekipman veya arıza kaydı bulunamadı.")

# --- ANA SAYFA DÜZENİ (ARAMA YAPILMADIYSA) ---
else:
    with st.container(border=True):
        st.markdown('<div class="arac-baslik-entegre">🎨 DİRENÇ RENK KODU HESAPLAMA PANELİ</div>', unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            b1 = st.selectbox("", list(RENK_DEGERLERI.keys()), index=1, key="b1")   # Kahve
        with c2:
            b2 = st.selectbox("", list(RENK_DEGERLERI.keys()), index=7, key="b2")   # Mor
        with c3:
            b3 = st.selectbox("", list(RENK_CARPANLARI.keys()), index=3, key="b3")   # Turuncu
        with c4:
            b4 = st.selectbox("", list(RENK_TOLERANSLAR.keys()), index=0, key="b4") # Altın
            
        deger = (RENK_DEGERLERI[b1] * 10 + RENK_DEGERLERI[b2]) * RENK_CARPANLARI[b3]
        if deger >= 1000:
            formatli_deger = f"{deger / 1000:.1f} kΩ"
        else:
            formatli_deger = f"{deger} Ω"
            
        st.write("")
        st.success(f"⚡ **Hesaplanan Değer:** {formatli_deger} ({RENK_TOLERANSLAR[b4]})")

    if "secilen_ipucu" not in st.session_state:
        st.session_state.secilen_ipucu = random.choice(SAHA_IPUCLARI)
        
    ipucu = st.session_state.secilen_ipucu
    
    html_ipucu = """
        <div class="saha-ipucu-kart">
            <span class="saha-ipucu-vurgu">💡 {}</span>
            {}
        </div>
    """.format(ipucu["baslik"], ipucu["icerik"])
    st.markdown(html_ipucu, unsafe_allow_html=True)

    st.markdown("""
        <div class="serit-kart">
            <div class="serit-sol">
                <span class="serit-ikon">🔥</span>
                <span class="serit-baslik">Yangın Algılama & Söndürme Sistemleri</span>
            </div>
        </div>
        <div class="serit-kart">
            <div class="serit-sol">
                <span class="serit-ikon">🚪</span>
                <span class="serit-baslik">Kartlı Geçiş & Zayıf Akım Güvenlik Sistemleri</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align: center; color: #4B5563; font-size: 11px;'>EEC Entegre Akıllı Altyapı Yönetimi</p>", unsafe_allow_html=True)
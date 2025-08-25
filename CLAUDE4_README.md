# Claude 4 Sonnet Hack for Cursor

Bu script Claude 4 Sonnet modelini Cursor editöründe geliştirir.

## Özellikler

- **Token Limiti**: Claude 4 Sonnet için 200,000 token limitine çıkarır
- **Düşünce Seviyesi**: Tüm konuşmalar için "high" düşünce seviyesi ayarlar
- **UI Styling**: Claude 4 Sonnet'e "HACKED" görünümü ekler

## Kurulum ve Kullanım

### Hızlı Başlangıç (Önerilen)

**Seçenek 1: Otomatik Yönetici Hakları (En Kolay)**
1. `run_auto_admin.bat` dosyasını çift tıklayarak çalıştırın
2. Windows UAC penceresinde "Yes" butonuna tıklayın
3. Script otomatik olarak Cursor dosyasını bulacak ve değişiklikleri uygulayacak
4. Cursor'ı yeniden başlatın

**Seçenek 2: Manuel Yönetici Hakları**
1. `run_admin.bat` dosyasına sağ tıklayın
2. "Run as administrator" seçeneğini tıklayın
3. Script çalışacak ve değişiklikleri uygulayacak
4. Cursor'ı yeniden başlatın

**Seçenek 3: Normal Kullanım (İzin hatası alabilirsiniz)**
1. `run.bat` dosyasını çift tıklayarak çalıştırın
2. Eğer izin hatası alırsanız yukarıdaki seçenekleri deneyin

### Manuel Kullanım

```bash
# Sadece Claude 4 Sonnet için (önerilen)
python hack_claude4.py --token-mode claude4_only --ui-style gradient

# Tüm modeller için
python hack_claude4.py --token-mode all_models --ui-style red

# Belirli dosya yolu ile
python hack_claude4.py --file "C:\Program Files\Cursor\resources\app\out\vs\workbench\workbench.desktop.main.js"
```

## Parametreler

### Token Modları
- `claude4_only` (varsayılan): Sadece Claude 4 Sonnet modelleri için 200K limit
- `all_models`: Tüm modeller için 200K limit

### UI Stilleri
- `gradient` (varsayılan): Gradyan efektli "HACKED" yazısı
- `red`: Kırmızı "HACKED" yazısı
- `animated`: Yanıp sönen kırmızı "HACKED" yazısı

## Güvenlik

- Script otomatik olarak orijinal dosyadan yedek oluşturur
- Yedek dosyalar `.backup_YYYYMMDD_HHMMSS` formatında kaydedilir
- `--skip-backup` parametresi ile yedekleme atlanabilir

## Desteklenen Platformlar

- ✅ Windows
- ✅ macOS  
- ✅ Linux

## Sorun Giderme

### "Permission denied" (İzin reddedildi) hatası
- **ÇÖZÜM**: `run_auto_admin.bat` dosyasını kullanın (otomatik yönetici hakları ister)
- **ALTERNATIF**: `run_admin.bat` dosyasına sağ tıklayıp "Run as administrator" seçin
- Bu hata Windows'ta Program Files klasörüne yazma izni gerektirdiğinden oluşur

### "Python bulunamadı" hatası
- Python 3.6+ sürümünü yükleyin
- Python'un PATH'e eklendiğinden emin olun

### "Dosya bulunamadı" hatası
- Cursor'ın yüklü olduğundan emin olun
- Manuel olarak dosya yolunu `--file` parametresi ile belirtin

### Değişiklikler görünmüyor
- Cursor'ı tamamen kapatıp yeniden başlatın
- Birden fazla Cursor penceresi varsa hepsini kapatın

## Geri Alma

Orijinal ayarlara dönmek için:
1. Yedek dosyayı bulun (`.backup_` ile başlar)
2. Yedek dosyayı orijinal dosya adıyla yeniden adlandırın
3. Cursor'ı yeniden başlatın

## Uyarılar

- Bu script Cursor'ın dahili dosyalarını değiştirir
- Cursor güncellendiğinde değişiklikler kaybolabilir
- Kullanım kendi sorumluluğunuzdadır

## Sürüm Bilgisi

Bu script Claude 4 Sonnet modelleri için özel olarak tasarlanmıştır:
- `claude-4-sonnet`
- `claude-4`

## Destek

Script çalışmıyorsa:
1. Cursor'ın en son sürümde olduğundan emin olun
2. Python 3.6+ kullandığınızdan emin olun
3. Yönetici hakları ile çalıştırmayı deneyin
4. Antivürüs yazılımının dosyayı engellemediğinden emin olun 
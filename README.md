# 🚀 Cursor Plus - Claude-4 Sonnet Boost Limit

**Cursor 1.2.0 destekli güncellenmiş sürüm!**

Bu araç Cursor editöründeki Claude-4 Sonnet modelinin token limitlerini artırır ve thinking level'ını yükseltir.

## ✨ Özellikler

- 🔓 **Claude-4 Sonnet** modeline erişim
- 📈 **200,000 token** limite çıkarma  
- 🧠 **Maksimum thinking level** (2 seviye)
- 🔄 **Cursor 1.2.0** tam uyumluluğu
- 💾 **Otomatik backup** oluşturma
- ⚡ **Admin yetkisi** ile çalışma

## 🎯 Desteklenen Cursor Sürümleri

- ✅ **Cursor 1.2.0** (Tam uyumlu)
- ✅ **Cursor 1.1.x** (Kısmi uyumlu)
- ⚠️ **Eski sürümler** (Test edilmemiş)

## 🚀 Hızlı Başlangıç

### Method 1: Auto Admin (Önerilen)
```batch
# Admin yetkisi ile otomatik çalıştırma
run_auto_admin.bat
```

### Method 2: Manuel Admin
```batch
# Admin olarak cmd açın ve çalıştırın
run_admin.bat
```

### Method 3: Python Script
```bash
# Claude-4 Sonnet için
python hack_claude4.py

# Tüm Claude modelleri için
python hack_claude.py
```

## 📋 Gereksinimler

- **Windows 10/11**
- **Cursor 1.2.0+** kurulu
- **Admin yetkisi** gerekli
- **Python 3.7+** (script için)

## 🔧 Gelişmiş Kullanım

### Özel dosya yolu belirtme:
```bash
python hack_claude4.py --file "C:\Custom\Path\workbench.desktop.main.js"
```

### Backup olmadan çalıştırma:
```bash
python hack_claude4.py --skip-backup
```

## ⚠️ Önemli Notlar

1. **Cursor'ı kapatın** script çalıştırmadan önce
2. **Admin yetkisi** gereklidir
3. **Backup** otomatik oluşturulur
4. **Restart** gereklidir değişikliklerin uygulanması için

## 🛠️ Sorun Giderme

### "Permission Denied" hatası
- Cursor'ın tamamen kapalı olduğundan emin olun
- Admin olarak çalıştırın
- Antivirus'ü geçici devre dışı bırakın

### "Pattern not found" uyarısı  
- Cursor sürümünüz desteklenmiyor olabilir
- Dosya zaten patchlenmiş olabilir
- Manuel analiz gerekebilir

### Değişiklikler uygulanmıyor
- Cursor'ı tamamen restart edin
- Browser cache'i temizleyin
- Backup'tan geri yükleyip tekrar deneyin

## 📁 Dosya Yapısı

```
CursorPlus/
├── hack_claude4.py          # Claude-4 Sonnet patcher
├── hack_claude.py           # Genel Claude patcher  
├── run_auto_admin.bat       # Otomatik admin çalıştırıcı
├── run_admin.bat            # Manuel admin çalıştırıcı
├── run.bat                  # Normal çalıştırıcı
└── README.md                # Bu dosya
```

## 🔍 Nasıl Çalışır

Script aşağıdaki fonksiyonları değiştirir:

1. **`getEffectiveTokenLimit`** - Token limitini 200,000'e çıkarır
2. **`getModeThinkingLevel`** - Thinking level'ı maksimuma (2) ayarlar  
3. **Model availability** - Claude-4 modellerini aktif eder
4. **Subscription checks** - Pro gereksinimini bypass eder

## 🎨 Cursor 1.2.0 Yenilikleri

- ✨ Yeni token limit algoritması
- 🔧 Geliştirilmiş thinking level kontrolü
- 🚀 Daha kararlı model erişimi
- 🛡️ Artırılmış güvenlik önlemleri

## ⚖️ Yasal Uyarı

Kullanımından doğacak sorumluluk kullanıcıya aittir.

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📝 Changelog

### v1.2.0 (2025-07-XX)
- ✅ Cursor 1.2.0 tam uyumluluğu
- 🔧 Yeni pattern recognition algoritması
- 🚀 Geliştirilmiş güvenilirlik
- 📈 200K token limit desteği

### v1.1.0 (2024-01-XX)  
- ✅ İlk sürüm
- 🔓 Claude-4 Sonnet unlock
- 💾 Backup sistemi
- ⚡ Admin runner

---

**Made with ❤️ for Arsilent Team**

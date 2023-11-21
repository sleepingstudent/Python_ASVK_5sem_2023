import locale
locale.getdefaultlocale()
a = "вопрос".encode("CP1251")
print(a.decode('KOI8-R'))
b = "бМХЛЮМХЭ"
c = "оХРЮМХЕ"
print(b.encode('KOI8-R').decode("CP1251"))
print(c.encode('KOI8-R').decode("CP1251"))
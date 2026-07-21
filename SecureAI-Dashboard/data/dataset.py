# data/dataset.py

# قاعدة بيانات افتراضية تحاكي نظام المشتريات للتحقق من العملاء (Know Your Customer)
STORE_DATABASE = {
    "0512345678": {
        "name": "أحمد",
        "product": "شاشة ذكية 55 بوصة",
        "purchased": True,
        "amount": 1200,
        "status": "مكتمل"
    },
    "0598765432": {
        "name": "سارة",
        "product": "لابتوب ألعاب احترافي",
        "purchased": True,
        "amount": 3500,
        "status": "مكتمل"
    },
    "0511111111": {
        "name": "خالد",
        "product": "سماعات لاسلكية",
        "purchased": False,  # لم يقم بالشراء فعلياً
        "amount": 0,
        "status": "لم يتم الشراء"
    }
}
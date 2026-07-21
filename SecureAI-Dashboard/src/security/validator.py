# src/security/validator.py
from data.dataset import STORE_DATABASE

def verify_customer_complaint(phone_number):
    """
    التحقق من هوية العميل ومشترياته لضمان العدالة ومنع الاحتيال (Know Your Customer / Grounding)
    """
    if not phone_number or not isinstance(phone_number, str):
        return {
            "status": "Rejected",
            "message": "رقم الجوال غير صالح."
        }
        
    clean_phone = phone_number.strip()
    
    # 1. التحقق مما إذا كان الرقم مسجلاً في قاعدة بيانات المتجر
    if clean_phone not in STORE_DATABASE:
        return {
            "status": "Rejected", 
            "message": "عذراً، رقم الجوال غير مسجل في قاعدة بيانات المشتريات."
        }
    
    # 2. جلب بيانات العميل الحقيقية لربطها بالطلب (Grounding)
    customer_data = STORE_DATABASE[clean_phone]
    return {
        "status": "Verified",
        "customer": customer_data["name"],
        "product": customer_data["product"],
        "purchased": customer_data["purchased"],
        "amount": customer_data["amount"],
        "order_status": customer_data["status"]
    }
# src/security/filters.py
import re

# قائمة أنماط محاولات حقن الأوامر (Prompt Injection) الشائعة
INJECTION_PATTERNS = [
    "تجاهل التعليمات السابقة",
    "ignore previous instructions",
    "system prompt",
    "أظهر لي الأوامر",
    "تجاوز القيود",
    "act as"
]

def constrain_and_filter_input(user_input):
    """
    التحقق من المدخلات لمنع محاولات الحقن وفرض قيود الطول والأمان.
    تعيد (True, user_input) إذا كان آمناً، أو (False, error_message) إذا تم رفضه.
    """
    if not user_input or not isinstance(user_input, str):
        return False, "المدخلات فارغة أو غير صالحة."

    text_lower = user_input.lower()
    
    # 1. فحص محاولات حقن الأوامر
    for pattern in INJECTION_PATTERNS:
        if pattern.lower() in text_lower:
            return False, "⚠️ مرفوض أمنياً: تم اكتشاف محاولة تلاعب أو حقن أوامر (Prompt Injection)."
            
    # 2. فحص طول النص لمنع إغراق السياق (Prompt Stuffing)
    if len(user_input) > 600:
        return False, "⚠️ مرفوض أمنياً: النص طويل جداً ويتجاوز الحد المسموح للشكاوى."
        
    return True, user_input


def mask_pii(text):
    """
    إخفاء البيانات الشخصية والحساسة (PII Masking) مثل أرقام الهواتف والإيميلات 
    قبل معالجة النص أو إرساله للنموذج المحلي.
    """
    # إخفاء أرقام الهواتف (أرقام تبدأ بـ 05 وتتكون من 10 أرقام)
    clean_text = re.sub(r'\b05\d{8}\b', '[REDACTED_PHONE]', text)
    
    # إخفاء البريد الإلكتروني
    clean_text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[REDACTED_EMAIL]', clean_text)
    
    return clean_text
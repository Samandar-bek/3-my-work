# home/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Level, Question
from django.conf import settings

# Agar Google Translate ishlatilsa:
try:
    from googletrans import Translator  # pip install googletrans==4.0.0-rc1
    translator = Translator()
    USE_TRANSLATE = True
except ImportError:
    USE_TRANSLATE = False
    print("⚠️ googletrans kutubxonasi o‘rnatilmagan. Avtomatik tarjima ishlamaydi.")


# =========================
# LEVEL SIGNALS
# =========================
@receiver(post_save, sender=Level)
def after_level_created(sender, instance, created, **kwargs):
    """
    Yangi Level yaratilganda ishga tushadi.
    Konsolga xabar chiqaradi.
    """
    if created:
        print(f"📚 Yangi Level yaratildi: {instance.name}")


# =========================
# QUESTION SIGNALS
# =========================
@receiver(pre_save, sender=Question)
def set_question_order_and_translate(sender, instance, **kwargs):
    """
    Question saqlanishidan oldin ishga tushadi:
    1️⃣ Order qiymatini avtomatik belgilaydi.
    2️⃣ Agar en_text bo'sh bo'lsa, uz_text'dan inglizchaga tarjima qiladi.
    """
    # ===== Order avtomatik berish =====
    if not hasattr(instance, 'order'):
        # Modelda order maydoni yo‘q bo‘lsa xato bermasligi uchun
        instance.order = 0

    if instance.order is None or instance.order == 0:
        last_question = (
            Question.objects.filter(level=instance.level)
            .order_by("-order")
            .first()
        )
        instance.order = last_question.order + 1 if last_question else 1

    # ===== Avtomatik inglizchaga tarjima =====
    if USE_TRANSLATE and (not instance.en_text or instance.en_text.strip() == ''):
        try:
            translated = translator.translate(instance.uz_text, src='uz', dest='en')
            instance.en_text = translated.text
        except Exception as e:
            print(f"⚠️ Tarjima xatosi: {e}")


@receiver(post_save, sender=Question)
def after_question_created(sender, instance, created, **kwargs):
    """
    Question yaratgandan keyin ishga tushadi.
    Konsolga xabar chiqaradi.
    """
    if created:
        question_preview = instance.uz_text[:50]  # faqat o‘zbekchasidan qisqartma
        print(f"📝 Yangi savol qo‘shildi: {question_preview} "
            f"(Level: {instance.level.name}, Order: {instance.order})")
    else:
        print(f"📝 Savol yangilandi: {instance.uz_text[:50]} (ID: {instance.id})")

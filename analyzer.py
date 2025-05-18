# analyzer.py

import openai
import os
from dotenv import load_dotenv

# تحميل المفاتيح من .env
load_dotenv()
openai.api_key = os.getenv("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")

def analyze_article(title, content):
    """
    يحلل الخبر باستخدام GPT ليحدد إن كان مضللًا.
    """
    prompt = f"""
أنت مساعد مختص في كشف التضليل الإعلامي.

مهمتك هي تحليل الأخبار وتحديد إن كانت تحتوي على تضليل أو معلومات غير موثوقة، مع شرح السبب باختصار.

العنوان: {title}

المحتوى:
{content}

هل هذا الخبر مضلل أو يحتوي على معلومات مشكوك بها؟ ولماذا؟
    """.strip()

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # يمكنك تغييره إلى gpt-4 إذا كان متوفرًا
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400,
        )

        result = response.choices[0].message["content"].strip()
        return result

    except Exception as e:
        print("خطأ أثناء تحليل الخبر:", e)
        return "❌ تعذر تحليل هذا الخبر بسبب مشكلة في الاتصال بـ OpenAI."

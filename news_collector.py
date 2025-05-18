# news_collector.py

import requests
import os
from dotenv import load_dotenv

# تحميل المفاتيح من .env
load_dotenv()
NEWSAPI_KEY = os.getenv("cb432eea97dd4cec984e6917dae798bf")

def fetch_news():
    """جلب أخبار تتعلق بسوريا باللغة العربية."""
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=سوريا OR سوريا&language=ar&sortBy=publishedAt&pageSize=10&apiKey={NEWSAPI_KEY}"
    )
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("status") != "ok":
            print("خطأ في جلب الأخبار:", data.get("message"))
            return []

        return data.get("articles", [])

    except Exception as e:
        print("فشل الاتصال بـ NewsAPI:", e)
        return []

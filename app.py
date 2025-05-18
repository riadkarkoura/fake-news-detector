# app.py

import streamlit as st
from news_collector import fetch_news
from analyzer import analyze_article
from database import save_article, get_all_articles

st.set_page_config(page_title="كشف الأخبار الكاذبة حول سوريا", layout="wide")

st.title("🕵️‍♂️ منصة كشف الأخبار الكاذبة حول سوريا")
st.markdown("هذه المنصة تجمع الأخبار وتُحللها باستخدام الذكاء الاصطناعي لتحديد مدى موثوقيتها.")

# زر جلب وتحليل الأخبار
if st.button("🔍 جلب وتحليل آخر الأخبار"):
    articles = fetch_news()
    with st.spinner("يتم تحليل الأخبار..."):
        for article in articles:
            title = article.get("title", "")
            content = article.get("content") or article.get("description", "")
            url = article.get("url", "")
            published_at = article.get("publishedAt", "")

            if title and content:
                analysis = analyze_article(title, content)
                save_article(title, content, url, analysis, published_at)

    st.success("✅ تم جلب وتحليل الأخبار بنجاح.")

st.markdown("---")
st.subheader("📰 الأخبار المحللة:")

# عرض الأخبار المحفوظة
rows = get_all_articles()
for row in rows:
    id, title, content, url, analysis, published_at = row

    with st.expander(f"🗞️ {title}"):
        st.write(f"**تاريخ النشر:** {published_at}")
        st.write(f"**الرابط:** [قراءة المصدر]({url})")
        st.write(f"**المحتوى:** {content}")
        st.markdown("---")
        st.write(f"**تحليل الذكاء الاصطناعي:**")
        st.info(analysis)

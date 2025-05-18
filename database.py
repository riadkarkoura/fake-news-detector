# database.py

import sqlite3

# إنشاء الاتصال بقاعدة البيانات
conn = sqlite3.connect("news.db", check_same_thread=False)
cursor = conn.cursor()

# إنشاء جدول لتخزين الأخبار إن لم يكن موجودًا
cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        url TEXT,
        analysis TEXT,
        published_at TEXT
    )
''')
conn.commit()

def save_article(title, content, url, analysis, published_at):
    """حفظ خبر جديد في قاعدة البيانات"""
    cursor.execute('''
        INSERT INTO news (title, content, url, analysis, published_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, content, url, analysis, published_at))
    conn.commit()

def get_all_articles():
    """إرجاع كل الأخبار من القاعدة"""
    cursor.execute('SELECT * FROM news ORDER BY id DESC')
    return cursor.fetchall()

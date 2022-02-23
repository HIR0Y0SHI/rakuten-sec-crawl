# Rakunten Crawl

楽天証券から「資産合計」と「評価損益」を取得します。

## 環境変数

| LOGIN_ID                       | LOGIN_PASS           | 
| ------------------------------ | -------------------- | 
| 楽天証券にログインするためのID | 楽天証券のパスワード | 

```bash
export LOGIN_ID="ID"
export LOGIN_PASS="PASSWORD"
```

## 依存

### selenium

```bash
pip install selenium
```

### chromedriver

ChromeDriver 98.0.4758.102
https://chromedriver.chromium.org/downloads
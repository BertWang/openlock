# 🚀 強匠鎖店 v2.0 - 快速開始清單

## ✅ 已建立的檔案

### 🎨 設計系統
- [x] `assets/css/tokens.css` - 全站 Design Token (顏色、間距、陰影、動畫)
- [x] `assets/css/skins.css` - 三層皮膚系統 (base/mid/high with data-skin selector)
- [x] `assets/css/home.css` - 首頁特定樣式
- [x] `assets/css/service-page.css` - 服務頁特定樣式

### 📄 HTML 頁面
- [x] `index.html` - 完整首頁 (包含首頁、服務卡片、信任條、評論、區域導航)
- [x] `service-page.html` - 8 區塊服務頁模板 (Hero, Pain Points, Process, Trust Bar, FAQ, Areas, Reviews, Bottom CTA)

### 📝 JavaScript
- [x] `assets/js/skin-switcher.js` - 皮膚切換器 + 工具函數 + 流暢滾動

### 📚 內容文檔
- [x] `content/copywriting-library.md` - 三層文案庫 (H1、副標題、CTA、特色、FAQ、評論)
- [x] `content/seo-regional-content.md` - 6 區域 SEO 內容 (引言、FAQ、關鍵字)
- [x] `README.md` - 專案完整指南

---

## 🎯 下一步行動

### 立即可做的事

# 用下拉菜單測試三種皮膚：base → mid → high
```

#### 2️⃣ 填入真實文案
使用 `copywriting-library.md` 的內容，替換 HTML 中的 `[Placeholder]` 標籤：
```html
<!-- 例：替換首頁 Hero 標題 -->
<h1 id="heroTitle">[Hero Title]</h1>
<!-- 改為 -->
<h1>24小時到府開鎖</h1>
```

#### 3️⃣ 建立 6 個區域 SEO 頁面
複製 `service-page.html`，逐一修改為：
- `sanmin.html` (三民區)
- `zuoying.html` (左營區)
- `xinxing.html` (新興區)
- `qianjin.html` (前金區)
- `lingya.html` (苓雅區)
- `qianzheng.html` (前鎮區)

根據 `seo-regional-content.md` 更新各區的內容。

#### 4️⃣ 補充圖片資源
建立高品質圖片並放入 `images/` 資料夾：
- `hero-locksmith.jpg` (首頁 Hero 圖)
- `smart-lock.jpg` (高端層範例圖)
- `car-keys.jpg` (中端層範例圖)
- `locksmith-at-work.jpg` (基礎層範例圖)

### 進階配置（可選）

#### 5️⃣ 建立 Sitemap
```xml
<!-- sitemap.xml -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yoursite.com/index.html</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://yoursite.com/service-page.html</loc>
  </url>
  <url>
    <loc>https://yoursite.com/sanmin.html</loc>
  </url>
  <!-- ... etc -->
</urlset>
```

#### 6️⃣ 建立 robots.txt
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/

Sitemap: https://yoursite.com/sitemap.xml
```

#### 7️⃣ Google Analytics 整合
在所有 HTML 的 `</head>` 前加入：
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

#### 8️⃣ 聯繫表單優化
在 `service-page.html` 中加入聯繫表單 (建議使用 Formspree、Netlify Forms 或自架後端)

---

## 📐 架構設計亮點

### 1️⃣ 皮膚系統 (Skin System)
- **動態切換**：三種視覺風格對應三種服務層級
- **易於維護**：顏色變數集中在 `skins.css`
- **SEO 友善**：同一套 HTML，不同視覺，避免內容重複

### 2️⃣ CSS Variables 設計
```css
:root {
  --bg: #ffffff;        /* 因皮膚而異 */
  --primary: #2f80ed;   /* 因皮膚而異 */
  --text: #111827;      /* 因皮膚而異 */
  --cta-phone: #16a34a; /* 統一綠色 */
  --cta-line: #06b6d4;  /* 統一藍色 */
}
```
優點：
- ✅ 快速換色（只需改 CSS 變數）
- ✅ 一致性（所有元件自動更新）
- ✅ 響應式友善（可在 media query 中覆蓋）

### 3️⃣ 8 區塊服務頁模板
```
1. Hero Section (標題 + 副標題 + CTA)
2. Pain Points (3 個特色卡片)
3. Process / Stepper (3 步驟流程)
4. Trust Bar (評分、保證、時間、報價)
5. FAQ (Bootstrap Accordion)
6. Service Areas (區域連結清單)
7. Reviews / Testimonials (客戶評論)
8. Bottom Fixed CTA Bar (手機專用)
```
這個結構覆蓋了**用戶決策路徑**的所有關鍵節點。

### 4️⃣ 三層文案系統
每層都有完整的「聲音」定義：
- **語氣** (Tone)：簡約 vs. 專業 vs. 親切
- **重點** (Focus)：品質 vs. 速度 vs. 透明
- **CTA 文案** (Call-to-Action)：預約 vs. 立即 vs. 撥號

這確保了品牌一致性，同時滿足不同客群的溝通需求。

### 5️⃣ 在地化 SEO 策略
```
首頁 (所有服務) 
  ↓
服務頁 (按層級)
  ↓
區域頁 (按地點 × 層級)
```
這個層級結構：
- ✅ 避免內容農場感（每區都有獨特內容）
- ✅ 覆蓋長尾關鍵字（「三民區開鎖」「前金區電子鎖」等）
- ✅ 增加內部連結（首頁 → 服務頁 → 區域頁）

---

## 🎬 實戰使用案例

### 案例 1：A/B 測試不同皮膚風格
```javascript
// 追蹤每種皮膚的轉換率
window.addEventListener('skin-changed', (e) => {
  const skin = e.detail.skin;
  gtag('event', 'skin_changed', {
    skin_type: skin
  });
});
```

### 案例 2：根據 URL 參數預設皮膚
```
https://yoursite.com/service-page.html?skin=high
// 高端客戶直接看到高端皮膚
```

### 案例 3：為不同區域推薦不同服務
```html
<!-- sanmin.html: 強調基礎開鎖 -->
<h1>三民區24小時開鎖服務</h1>
<a href="?skin=base">查看基礎方案</a>

<!-- zuoying.html: 強調電子鎖 -->
<h1>左營區電子鎖安裝服務</h1>
<a href="?skin=high">查看高端方案</a>
```

---

## 🔍 SEO 檢查清單

- [ ] 每頁都有獨特的 `<title>` (60-70 字元)
- [ ] 每頁都有獨特的 `<meta name="description">` (150-160 字元)
- [ ] H1 標題包含主要關鍵字
- [ ] 圖片都有 `alt` 屬性
- [ ] 內部連結用描述文字（而不是「點此」）
- [ ] 結構化資料 (Schema) 已加入
- [ ] Sitemap.xml 已提交 Google Search Console
- [ ] robots.txt 已設定
- [ ] Mobile-first 測試通過 (Google Mobile-Friendly Test)
- [ ] Core Web Vitals 優化完成 (PageSpeed Insights)

---

## 📞 聯繫方式集成

目前 HTML 中的電話與 LINE 是範例。需要替換為真實資訊：

```html
<!-- 電話 -->
<a href="tel:+886XXXXXXXXX">📞 撥號</a>

<!-- LINE -->
<a href="https://line.me/R/ti/p/@YOUR_LINE_ID">💬 LINE</a>
```

---

## 💡 進一步改進建議

1. **建立後端**：收集聯繫表單、追蹤預約、客戶管理
2. **加入 Blog**：寫開鎖小知識、電子鎖保養提示（增加流量）
3. **Video 內容**：錄製安裝流程、客戶見證（提高轉換)
4. **WhatsApp 整合**：除了 LINE，加入 WhatsApp 聯繫
5. **在線客服**：Chatbot 或人工客服（即時回應客戶）
6. **評論系統**：與 Google Review、Facebook 同步

---

## 📌 重點提醒

✅ **目前可做**：
- 本地測試 HTML + CSS + JS
- 替換文案與圖片
- 建立 6 個區域頁面
- 上傳到虛擬主機

⚠️ **即將需要**：
- 聯繫表單後端
- Google Analytics 追蹤
- Google Search Console 驗證
- SSL 憑證（HTTPS）

🚀 **長期規劃**：
- Blog 部落格
- SEO 持續優化
- 客戶評論管理
- 轉換率優化 (CRO)

---

**祝您的強匠鎖店網站成功上線！** 🔐✨

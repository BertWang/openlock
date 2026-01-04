# 🔐 強匠鎖店 v2.0 - 架構調整版

## 📋 項目概述

強匠鎖店官網採用 **Bootstrap 5** + **自訂 CSS (Token/Skin System)** + **輕量 JavaScript**，內化三層質感分層設計、服務排序邏輯、與區域 SEO 策略。核心原則：**行動優先、CTA 優先、內容一致**。

---

## 📂 文件結構（按新規範）

```
openlock/
│
├── 📄 根目錄頁面
│   ├── index.html              # 首頁（所有服務入口 + 6 區域導航）
│   ├── services.html           # 服務總覽（服務排序：汽車鑰匙 → 電子鎖 → 開鎖）
│   ├── reviews.html            # 完整評論/案例頁
│   ├── faq.html                # 常見問題（全站 + 服務別）
│   ├── contact.html            # 聯絡頁（NAP + 地圖 + LINE + 到府說明）
│   │
│   ├── 🔑 服務頁（3 個 + 模板）
│   ├── digital-locks.html      # 電子鎖服務頁（或 services-digital.html）
│   ├── auto-keys.html          # 汽車鑰匙服務頁（或 services-auto.html）
│   ├── emergency-lock.html     # 一般開鎖服務頁（或 services-lock.html）
│   │
│   ├── 📦 電子鎖型錄
│   ├── digital-locks-catalog.html   # 型錄總覽（篩選 + 產品卡 Grid）
│   ├── lock-model-001.html          # 型號詳情頁模板（規格 + FAQ + 詢問 CTA）
│   ├── lock-model-002.html
│   ├── ... lock-model-*.html
│   │
│   ├── 🗺️  6 個區域頁
│   ├── area-sanmin.html        # 三民區（或 areas-sanmin.html）
│   ├── area-zuoying.html       # 左營區
│   ├── area-xinxing.html       # 新興區
│   ├── area-qianjin.html       # 前金區
│   ├── area-lingya.html        # 苓雅區
│   └── area-qianzheng.html     # 前鎮區
│
├── /assets/                    # 前端資源（Bootstrap + 自訂 CSS/JS）
│   │
│   ├── /css/
│   │   ├── bootstrap.min.css   # Bootstrap 5（CDN 或本地）
│   │   ├── tokens.css          # 全站 Token（顏色/字體/陰影/圓角/間距）
│   │   ├── components.css      # 共用元件（CTA Bar / Service Card / Trust Badge / Stepper）
│   │   ├── skins.css           # 三層 Skin（[data-skin="high|mid|base"]）
│   │   └── pages.css           # 頁面微調（首頁/服務頁/區域頁/型錄）
│   │
│   ├── /js/
│   │   ├── bootstrap.bundle.min.js  # Bootstrap 5 JS（含 Popper）
│   │   └── app.js              # 自寫 JS（主題切換、CTA、表單、Offcanvas）
│   │
│   ├── /images/
│   │   ├── logo.svg
│   │   ├── hero-*.jpg          # Hero 背景圖（按 Skin）
│   │   ├── service-*.jpg       # 服務圖片
│   │   ├── lock-model-*.jpg    # 產品圖
│   │   └── ...
│   │
│   └── /fonts/                 # 自訂字體（如需要）
│
├── /content/                   # 內容資料庫
│   ├── copywriting-library.md  # 三層文案庫（高/中/基）
│   └── seo-regional-content.md # 6 區域內容 + FAQ
│
└── 📄 文檔
    ├── README.md               # 本檔案（架構 + 規範）
    ├── QUICK_START.md          # 快速開始清單
    └── PROJECT_SUMMARY.md      # 交付成果總結
```

---

## � 設計大方向（必遵守）

### 1.1 共同原則（全站一致）
- ✅ **全站固定 CTA**：一鍵撥號 + LINE 諮詢（並提示「可傳照片加快效率」）
- ✅ **行動優先**：手機端首屏必見 CTA（固定底部 CTA Bar）
- ✅ **內容一致**：店名/地址/電話/營業時間/到府說明全站一致
- ✅ **服務排序（高單價優先）**：汽車鑰匙 → 電子鎖 → 一般開鎖（但緊急 CTA 置頂不變）

### 1.2 質感分層（同版型三套 Skin）

同一套元件/版型，換「色彩 Token、圖片風格、文案語氣」來分眾：

#### 🏆 高端層（電子鎖 - [data-skin="high"]）
- **視覺**：深藍 (#0b1b3a) + 金色 (#d6b15e) 點綴、簡約高級（大留白、少字、強對比）
- **文案**：「智能家居升級」、「安全新定義」、「美學與科技結合」
- **受眾**：30–55 歲、月收 10 萬+、新屋主
- **重點**：品質、設計、安全、遠端控制

#### 💼 中端層（汽車鑰匙 - [data-skin="mid"]）
- **視覺**：天藍 (#1e88e5) + 銀灰 (#b0bec5)、專業科技感（資訊密度略高、圖示強調效率）
- **文案**：「車鑰匙丟失？5分鐘到府複製」、「原廠品質、快速解碼」
- **受眾**：25–50 歲、車主、商務人士
- **重點**：速度、效率、技術、成本

#### 🚪 基礎層（開鎖 - [data-skin="base"]）
- **視覺**：清爽藍 (#2f80ed) + 白、親切易近（更明亮、資訊更直覺）
- **文案**：「24小時應急開鎖」、「專業、快速、透明價格」、「不開不收錢」
- **受眾**：全年齡、緊急需求者
- **重點**：誠信、快速、透明、可靠

---

## �🎨 設計系統詳解

### 三層質感皮膚 (Skin System)

使用 `[data-skin="value"]` 選擇器，網站可動態切換三種視覺風格，每種都對應不同的服務層級：

#### 1️⃣ **Base Skin (基礎層 - 一般開鎖)**
```html
<html lang="zh-Hant" data-skin="base">
```
- **背景色**: `#ffffff` (純白)
- **主色**: `#2f80ed` (清爽藍)
- **強調色**: `#2f80ed` (同上)
- **文字色**: `#111827` (深灰黑)
- **風格**: 親切、明亮、可靠
- **目標客群**: 緊急需求者、大眾

#### 2️⃣ **Mid Skin (中端層 - 汽車鑰匙)**
```html
<html lang="zh-Hant" data-skin="mid">
```
- **背景色**: `#f8fafc` (淡藍灰)
- **主色**: `#1e88e5` (天藍)
- **強調色**: `#b0bec5` (銀灰)
- **文字色**: `#0d1b2a` (深色)
- **風格**: 科技、專業、結果導向
- **目標客群**: 車主、商務人士

#### 3️⃣ **High Skin (高端層 - 電子鎖)**
```html
<html lang="zh-Hant" data-skin="high">
```
- **背景色**: `#0b1b3a` (深海藍)
- **主色**: `#d6b15e` (金色)
- **強調色**: `#d6b15e` (同上)
- **文字色**: `#f5f5f5` (淡白)
- **風格**: 奢華、高對比、高級感
- **目標客群**: 30-55 歲新屋主、高收入

### 動態切換方式

#### 方法 1 - 下拉選擇器
```html
<select id="skinSelector">
    <option value="base">基礎版</option>
    <option value="mid">中端版</option>
    <option value="high">高端版</option>
</select>
```
會自動觸發 `skin-switcher.js`

#### 方法 2 - URL 參數
```
https://example.com/service-page.html?skin=high
```

#### 方法 3 - JavaScript 控制
```javascript
window.SkinSwitcher.applySkin('high');
```

---

## 🎯 內容系統

### 1. 三層文案庫 (`copywriting-library.md`)

針對三個服務層級，提供了完整的文案變體：

| 層級 | 語氣 | 關鍵詞 | 目標客群 |
|------|------|-------|---------|
| **高端** | 簡約、高級、價值導向 | 智能家居、安全新定義、美學 | 新屋主、高收入 |
| **中端** | 效率、專業、結果導向 | 原廠品質、5分鐘複製、晶片解碼 | 車主、商務人士 |
| **基礎** | 親切、安心、可靠 | 24小時、不開不收錢、透明報價 | 緊急需求者、大眾 |

內容包括：
- H1 標題、副標題、CTA 文案（各 3 個變體）
- 特色描述、常見問題、客戶評價
- 按鈕文案、信任條、流程說明

### 2. 區域 SEO 內容 (`seo-regional-content.md`)

針對 6 個高雄行政區建立差異化內容，避免「內容農場」與重複內容懲罰：

| 區域 | 特色情境 | 關鍵字 |
|------|---------|-------|
| **三民區** | 住宅密集區 | 三民區開鎖、大樓住戶換鎖 |
| **左營區** | 高鐵周邊、新社區 | 左營開鎖、電子鎖安裝 |
| **新興區** | 商圈、夜間營業 | 新興商圈、夜間急開 |
| **前金區** | 金融、商務辦公 | 前金開鎖、商務門禁 |
| **苓雅區** | 傳統住宅區、年長戶 | 苓雅開鎖、住宅換鎖 |
| **前鎮區** | 工業區、製造業 | 前鎮開鎖、工業區汽車鑰匙 |

每區提供：
- 100-150 字區域服務引言
- 3 條常見問題 (FAQ)
- 在地化關鍵字與信任因素

---

## 🚀 快速開始

### 1. 基本設定

在任何 HTML 頁面中，只需三行：

```html
<!-- Bootstrap 5 -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- 設計系統 -->
<link rel="stylesheet" href="css/tokens.css">
<link rel="stylesheet" href="css/skins.css">
<link rel="stylesheet" href="css/home.css">  <!-- 或 service-page.css -->

<!-- 皮膚切換 -->
<script src="js/skin-switcher.js"></script>
```

### 2. 建立新的區域 SEO 頁面

根據 `seo-regional-content.md` 的內容，複製 `service-page.html` 並：
1. 修改 Hero 標題 (H1) 為「[地名] + 服務」
2. 更新 FAQ 與區域特色
3. 保持同樣的 HTML 結構以利 SEO

### 3. 填入文案內容

使用 `copywriting-library.md` 中的文案變體，替換 HTML 中的 `[Placeholder]` 標籤。

### 4. 切換皮膚測試

在瀏覽器開發者工具中執行：
```javascript
window.SkinSwitcher.applySkin('high');  // 測試高端層
window.SkinSwitcher.applySkin('mid');   // 測試中端層
window.SkinSwitcher.applySkin('base');  // 回到基礎層
```

---

## 🔧 CSS 變數快速參考

### 顏色變數 (在 tokens.css 中定義)

```css
:root {
  --primary: ...;        /* 主色（因皮膚而異）*/
  --accent: ...;         /* 強調色（因皮膚而異）*/
  --text: ...;           /* 文字色（因皮膚而異）*/
  --bg: ...;             /* 背景色（因皮膚而異）*/
  --cta-phone: #16a34a;  /* 撥號綠 */
  --cta-line: #06b6d4;   /* LINE 藍 */
}
```

### 間距 (Spacing)

```css
--spacing-xs: 0.25rem;  /* 4px */
--spacing-sm: 0.5rem;   /* 8px */
--spacing-md: 1rem;     /* 16px */
--spacing-lg: 1.5rem;   /* 24px */
--spacing-xl: 2rem;     /* 32px */
```

### 圓角 (Border Radius)

```css
--radius: 16px;      /* 全局預設 */
--radius-sm: 8px;    /* 小元件 */
--radius-md: 12px;   /* 中等 */
--radius-lg: 20px;   /* 大元件 */
```

### 陰影 (Shadows)

```css
--shadow-card: 0 4px 12px rgba(0,0,0,0.08);
--shadow-card-hover: 0 8px 24px rgba(0,0,0,0.12);
--shadow-lg: 0 12px 32px rgba(0,0,0,0.15);
```

### 動畫 (Transitions)

```css
--transition-fast: 150ms ease-in-out;
--transition-base: 250ms ease-in-out;
--transition-slow: 350ms ease-in-out;
```

---

## 📱 響應式設計

所有頁面已根據 Bootstrap 5 的斷點進行優化：

- **桌面**: >= 1200px
- **平板**: 768px - 1199px
- **手機**: < 768px

特別注意：
- **底部固定 CTA Bar** 僅在手機版顯示 (`@media (max-width: 768px)`)
- **Hero 圖片** 在平板以上顯示；手機版隱藏以提升載入速度

---

## 🔍 SEO 最佳實踐

### 頁面標籤範例

#### 高端層服務頁
```html
<title>電子鎖安裝 | 智能家居安全解決方案 | 強匠鎖店</title>
<meta name="description" content="高端電子鎖安裝服務，提供智能門禁、生物辨識、遠端控制。原廠保固10年，專業技師24小時待命。">
```

#### 區域 SEO 頁面
```html
<title>[地名]開鎖 | 24小時應急服務 | 強匠鎖店</title>
<meta name="description" content="[地名]開鎖、電子鎖安裝、汽車鑰匙複製。強匠在地[年份]年經驗，[數字]則好評。不開不收錢保證。">
```

### 結構化資料 (Schema)

建議添加 `LocalBusiness` 與 `BreadcrumbList`：

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "強匠鎖店",
  "image": "...",
  "description": "24小時開鎖、電子鎖安裝、汽車鑰匙複製服務",
  "telephone": "+886-123-456-78",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "高雄市",
    "addressRegion": "台灣"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "442"
  }
}
```

---

## ✅ 待完成任務

- [ ] 建立 6 個區域 SEO 落地頁 (sanmin.html 等)
- [ ] 補充圖片資源到 `images/` 資料夾
- [ ] 建立 Sitemap.xml
- [ ] 設定 robots.txt
- [ ] Google Analytics / GTM 整合
- [ ] Google Search Console 驗證
- [ ] 美化表單與聯繫方式
- [ ] 建立部落格區域（選擇性）

---

## 📞 使用提示

### 動態更新文案

所有文案都存放在 `content/` 資料夾內的 Markdown 檔案。修改內容後，複製到 HTML 相應位置即可。

### 切換皮膚進行 AB 測試

使用皮膚切換功能，可以快速測試三種設計方案對用戶的吸引力：
- 追蹤每種皮膚的點擊率、轉換率
- 根據數據優化設計與文案

### 本地開發

如要在本地測試，建議使用簡易 HTTP 伺服器：

```bash
# Python 3
python -m http.server 8000

# Node.js (如有安裝 http-server)
npx http-server -p 8000
```

然後訪問：`http://localhost:8000/html/index.html`

---

## 📚 參考文件

- [Bootstrap 5 文檔](https://getbootstrap.com/docs/5.3/)
- [CSS Variables MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)
- [Web Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 📝 版本紀錄

- **v2.0** (2026-01-04) - 初始發佈，包含設計系統、首頁、服務頁、三層文案庫、6 區域 SEO 內容

---

## 🤝 貢獻指南

遵循以下規範：
1. 所有新增頁面應符合 `[data-skin]` 系統
2. 文案修改請更新 `content/` 資料夾中的對應檔案
3. 新增 CSS 變數時，務必在 `tokens.css` 或 `skins.css` 中明確註記

---

**強匠鎖店 v2.0**  
*智能安全，在地服務。*

# 🔐 強匠鎖店 v2.0 - Bootstrap + 自訂 CSS 架構

> **技術底座**：Bootstrap 5（Navbar / Offcanvas / Card / Grid） + Bootstrap Bundle JS + 自訂 CSS（Tokens/Components/Skins/Pages） + 輕量自寫 JS。

---

## 📋 項目概述

強匠鎖店官網採用現代化的設計系統，核心邏輯：
- ✅ **行動優先**：手機端首屏 3 秒內可點「撥號 / LINE」
- ✅ **三層質感分層**：同一套元件，三種皮膚（高端 / 中端 / 基礎）
- ✅ **服務排序**：高單價優先呈現（汽車鑰匙 → 電子鎖 → 一般開鎖）
- ✅ **全站一致**：NAP（店名/地址/電話）、營業時間、到府說明一致

---

## 📂 文件結構（新規範）

```
openlock/
│
├── 📄 根目錄 HTML 頁面
│   ├── index.html                      # 首頁（服務入口 + 6 區域導航）
│   ├── services.html                   # 服務總覽（服務排序：汽車鑰匙 → 電子鎖 → 開鎖）
│   ├── reviews.html                    # 完整評論/案例頁
│   ├── faq.html                        # 全站 FAQ（+ 服務別 FAQ）
│   ├── contact.html                    # 聯絡頁（NAP + 地圖 + LINE + 到府說明）
│   │
│   ├── 🔑 三個服務頁（對應三層 Skin）
│   ├── service-digital-locks.html      # 電子鎖服務頁 [data-skin="high"]
│   ├── service-auto-keys.html          # 汽車鑰匙服務頁 [data-skin="mid"]
│   ├── service-emergency-lock.html     # 一般開鎖服務頁 [data-skin="base"]
│   │
│   ├── 📦 電子鎖型錄
│   ├── digital-locks-catalog.html      # 型錄總覽（產品卡 + 篩選）
│   ├── lock-model-001.html             # 型號詳情頁模板（規格 + FAQ + CTA）
│   ├── lock-model-002.html
│   ├── ... lock-model-XXX.html
│   │
│   ├── 🗺️ 六個區域頁
│   ├── area-sanmin.html                # 三民區
│   ├── area-zuoying.html               # 左營區
│   ├── area-xinxing.html               # 新興區
│   ├── area-qianjin.html               # 前金區
│   ├── area-lingya.html                # 苓雅區
│   └── area-qianzheng.html             # 前鎮區
│
├── /assets/                            # 前端資源
│   │
│   ├── /css/
│   │   ├── bootstrap.min.css           # Bootstrap 5（CDN 或本地）
│   │   ├── tokens.css                  # 全站 Token（顏色/字體/陰影/圓角/間距）
│   │   ├── components.css              # 共用元件（CTA Bar / Service Card / Trust Badge / Stepper）
│   │   ├── skins.css                   # 三層 Skin（[data-skin="high|mid|base"]）
│   │   └── pages.css                   # 頁面微調（首頁/服務頁/區域頁/型錄）
│   │
│   ├── /js/
│   │   ├── bootstrap.bundle.min.js     # Bootstrap 5 JS（含 Popper）
│   │   └── app.js                      # 自寫 JS（主題切換、CTA、表單、Offcanvas）
│   │
│   ├── /images/
│   │   ├── logo.svg
│   │   ├── favicon.ico
│   │   ├── hero-high.jpg               # 高端層 Hero 背景（深藍+金）
│   │   ├── hero-mid.jpg                # 中端層 Hero 背景（天藍+銀灰）
│   │   ├── hero-base.jpg               # 基礎層 Hero 背景（清爽藍+白）
│   │   ├── service-*.jpg               # 服務圖片
│   │   ├── lock-model-*.jpg            # 產品圖
│   │   └── testimonial-*.jpg           # 評論頭像
│   │
│   └── /fonts/                         # 自訂字體（如需）
│
├── /content/                           # 內容資料庫
│   ├── copywriting-library.md          # 三層文案庫（高/中/基層的 H1、副標、CTA、FAQ、評論）
│   └── seo-regional-content.md         # 六區域內容（引言 + FAQ）
│
└── 📄 文檔
    ├── README.md                       # 本檔案
    ├── QUICK_START.md                  # 快速開始清單
    └── PROJECT_SUMMARY.md              # 交付成果總結
```

---

## 🎯 設計大方向（必遵守）

### 1.1 共同原則（全站一致）

- **全站固定 CTA**：一鍵撥號 + LINE 諮詢（並提示「可傳照片加快效率」）
- **行動優先**：手機端首屏必見 CTA（固定底部 CTA Bar，高 z-index）
- **內容一致**：店名/地址/電話/營業時間/到府說明全站統一
- **服務排序（高單價優先）**：汽車鑰匙 → 電子鎖 → 一般開鎖
- **CTA 按鈕顏色統一**：
  - 撥號：`--cta-phone: #16a34a`（綠）
  - LINE：`--cta-line: #06b6d4`（藍）

### 1.2 質感分層（同版型三套 Skin）

#### 🏆 高端層（電子鎖）[data-skin="high"]
- **視覺**：深藍 (#0b1b3a) + 金色 (#d6b15e)、簡約高級（大留白、少字、強對比）
- **文案語氣**：「智能家居升級」、「安全新定義」、「美學與科技結合」
- **受眾**：30–55 歲、月收 10 萬+、新屋主、對品質敏感
- **重點**：品質、設計、安全性、遠端控制、高級感

#### 💼 中端層（汽車鑰匙）[data-skin="mid"]
- **視覺**：天藍 (#1e88e5) + 銀灰 (#b0bec5)、專業科技感（資訊密度中等、圖示強調效率）
- **文案語氣**：「車鑰匙丟失？5分鐘到府複製」、「原廠品質、快速解碼」
- **受眾**：25–50 歲、車主、商務人士、對效率敏感
- **重點**：速度、效率、技術、成本、可靠性

#### 🚪 基礎層（開鎖）[data-skin="base"]
- **視覺**：清爽藍 (#2f80ed) + 白、親切易近（更明亮、資訊直覺、CTA 醒目）
- **文案語氣**：「24小時應急開鎖」、「專業、快速、透明價格」、「不開不收錢」
- **受眾**：全年齡、緊急需求者、對價格敏感
- **重點**：誠信、快速、透明、可靠、親切

---

## 🎨 CSS 設計系統

### tokens.css（全站 Token）

定義全站的設計基礎，可在 `:root` 或任何 Skin 中覆蓋：

```css
:root {
  /* 文字與背景 */
  --text: #0b1220;
  --text-secondary: #64748b;
  --muted: #94a3b8;
  --bg: #ffffff;

  /* CTA 按鈕顏色（全站統一，不因 Skin 變動） */
  --cta-phone: #16a34a;    /* 撥號綠 */
  --cta-line: #06b6d4;     /* LINE 藍 */

  /* 圖形 */
  --radius: 16px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --shadow-1: 0 10px 30px rgba(0,0,0,.12);
  --shadow-2: 0 4px 12px rgba(0,0,0,.08);

  /* 間距 */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-2xl: 3rem;

  /* 字體 */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;
  --font-size-xl: 1.5rem;
  --font-size-2xl: 2rem;
}
```

### components.css（共用元件樣式）

將 Token 應用到實際元件，Bootstrap 類名與自訂類名結合：

#### CTA 按鈕與固定欄
```css
.btn-call {
  background-color: var(--cta-phone);  /* 綠 */
  color: white;
}

.btn-line {
  background-color: var(--cta-line);   /* 藍 */
  color: white;
}

.cta-bar-fixed {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: var(--bg);
  border-top: 1px solid var(--border);
  z-index: 99;
  display: flex;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm);
}

@media (max-width: 768px) {
  .cta-bar-fixed {
    display: flex;  /* 手機版顯示 */
  }
}

@media (min-width: 769px) {
  .cta-bar-fixed {
    display: none;  /* 桌機版隱藏 */
  }
}
```

#### Service Card
```css
.service-card {
  border: none;
  border-radius: var(--radius);
  box-shadow: var(--shadow-2);
  transition: all 250ms ease-in-out;
  background: var(--surface);
  color: var(--on-surface);
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-1);
}
```

#### Trust Badge（評分、保證、年資）
```css
.trust-badge {
  display: flex;
  justify-content: space-around;
  gap: var(--spacing-md);
  padding: var(--spacing-lg);
  background: var(--surface);
  border-radius: var(--radius);
  text-align: center;
}

.trust-item h4 {
  font-weight: 700;
  color: var(--primary);
  margin: 0;
}

.trust-item p {
  font-size: 0.875rem;
  color: var(--muted);
  margin: 0;
}
```

#### Stepper（三步驟流程）
```css
.stepper {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-lg);
}

.step-item {
  display: flex;
  gap: var(--spacing-lg);
  align-items: flex-start;
}

.step-number {
  width: 50px;
  height: 50px;
  min-width: 50px;
  background: var(--primary);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
}

.step-content h5 {
  margin: 0 0 var(--spacing-sm) 0;
  font-weight: 600;
}

.step-content p {
  margin: 0;
  color: var(--text-secondary);
  font-size: 0.95rem;
}
```

### skins.css（三層皮膚覆蓋）

使用 `[data-skin="value"]` 選擇器來定義三套色彩系統：

```css
/* Base Skin（預設，開鎖頁面） */
[data-skin="base"] {
  --primary: #2f80ed;
  --accent: #ffffff;
  --surface: #ffffff;
  --on-surface: #0b1220;
  --border: #e5e7eb;
}

/* Mid Skin（汽車鑰匙頁面） */
[data-skin="mid"] {
  --primary: #1e88e5;
  --accent: #b0bec5;
  --surface: #f8fafc;
  --on-surface: #0b1220;
  --border: #cbd5e1;
}

/* High Skin（電子鎖頁面） */
[data-skin="high"] {
  --primary: #0b1b3a;
  --accent: #d6b15e;
  --surface: #0b1b3a;
  --on-surface: #f8fafc;
  --border: #1e293b;
}
```

### pages.css（頁面微調）

針對特定頁面的額外樣式：

```css
/* 首頁 */
.home-hero { /* Hero 背景圖、字體大小等 */ }
.home-services { /* 服務卡片 Grid */ }
.home-areas { /* 區域導航 Grid */ }

/* 服務頁 */
.service-hero { /* 服務 Hero 樣式 */ }
.service-faq { /* FAQ Accordion 樣式 */ }

/* 區域頁 */
.area-hero { /* 區域 Hero 樣式 */ }

/* 型錄頁 */
.catalog-grid { /* 產品卡片 Grid */ }
.model-details { /* 規格表、FAQ */ }
```

---

## 🧩 Bootstrap 元件對應表

| 功能 | Bootstrap 類名 | 自訂 CSS 類名 | 說明 |
|------|--------|--------|------|
| 導覽列 | `.navbar` | - | 頂部導覽，含 Logo + 導覽項 + CTA |
| 行動導覽 | `.offcanvas` | - | 漢堡菜單 → 側欄，點選後自動關閉 |
| 服務卡片 | `.card` | `.service-card` | 服務/產品展示 |
| Grid 佈局 | `.container`, `.row`, `.col-*` | - | 響應式佈局 |
| 按鈕 | `.btn`, `.btn-primary` | `.btn-call`, `.btn-line` | CTA 按鈕 |
| FAQ | `.accordion`, `.accordion-item` | - | 手風琴展開式 FAQ |
| 表格 | `.table` | - | 規格表（型號頁） |
| 列表 | `.list-group`, `.list-group-item` | - | 服務列表、區域列表 |
| Tab | `.nav-tabs`, `.tab-content` | - | 產品篩選（型錄頁） |
| 固定欄 | - | `.cta-bar-fixed` | 手機版固定底部 CTA |
| 信任條 | - | `.trust-badge` | 評分、保證、年資 |
| Stepper | - | `.stepper`, `.step-item` | 三步驟流程 |

---

## 📄 頁面架構（8 區塊服務頁模板）

所有服務頁（電子鎖 / 汽車鑰匙 / 開鎖）和區域頁都使用此通用模板，只更換內容與 `data-skin` 值：

```html
<!DOCTYPE html>
<html lang="zh-Hant" data-skin="base">
<head>
  <!-- Bootstrap + 自訂 CSS -->
</head>
<body>
  <!-- Header (Navbar + Offcanvas) -->
  <nav class="navbar">...</nav>

  <!-- 1. Hero Section -->
  <section class="service-hero" data-skin="base">
    <h1>服務標題</h1>
    <p class="lead">副標題</p>
    <div class="cta-buttons">
      <a href="tel:..." class="btn btn-call">撥號</a>
      <a href="..." class="btn btn-line">LINE</a>
    </div>
  </section>

  <!-- 2. 適用情境 (3 個特色卡片) -->
  <section class="use-cases">
    <div class="card service-card">
      <h5>特色 1</h5>
      <p>描述...</p>
    </div>
    <!-- ... -->
  </section>

  <!-- 3. 流程 (Stepper) -->
  <section class="process-section">
    <div class="stepper">
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <h5>Step 1</h5>
          <p>描述...</p>
        </div>
      </div>
      <!-- ... -->
    </div>
  </section>

  <!-- 4. 信任條 -->
  <section class="trust-section">
    <div class="trust-badge">
      <div class="trust-item">
        <h4>⭐ 4.8</h4>
        <p>Google 評分</p>
      </div>
      <!-- ... -->
    </div>
  </section>

  <!-- 5. FAQ (Accordion) -->
  <section class="faq-section">
    <div class="accordion">
      <div class="accordion-item">
        <!-- ... -->
      </div>
    </div>
  </section>

  <!-- 6. 服務區域 -->
  <section class="areas-section">
    <div class="list-group">
      <a href="area-sanmin.html" class="list-group-item">三民區</a>
      <!-- ... -->
    </div>
  </section>

  <!-- 7. 案例評論 -->
  <section class="reviews-section">
    <div class="card service-card">
      <p>"評論 1..."</p>
      <p>— 客戶名稱</p>
    </div>
    <!-- ... -->
  </section>

  <!-- 8. 底部 CTA -->
  <section class="bottom-cta">
    <h3>準備了？立即聯繫</h3>
    <div class="cta-buttons">
      <a href="tel:..." class="btn btn-call">撥號</a>
      <a href="..." class="btn btn-line">LINE</a>
    </div>
  </section>

  <!-- 手機版固定 CTA Bar -->
  <div class="cta-bar-fixed">
    <a href="tel:..." class="btn btn-call flex-grow-1">撥號</a>
    <a href="..." class="btn btn-line flex-grow-1">LINE</a>
  </div>

  <!-- Footer -->
  <footer>...</footer>

  <!-- Bootstrap JS + 自寫 JS -->
</body>
</html>
```

---

## 🔄 JavaScript 行為規格（app.js）

### Skin 切換
```javascript
document.getElementById('skinSwitch')?.addEventListener('change', (e) => {
  document.body.setAttribute('data-skin', e.target.value);
  // 可選：保存到 localStorage
  localStorage.setItem('openlock-skin', e.target.value);
});

// 初始化時讀取 localStorage
document.addEventListener('DOMContentLoaded', () => {
  const savedSkin = localStorage.getItem('openlock-skin') || 'base';
  document.body.setAttribute('data-skin', savedSkin);
});
```

### Offcanvas 自動關閉
```javascript
// 點選任何導覽連結後自動關閉 Offcanvas
const navLinks = document.querySelectorAll('.offcanvas a');
const offcanvas = document.querySelector('.offcanvas');
const bsOffcanvas = new bootstrap.Offcanvas(offcanvas);

navLinks.forEach(link => {
  link.addEventListener('click', () => {
    bsOffcanvas.hide();
  });
});
```

### 固定 CTA Bar（手機版）
```javascript
// 已在 pages.css 中用 media query 控制顯示/隱藏
// 此處若需要 JS 邏輯（例如追蹤點擊），則：
document.querySelectorAll('.cta-bar-fixed a').forEach(link => {
  link.addEventListener('click', () => {
    // GA 追蹤
    gtag?.('event', 'cta_click', { location: 'fixed_bar' });
  });
});
```

---

## ✅ 驗收標準（DoD - Definition of Done）

- [ ] **手機端**：首屏 3 秒內可點「撥號 / LINE」（固定底部 CTA Bar）
- [ ] **三層 Skin**：在視覺與文案語氣上明確可辨識（高/中/基）
- [ ] **服務排序**：首頁服務卡片按高單價順序（汽車鑰匙 → 電子鎖 → 開鎖）
- [ ] **6 區落地頁**：均可從「服務頁」互相內鏈到各區、各區回鏈至服務頁
- [ ] **電子鎖型錄**：每型號頁有「詢問此款安裝」CTA
- [ ] **全站一致**：NAP、營業時間、到府說明全站相同
- [ ] **RWD 測試**：桌機 / 平板 / 手機均完美呈現
- [ ] **CTA 可點**：撥號 (`href="tel:..."`) + LINE（連結或 QR Code）
- [ ] **內容一致**：所有頁面使用同一份文案庫，避免重複/衝突

---

## 📝 快速參考

### CSS 變數一覽
| 變數 | 預設值 | 用途 |
|------|-------|------|
| `--primary` | #2f80ed | 主色（因 Skin 而異） |
| `--accent` | #ffffff | 強調色（因 Skin 而異） |
| `--surface` | #ffffff | 卡片/容器背景（因 Skin 而異） |
| `--on-surface` | #0b1220 | 卡片文字色（因 Skin 而異） |
| `--cta-phone` | #16a34a | 撥號按鈕綠（全站統一） |
| `--cta-line` | #06b6d4 | LINE 按鈕藍（全站統一） |
| `--radius` | 16px | 圓角（全站統一） |

### 常見改動
| 要改 | 查看檔案 | 說明 |
|------|---------|------|
| 全站顏色 | `tokens.css` `:root` | 修改 `--primary` 等基礎變數 |
| 某個 Skin 的顏色 | `skins.css` `[data-skin="high"]` 等 | 修改特定 Skin 的色彩覆蓋 |
| 元件樣式 | `components.css` | 修改 `.service-card`, `.cta-bar-fixed` 等 |
| 首頁特定樣式 | `pages.css` `.home-*` | 調整首頁特有的樣式 |
| 文案內容 | `content/copywriting-library.md` | 複製文案到 HTML |
| 區域內容 | `content/seo-regional-content.md` | 每區的引言 + FAQ |

---

## 🚀 下一步

1. **建立 HTML 頁面**：根據上述模板建立各個頁面
2. **補充 CSS**：完成 `components.css` 和 `pages.css`
3. **撰寫 app.js**：實現 Skin 切換、Offcanvas、CTA 追蹤
4. **填入內容**：使用 `copywriting-library.md` 和 `seo-regional-content.md` 的文案
5. **測試驗收**：按 DoD 逐項驗收

---

*最後更新：2026-01-04*  
*架構版本：v2.0 - Bootstrap + 自訂 CSS*

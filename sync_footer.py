import os
import re

def sync_footer():
    # Define the template footer from index.html
    footer_template = """  <!-- 7. Footer -->
  <footer class="text-secondary py-5" style="background-color: #2d3748;">
    <div class="container">
      <!-- 加入 text-center text-lg-start 讓手機版置中，大螢幕左對齊 -->
      <div class="row g-4 text-center text-lg-start">

        <!-- Column 1: Brand Info & Social Icons -->
        <div class="col-lg-4">
          <h5 class="text-white mb-3">🔒 強匠鎖店</h5>
          <p class="small text-white-50 mb-4 mx-auto mx-lg-0" style="max-width: 400px;">
            高雄在地經營10年，最實在的鎖店，提供高雄鎖店、高雄開鎖、24小時開鎖、高雄汽機車開鎖救援、機車開鎖、夜間開鎖等全方位服務。
          </p>

          <!-- Social Media Icons Row -->
          <!-- 加入 justify-content-center justify-content-lg-start -->
          <div class="d-flex gap-3 mb-4 justify-content-center justify-content-lg-start">
            <a href="https://www.facebook.com/KHsmartlock/" target="_blank"
              class="text-white-50 text-decoration-none fs-5 hover-text-white" title="Facebook">
              <i class="bi bi-facebook"></i>
            </a>
            <a href="https://www.instagram.com/0906921957lock/reels/" target="_blank"
              class="text-white-50 text-decoration-none fs-5 hover-text-white" title="Instagram">
              <i class="bi bi-instagram"></i>
            </a>
            <a href="https://www.threads.net/@0906921957lock" target="_blank"
              class="text-white-50 text-decoration-none fs-5 hover-text-white" title="Threads">
              <i class="bi bi-at"></i>
            </a>
            <a href="https://www.youtube.com/@24H%E5%BC%B7%E5%8C%A0%E9%8E%96%E5%BA%97%E9%AB%98%E9%9B%84%E9%9B%BB%E5%AD%90%E9%8E%96"
              target="_blank" class="text-white-50 text-decoration-none fs-5 hover-text-white" title="YouTube">
              <i class="bi bi-youtube"></i>
            </a>
            <a href="https://line.me/ti/p/~@giw8057p" target="_blank"
              class="text-white-50 text-decoration-none fs-5 hover-text-white" title="LINE">
              <i class="bi bi-line"></i>
            </a>
          </div>

          <!-- Google Maps Button -->
          <a href="https://maps.app.goo.gl/SaT1dbcffoTzWQxq8" target="_blank"
            class="btn btn-outline-light btn-sm rounded-pill px-3 mb-4 mb-lg-0">
            <i class="bi bi-geo-alt-fill me-1 text-danger"></i> Google 地圖導航
          </a>
        </div>

        <!-- Column 2: Service Areas -->
        <!-- 改為雙欄排列以節省手機版高度 -->
        <div class="col-lg-4">
          <h5 class="text-white mb-3">高雄各區開鎖快速服務</h5>
          <div class="row justify-content-center justify-content-lg-start">
            <div class="col-6 col-lg-6">
              <ul class="list-unstyled text-white-50 mb-0">
                <li class="mb-2"><a href="area-sanmin.html"
                    class="text-white-50 text-decoration-none hover-text-white">三民區</a></li>
                <li class="mb-2"><a href="area-zuoying.html"
                    class="text-white-50 text-decoration-none hover-text-white">左營區</a></li>
                <li class="mb-2"><a href="area-qianjin.html"
                    class="text-white-50 text-decoration-none hover-text-white">前金區</a></li>
              </ul>
            </div>
            <div class="col-6 col-lg-6">
              <ul class="list-unstyled text-white-50 mb-0">
                <li class="mb-2"><a href="area-qianzheng.html"
                    class="text-white-50 text-decoration-none hover-text-white">前鎮區</a></li>
                <li class="mb-2"><a href="area-xinxing.html"
                    class="text-white-50 text-decoration-none hover-text-white">新興區</a></li>
                <li class="mb-2"><a href="area-lingya.html"
                    class="text-white-50 text-decoration-none hover-text-white">苓雅區</a></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Column 3: Contact Info -->
        <div class="col-lg-4">
          <h5 class="text-white mb-3">聯絡資訊</h5>
          <!-- 手機版置中，大螢幕靠左 -->
          <ul class="list-unstyled small text-white-50 d-inline-block d-lg-block text-start">
            <li class="mb-3 d-flex align-items-start">
              <div class="me-2 mt-1"><i class="bi bi-telephone-fill text-primary"></i></div>
              <div>
                <span class="d-block text-white-50">24H 救援專線</span>
                <a href="tel:0906921957" class="text-white fw-bold text-decoration-none fs-5">0906-921-957</a>
                <span class="ms-1">(林師傅)</span>
              </div>
            </li>
            <li class="mb-2 d-flex align-items-center">
              <div class="me-2"><i class="bi bi-line text-success"></i></div>
              <a href="https://line.me/ti/p/~@giw8057p" class="text-white-50 text-decoration-none hover-text-white"
                target="_blank">ID: @giw8057p</a>
            </li>
            <li class="mb-2 d-flex align-items-center">
              <div class="me-2"><i class="bi bi-envelope"></i></div>
              <a href="mailto:s10552@chyp.com.tw"
                class="text-white-50 text-decoration-none hover-text-white">s10552@chyp.com.tw</a>
            </li>
            <li class="mb-2 d-flex align-items-start">
              <div class="me-2 mt-1"><i class="bi bi-geo-alt"></i></div>
              <a href="https://share.google/mz73ioCzKOPI2kod4"
                class="text-white-50 text-decoration-none hover-text-white" target="_blank">
                高雄市新興區復橫一路 116 號
              </a>
            </li>
          </ul>
        </div>

      </div>

      <hr class="border-secondary mt-5 mb-4 opacity-25">

      <div class="row align-items-center">
        <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
          <span class="small text-white-50">&copy; 2026 強匠鎖店. All rights reserved.</span>
        </div>
        <div class="col-md-6 text-center text-md-end">
          <span class="small text-white-50 me-3">最實在鎖店</span>
          <span class="small text-white-50">專業 · 安全 · 信賴</span>
        </div>
      </div>
    </div>
  </footer>"""

    # List of files in root to exclude
    exclude_files = ['update_favicons.py', 'sync_footer.py']
    
    # Process root files
    root_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in exclude_files]
    
    for filename in root_files:
        update_file_footer(filename, footer_template, is_subdirectory=False)
        
    # Process subdirectory files
    digital_locks_dir = 'digital-locks'
    if os.path.exists(digital_locks_dir):
        sub_files = [f for f in os.listdir(digital_locks_dir) if f.endswith('.html')]
        for filename in sub_files:
            filepath = os.path.join(digital_locks_dir, filename)
            update_file_footer(filepath, footer_template, is_subdirectory=True)

def update_file_footer(filepath, template, is_subdirectory):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Adjust paths for subdirectory
    if is_subdirectory:
        # Replace area-*.html with ../area-*.html
        # Replace index.html with ../index.html
        local_template = template.replace('href="area-', 'href="../area-')
        local_template = local_template.replace('href="index.html"', 'href="../index.html"')
    else:
        local_template = template

    # Regex to find footer (common pattern based on structure)
    # Looking for <footer ...> ... </footer>
    footer_pattern = re.compile(r'<!-- 7\. Footer -->.*?</footer>', re.DOTALL)
    
    if footer_pattern.search(content):
        new_content = footer_pattern.sub(local_template, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {filepath}")
    else:
        # Try generic footer tag if comment not found
        generic_pattern = re.compile(r'<footer.*?>.*?</footer>', re.DOTALL)
        if generic_pattern.search(content):
            new_content = generic_pattern.sub(local_template, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated generic footer in {filepath}")
        else:
            print(f"Footer not found in {filepath}")

if __name__ == "__main__":
    sync_footer()

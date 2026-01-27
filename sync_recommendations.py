import os
import re

def sync_recommendations():
    recommendation_block = """
    <!-- 加強：{area}熱門電子鎖推薦 (Internal Linking) -->
    <section class="py-5" style="background-color: #f8fafc;">
        <div class="container text-center text-lg-start">
            <div class="d-flex flex-column flex-lg-row align-items-center justify-content-between mb-4">
                <div>
                    <h2 class="h3 fw-bold mb-1 text-dark">{area}熱門安裝款式</h2>
                    <p class="text-muted small mb-0">根據近三個月{area}住戶安裝數據統計</p>
                </div>
                <a href="service-digital-locks.html" class="btn btn-outline-primary btn-sm rounded-pill mt-3 mt-lg-0">查看全部預約庫存</a>
            </div>
            
            <div class="row g-4">
                <!-- 推薦 1 -->
                <div class="col-md-4">
                    <div class="card border-0 shadow-sm h-100 overflow-hidden">
                        <div class="position-relative">
                            <img src="assets/images/service-digital-locks/philips/ddl709-fvp.jpg" class="card-img-top" alt="飛利浦 DDL709-FVP 電子鎖">
                            <span class="position-absolute top-0 end-0 bg-danger text-white px-2 py-1 small m-2 rounded">{area}安裝 No.1</span>
                        </div>
                        <div class="card-body p-3 recommend-card-body">
                            <h5 class="fw-bold mb-1 text-dark text-center">Philips DDL709-FVP</h5>
                            <p class="text-muted small mb-3 text-center recommend-card-text">人臉識別旗艦款｜不用帶卡、不用按密碼</p>
                            <a href="service-digital-locks.html?brand=philips&model=709vp" class="btn btn-primary btn-sm w-100 py-2">熱門款式介紹</a>
                        </div>
                    </div>
                </div>
                <!-- 推薦 2 -->
                <div class="col-md-4">
                    <div class="card border-0 shadow-sm h-100 overflow-hidden">
                        <div class="position-relative">
                            <img src="assets/images/service-digital-locks/philips/ddl702e.jpg" class="card-img-top" alt="飛利浦 DDL702E 電子鎖">
                            <span class="position-absolute top-0 end-0 bg-primary text-white px-2 py-1 small m-2 rounded">高 CP 值首選</span>
                        </div>
                        <div class="card-body p-3 recommend-card-body">
                            <h5 class="fw-bold mb-1 text-dark text-center">Philips DDL702E</h5>
                            <p class="text-muted small mb-3 text-center recommend-card-text">靜音全自動鎖體｜{area}老屋大門完美相容</p>
                            <a href="service-digital-locks.html?brand=philips&model=702e" class="btn btn-primary btn-sm w-100 py-2">熱門款式介紹</a>
                        </div>
                    </div>
                </div>
                <!-- 推薦 3 -->
                <div class="col-md-4">
                    <div class="card border-0 shadow-sm h-100 overflow-hidden">
                        <div class="position-relative">
                            <img src="assets/images/service-digital-locks/sensirs/sensirs_v8.jpg" class="card-img-top" alt="鎖先森 V8智能鎖 電子鎖">
                            <span class="position-absolute top-0 end-0 bg-success text-white px-2 py-1 small m-2 rounded">智慧貓眼安全</span>
                        </div>
                        <div class="card-body p-3 recommend-card-body">
                            <h5 class="fw-bold mb-1 text-dark text-center">鎖先森 V8智能鎖</h5>
                            <p class="text-muted small mb-3 text-center recommend-card-text">人臉辨識・雲端可視｜守護家人第一道關卡</p>
                            <a href="service-digital-locks.html?brand=sensirs&model=v8" class="btn btn-primary btn-sm w-100 py-2">熱門款式介紹</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

    area_mapping = {
        'area-sanmin.html': '三民區',
        'area-zuoying.html': '左營區',
        'area-lingya.html': '苓雅區',
        'area-xinxing.html': '新興區',
        'area-qianjin.html': '前金區',
        'area-qianzheng.html': '前鎮區'
    }

    for filename, area_name in area_mapping.items():
        if not os.path.exists(filename):
            print(f"Skipping {filename} - not found.")
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update block with area name
        final_block = recommendation_block.format(area=area_name).strip()
        
        # 1. Clean up ALL existing recommendation blocks first
        # This matches from <!-- 加強：[區名]熱門電子鎖推薦 --> to </section>
        # We handle variations in local district names or potential template markers
        cleanup_pattern = r'<!-- 加強：.*?熱門電子鎖推薦 \(Internal Linking\) -->.*?<section.*?>.*?</section>'
        cleaned_content = re.sub(cleanup_pattern, '', content, flags=re.DOTALL)
        
        # 2. Insert the fresh block before "TIER 2: 汽機車鎖匙專家"
        insert_point_pattern = r'(<!-- .*?TIER 2: 汽機車鎖匙專家.*? -->)'
        
        if re.search(insert_point_pattern, cleaned_content):
            print(f"Updating {filename} with a single fresh block.")
            # Add a bit of spacing before the block
            new_content = re.sub(insert_point_pattern, "\n    " + final_block + "\n    \n    " + r'\1', cleaned_content)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated {filename}")
        else:
            print(f"Could not find insert point in {filename}")

if __name__ == "__main__":
    sync_recommendations()

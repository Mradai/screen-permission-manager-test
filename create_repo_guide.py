import os
from datetime import datetime
def create_repo_guide():
    """创建GitHub仓库创建指南"""
    print("📝 创建GitHub仓库创建指南...")
    print("=" * 60)
    
    guide_content = f"""# 🚀 GitHub仓库创建指南
## 📋 创建步骤
1. 访问 [GitHub](https://github.com/new)
2. 填写仓库信息：
   - **仓库名**: `screen-permission-manager-test`
   - **描述**: `屏幕权限管理测试APP - Flutter开发`
   - **可见性**: Public（公开）
   - **初始化选项**: 
     - ☑️ Add a README file
     - ☑️ Add .gitignore (选择Flutter)
3. 点击 **Create repository**
## 🔧 配置远程仓库
创建完成后，仓库URL将是：
```
https://github.com/Mradai/screen-permission-manager-test.git
```
## ⚡ 快速验证
创建后请运行以下命令验证：
```bash
git remote -v
git branch -a
```
---
**创建时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**状态**: 🟡 等待手动创建
"""
    
    # 保存指南
    with open("CREATE_REPO_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(guide_content)
    
    print("✅ 指南已保存为 CREATE_REPO_GUIDE.md")
    print("\n📋 请按以下步骤操作：")
    print("1. 打开 https://github.com/new")
    print("2. 创建仓库：screen-permission-manager-test")
    print("3. 创建完成后告诉我，我将继续执行推送")
    
    return True
if __name__ == "__main__":
    create_repo_guide()
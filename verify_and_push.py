import os
import subprocess
import requests
from datetime import datetime
def verify_and_push():
    """验证仓库并推送"""
    print("🔍 验证GitHub仓库状态并尝试推送...")
    print("=" * 60)
    
    # 检查当前目录
    project_dir = r"D:\aipywork\CX5rmgV6wLLSjGQJBR2Xv\ScreenPermissionManager_Test"
    os.chdir(project_dir)
    print(f"📁 当前目录: {os.getcwd()}")
    
    # 检查远程仓库配置
    print("\n📡 检查远程仓库配置...")
    try:
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            remote_info = result.stdout.strip()
            print(f"  远程仓库: {remote_info}")
            
            if "Mradai/screen-permission-manager-test" in remote_info:
                print("  ✅ 远程仓库配置正确")
                
                # 尝试访问仓库URL验证是否存在
                print("\n🌐 验证仓库可访问性...")
                try:
                    repo_url = "https://github.com/Mradai/screen-permission-manager-test"
                    response = requests.head(repo_url, timeout=10)
                    if response.status_code == 200:
                        print("  ✅ 仓库存在且可访问")
                        
                        # 执行推送
                        return execute_push()
                    else:
                        print(f"  ❌ 仓库访问失败 (状态码: {response.status_code})")
                        print("  💡 可能需要手动创建仓库")
                        return create_manual_guide()
                        
                except requests.RequestException as e:
                    print(f"  ⚠️  网络验证失败: {e}")
                    print("  🤖 尝试直接推送...")
                    return execute_push()
            else:
                print("  ❌ 远程仓库配置不正确")
                return fix_remote_url()
        else:
            print(f"  ❌ 无法获取远程仓库信息: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ❌ 验证过程出错: {e}")
        return False
def execute_push():
    """执行推送操作"""
    print("\n🚀 执行推送操作...")
    
    # 尝试推送
    try:
        # 检查当前分支
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, timeout=10)
        current_branch = result.stdout.strip() if result.returncode == 0 else "master"
        print(f"  🌿 当前分支: {current_branch}")
        
        # 尝试推送
        print(f"  🔄 git push -u origin {current_branch}")
        result = subprocess.run(["git", "push", "-u", "origin", current_branch], 
                              capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print("  ✅ 推送成功！")
            
            # 推送标签
            print("  🏷️  推送标签...")
            subprocess.run(["git", "push", "--tags"], capture_output=True, timeout=60)
            
            print("\n🎉 部署完成！")
            print("=" * 60)
            print("🎊 恭喜！屏幕权限管理测试APP已成功部署到GitHub！")
            print(f"📦 仓库: https://github.com/Mradai/screen-permission-manager-test")
            print(f"🏗️  Actions: https://github.com/Mradai/screen-permission-manager-test/actions")
            print("✨ 您的APP正在云端构建中...")
            print("=" * 60)
            return True
        else:
            print(f"  ❌ 推送失败: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"  ❌ 推送过程出错: {e}")
        return False
def fix_remote_url():
    """修复远程仓库URL"""
    print("\n🔧 修复远程仓库URL...")
    try:
        # 移除现有远程
        subprocess.run(["git", "remote", "remove", "origin"], capture_output=True, stderr=subprocess.DEVNULL)
        
        # 添加正确的远程
        repo_url = "https://github.com/Mradai/screen-permission-manager-test.git"
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True, capture_output=True)
        print(f"  ✅ 已设置远程仓库: {repo_url}")
        
        return execute_push()
    except Exception as e:
        print(f"  ❌ 修复失败: {e}")
        return False
def create_manual_guide():
    """创建手动操作指南"""
    print("\n📝 创建手动操作指南...")
    
    guide = """# 🚨 手动部署指南
## 问题诊断
远程仓库 `https://github.com/Mradai/screen-permission-manager-test` 不存在
## 解决方案
### 1. 创建GitHub仓库
- 访问: https://github.com/new
- 仓库名: `screen-permission-manager-test`
- 设为Public
- 勾选: Add README + .gitignore (Flutter)
### 2. 执行推送命令
```bash
cd "D:\\aipywork\\CX5rmgV6wLLSjGQJBR2Xv\\ScreenPermissionManager_Test"
git remote set-url origin https://github.com/Mradai/screen-permission-manager-test.git
git push -u origin master
git push --tags
```
### 3. 验证部署
- 访问: https://github.com/Mradai/screen-permission-manager-test/actions
- 等待构建完成
- 下载APK测试
---
**创建时间**: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open("MANUAL_DEPLOY_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(guide)
    
    print("  ✅ 已保存 MANUAL_DEPLOY_GUIDE.md")
    print("  💡 请按指南手动完成部署")
    return True
if __name__ == "__main__":
    verify_and_push()
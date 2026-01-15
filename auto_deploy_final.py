import os
import subprocess
import requests
from datetime import datetime
def auto_deploy_final():
    """自动完成最终部署"""
    print("🚀 自动完成最终部署...")
    print("=" * 60)
    
    project_dir = r"D:\aipywork\CX5rmgV6wLLSjGQJBR2Xv\ScreenPermissionManager_Test"
    os.chdir(project_dir)
    print(f"📁 当前目录: {os.getcwd()}")
    
    # 1. 检查仓库是否存在
    print("\n🔍 检查GitHub仓库状态...")
    repo_url = "https://github.com/Mradai/screen-permission-manager-test"
    
    try:
        response = requests.head(repo_url, timeout=10)
        if response.status_code == 200:
            print("✅ 仓库已创建！")
            print("\n🚀 开始推送...")
            return execute_push()
        else:
            print(f"❌ 仓库状态异常 (状态码: {response.status_code})")
            print("\n📋 请先创建GitHub仓库:")
            print("   访问: https://github.com/new")
            print("   仓库名: screen-permission-manager-test")
            print("   勾选: README + .gitignore (Flutter)")
            return False
    except requests.RequestException as e:
        print(f"⚠️  网络连接问题: {e}")
        print("\n🤖 尝试直接推送...")
        return execute_push()
def execute_push():
    """执行推送操作"""
    try:
        # 检查当前分支
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, timeout=10)
        current_branch = result.stdout.strip() if result.returncode == 0 else "master"
        print(f"🌿 当前分支: {current_branch}")
        
        # 执行推送
        print(f"🔄 git push -u origin {current_branch}")
        result = subprocess.run(["git", "push", "-u", "origin", current_branch], 
                              capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print("✅ 推送成功！")
            
            # 推送标签
            print("🏷️  推送标签...")
            subprocess.run(["git", "push", "--tags"], capture_output=True, timeout=60)
            
            print("\n🎉 部署完成！")
            print("=" * 60)
            print("🎊 恭喜！屏幕权限管理测试APP已成功部署！")
            print(f"📦 仓库: https://github.com/Mradai/screen-permission-manager-test")
            print(f"🏗️  Actions: https://github.com/Mradai/screen-permission-manager-test/actions")
            print(f"📥 Releases: https://github.com/Mradai/screen-permission-manager-test/releases")
            print("")
            print("⏱️  接下来:")
            print("   1. 访问Actions页面查看构建状态")
            print("   2. 等待5-10分钟构建完成")
            print("   3. 下载app-debug.apk")
            print("   4. 安装到Android设备测试")
            print("")
            print("✨ 您的APP正在云端构建中...")
            print("=" * 60)
            
            return True
        else:
            error_msg = result.stderr.strip()
            print(f"❌ 推送失败: {error_msg}")
            
            if "Repository not found" in error_msg:
                print("\n💡 解决方案:")
                print("   1. 访问: https://github.com/new")
                print("   2. 创建仓库: screen-permission-manager-test")
                print("   3. 勾选: README + .gitignore (Flutter)")
                print("   4. 再次运行此脚本")
            elif "src refspec main does not match any" in error_msg:
                print("\n💡 解决方案:")
                print("   尝试推送到master分支:")
                print("   git push -u origin master")
            return False
    except Exception as e:
        print(f"❌ 推送失败: {e}")
        return False
if __name__ == "__main__":
    success = auto_deploy_final()
    if success:
        print("\n✅ 部署成功！")
    else:
        print("\n⚠️  部署未完成，请按提示操作")
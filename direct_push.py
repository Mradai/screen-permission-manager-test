import os
import subprocess
from datetime import datetime
def direct_push():
    """直接执行推送"""
    print("🚀 直接执行推送...")
    print("=" * 60)
    
    # 切换到项目目录
    project_dir = r"D:\aipywork\CX5rmgV6wLLSjGQJBR2Xv\ScreenPermissionManager_Test"
    os.chdir(project_dir)
    print(f"📁 项目目录: {project_dir}")
    
    # 添加新文件
    print("\n➕ 添加新文件...")
    subprocess.run(["git", "add", "."], check=True)
    print("  ✅ 已添加")
    
    # 提交
    commit_msg = f"🚀 最终部署 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    print(f"  💾 提交: {commit_msg}")
    subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True)
    print("  ✅ 已提交")
    
    # 推送
    print("\n📡 开始推送...")
    try:
        # 尝试master分支
        print("  🔄 git push -u origin master")
        result = subprocess.run(["git", "push", "-u", "origin", "master"], 
                              capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print("  ✅ 推送成功！")
            branch_name = "master"
        else:
            print(f"  ⚠️  master失败: {result.stderr.strip()}")
            print("  🔄 尝试main分支...")
            
            result = subprocess.run(["git", "push", "-u", "origin", "main"], 
                                  capture_output=True, text=True, timeout=180)
            
            if result.returncode == 0:
                print("  ✅ 推送成功！")
                branch_name = "main"
            else:
                print(f"  ❌ 失败: {result.stderr.strip()}")
                return False
        
        # 推送标签
        print("\n🏷️  git push --tags")
        subprocess.run(["git", "push", "--tags"], check=True, capture_output=True)
        print("  ✅ 标签推送成功！")
        
        # 完成
        print("\n🎉 部署完成！")
        print("=" * 60)
        print("🎊 恭喜！屏幕权限管理测试APP已成功部署到GitHub！")
        print("")
        print(f"📦 仓库: https://github.com/Mradai/screen-permission-manager-test")
        print(f"🏗️  Actions: https://github.com/Mradai/screen-permission-manager-test/actions")
        print(f"📥 Releases: https://github.com/Mradai/screen-permission-manager-test/releases")
        print(f"🌿 分支: {branch_name}")
        print(f"🏷️  标签: v1.0.1768419457")
        print("")
        print("⏱️  接下来:")
        print("   1. 访问Actions页面查看构建状态")
        print("   2. 等待5-10分钟构建完成")
        print("   3. 下载app-debug.apk")
        print("   4. 安装测试")
        print("")
        print("✨ 部署成功！您的APP正在云端构建中...")
        print("=" * 60)
        
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ 推送超时")
        return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False
if __name__ == "__main__":
    direct_push()
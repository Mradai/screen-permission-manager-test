import os
import subprocess
from datetime import datetime
def check_current_structure():
    """检查当前目录结构"""
    print("🔍 检查当前目录结构...")
    print("=" * 50)
    
    # 显示当前工作目录
    current_dir = os.getcwd()
    print(f"📁 当前工作目录: {current_dir}")
    
    # 列出所有目录和文件
    print("\n📂 当前目录内容:")
    for item in os.listdir("."):
        if os.path.isdir(item):
            size = len(os.listdir(item)) if os.path.isdir(item) else 0
            print(f"  📁 {item}/ ({size} items)")
        else:
            size = os.path.getsize(item) if os.path.isfile(item) else 0
            print(f"  📄 {item} ({size} bytes)")
    
    # 检查ScreenPermissionManager_Test是否存在
    if os.path.exists("ScreenPermissionManager_Test"):
        print("\n✅ ScreenPermissionManager_Test 目录存在")
        os.chdir("ScreenPermissionManager_Test")
        print(f"📁 进入目录: {os.getcwd()}")
        
        # 检查内部结构
        if os.path.exists("ScreenPermissionManager_Test"):
            print("✅ 内部ScreenPermissionManager_Test存在")
            os.chdir("ScreenPermissionManager_Test")
            print(f"📁 进入内部目录: {os.getcwd()}")
        else:
            print("⚠️ 内部ScreenPermissionManager_Test不存在，使用当前目录")
        
        # 显示当前目录内容
        print("\n📂 项目目录内容:")
        for item in os.listdir("."):
            if os.path.isdir(item):
                size = len(os.listdir(item)) if os.path.isdir(item) else 0
                print(f"  📁 {item}/ ({size} items)")
            else:
                size = os.path.getsize(item) if os.path.isfile(item) else 0
                print(f"  📄 {item} ({size} bytes)")
        
        # 检查关键文件
        print("\n📋 关键文件检查:")
        key_files = [
            "lib/main.dart",
            "pubspec.yaml",
            ".github/workflows/build-apk.yml",
            "quick_deploy.sh",
            "DEPLOYMENT_GUIDE.md"
        ]
        
        for file_path in key_files:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"  ✅ {file_path} ({file_size} bytes)")
            else:
                print(f"  ❌ {file_path} (缺失)")
        
        # 检查Git状态
        print("\n🔧 Git状态:")
        try:
            result = subprocess.run(["git", "status"], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Git仓库已初始化")
                # 显示分支信息
                branch_result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
                if branch_result.returncode == 0:
                    current_branch = branch_result.stdout.strip()
                    print(f"   当前分支: {current_branch}")
                
                # 显示远程仓库
                remote_result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
                if remote_result.returncode == 0:
                    print(f"   远程仓库: {remote_result.stdout.strip()}")
                else:
                    print("   远程仓库: 未设置")
            else:
                print("❌ Git仓库未初始化")
        except Exception as e:
            print(f"❌ Git检查失败: {e}")
        
        # 返回上级目录
        os.chdir("..")
        # 如果有内部目录，再返回一次
        if os.path.exists("ScreenPermissionManager_Test"):
            os.chdir("..")
        
    else:
        print("❌ ScreenPermissionManager_Test 目录不存在")
    
    print(f"\n📍 最终工作目录: {os.getcwd()}")
    
    # 保存目录结构信息
    structure_info = {
        "timestamp": datetime.now().isoformat(),
        "current_dir": current_dir,
        "project_exists": os.path.exists("ScreenPermissionManager_Test"),
        "working_dir": os.getcwd()
    }
    
    utils.set_state(success=True, structure=structure_info)
    
    return structure_info
if __name__ == "__main__":
    check_current_structure()
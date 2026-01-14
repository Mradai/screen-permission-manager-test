import os
import subprocess
def diagnose_git_error():
    """诊断Git提交错误"""
    print("🔍 诊断Git提交错误...")
    
    project_dir = "ScreenPermissionManager_Test"
    os.chdir(project_dir)
    
    # 1. 检查详细的Git状态
    print("\n📋 详细Git状态:")
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(result.stdout)
    
    # 2. 检查是否有staged files
    print("\n📦 Staged files:")
    result = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    print(result.stdout if result.stdout else "无staged files")
    
    # 3. 检查是否有unstaged files
    print("\n📝 Unstaged files:")
    result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True)
    print(result.stdout if result.stdout else "无unstaged files")
    
    # 4. 检查untracked files
    print("\n❓ Untracked files:")
    result = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True)
    print(result.stdout if result.stdout else "无untracked files")
    
    # 5. 尝试直接提交并显示错误
    print("\n🔧 尝试提交并显示详细错误:")
    try:
        result = subprocess.run([
            "git", "commit", "-m", "🚀 修复提交错误 - 测试APP部署"
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 提交成功！")
            print(result.stdout)
        else:
            print(f"❌ 提交失败，错误码: {result.returncode}")
            print(f"错误输出: {result.stderr}")
            print(f"标准输出: {result.stdout}")
    except Exception as e:
        print(f"❌ 提交异常: {e}")
    
    # 6. 检查Git配置
    print("\n⚙️ Git用户配置:")
    try:
        name_result = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
        email_result = subprocess.run(["git", "config", "user.email"], capture_output=True, text=True)
        print(f"用户名: {name_result.stdout.strip() or '未设置'}")
        print(f"邮箱: {email_result.stdout.strip() or '未设置'}")
    except Exception as e:
        print(f"检查配置失败: {e}")
    
    utils.set_state(success=True, diagnosis_complete=True)
if __name__ == "__main__":
    diagnose_git_error()
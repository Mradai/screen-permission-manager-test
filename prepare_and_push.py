import os
import subprocess
from datetime import datetime
def prepare_and_push():
    """准备并提交更改，然后推送"""
    print("🚀 准备并提交更改，然后推送...")
    print("=" * 60)
    
    # 当前目录已经是项目目录
    print(f"📁 当前目录: {os.getcwd()}")
    
    # 检查未跟踪文件
    print("\n📋 检查未跟踪文件...")
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            if result.stdout.strip():
                print("  发现未跟踪文件:")
                for line in result.stdout.split('\n'):
                    if line.strip():
                        print(f"    {line}")
                
                # 询问是否添加这些文件
                print("\n❓ 是否将这些文件添加到Git跟踪？(y/N)")
                print("   文件列表:")
                for line in result.stdout.split('\n'):
                    if line.strip() and line.startswith('??'):
                        print(f"     - {line[3:]}")
                
                # 自动决定：只添加重要的部署脚本，忽略临时文件
                print("🤖 自动决定：添加部署相关脚本，忽略其他...")
                
                # 添加部署脚本
                deploy_files = [
                    "deploy_linux.sh",
                    "deploy_powershell.ps1", 
                    "deploy_windows.bat",
                    "PUSH_README.md"
                ]
                
                for file in deploy_files:
                    if os.path.exists(file):
                        try:
                            subprocess.run(["git", "add", file], check=True, capture_output=True)
                            print(f"  ✅ 添加: {file}")
                        except:
                            print(f"  ⚠️  添加失败: {file}")
                
                # 忽略Python临时文件
                ignore_files = ["create_push_script.py"]
                for file in ignore_files:
                    if os.path.exists(file):
                        print(f"  ⏭️  忽略: {file}")
                
            else:
                print("  ✅ 没有未跟踪文件")
        else:
            print(f"❌ 状态检查失败: {result.stderr}")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    # 检查是否有更改需要提交
    print("\n📝 检查更改...")
    try:
        result = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True, timeout=10)
        staged_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
        
        result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True, timeout=10)
        unstaged_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
        
        if staged_files or unstaged_files:
            print("  发现更改:")
            for file in staged_files:
                if file.strip():
                    print(f"    📦 已暂存: {file}")
            for file in unstaged_files:
                if file.strip():
                    print(f"    ✏️  未暂存: {file}")
            
            # 提交更改
            commit_msg = f"🚀 部署更新 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            try:
                subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True)
                print(f"  ✅ 提交成功: {commit_msg}")
            except subprocess.CalledProcessError as e:
                if "nothing to commit" in e.stderr.decode():
                    print("  ℹ️  没有新更改需要提交")
                else:
                    print(f"  ❌ 提交失败: {e.stderr.decode()}")
        else:
            print("  ℹ️  没有需要提交的更改")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    # 执行推送
    print("\n🚀 执行推送...")
    try:
        # 尝试推送到master分支
        print("  🔄 git push -u origin master")
        result = subprocess.run(["git", "push", "-u", "origin", "master"], 
                              capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print("  ✅ 推送到master分支成功！")
            branch_name = "master"
        else:
            print(f"  ⚠️  master分支失败: {result.stderr.strip()}")
            
            # 尝试main分支
            print("  🔄 git push -u origin main")
            result = subprocess.run(["git", "push", "-u", "origin", "main"], 
                                  capture_output=True, text=True, timeout=180)
            
            if result.returncode == 0:
                print("  ✅ 推送到main分支成功！")
                branch_name = "main"
            else:
                print(f"  ❌ 推送失败: {result.stderr.strip()}")
                return False
        
        # 推送标签
        print("\n🏷️  推送标签...")
        result = subprocess.run(["git", "push", "--tags"], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("  ✅ 标签推送成功！")
        else:
            print(f"  ⚠️  标签推送警告: {result.stderr.strip()}")
        
        # 成功！
        print("\n🎉 推送完成！")
        print("=" * 60)
        print("🎊 恭喜！屏幕权限管理测试APP已成功部署到GitHub！")
        print("")
        print(f"📦 仓库: https://github.com/Mradai/screen-permission-manager-test")
        print(f"🏗️  Actions: https://github.com/Mradai/screen-permission-manager-test/actions")
        print(f"📥 Releases: https://github.com/Mradai/screen-permission-manager-test/releases")
        print(f"🌿 分支: {branch_name}")
        print(f"🏷️  最新标签: v1.0.1768419457")
        print("")
        print("⏱️  接下来:")
        print("   1. 访问Actions页面查看构建状态")
        print("   2. 等待5-10分钟构建完成")
        print("   3. 下载app-debug.apk")
        print("   4. 安装到Android设备测试")
        print("")
        print("✨ 部署成功！您的APP正在云端构建中...")
        print("=" * 60)
        
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ 推送超时，请检查网络连接")
        return False
    except Exception as e:
        print(f"❌ 推送失败: {e}")
        return False
if __name__ == "__main__":
    prepare_and_push()
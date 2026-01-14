import os
import subprocess
import json
from datetime import datetime
def one_click_deploy():
    """一键部署到GitHub"""
    print("🚀 一键部署到GitHub...")
    print("=" * 50)
    
    project_dir = "ScreenPermissionManager_Test/ScreenPermissionManager_Test"
    if not os.path.exists(project_dir):
        print("❌ 项目目录不存在")
        utils.set_state(success=False, error="项目目录不存在")
        return
    
    os.chdir(project_dir)
    
    # 1. 获取GitHub用户名
    print("🔐 获取GitHub账户信息...")
    github_username = input("请输入您的GitHub用户名: ").strip()
    if not github_username:
        print("❌ 用户名不能为空")
        utils.set_state(success=False, error="用户名为空")
        return
    
    repo_name = "screen-permission-manager-test"
    repo_url = f"https://github.com/{github_username}/{repo_name}.git"
    
    print(f"\n📋 部署信息:")
    print(f"   GitHub用户名: {github_username}")
    print(f"   仓库名称: {repo_name}")
    print(f"   仓库URL: {repo_url}")
    
    # 2. 验证文件完整性
    print("\n📁 验证文件完整性...")
    required_files = [
        "lib/main.dart",
        "pubspec.yaml",
        ".github/workflows/build-apk.yml",
        "quick_deploy.sh",
        "DEPLOYMENT_GUIDE.md",
        "README.md"
    ]
    
    all_files_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} (缺失)")
            all_files_exist = False
    
    if not all_files_exist:
        print("❌ 关键文件缺失，无法继续")
        utils.set_state(success=False, error="关键文件缺失")
        return
    
    # 3. 检查Git状态
    print("\n🔧 检查Git状态...")
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Git仓库未初始化")
            utils.set_state(success=False, error="Git仓库未初始化")
            return
        
        # 检查是否有未提交的更改
        if "Changes not staged for commit" in result.stdout or "Untracked files" in result.stdout:
            print("⚠️ 发现未提交的更改")
            print("➕ 添加所有文件到暂存区...")
            subprocess.run(["git", "add", "."], check=True)
            
            commit_msg = f"🚀 一键部署更新 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            print(f"💾 提交更改: {commit_msg}")
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            print("✅ 更改已提交")
        else:
            print("✅ 没有未提交的更改")
            
    except Exception as e:
        print(f"❌ Git操作失败: {e}")
        utils.set_state(success=False, error=f"Git操作失败: {e}")
        return
    
    # 4. 设置远程仓库
    print("\n📡 设置远程仓库...")
    try:
        # 检查是否已有远程仓库
        result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
        if result.returncode == 0:
            current_url = result.stdout.strip()
            print(f"当前远程仓库: {current_url}")
            if current_url != repo_url:
                print("🔄 更新远程仓库URL...")
                subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True)
                print("✅ 远程仓库URL已更新")
            else:
                print("✅ 远程仓库URL正确")
        else:
            print("➕ 添加新的远程仓库...")
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
            print("✅ 远程仓库已添加")
            
    except Exception as e:
        print(f"❌ 设置远程仓库失败: {e}")
        utils.set_state(success=False, error=f"设置远程仓库失败: {e}")
        return
    
    # 5. 推送代码到GitHub
    print("\n🚀 推送代码到GitHub...")
    print("💡 这将推送代码到GitHub并触发Actions自动构建")
    print("💡 如果是首次推送，需要输入GitHub用户名和密码/Token")
    print("💡 如果启用了2FA，请使用Personal Access Token")
    
    confirm = input("\n确认开始推送? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 推送已取消")
        utils.set_state(success=False, error="用户取消推送")
        return
    
    print("\n⏳ 正在推送...")
    try:
        # 尝试推送到master分支
        result = subprocess.run(
            ["git", "push", "-u", "origin", "master"],
            capture_output=True,
            text=True,
            timeout=120  # 2分钟超时
        )
        
        if result.returncode == 0:
            print("✅ 推送到master分支成功！")
            branch_name = "master"
        else:
            # 尝试推送到main分支
            print("⚠️  master分支推送失败，尝试main分支...")
            result = subprocess.run(
                ["git", "push", "-u", "origin", "main"],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                print("✅ 推送到main分支成功！")
                branch_name = "main"
            else:
                print(f"❌ 推送失败")
                print(f"错误信息: {result.stderr}")
                utils.set_state(success=False, error=f"推送失败: {result.stderr}")
                return
        
        # 推送标签
        print("\n🏷️  推送标签...")
        subprocess.run(["git", "push", "--tags"], check=True)
        print("✅ 标签已推送")
        
        # 6. 显示成功信息
        print("\n🎉 部署成功！")
        print("=" * 50)
        print("🎊 恭喜！代码已成功推送到GitHub！")
        print("")
        print("📱 下一步操作:")
        print(f"   1. 访问: {repo_url}")
        print(f"   2. 点击 'Actions' 标签页")
        print(f"   3. 等待构建完成 (5-10分钟)")
        print(f"   4. 进入 'Releases' 标签页")
        print(f"   5. 下载APK文件")
        print("")
        print("🔗 快速链接:")
        print(f"   仓库: {repo_url}")
        print(f"   Actions: {repo_url}/actions")
        print(f"   Releases: {repo_url}/releases")
        print("")
        print("📦 构建说明:")
        print("   - GitHub Actions会自动构建APK")
        print("   - 构建完成后会创建Release")
        print("   - APK文件会上传到Release中")
        print("   - 您可以直接从Release下载")
        print("")
        print("📱 安装和测试:")
        print("   1. 将APK传输到Android手机")
        print("   2. 设置 → 安全 → 未知来源应用: 启用")
        print("   3. 点击APK文件安装")
        print("   4. 打开APP，测试所有功能")
        print("")
        print("🎯 APP测试要点:")
        print("   • 打开APP，确认蓝色主题界面")
        print("   • 点击右下角按钮，观察屏幕状态变化")
        print("   • 开启自动管理，测试智能权限控制")
        print("   • 使用手动控制，测试恢复/停止功能")
        print("   • 查看实时统计和操作日志")
        print("")
        print("📖 完整指南:")
        print(f"   项目中的 DEPLOYMENT_GUIDE.md 有详细部署步骤")
        print(f"   TEST_GUIDE.md 包含完整测试流程")
        print("")
        print("✨ 您的测试APP已成功部署！")
        print("=" * 50)
        
        # 保存部署信息
        deploy_result = {
            "timestamp": datetime.now().isoformat(),
            "github_username": github_username,
            "repo_name": repo_name,
            "repo_url": repo_url,
            "branch": branch_name,
            "status": "success",
            "message": "部署成功"
        }
        
        utils.set_state(success=True, deploy_result=deploy_result)
        utils.set_persistent_state(deploy_result=deploy_result)
        
        # 7. 创建快速访问指南
        quick_access = f"""# 🚀 快速访问指南
## 📱 屏幕权限管理测试APP
### 🔗 项目链接
- **GitHub仓库**: {repo_url}
- **Actions构建**: {repo_url}/actions
- **Releases下载**: {repo_url}/releases
### 📋 部署信息
- **用户名**: {github_username}
- **仓库名**: {repo_name}
- **分支**: {branch_name}
- **部署时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
### 📱 下载和安装
1. 访问 {repo_url}/releases
2. 找到最新版本
3. 下载 `app-debug.apk` 文件
4. 传输到Android设备安装
### 🎯 测试要点
- ✅ 蓝色主题主界面
- ✅ 屏幕状态切换功能
- ✅ 自动权限管理
- ✅ 手动控制功能
- ✅ 实时统计显示
- ✅ 操作日志记录
### 📊 构建状态
GitHub Actions正在自动构建APK，大约需要5-10分钟
构建完成后会在Releases中显示可下载的APK文件
---
**状态**: 🟢 部署成功
**下一步**: 等待构建完成，下载APK"""
        
        with open("QUICK_ACCESS.md", "w", encoding="utf-8") as f:
            f.write(quick_access)
        print("✅ 快速访问指南已创建")
        
    except subprocess.TimeoutExpired:
        print("❌ 推送超时（2分钟）")
        print("💡 请检查网络连接，或手动执行推送")
        utils.set_state(success=False, error="推送超时")
    except Exception as e:
        print(f"❌ 推送失败: {e}")
        utils.set_state(success=False, error=f"推送失败: {e}")
    finally:
        os.chdir("../../")
    
    return True
if __name__ == "__main__":
    one_click_deploy()
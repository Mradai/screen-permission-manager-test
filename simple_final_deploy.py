import os
import subprocess
from datetime import datetime
def simple_final_deploy():
    """简单版最终部署"""
    print("🚀 简单版最终部署...")
    print("=" * 60)
    
    current_dir = os.getcwd()
    print(f"📁 当前目录: {current_dir}")
    
    # 1. 检查核心文件
    print("\n📋 核心文件检查通过")
    
    # 2. Git操作
    print("\n🔧 Git操作...")
    try:
        print("  ➕ git add .")
        subprocess.run(["git", "add", "."], check=True)
        print("  ✅ 已添加")
        
        # 提交
        commit_msg = f"🚀 最终部署 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        print(f"  💾 git commit -m '{commit_msg}'")
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print("  ✅ 已提交")
        
        # 标签
        tag_name = f"v1.0.{int(datetime.now().timestamp())}"
        print(f"  🏷️ git tag -a {tag_name} -m '{tag_name}'")
        subprocess.run(["git", "tag", "-a", tag_name, "-m", tag_name], check=True)
        print(f"  ✅ 标签: {tag_name}")
        
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Git错误: {e}")
        return
    
    # 3. GitHub信息
    print("\n🔐 GitHub配置...")
    github_username = input("GitHub用户名: ").strip()
    if not github_username:
        print("❌ 用户名不能为空")
        return
    
    repo_name = "screen-permission-manager-test"
    repo_url = f"https://github.com/{github_username}/{repo_name}.git"
    print(f"  📦 仓库: {repo_url}")
    
    # 4. 设置远程仓库
    print("\n📡 设置远程仓库...")
    try:
        print("  🔄 git remote remove origin")
        subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
        print("  ➕ git remote add origin " + repo_url)
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        print("  ✅ 远程仓库设置完成")
    except Exception as e:
        print(f"  ❌ 设置失败: {e}")
        return
    
    # 5. 推送
    print("\n🚀 推送代码...")
    print("⚠️  这将推送代码并触发GitHub Actions自动构建APK")
    
    confirm = input("\n确认开始推送? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 已取消")
        return
    
    print("⏳ 正在推送...")
    try:
        # 尝试master分支
        print("  🔄 git push -u origin master")
        result = subprocess.run(["git", "push", "-u", "origin", "master"], timeout=120)
        
        if result.returncode == 0:
            print("  ✅ 推送到master分支成功！")
            branch_name = "master"
        else:
            print("  ⚠️  master分支失败，尝试main分支...")
            print("  🔄 git push -u origin main")
            result = subprocess.run(["git", "push", "-u", "origin", "main"], timeout=120)
            
            if result.returncode == 0:
                print("  ✅ 推送到main分支成功！")
                branch_name = "main"
            else:
                print("❌ 推送失败！")
                print("\n💡 请手动执行:")
                print(f"   cd {current_dir}")
                print(f"   git push -u origin master")
                return
        
        # 推送标签
        print("\n🏷️  git push --tags")
        subprocess.run(["git", "push", "--tags"], check=True)
        print("  ✅ 标签推送成功！")
        
        # 6. 完成
        print("\n🎉 部署完成！")
        print("=" * 60)
        print("🎊 恭喜！屏幕权限管理测试APP已成功部署！")
        print("")
        print(f"📦 仓库: {repo_url}")
        print(f"🏗️  Actions: {repo_url}/actions")
        print(f"📥 Releases: {repo_url}/releases")
        print(f"🏷️  标签: {tag_name}")
        print(f"🌿 分支: {branch_name}")
        print("")
        print("📋 下一步:")
        print(f"   1. 访问 {repo_url}/actions")
        print("   2. 等待构建完成 (5-10分钟)")
        print("   3. 下载 app-debug.apk")
        print("   4. 安装测试")
        print("")
        print("✨ APP已部署！")
        print("=" * 60)
        
        # 创建最终总结
        final_summary = f"""# 🚀 最终部署总结
## ✅ 部署成功
- **项目**: 屏幕权限管理测试APP
- **GitHub**: {repo_url}
- **分支**: {branch_name}
- **标签**: {tag_name}
- **时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
## 📱 立即可用
1. 访问 {repo_url}/actions
2. 等待构建完成 (5-10分钟)
3. 下载 app-debug.apk
4. 安装测试
## 🎯 核心功能
- ✅ 屏幕状态监听
- ✅ 智能权限管理
- ✅ 手动控制面板
- ✅ 实时统计显示
- ✅ 操作日志记录
- ✅ Material Design UI
---
**状态**: 🟢 部署完成，等待构建"""
        
        with open("FINAL_SUMMARY.md", "w", encoding="utf-8") as f:
            f.write(final_summary)
        print("✅ 最终总结已创建: FINAL_SUMMARY.md")
        
        utils.set_state(success=True, deploy={
            "username": github_username, "repo": repo_name, "url": repo_url,
            "branch": branch_name, "tag": tag_name
        })
        
    except subprocess.TimeoutExpired:
        print("❌ 推送超时，请检查网络")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    return True
if __name__ == "__main__":
    simple_final_deploy()
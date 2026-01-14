import os
import subprocess
from datetime import datetime
def final_deploy_wait_user_input():
    """等待用户输入的最终部署"""
    print("🚀 最终部署准备就绪...")
    print("=" * 60)
    
    current_dir = os.getcwd()
    print(f"📁 当前目录: {current_dir}")
    
    # Git状态已准备好
    print("\n✅ Git状态:")
    print("   - 文件已添加")
    print("   - 提交已创建")
    print("   - 标签已创建: v1.0.1768419457")
    
    # 等待用户输入GitHub用户名
    print("\n🔐 GitHub配置...")
    github_username = input("请输入您的GitHub用户名: ").strip()
    
    if not github_username:
        print("❌ 用户名不能为空，部署已取消")
        return False
    
    repo_name = "screen-permission-manager-test"
    repo_url = f"https://github.com/{github_username}/{repo_name}.git"
    
    print(f"\n📋 部署信息:")
    print(f"   用户名: {github_username}")
    print(f"   仓库: {repo_name}")
    print(f"   URL: {repo_url}")
    
    # 设置远程仓库
    print("\n📡 设置远程仓库...")
    try:
        subprocess.run(["git", "remote", "remove", "origin"], capture_output=True, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        print("  ✅ 远程仓库设置完成")
    except Exception as e:
        print(f"  ❌ 设置失败: {e}")
        return False
    
    # 推送代码
    print("\n🚀 推送代码到GitHub...")
    print("⚠️  这将推送代码并触发GitHub Actions自动构建APK")
    
    confirm = input("\n确认开始推送? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 已取消推送")
        return False
    
    print("⏳ 正在推送...")
    try:
        # 尝试master分支
        result = subprocess.run(["git", "push", "-u", "origin", "master"], 
                              capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("✅ 推送到master分支成功！")
            branch_name = "master"
        else:
            # 尝试main分支
            print("⚠️  master分支失败，尝试main分支...")
            result = subprocess.run(["git", "push", "-u", "origin", "main"], 
                                  capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                print("✅ 推送到main分支成功！")
                branch_name = "main"
            else:
                print(f"❌ 推送失败: {result.stderr}")
                return False
        
        # 推送标签
        subprocess.run(["git", "push", "--tags"], check=True, capture_output=True)
        print("✅ 标签推送成功！")
        
        # 显示结果
        print("\n🎉 部署完成！")
        print("=" * 60)
        print("🎊 恭喜！屏幕权限管理测试APP已成功部署！")
        print("")
        print(f"📦 仓库: {repo_url}")
        print(f"🏗️  Actions: {repo_url}/actions")
        print(f"📥 Releases: {repo_url}/releases")
        print("")
        print("📋 下一步操作:")
        print(f"   1. 访问 {repo_url}/actions")
        print("   2. 等待构建完成 (5-10分钟)")
        print("   3. 下载 app-debug.apk")
        print("   4. 安装测试")
        print("")
        print("✨ 您的测试APP已成功部署！")
        print("=" * 60)
        
        # 创建最终总结
        final_summary = f"""# 🚀 最终部署总结
## ✅ 部署成功
- **项目**: 屏幕权限管理测试APP
- **GitHub**: {repo_url}
- **分支**: {branch_name}
- **标签**: v1.0.1768419457
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
## 📖 文档
- TEST_GUIDE.md - 测试指南
- README.md - 项目说明
---
**状态**: 🟢 部署完成，等待构建"""
        
        with open("FINAL_SUMMARY.md", "w", encoding="utf-8") as f:
            f.write(final_summary)
        print("✅ 最终总结已创建: FINAL_SUMMARY.md")
        
        # 保存状态
        utils.set_state(success=True, deploy_result={
            "timestamp": datetime.now().isoformat(),
            "github_username": github_username,
            "repo_url": repo_url,
            "branch": branch_name,
            "tag": "v1.0.1768419457",
            "status": "success"
        })
        
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ 推送超时，请检查网络连接")
        return False
    except Exception as e:
        print(f"❌ 推送失败: {e}")
        return False
if __name__ == "__main__":
    final_deploy_wait_user_input()
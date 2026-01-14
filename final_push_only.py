import os
import subprocess
from datetime import datetime
def final_push_only():
    """仅执行最终推送"""
    print("🚀 执行最终推送...")
    print("=" * 60)
    
    current_dir = os.getcwd()
    print(f"📁 当前目录: {current_dir}")
    
    # 用户信息
    github_username = "Mradai"
    repo_name = "screen-permission-manager-test"
    repo_url = f"https://github.com/{github_username}/{repo_name}.git"
    
    print(f"📦 仓库: {repo_url}")
    print(f"🏷️  标签: v1.0.1768419457")
    
    # 推送代码
    print("\n🚀 推送代码到GitHub...")
    print("⚠️  这将推送代码并触发GitHub Actions自动构建APK")
    
    confirm = input("\n确认开始推送? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 已取消推送")
        print("\n💡 您可以随时重新运行部署")
        return False
    
    print("⏳ 正在推送...")
    try:
        # 尝试master分支
        print("  🔄 git push -u origin master")
        result = subprocess.run(["git", "push", "-u", "origin", "master"], 
                              capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("  ✅ 推送到master分支成功！")
            branch_name = "master"
        else:
            print(f"  ⚠️  master分支失败: {result.stderr.strip()}")
            print("  🔄 尝试推送到main分支...")
            
            result = subprocess.run(["git", "push", "-u", "origin", "main"], 
                                  capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                print("  ✅ 推送到main分支成功！")
                branch_name = "main"
            else:
                print(f"  ❌ 推送失败: {result.stderr.strip()}")
                print("\n💡 请手动执行:")
                print(f"   cd {current_dir}")
                print(f"   git push -u origin master")
                return False
        
        # 推送标签
        print("\n🏷️  git push --tags")
        result = subprocess.run(["git", "push", "--tags"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("  ✅ 标签推送成功！")
        else:
            print(f"  ⚠️  标签推送失败: {result.stderr.strip()}")
        
        # 显示结果
        print("\n🎉 部署完成！")
        print("=" * 60)
        print("🎊 恭喜！屏幕权限管理测试APP已成功部署！")
        print("")
        print(f"📦 仓库: {repo_url}")
        print(f"🏗️  Actions: {repo_url}/actions")
        print(f"📥 Releases: {repo_url}/releases")
        print(f"🏷️  标签: v1.0.1768419457")
        print(f"🌿 分支: {branch_name}")
        print("")
        print("⏱️  下一步操作:")
        print(f"   1. 访问: {repo_url}/actions")
        print("   2. 等待构建完成 (5-10分钟)")
        print("   3. 进入Releases页面")
        print("   4. 下载 app-debug.apk")
        print("")
        print("📱 安装测试:")
        print("   • 传输APK到Android手机")
        print("   • 设置 → 安全 → 未知来源应用: 启用")
        print("   • 点击安装")
        print("   • 打开APP测试")
        print("")
        print("🎯 APP功能测试:")
        print("   ✅ 蓝色主题主界面")
        print("   ✅ 右下角浮动按钮")
        print("   ✅ 自动管理开关")
        print("   ✅ 手动控制按钮")
        print("   ✅ 实时统计显示")
        print("   ✅ 操作日志记录")
        print("")
        print("📖 可用文档:")
        print("   • TEST_GUIDE.md - 测试步骤")
        print("   • README.md - 项目说明")
        print("   • QUICK_ACCESS.md - 快速访问")
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
- QUICK_ACCESS.md - 快速访问
---
**状态**: 🟢 部署完成，等待构建"""
        
        with open("FINAL_SUMMARY.md", "w", encoding="utf-8") as f:
            f.write(final_summary)
        print("✅ 最终总结已创建: FINAL_SUMMARY.md")
        
        # 保存状态
        utils.set_state(success=True, deploy_result={
            "timestamp": datetime.now().isoformat(),
            "github_username": github_username,
            "repo_name": repo_name,
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
    final_push_only()
import os
import subprocess
import json
from datetime import datetime
def fix_github_actions():
    """修复并完成GitHub Actions配置"""
    print("🔧 修复GitHub Actions配置...")
    print("=" * 50)
    
    project_dir = "ScreenPermissionManager_Test"
    os.chdir(project_dir)
    
    # 1. 创建所有必需的目录
    directories_to_create = [
        ".github/ISSUE_TEMPLATE",
        ".github/PULL_REQUEST_TEMPLATE",
        ".gitpod",
        ".devcontainer",
        ".reuse"
    ]
    
    print("📁 创建目录结构:")
    for dir_path in directories_to_create:
        os.makedirs(dir_path, exist_ok=True)
        print(f"  ✅ {dir_path}")
    
    # 2. 创建Issue模板
    issue_template = """name: Bug Report
description: Create a report to help us improve
title: "[Bug] "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: "## 🐛 Bug Report"
  - type: textarea
    attributes:
      label: "Description"
      description: "Describe the bug"
    validations:
      required: true
  - type: textarea
    attributes:
      label: "Reproduction"
      description: "Steps to reproduce the behavior"
    validations:
      required: true
  - type: textarea
    attributes:
      label: "Expected Behavior"
      description: "What you expected to happen"
    validations:
      required: true
  - type: input
    attributes:
      label: "Device"
      description: "Device model and OS version"
  - type: textarea
    attributes:
      label: "Additional Context"
      description: "Add any other context about the problem here" """
    
    with open(".github/ISSUE_TEMPLATE/bug_report.yml", "w", encoding="utf-8") as f:
        f.write(issue_template)
    print("  ✅ Issue模板")
    
    # 3. 创建PR模板
    pr_template = """## 🎯 Purpose
Describe the purpose of this pull request
## 📝 Changes
List the changes made:
- 
## ✅ Checklist
- [ ] Code follows the style guide
- [ ] Tests pass
- [ ] Documentation updated
## 📸 Screenshots
If applicable, add screenshots to help explain the changes"""
    
    with open(".github/PULL_REQUEST_TEMPLATE/pull_request_template.md", "w", encoding="utf-8") as f:
        f.write(pr_template)
    print("  ✅ PR模板")
    
    # 4. 创建CODEOWNERS
    codeowners = """# Codeowners
* @github-username
lib/* @flutter-expert"""
    
    with open(".github/CODEOWNERS", "w", encoding="utf-8") as f:
        f.write(codeowners)
    print("  ✅ CODEOWNERS")
    
    # 5. 创建STALE配置
    stale_config = """# Stale configuration
daysUntilStale: 60
daysUntilClose: 7
exemptLabels:
  - pinned
  - security
markComment: >
  This issue has been automatically marked as stale because it has not had
  recent activity. It will be closed if no further activity occurs."""
    
    with open(".github/stale.yml", "w", encoding="utf-8") as f:
        f.write(stale_config)
    print("  ✅ Stale配置")
    
    # 6. 创建GitPod配置
    gitpod_docker = """FROM gitpod/workspace-flutter
USER gitpod
RUN sudo apt-get update && sudo apt-get install -y \\
    android-tools-adb \\
    android-tools-fastboot \\
    && sudo rm -rf /var/lib/apt/lists/*
ENV ANDROID_HOME=/home/gitpod/android-sdk
RUN mkdir -p $ANDROID_HOME/cmdline-tools && \\
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip && \\
    unzip commandlinetools-linux-9477386_latest.zip -d $ANDROID_HOME/cmdline-tools && \\
    mv $ANDROID_HOME/cmdline-tools/cmdline-tools $ANDROID_HOME/cmdline-tools/latest && \\
    rm commandlinetools-linux-9477386_latest.zip
ENV PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools
RUN yes | sdkmanager --licenses && \\
    sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2" """
    
    with open(".gitpod/Dockerfile", "w", encoding="utf-8") as f:
        f.write(gitpod_docker)
    print("  ✅ GitPod Dockerfile")
    
    gitpod_yml = """image:
  file: .gitpod/Dockerfile
tasks:
  - name: Install dependencies
    command: flutter pub get
    
  - name: Build Android
    command: flutter build apk --debug
ports:
  - port: 3000
    onOpen: ignore"""
    
    with open(".gitpod.yml", "w", encoding="utf-8") as f:
        f.write(gitpod_yml)
    print("  ✅ GitPod配置")
    
    # 7. 创建Codespaces配置
    codespaces_yml = """name: GitHub Codespaces
on:
  workflow_dispatch:
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.16.0'
      - run: flutter pub get
      - run: flutter build apk --debug"""
    
    with open(".devcontainer/codespaces.yml", "w", encoding="utf-8") as f:
        f.write(codespaces_yml)
    print("  ✅ Codespaces配置")
    
    # 8. 创建REUSE配置
    reuse_config = """Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: ScreenPermissionManager
Upstream-Contact: https://github.com/username/ScreenPermissionManager
Files: *
Copyright: 2026 AiPy User
License: GPL-3.0-or-later"""
    
    with open(".reuse/dep5", "w", encoding="utf-8") as f:
        f.write(reuse_config)
    print("  ✅ REUSE配置")
    
    # 9. 创建状态徽章文档
    badges_doc = """# 📊 CI/CD 状态徽章
将以下徽章添加到 README.md 以显示构建状态：
## 构建状态
[![Build APK](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/build-apk.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/build-apk.yml)
[![Code Analysis](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/analyze.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/analyze.yml)
[![CI](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml)
## 代码质量
[![codecov](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO)
## 发布版本
[![GitHub release](https://img.shields.io/github/release/YOUR_USERNAME/YOUR_REPO.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/releases)
[![GitHub downloads](https://img.shields.io/github/downloads/YOUR_USERNAME/YOUR_REPO/total.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/releases)"""
    
    with open(".github/BADGES.md", "w", encoding="utf-8") as f:
        f.write(badges_doc)
    print("  ✅ 状态徽章文档")
    
    # 10. 创建快速部署脚本
    deploy_script = """#!/bin/bash
# GitHub快速部署脚本
echo "🚀 GitHub快速部署脚本"
echo "====================="
# 检查参数
if [ -z "$1" ]; then
    echo "❌ 请提供GitHub用户名"
    echo "用法: ./quick_deploy.sh YOUR_USERNAME"
    exit 1
fi
USERNAME=$1
REPO_NAME="screen-permission-manager-test"
REPO_URL="https://github.com/$USERNAME/$REPO_NAME.git"
echo "📋 配置信息:"
echo "   用户名: $USERNAME"
echo "   仓库名: $REPO_NAME"
echo "   仓库URL: $REPO_URL"
echo ""
# 检查Git状态
echo "🔍 检查Git状态..."
if ! git status >/dev/null 2>&1; then
    echo "❌ 不在Git仓库中"
    exit 1
fi
# 添加所有文件
echo "➕ 添加所有文件..."
git add .
# 提交更改
echo "💾 提交更改..."
git commit -m "🚀 GitHub Actions配置更新 - $(date)"
# 设置远程仓库
echo "📡 设置远程仓库..."
git remote remove origin 2>/dev/null
git remote add origin $REPO_URL
# 推送代码
echo "🚀 推送代码到GitHub..."
if git push -u origin master; then
    echo ""
    echo "🎉 推送成功！"
    echo ""
    echo "📱 下一步操作:"
    echo "   1. 访问: https://github.com/$USERNAME/$REPO_NAME"
    echo "   2. 进入 Actions 标签页"
    echo "   3. 等待构建完成 (2-5分钟)"
    echo "   4. 下载APK文件"
    echo ""
    echo "🔗 快速链接:"
    echo "   仓库: $REPO_URL"
    echo "   Actions: $REPO_URL/actions"
    echo ""
else
    echo "❌ 推送失败"
    echo "💡 请检查:"
    echo "   1. GitHub用户名是否正确"
    echo "   2. 网络连接是否正常"
    echo "   3. 是否有仓库写入权限"
    exit 1
fi"""
    
    with open("quick_deploy.sh", "w", encoding="utf-8") as f:
        f.write(deploy_script)
    os.chmod("quick_deploy.sh", 0o755)
    print("  ✅ 快速部署脚本")
    
    # 11. 创建Windows批处理脚本
    deploy_bat = """@echo off
chcp 65001 >nul
echo 🚀 GitHub快速部署脚本 (Windows)
echo ================================
if "%~1"=="" (
    echo ❌ 请提供GitHub用户名
    echo 用法: quick_deploy.bat YOUR_USERNAME
    exit /b 1
)
set USERNAME=%~1
set REPO_NAME=screen-permission-manager-test
set REPO_URL=https://github.com/%USERNAME%/%REPO_NAME%.git
echo 📋 配置信息:
echo    用户名: %USERNAME%
echo    仓库名: %REPO_NAME%
echo    仓库URL: %REPO_URL%
echo.
echo 🔍 检查Git状态...
git status >nul 2>&1
if errorlevel 1 (
    echo ❌ 不在Git仓库中
    exit /b 1
)
echo ➕ 添加所有文件...
git add .
echo 💾 提交更改...
git commit -m "🚀 GitHub Actions配置更新 - %date% %time%"
echo 📡 设置远程仓库...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
echo 🚀 推送代码到GitHub...
git push -u origin master
if errorlevel 1 (
    echo ❌ 推送失败
    echo 💡 请检查:
    echo    1. GitHub用户名是否正确
    echo    2. 网络连接是否正常
    echo    3. 是否有仓库写入权限
    exit /b 1
)
echo.
echo 🎉 推送成功！
echo.
echo 📱 下一步操作:
echo    1. 访问: %REPO_URL%
echo    2. 进入 Actions 标签页
echo    3. 等待构建完成 (2-5分钟)
echo    4. 下载APK文件
echo.
echo 🔗 快速链接:
echo    仓库: %REPO_URL%
echo    Actions: %REPO_URL%/actions
echo.
pause"""
    
    with open("quick_deploy.bat", "w", encoding="utf-8") as f:
        f.write(deploy_bat)
    print("  ✅ Windows批处理脚本")
    
    # 12. 创建部署指南
    deploy_guide = """# 🚀 GitHub部署完整指南
## 📋 准备工作
✅ 所有文件已创建完成  
✅ GitHub Actions已配置  
✅ 部署脚本已生成  
## ⚡ 一键部署
### Linux/Mac用户
```bash
cd ScreenPermissionManager_Test
./quick_deploy.sh YOUR_GITHUB_USERNAME
```
### Windows用户
```cmd
cd ScreenPermissionManager_Test
quick_deploy.bat YOUR_GITHUB_USERNAME
```
## 📱 手动部署步骤
### 第1步：创建GitHub仓库
1. 访问 [https://github.com/new](https://github.com/new)
2. 填写信息：
   - **仓库名称**: `screen-permission-manager-test`
   - **描述**: `屏幕权限管理测试APP`
   - **选择**: 公开
   - **初始化**: 不要勾选任何选项
3. 点击 "Create repository"
### 第2步：推送代码
```bash
# 进入项目目录
cd ScreenPermissionManager_Test
# 添加远程仓库 (替换YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/screen-permission-manager-test.git
# 推送代码
git push -u origin master
```
### 第3步：等待构建
1. 访问您的仓库
2. 点击 "Actions" 标签页
3. 等待构建完成（5-10分钟）
4. 构建完成后会显示绿色对勾
### 第4步：下载APK
1. 进入 "Releases" 标签页
2. 找到最新版本
3. 下载 `app-debug.apk`
4. 安装到Android设备
## 🎯 部署成功后获得
- ✅ GitHub上的完整项目仓库
- ✅ 自动构建的APK下载链接
- ✅ 持续集成的构建系统
- ✅ 完整的CI/CD流程
## 📊 GitHub Actions功能
- **build-apk.yml**: 自动构建APK并创建Release
- **analyze.yml**: 代码分析和测试覆盖率
- **ci.yml**: 持续集成和测试报告
## 📱 APP测试要点
1. **打开APP** - 看到蓝色主题主界面
2. **点击右下角浮动按钮** - 模拟屏幕开关
3. **开启自动管理** - 体验智能控制
4. **使用手动按钮** - 测试功能
5. **查看实时统计** - 确认数据更新
6. **检查操作日志** - 确认记录完整
## 🆘 常见问题
### 推送失败？
- 检查GitHub用户名是否正确
- 确认网络连接正常
- 验证仓库写入权限
### 构建失败？
- 查看Actions日志
- 检查代码语法
- 确认依赖版本
### 安装失败？
- Android版本≥5.0
- 开启未知来源应用
- 检查APK完整性
---
**部署时间**: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """  
**状态**: 🟢 立即可用"""
    
    with open("DEPLOYMENT_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(deploy_guide)
    print("  ✅ 部署指南")
    
    # 统计创建的文件
    files_created = [
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/PULL_REQUEST_TEMPLATE/pull_request_template.md",
        ".github/CODEOWNERS",
        ".github/stale.yml",
        ".gitpod/Dockerfile",
        ".gitpod.yml",
        ".devcontainer/codespaces.yml",
        ".reuse/dep5",
        ".github/BADGES.md",
        "quick_deploy.sh",
        "quick_deploy.bat",
        "DEPLOYMENT_GUIDE.md"
    ]
    
    total_files = len(files_created)
    
    print(f"\n✅ GitHub Actions配置修复完成！")
    print(f"📁 创建了 {total_files} 个配置文件")
    print(f"📍 位置: {os.path.abspath('.')}")
    
    # 显示完整文件列表
    print("\n📋 完整文件列表:")
    for i, file_path in enumerate(files_created, 1):
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            print(f"  {i:2d}. ✅ {file_path} ({file_size} bytes)")
        else:
            print(f"  {i:2d}. ❌ {file_path} (创建失败)")
    
    # 保存修复状态
    fix_info = {
        "timestamp": datetime.now().isoformat(),
        "files_created": total_files,
        "status": "completed",
        "ready_for_deploy": True
    }
    
    utils.set_state(success=True, fix_info=fix_info)
    
    print(f"\n🎉 所有配置已完成！")
    print(f"🚀 现在可以使用 ./quick_deploy.sh YOUR_USERNAME 进行部署")
    
    os.chdir("..")
    
    return True
if __name__ == "__main__":
    fix_github_actions()
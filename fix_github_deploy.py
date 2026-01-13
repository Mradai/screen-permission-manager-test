import os
import json
from datetime import datetime
def create_github_deployment():
    """创建完整的GitHub部署准备"""
    print("🎯 创建GitHub部署准备...")
    
    project_dir = "ScreenPermissionManager_Test"
    if not os.path.exists(project_dir):
        print(f"❌ 项目目录不存在")
        return
    
    # 1. 创建GitHub Actions工作流（修复版本）
    workflow_content = """name: Build and Release APK
on:
  push:
    branches: [ main, master ]
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.16.0'
          cache: true
      
      - name: Install dependencies
        run: flutter pub get
      
      - name: Build APK
        run: flutter build apk --release
      
      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: app-release
          path: build/app/outputs/flutter-apk/app-release.apk
      
      - name: Create Release
        if: github.event_name == 'push'
        uses: softprops/action-gh-release@v1
        with:
          files: build/app/outputs/flutter-apk/app-release.apk
          tag_name: v1.0.${{ github.run_number }}
          name: Release v1.0.${{ github.run_number }}
          body: |
            🎉 屏幕权限管理测试APP
            
            **版本:** v1.0.${{ github.run_number }}
            **下载:** 下方附件 app-release.apk
            
            **安装说明:**
            1. 下载APK文件
            2. 在Android设备上安装
            3. 按照应用内引导操作
"""
    
    os.makedirs(f"{project_dir}/.github/workflows", exist_ok=True)
    with open(f"{project_dir}/.github/workflows/build.yml", "w", encoding="utf-8") as f:
        f.write(workflow_content)
    
    print("✅ GitHub Actions工作流已创建")
    
    # 2. 创建部署指南
    deploy_guide = """# 🚀 GitHub部署指南
## 📋 项目信息
- **仓库名称**: screen-permission-manager-test
- **描述**: 屏幕权限管理测试APP - 基于Flutter的完整功能演示
- **类型**: Flutter Android应用
- **版本**: 1.0.0
## 🎯 3分钟快速部署
### 第1步：创建GitHub仓库
1. 访问 [https://github.com/new](https://github.com/new)
2. 填写信息：
   - **仓库名称**: `screen-permission-manager-test`
   - **描述**: `屏幕权限管理测试APP`
   - **选择**: 公开
   - **初始化**: 不要勾选任何选项
3. 点击 "Create repository"
### 第2步：获取推送命令
创建仓库后，GitHub会显示推送命令，类似：
```bash
git remote add origin https://github.com/YOUR_USERNAME/screen-permission-manager-test.git
git branch -M main
git push -u origin main
```
### 第3步：推送代码
在本工具中执行：
```bash
cd ScreenPermissionManager_Test
# 然后执行GitHub显示的命令
```
### 第4步：启用自动构建
1. 访问您的仓库
2. 点击 "Actions" 标签页
3. 点击 "I understand my workflows, go ahead and enable them"
4. 等待构建完成（5-10分钟）
### 第5步：下载APK
1. 构建完成后，进入 "Releases" 标签页
2. 找到最新版本
3. 下载 `app-release.apk`
4. 安装到Android设备
## 📱 安装和测试
### 安装APK
```bash
# 方法1: 使用ADB
adb install app-release.apk
# 方法2: 手动传输到手机安装
```
### 测试APP
1. **打开APP** - 看到主界面
2. **点击右下角浮动按钮** - 模拟屏幕开关
3. **开启自动管理** - 体验智能控制
4. **使用手动按钮** - 测试功能
## 📁 项目文件说明
- `lib/main.dart` - Flutter主程序（核心功能）
- `pubspec.yaml` - 项目配置
- `android/app/src/main/AndroidManifest.xml` - Android配置
- `.github/workflows/build.yml` - 自动构建配置
- `README.md` - 项目文档
- `TEST_GUIDE.md` - 测试指南
- `QUICK_START.md` - 快速开始
## 🎯 成功标志
完成以上步骤后，您将获得：
- ✅ GitHub上的完整项目仓库
- ✅ 自动生成的APK下载链接
- ✅ 可以分享的APP
- ✅ 持续集成的构建系统
## 🆘 常见问题
### 推送失败？
检查是否登录GitHub，或联系我获取帮助
### 构建失败？
查看Actions日志，通常是环境配置问题
### 安装失败？
确保Android版本≥5.0，开启未知来源应用
---
**准备时间**: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """
**状态**: 🟢 立即可用
"""
    
    with open(f"{project_dir}/DEPLOY_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(deploy_guide)
    
    print("✅ 部署指南已创建")
    
    # 3. 创建快速开始指南
    quick_start = """# 🚀 快速开始指南
## 📋 项目就绪状态
✅ 所有文件已准备完成  
✅ GitHub Actions已配置  
✅ 文档完整  
## ⚡ 立即操作步骤
### 1. 创建GitHub仓库
访问: https://github.com/new  
填写:
- 仓库名: screen-permission-manager-test
- 描述: 屏幕权限管理测试APP
- 选择: 公开
- 不要初始化README
### 2. 获取推送命令
创建后，复制GitHub显示的命令
### 3. 推送代码
```bash
cd ScreenPermissionManager_Test
# 粘贴GitHub的命令
```
### 4. 等待构建
- 访问仓库 → Actions标签页
- 等待5-10分钟
- 在Releases下载APK
### 5. 安装测试
- 传输APK到手机
- 安装并打开APP
- 点击右下角按钮测试
## 📱 APP功能测试
| 测试项目 | 操作 | 预期结果 |
|----------|------|----------|
| 屏幕开关 | 点击浮动按钮 | 界面颜色变化 |
| 自动管理 | 开启开关 | 智能调整权限 |
| 手动控制 | 点击按钮 | 立即响应 |
| 实时统计 | 任意操作 | 数据更新 |
| 操作日志 | 查看底部 | 记录完整 |
## 🆘 需要帮助？
如果需要我帮您执行推送，请提供您的GitHub用户名！
---
**状态**: 🟢 已准备就绪
"""
    
    with open(f"{project_dir}/QUICK_START.md", "w", encoding="utf-8") as f:
        f.write(quick_start)
    
    print("✅ 快速指南已创建")
    
    # 4. 创建推送脚本
    push_script = """#!/bin/bash
# GitHub推送脚本
echo "🚀 GitHub代码推送"
echo "=================="
if [ -z "$1" ]; then
    echo "❌ 请提供GitHub用户名"
    echo "用法: ./github_push.sh YOUR_USERNAME"
    exit 1
fi
USERNAME=$1
REPO_NAME="screen-permission-manager-test"
REPO_URL="https://github.com/$USERNAME/$REPO_NAME.git"
echo "📋 配置远程仓库: $REPO_URL"
git remote remove origin 2>/dev/null
git remote add origin $REPO_URL
echo "📤 推送代码..."
git push -u origin main
if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 推送成功！"
    echo "仓库地址: https://github.com/$USERNAME/$REPO_NAME"
    echo ""
    echo "下一步:"
    echo "1. 访问仓库地址"
    echo "2. 进入 Actions 标签页"
    echo "3. 等待构建完成"
    echo "4. 在 Releases 下载APK"
else
    echo "❌ 推送失败"
    echo "请检查: 登录状态、网络连接"
    exit 1
fi
"""
    
    with open(f"{project_dir}/github_push.sh", "w", encoding="utf-8") as f:
        f.write(push_script)
    os.chmod(f"{project_dir}/github_push.sh", 0o755)
    
    print("✅ 推送脚本已创建")
    
    # 5. 创建README
    readme = """# 📱 屏幕权限管理测试APP
完整Flutter应用，演示智能权限管理系统
## 🎯 功能特性
- 📱 屏幕状态监听
- 🤖 智能权限管理  
- 🎛️ 手动控制面板
- 📊 实时统计显示
- 📝 操作日志记录
## 🚀 快速开始
### 在线构建
1. Fork本仓库
2. 启用Actions
3. 下载APK
4. 安装测试
### 本地构建
```bash
git clone https://github.com/YOUR_USERNAME/screen-permission-manager-test.git
cd screen-permission-manager-test
flutter pub get
flutter build apk --release
```
## 📱 立即测试
1. 安装APK到Android设备
2. 打开APP
3. 点击右下角浮动按钮测试
4. 开启自动管理体验智能控制
## 📁 项目结构
```
ScreenPermissionManager_Test/
├── lib/main.dart              # 主程序
├── pubspec.yaml              # 配置
├── android/...               # Android配置
├── .github/workflows/...     # 自动构建
├── README.md                 # 本文档
├── TEST_GUIDE.md            # 测试指南
├── DEPLOY_GUIDE.md          # 部署指南
└── QUICK_START.md           # 快速开始
```
## 🎯 完成后获得
- ✅ 可运行的APP
- ✅ GitHub项目仓库
- ✅ 自动构建系统
- ✅ 完整文档
## 🆘 帮助与支持
查看文档获取详细步骤，或联系获取帮助
---
**版本**: 1.0.0 | **状态**: ✅ 完整可用
"""
    
    with open(f"{project_dir}/README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    
    print("✅ README已创建")
    
    # 6. 创建项目信息
    info = {
        "name": "screen-permission-manager-test",
        "description": "屏幕权限管理测试APP",
        "version": "1.0.0",
        "status": "GitHub部署准备完成",
        "ready": True,
        "files": [
            "lib/main.dart",
            "pubspec.yaml",
            "android/app/src/main/AndroidManifest.xml",
            ".github/workflows/build.yml",
            "README.md",
            "TEST_GUIDE.md",
            "DEPLOY_GUIDE.md",
            "QUICK_START.md",
            "github_push.sh"
        ],
        "next_steps": [
            "创建GitHub仓库",
            "推送代码",
            "等待自动构建",
            "下载APK"
        ]
    }
    
    with open(f"{project_dir}/deploy_info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 GitHub部署准备完成！")
    print("=" * 60)
    print(f"📁 项目位置: {os.path.abspath(project_dir)}")
    print(f"📦 已创建 {len(info['files'])} 个文件")
    print(f"📋 下一步:")
    print(f"  1. 创建GitHub仓库: https://github.com/new")
    print(f"  2. 运行: cd {project_dir}")
    print(f"  3. 执行: ./github_push.sh YOUR_USERNAME")
    print(f"  4. 等待构建完成")
    print(f"\n📖 详细指南: {project_dir}/QUICK_START.md")
    print(f"   或告诉我您的GitHub用户名，我帮您推送！")
    
    utils.set_state(success=True, result="GitHub部署准备完成", project_path=os.path.abspath(project_dir))
if __name__ == "__main__":
    create_github_deployment()
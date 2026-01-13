# 🎉 屏幕权限管理测试APP
## 📱 项目介绍
这是一个基于Flutter开发的**屏幕权限管理测试APP**，完整演示了屏幕状态联动APP权限管理的核心功能。
### ✨ 主要功能
- 📱 **屏幕状态监听** - 实时检测屏幕开关状态
- 🤖 **智能权限管理** - 根据屏幕状态自动调整应用权限
- 🎛️ **手动控制面板** - 一键恢复/停止应用权限
- 📊 **实时统计显示** - 显示受管应用数量和状态
- 📝 **操作日志记录** - 记录所有操作和状态变化
- 🎨 **美观UI界面** - Material Design设计风格
## 🚀 快速开始
### 方法1: 使用部署脚本（推荐）
```bash
# Linux/Mac
./deploy_to_github.sh
# Windows
deploy_to_github.bat
```
### 方法2: 手动部署
1. **创建GitHub仓库**
   - 访问 [GitHub](https://github.com)
   - 创建新仓库 `screen-permission-manager-test`
   
2. **推送代码**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/screen-permission-manager-test.git
   git push -u origin main
   ```
3. **下载APK**
   - 访问仓库的 Actions 页面
   - 下载 `app-debug` artifact
   - 安装到Android手机
## 📱 APP功能演示
### 🎯 测试步骤
1. **基础功能测试**
   - 打开APP，看到蓝色主题主界面 ✅
   - 点击右下角浮动按钮，模拟屏幕开关 ✅
   - 观察屏幕状态变化（颜色和文字） ✅
2. **智能管理测试**
   - 开启自动管理开关 ✅
   - 点击右下角按钮关闭屏幕 ✅
   - 观察系统自动限制3个应用 ✅
   - 再次点击按钮开启屏幕 ✅
   - 观察系统自动恢复权限 ✅
3. **手动控制测试**
   - 点击"恢复权限"按钮 ✅
   - 观察受管应用数量变为0 ✅
   - 点击"停止应用"按钮 ✅
   - 观察受管应用数量变为5 ✅
4. **统计和日志测试**
   - 查看顶部实时统计 ✅
   - 查看操作日志记录 ✅
## 📁 项目结构
```
ScreenPermissionManager_Test/
├── lib/
│   └── main.dart              # Flutter主程序
├── android/
│   └── app/
│       └── src/
│           └── main/
│               └── AndroidManifest.xml
├── .github/
│   └── workflows/
│       └── build-apk.yml      # GitHub Actions配置
├── pubspec.yaml               # 项目配置
├── build.sh                   # 构建脚本
├── deploy_to_github.sh        # Linux/Mac部署脚本
├── deploy_to_github.bat       # Windows部署脚本
├── TEST_GUIDE.md             # 详细测试指南
└── README.md                 # 项目说明
```
## 🔧 技术栈
- **Flutter 3.16.0** - 跨平台UI框架
- **Dart** - 编程语言
- **Material Design** - UI设计规范
- **GitHub Actions** - 自动化构建和部署
## 📦 构建和部署
### 本地构建
```bash
# 安装依赖
flutter pub get
# 构建APK
flutter build apk --debug
# 输出位置: build/app/outputs/flutter-apk/app-debug.apk
```
### 自动构建
项目已配置GitHub Actions，每次推送代码会自动构建APK：
- 构建文件: `.github/workflows/build-apk.yml`
- 输出文件: `app-debug.apk`
- 下载位置: GitHub仓库的Actions页面
## 🎯 使用场景
### 开发测试
- 验证屏幕状态监听逻辑
- 测试权限管理算法
- 演示用户界面交互
### 产品演示
- 展示APP核心功能
- 演示智能权限控制
- 用户体验测试
### 教学培训
- Flutter开发示例
- Material Design实践
- Git/GitHub工作流
## 📋 系统要求
### 开发环境
- Flutter SDK 3.16.0+
- Dart SDK 3.0+
- Git
### 运行环境
- Android 5.0+ (推荐Android 8.0+)
- 至少100MB存储空间
- 未知来源应用安装权限
## 🆘 常见问题
### Q: GitHub Actions构建失败？
**A:** 检查：
1. `.github/workflows/build-apk.yml` 文件路径
2. Flutter版本兼容性
3. 网络连接
### Q: APK安装失败？
**A:** 检查：
1. Android版本兼容性
2. 存储空间是否充足
3. 未知来源应用权限
### Q: 功能不正常？
**A:** 检查：
1. APP是否获得必要权限
2. 设备是否支持所需功能
3. 是否为测试版本限制
## 📞 获取帮助
- 📖 **详细指南**: 查看 `TEST_GUIDE.md`
- 🚀 **快速部署**: 运行 `deploy_to_github.sh` 或 `deploy_to_github.bat`
- 🐛 **问题反馈**: 在GitHub仓库创建Issue
## 🎉 成功标准
✅ **GitHub仓库创建完成**  
✅ **代码成功上传**  
✅ **GitHub Actions配置完成**  
✅ **APK构建成功**  
✅ **可下载的APK文件**  
✅ **测试APP正常运行**  
## 📄 许可证
本项目仅供学习和测试使用。
## 🙏 致谢
感谢Flutter团队和开源社区的贡献！
---
**🚀 现在就开始您的屏幕权限管理之旅吧！**
*创建时间: 2026-01-14 05:09:03*  
*版本: 1.0.0 测试版*

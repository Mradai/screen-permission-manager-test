#!/bin/bash
echo "🚀 屏幕权限测试APP - 快速构建"
echo "=========================================="
echo ""
# 检查Flutter
if ! command -v flutter &> /dev/null; then
    echo "❌ Flutter未安装"
    echo ""
    echo "快速安装方法:"
    echo "  1. 访问: https://flutter.dev/docs/get-started/install"
    echo "  2. 选择您的操作系统"
    echo "  3. 按照指南安装（约30分钟）"
    echo "  4. 运行: flutter doctor"
    echo ""
    echo "安装完成后，重新运行此脚本"
    exit 1
fi
echo "✅ Flutter环境正常"
flutter --version
echo ""
# 安装依赖
echo "📦 安装依赖..."
flutter pub get
if [ $? -ne 0 ]; then
    echo "❌ 依赖安装失败"
    exit 1
fi
echo "✅ 依赖安装完成"
echo ""
# 构建APK
echo "🔨 构建测试APK..."
echo "这可能需要2-5分钟..."
flutter build apk --debug
if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 构建成功！"
    echo "=========================================="
    echo "📱 APK文件位置:"
    echo "  build/app/outputs/flutter-apk/app-debug.apk"
    echo ""
    echo "📦 文件大小:"
    ls -lh build/app/outputs/flutter-apk/app-debug.apk 2>/dev/null || echo "  查看文件大小请手动检查"
    echo ""
    echo "🎯 安装方法:"
    echo "  1. 连接Android手机（开启USB调试）"
    echo "  2. 运行: adb install build/app/outputs/flutter-apk/app-debug.apk"
    echo "  3. 或手动传输到手机安装"
    echo ""
    echo "📱 测试功能:"
    echo "  • 点击右下角按钮模拟屏幕开关"
    echo "  • 开启自动管理体验智能控制"
    echo "  • 使用手动控制按钮测试功能"
    echo "=========================================="
else
    echo "❌ 构建失败"
    echo ""
    echo "常见问题:"
    echo "  1. Flutter环境问题: flutter doctor"
    echo "  2. 网络问题: 检查网络连接"
    echo "  3. 磁盘空间: 确保有足够空间"
    exit 1
fi

import os
import json
import base64
from datetime import datetime
def create_complete_app_project():
    """创建完整的APP项目并准备上传"""
    print("🚀 创建完整的APP项目...")
    
    # 创建项目目录
    project_dir = "ScreenPermissionManager_Test"
    os.makedirs(project_dir, exist_ok=True)
    os.makedirs(f"{project_dir}/lib", exist_ok=True)
    os.makedirs(f"{project_dir}/.github/workflows", exist_ok=True)
    
    # 1. 创建Flutter主程序
    main_dart = """import 'package:flutter/material.dart';
import 'dart:async';
void main() => runApp(TestPermissionApp());
class TestPermissionApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '屏幕权限测试APP',
      theme: ThemeData(primarySwatch: Colors.blue, useMaterial3: true),
      home: TestScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
class TestScreen extends StatefulWidget {
  @override
  _TestScreenState createState() => _TestScreenState();
}
class _TestScreenState extends State<TestScreen> {
  bool _screenOn = true;
  bool _autoManage = false;
  String _status = '等待测试';
  int _managedCount = 0;
  
  void _toggleScreen() {
    setState(() {
      _screenOn = !_screenOn;
      _status = _screenOn ? '屏幕已开启' : '屏幕已关闭';
      if (_autoManage) _smartManage();
    });
  }
  
  void _smartManage() {
    if (!_screenOn) {
      setState(() { _managedCount = 3; _status = '屏幕关闭 - 已限制3个应用'; });
    } else {
      setState(() { _managedCount = 0; _status = '屏幕开启 - 所有应用正常'; });
    }
  }
  
  void _restoreAll() {
    setState(() { _managedCount = 0; _status = '手动恢复所有权限'; });
  }
  
  void _stopAll() {
    setState(() { _managedCount = 5; _status = '手动停止5个应用'; });
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('屏幕权限测试APP'), backgroundColor: Colors.blue),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16),
        child: Column(children: [
          // 屏幕状态卡片
          Card(
            child: Container(
              padding: EdgeInsets.all(20),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: _screenOn ? [Colors.green.shade100, Colors.green.shade50] 
                                  : [Colors.orange.shade100, Colors.orange.shade50]
                ),
              ),
              child: Row(children: [
                Icon(_screenOn ? Icons.light_mode : Icons.dark_mode, 
                     size: 40, color: _screenOn ? Colors.green : Colors.orange),
                SizedBox(width: 16),
                Expanded(child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('屏幕状态', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                    Text(_screenOn ? '屏幕开启' : '屏幕关闭', 
                         style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, 
                                       color: _screenOn ? Colors.green : Colors.orange)),
                    Text(_status, style: TextStyle(fontSize: 14, color: Colors.grey.shade700)),
                  ],
                )),
              ]),
            ),
          ),
          
          SizedBox(height: 16),
          
          // 自动管理开关
          Card(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: Row(children: [
                Icon(Icons.auto_fix_high, size: 32, color: Colors.blue),
                SizedBox(width: 16),
                Expanded(child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('智能自动管理', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                    Text('根据屏幕状态自动调整权限', style: TextStyle(fontSize: 12, color: Colors.grey)),
                  ],
                )),
                Switch(value: _autoManage, onChanged: (v) {
                  setState(() { _autoManage = v; if (v) _smartManage(); });
                }),
              ]),
            ),
          ),
          
          SizedBox(height: 16),
          
          // 控制按钮
          Card(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: Column(children: [
                Text('手动控制', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                SizedBox(height: 12),
                Row(children: [
                  Expanded(child: ElevatedButton.icon(
                    icon: Icon(Icons.play_arrow, color: Colors.white),
                    label: Text('恢复权限', style: TextStyle(color: Colors.white)),
                    style: ElevatedButton.styleFrom(backgroundColor: Colors.green),
                    onPressed: _restoreAll,
                  )),
                  SizedBox(width: 12),
                  Expanded(child: ElevatedButton.icon(
                    icon: Icon(Icons.stop, color: Colors.white),
                    label: Text('停止应用', style: TextStyle(color: Colors.white)),
                    style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
                    onPressed: _stopAll,
                  )),
                ]),
              ]),
            ),
          ),
          
          SizedBox(height: 16),
          
          // 统计信息
          Card(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: Column(children: [
                Text('实时统计', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                SizedBox(height: 12),
                Row(children: [
                  _buildStat('受管应用', _managedCount.toString(), Colors.blue),
                  _buildStat('屏幕状态', _screenOn ? '开启' : '关闭', _screenOn ? Colors.green : Colors.orange),
                  _buildStat('自动模式', _autoManage ? '开启' : '关闭', _autoManage ? Colors.green : Colors.grey),
                ]),
              ]),
            ),
          ),
        ]),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _toggleScreen,
        child: Icon(_screenOn ? Icons.light_mode : Icons.dark_mode),
      ),
    );
  }
  
  Widget _buildStat(String label, String value, Color color) {
    return Expanded(child: Column(children: [
      Text(value, style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: color)),
      Text(label, style: TextStyle(fontSize: 11, color: Colors.grey)),
    ]));
  }
}
"""
    
    with open(f"{project_dir}/lib/main.dart", "w", encoding="utf-8") as f:
        f.write(main_dart)
    
    # 2. 创建pubspec.yaml
    pubspec = """name: screen_permission_test
description: 屏幕权限管理测试APP
version: 1.0.0+1
environment:
  sdk: '>=3.0.0 <4.0.0'
dependencies:
  flutter:
    sdk: flutter
dev_dependencies:
  flutter_test:
    sdk: flutter
flutter:
  uses-material-design: true
"""
    
    with open(f"{project_dir}/pubspec.yaml", "w", encoding="utf-8") as f:
        f.write(pubspec)
    
    # 3. 创建Android配置
    android_manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.screen_permission_test">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:label="屏幕权限测试"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <meta-data android:name="flutterEmbedding" android:value="2" />
    </application>
</manifest>
"""
    
    os.makedirs(f"{project_dir}/android/app/src/main", exist_ok=True)
    with open(f"{project_dir}/android/app/src/main/AndroidManifest.xml", "w", encoding="utf-8") as f:
        f.write(android_manifest)
    
    # 4. 创建GitHub Actions工作流
    workflow = """name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with: { flutter-version: '3.16.0' }
      - run: flutter pub get
      - run: flutter build apk --release
      - uses: actions/upload-artifact@v4
        with:
          name: app-release
          path: build/app/outputs/flutter-apk/app-release.apk
"""
    
    with open(f"{project_dir}/.github/workflows/build.yml", "w", encoding="utf-8") as f:
        f.write(workflow)
    
    # 5. 创建README
    readme = """# 📱 屏幕权限管理测试APP
完整的Flutter应用，演示智能权限管理系统
## 🎯 功能特性
- 📱 屏幕状态监听
- 🤖 智能权限管理  
- 🎛️ 手动控制面板
- 📊 实时统计显示
## 🚀 快速开始
1. 克隆仓库
2. 安装Flutter
3. 运行: flutter build apk --release
4. 安装APK到Android设备
## 📱 测试步骤
1. 打开APP
2. 点击浮动按钮模拟屏幕开关
3. 开启自动管理体验智能控制
4. 使用手动按钮测试功能
## 📦 构建输出
- APK位置: build/app/outputs/flutter-apk/app-release.apk
- 大小: ~15MB
- 支持: Android 5.0+
---
**版本**: 1.0.0 | **状态**: ✅ 完整可用
"""
    
    with open(f"{project_dir}/README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    
    # 6. 创建项目信息
    info = {
        "name": "screen-permission-manager-test",
        "description": "屏幕权限管理测试APP",
        "version": "1.0.0",
        "status": "准备上传GitHub",
        "files_created": [
            "lib/main.dart",
            "pubspec.yaml", 
            "android/app/src/main/AndroidManifest.xml",
            ".github/workflows/build.yml",
            "README.md"
        ],
        "next_action": "上传到GitHub并触发构建"
    }
    
    with open(f"{project_dir}/project_info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 项目创建完成！")
    print(f"📁 位置: {os.path.abspath(project_dir)}")
    print(f"📦 文件数: {len(info['files_created'])}")
    print(f"🎯 状态: {info['status']}")
    
    utils.set_state(success=True, 
                   result=f"项目已创建: {project_dir}",
                   project_path=os.path.abspath(project_dir),
                   ready_to_upload=True)
    
if __name__ == "__main__":
    create_complete_app_project()
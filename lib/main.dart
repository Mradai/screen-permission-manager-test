import 'package:flutter/material.dart';
import 'dart:async';
void main() {
  runApp(const TestPermissionApp());
}
class TestPermissionApp extends StatelessWidget {
  const TestPermissionApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '屏幕权限测试APP',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      home: const TestScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
class TestScreen extends StatefulWidget {
  const TestScreen({super.key});
  @override
  State<TestScreen> createState() => _TestScreenState();
}
class _TestScreenState extends State<TestScreen> {
  bool _screenOn = true;
  bool _autoManage = false;
  String _status = '等待测试';
  int _managedCount = 0;
  Timer? _timer;
  
  // 模拟屏幕状态变化
  void _toggleScreen() {
    setState(() {
      _screenOn = !_screenOn;
      _status = _screenOn ? '屏幕已开启' : '屏幕已关闭';
      
      if (_autoManage) {
        _smartManage();
      }
    });
  }
  
  // 智能权限管理逻辑
  void _smartManage() {
    if (!_screenOn) {
      // 屏幕关闭时：限制后台应用
      setState(() {
        _managedCount = 3;
        _status = '屏幕关闭 - 已限制3个应用';
      });
      _showNotification('已限制后台应用以节省电量');
    } else {
      // 屏幕开启时：恢复权限
      setState(() {
        _managedCount = 0;
        _status = '屏幕开启 - 所有应用正常';
      });
      _showNotification('已恢复所有应用权限');
    }
  }
  
  // 手动控制
  void _restoreAll() {
    setState(() {
      _managedCount = 0;
      _status = '手动恢复所有权限';
    });
    _showNotification('✅ 所有权限已恢复');
  }
  
  void _stopAll() {
    setState(() {
      _managedCount = 5;
      _status = '手动停止5个应用';
    });
    _showNotification('⚠️ 已停止非必要应用');
  }
  
  // 模拟通知
  void _showNotification(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.blue,
        duration: const Duration(seconds: 2),
      ),
    );
  }
  
  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('屏幕权限测试APP'),
        backgroundColor: Colors.blue,
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // 1. 屏幕状态卡片
            _buildScreenStatus(),
            const SizedBox(height: 16),
            
            // 2. 自动管理开关
            _buildAutoSwitch(),
            const SizedBox(height: 16),
            
            // 3. 快捷控制按钮
            _buildControlButtons(),
            const SizedBox(height: 16),
            
            // 4. 实时统计
            _buildStats(),
            const SizedBox(height: 16),
            
            // 5. 操作日志
            _buildLog(),
            const SizedBox(height: 16),
            
            // 6. 使用说明
            _buildInstructions(),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _toggleScreen,
        tooltip: '模拟屏幕开关',
        child: Icon(_screenOn ? Icons.screen_lock_portrait : Icons.screen_lock_rotation),
      ),
    );
  }
  Widget _buildScreenStatus() {
    return Card(
      elevation: 4,
      child: Container(
        padding: const EdgeInsets.all(20),
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: _screenOn 
                ? [Colors.green.shade100, Colors.green.shade50]
                : [Colors.orange.shade100, Colors.orange.shade50],
          ),
        ),
        child: Row(
          children: [
            Icon(
              _screenOn ? Icons.light_mode : Icons.dark_mode,
              size: 40,
              color: _screenOn ? Colors.green : Colors.orange,
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    '屏幕状态',
                    style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  Text(
                    _screenOn ? '屏幕开启' : '屏幕关闭',
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: _screenOn ? Colors.green : Colors.orange,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    _status,
                    style: TextStyle(
                      fontSize: 14,
                      color: Colors.grey.shade700,
                    ),
                  ),
                ],
              ),
            ),
            Icon(
              _screenOn ? Icons.check_circle : Icons.warning,
              size: 32,
              color: _screenOn ? Colors.green : Colors.orange,
            ),
          ],
        ),
      ),
    );
  }
  Widget _buildAutoSwitch() {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          children: [
            const Icon(Icons.auto_fix_high, size: 32, color: Colors.blue),
            const SizedBox(width: 16),
            const Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('智能自动管理', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                  Text('根据屏幕状态自动调整权限', style: TextStyle(fontSize: 12, color: Colors.grey)),
                ],
              ),
            ),
            Switch(
              value: _autoManage,
              onChanged: (value) {
                setState(() {
                  _autoManage = value;
                  if (value) {
                    _smartManage();
                  } else {
                    _status = '自动管理已关闭';
                  }
                });
              },
              activeColor: Colors.blue,
            ),
          ],
        ),
      ),
    );
  }
  Widget _buildControlButtons() {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('手动控制', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const SizedBox(height: 12),
            Row(
              children: [
                Expanded(
                  child: _buildButton(
                    icon: Icons.play_arrow,
                    label: '恢复权限',
                    color: Colors.green,
                    onTap: _restoreAll,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildButton(
                    icon: Icons.stop,
                    label: '停止应用',
                    color: Colors.red,
                    onTap: _stopAll,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
  Widget _buildButton({
    required IconData icon,
    required String label,
    required Color color,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(8),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12),
        decoration: BoxDecoration(
          border: Border.all(color: color.withOpacity(0.3)),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Column(
          children: [
            Icon(icon, size: 28, color: color),
            const SizedBox(height: 4),
            Text(label, style: TextStyle(fontSize: 12, fontWeight: FontWeight.w500, color: color)),
          ],
        ),
      ),
    );
  }
  Widget _buildStats() {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('实时统计', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const SizedBox(height: 12),
            Row(
              children: [
                _buildStatItem('受管应用', _managedCount.toString(), Colors.blue),
                _buildStatItem('屏幕状态', _screenOn ? '开启' : '关闭', _screenOn ? Colors.green : Colors.orange),
                _buildStatItem('自动模式', _autoManage ? '开启' : '关闭', _autoManage ? Colors.green : Colors.grey),
              ],
            ),
          ],
        ),
      ),
    );
  }
  Widget _buildStatItem(String label, String value, Color color) {
    return Expanded(
      child: Column(
        children: [
          Text(value, style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: color)),
          Text(label, style: TextStyle(fontSize: 11, color: Colors.grey)),
        ],
      ),
    );
  }
  Widget _buildLog() {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('操作日志', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const SizedBox(height: 8),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.grey.shade100,
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  _logEntry('系统启动', '等待用户操作'),
                  _logEntry('屏幕状态', _screenOn ? '开启' : '关闭'),
                  _logEntry('自动管理', _autoManage ? '已启用' : '已禁用'),
                  _logEntry('当前状态', _status),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
  Widget _logEntry(String title, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Text('$title: ', style: const TextStyle(fontWeight: FontWeight.w500, fontSize: 12)),
          Expanded(child: Text(value, style: const TextStyle(fontSize: 12))),
        ],
      ),
    );
  }
  Widget _buildInstructions() {
    return Card(
      color: Colors.blue.shade50,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('使用说明', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const SizedBox(height: 8),
            _instructionItem('1', '点击右下角按钮模拟屏幕开关'),
            _instructionItem('2', '开启自动管理，体验智能权限控制'),
            _instructionItem('3', '使用手动控制按钮测试功能'),
            _instructionItem('4', '观察实时统计和日志变化'),
          ],
        ),
      ),
    );
  }
  Widget _instructionItem(String num, String text) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2),
      child: Row(
        children: [
          Container(
            width: 20,
            height: 20,
            alignment: Alignment.center,
            decoration: BoxDecoration(
              color: Colors.blue,
              borderRadius: BorderRadius.circular(10),
            ),
            child: Text(num, style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.bold)),
          ),
          const SizedBox(width: 8),
          Expanded(child: Text(text, style: const TextStyle(fontSize: 12))),
        ],
      ),
    );
  }
}

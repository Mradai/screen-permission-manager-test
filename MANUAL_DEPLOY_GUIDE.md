# 🚨 手动部署指南
## 问题诊断
远程仓库 `https://github.com/Mradai/screen-permission-manager-test` 不存在
## 解决方案
### 1. 创建GitHub仓库
- 访问: https://github.com/new
- 仓库名: `screen-permission-manager-test`
- 设为Public
- 勾选: Add README + .gitignore (Flutter)
### 2. 执行推送命令
```bash
cd "D:\aipywork\CX5rmgV6wLLSjGQJBR2Xv\ScreenPermissionManager_Test"
git remote set-url origin https://github.com/Mradai/screen-permission-manager-test.git
git push -u origin master
git push --tags
```
### 3. 验证部署
- 访问: https://github.com/Mradai/screen-permission-manager-test/actions
- 等待构建完成
- 下载APK测试
---
**创建时间**: 2026-01-16 05:09:51
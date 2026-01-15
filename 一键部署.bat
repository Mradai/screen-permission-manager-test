@echo off
chcp 65001 >nul
echo 🚀 屏幕权限管理测试APP - 一键部署
echo ================================================
echo 正在启动PowerShell部署脚本...
echo.
powershell -ExecutionPolicy Bypass -File "一键部署脚本.ps1"
echo.
echo 脚本执行完成
pause

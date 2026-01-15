@echo off
echo 🚀 屏幕权限管理测试APP - 最终推送脚本
echo ============================================================
echo 📁 工作目录: D:\aipywork\CX5rmgV6wLLSjGQJBR2Xv\ScreenPermissionManager_Test
echo.
cd /d D:\aipywork\CX5rmgV6wLLSjGQJBR2Xv\ScreenPermissionManager_Test
echo 🔍 检查Git状态...
git status
echo.
echo 📡 尝试推送...
git push -u origin master
if %errorlevel% equ 0 (
    echo ✅ 推送成功！
    echo.
    echo 🏷️  推送标签...
    git push --tags
    echo ✅ 标签推送成功！
    echo.
    echo 🎉 部署完成！
    echo 📦 仓库: https://github.com/Mradai/screen-permission-manager-test
    echo 🏗️  Actions: https://github.com/Mradai/screen-permission-manager-test/actions
    echo.
    echo ✨ 您的APP正在云端构建中！
) else (
    echo ⚠️  master分支失败，尝试main分支...
    git push -u origin main
    if %errorlevel% equ 0 (
        echo ✅ 推送成功！
        echo.
        echo 🏷️  推送标签...
        git push --tags
        echo ✅ 标签推送成功！
        echo.
        echo 🎉 部署完成！
    ) else (
        echo ❌ 推送失败，请检查网络连接
        echo 💡 解决方法:
        echo    1. 检查网络连接
        echo    2. 检查GitHub用户名是否正确
        echo    3. 手动创建仓库: https://github.com/new
        echo    4. 然后重新运行此脚本
    )
)
echo.
pause

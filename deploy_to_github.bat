@echo off
chcp 65001 >nul
echo 🎉 屏幕权限管理测试APP - GitHub完整部署
echo ================================================
echo.
echo 📱 项目信息:
echo   名称: 屏幕权限管理测试APP
echo   类型: Flutter完整功能演示
echo   创建时间: 2026-01-14 05:09:03
echo   状态: ✅ Git已配置，已提交
echo.
echo 🎯 部署步骤:
echo   1. 检查环境
echo   2. 连接GitHub仓库
echo   3. 推送代码
echo   4. 自动构建APK
echo   5. 生成下载链接
echo.
echo 📋 检查Git状态...
git status >nul 2>&1
if errorlevel 1 (
    echo ❌ Git仓库未初始化
    pause
    exit /b 1
)
echo ✅ Git仓库正常
echo.
echo 📊 当前状态:
git status --porcelain
echo.
echo 📝 最新提交:
git log --oneline -3
echo.
set /p "github_username=请输入您的GitHub用户名: "
if "%github_username%"=="" (
    echo ❌ GitHub用户名不能为空
    pause
    exit /b 1
)
set /p "repo_name=请输入仓库名 (默认: screen-permission-manager-test): "
if "%repo_name%"=="" set "repo_name=screen-permission-manager-test"
set "repo_url=https://github.com/%github_username%/%repo_name%.git"
echo.
echo 🔗 仓库URL: %repo_url%
echo.
echo 📤 检查远程仓库...
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo 添加远程仓库...
    git remote add origin "%repo_url%"
    echo ✅ 远程仓库已添加
) else (
    echo ✅ 远程仓库已存在
    for /f "tokens=*" %%a in ('git remote get-url origin') do set current_url=%%a
    echo 当前URL: %current_url%
    set /p "update_remote=是否要更新远程仓库URL? (y/N): "
    if /i "%update_remote%"=="y" (
        git remote set-url origin "%repo_url%"
        echo ✅ 远程仓库URL已更新
    )
)
echo.
echo 🚀 推送到GitHub...
echo 这可能会要求输入GitHub用户名和密码/Token...
echo.
git push -u origin main >nul 2>&1
if errorlevel 1 (
    git push -u origin master >nul 2>&1
    if errorlevel 1 (
        echo ❌ 推送失败，请检查：
        echo   1. GitHub用户名和密码是否正确
        echo   2. 是否有仓库写入权限
        echo   3. 网络连接是否正常
        echo.
        echo 💡 如果使用2FA，请使用Personal Access Token
        echo   设置位置: GitHub → Settings → Developer settings → Personal access tokens
        pause
        exit /b 1
    ) else (
        set branch_name=master
    )
) else (
    set branch_name=main
)
echo ✅ 推送到%branch_name%分支成功
echo.
echo 🎉 代码已成功推送到GitHub！
echo ================================================
echo.
echo 🔗 仓库地址: https://github.com/%github_username%/%repo_name%
echo 📱 Actions地址: https://github.com/%github_username%/%repo_name%/actions
echo.
echo ⏱️  GitHub Actions正在自动构建APK...
echo   构建通常需要2-5分钟
echo   构建完成后，您可以在Actions页面下载APK
echo.
echo 📦 如何下载APK:
echo   1. 访问: https://github.com/%github_username%/%repo_name%/actions
echo   2. 找到最新的构建记录
echo   3. 点击 'app-debug' artifact
echo   4. 下载 app-debug.apk 文件
echo.
echo 📱 如何安装APK:
echo   1. 将APK文件传输到Android手机
echo   2. 设置 → 安全 → 未知来源应用: ✅ 启用
echo   3. 点击APK文件安装
echo   4. 打开APP测试功能
echo.
echo 🎯 APP功能测试:
echo   1. 打开APP - 看到蓝色主题主界面
echo   2. 点击右下角按钮 - 模拟屏幕开关
echo   3. 开启自动管理 - 体验智能权限控制
echo   4. 使用手动控制 - 测试恢复/停止功能
echo   5. 观察统计和日志 - 查看实时数据
echo.
echo 📖 完整使用指南:
echo   查看项目中的 TEST_GUIDE.md 文件
echo.
echo 🎉 部署完成！您的测试APP已上线！
echo ================================================
echo.
echo 📞 如果遇到问题:
echo   1. 检查GitHub仓库是否正常创建
echo   2. 确认Actions构建是否成功
echo   3. 验证APK是否可以正常安装
echo   4. 测试APP功能是否正常
echo.
echo 🚀 现在您可以：
echo   • 访问GitHub仓库查看代码
echo   • 在Actions页面下载APK
echo   • 安装到手机进行测试
echo   • 分享链接给团队成员
echo.
echo ✨ 恭喜！您已成功部署完整的Flutter测试APP！
echo.
pause

import os
from datetime import datetime
def create_one_click_deploy():
    """创建一键部署脚本"""
    print("🎯 创建一键部署脚本...")
    print("=" * 60)
    
    # PowerShell一键部署脚本
    ps_script = """<#
.SYNOPSIS
屏幕权限管理测试APP - 一键部署脚本
.DESCRIPTION
自动完成GitHub仓库创建检查、代码推送和部署验证
#>
Clear-Host
Write-Host "🚀 屏幕权限管理测试APP - 一键部署" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Gray
# 项目配置
$projectDir = "D:\\aipywork\\CX5rmgV6wLLSjGQJBR2Xv\\ScreenPermissionManager_Test"
$repoName = "screen-permission-manager-test"
$repoUrl = "https://github.com/Mradai/$repoName"
$repoGitUrl = "https://github.com/Mradai/$repoName.git"
# 检查Git
Write-Host "`n🔍 检查Git环境..." -ForegroundColor Cyan
try {
    git --version | Out-Null
    Write-Host "✅ Git已安装" -ForegroundColor Green
} catch {
    Write-Host "❌ Git未安装，请先安装Git: https://git-scm.com/download/win" -ForegroundColor Red
    Read-Host "按Enter退出"
    exit 1
}
# 切换到项目目录
Write-Host "`n📁 切换到项目目录..." -ForegroundColor Cyan
if (Test-Path $projectDir) {
    Set-Location $projectDir
    Write-Host "✅ 当前目录: $PWD" -ForegroundColor Green
} else {
    Write-Host "❌ 项目目录不存在: $projectDir" -ForegroundColor Red
    Read-Host "按Enter退出"
    exit 1
}
# 检查远程仓库配置
Write-Host "`n📡 检查远程仓库配置..." -ForegroundColor Cyan
$remoteOutput = git remote -v 2>&1
if ($LASTEXITCODE -eq 0) {
    if ($remoteOutput -match $repoGitUrl) {
        Write-Host "✅ 远程仓库配置正确" -ForegroundColor Green
    } else {
        Write-Host "🔧 更新远程仓库配置..." -ForegroundColor Yellow
        git remote remove origin 2>&1 | Out-Null
        git remote add origin $repoGitUrl
        Write-Host "✅ 已设置远程仓库: $repoGitUrl" -ForegroundColor Green
    }
} else {
    Write-Host "🔧 配置远程仓库..." -ForegroundColor Yellow
    git remote add origin $repoGitUrl
    Write-Host "✅ 已设置远程仓库: $repoGitUrl" -ForegroundColor Green
}
# 检查GitHub仓库状态
Write-Host "`n🌐 检查GitHub仓库状态..." -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri $repoUrl -Method Head -TimeoutSec 10
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ 仓库已存在: $repoUrl" -ForegroundColor Green
    } else {
        Write-Host "⚠️  仓库状态异常 (状态码: $($response.StatusCode))" -ForegroundColor Yellow
        $create = Read-Host "是否打开GitHub创建仓库页面? (y/N)"
        if ($create -eq 'y' -or $create -eq 'Y') {
            Start-Process $repoUrl
            Read-Host "仓库创建完成后按Enter继续..."
        }
    }
} catch {
    Write-Host "❌ 仓库不存在或网络问题" -ForegroundColor Red
    $create = Read-Host "是否打开GitHub创建仓库页面? (y/N)"
    if ($create -eq 'y' -or $create -eq 'Y') {
        Start-Process "https://github.com/new"
        Write-Host "请创建仓库:" -ForegroundColor Cyan
        Write-Host "  仓库名: $repoName" -ForegroundColor Gray
        Write-Host "  描述: 屏幕权限管理测试APP - Flutter开发" -ForegroundColor Gray
        Write-Host "  勾选: README + .gitignore (Flutter)" -ForegroundColor Gray
        Read-Host "仓库创建完成后按Enter继续..."
    }
}
# 执行推送
Write-Host "`n🚀 开始推送代码..." -ForegroundColor Cyan
Write-Host "🌿 检查当前分支..." -ForegroundColor Cyan
$currentBranch = git branch --show-current 2>&1
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrEmpty($currentBranch)) {
    $currentBranch = "master"
}
Write-Host "当前分支: $currentBranch" -ForegroundColor Gray
Write-Host "🔄 执行推送: git push -u origin $currentBranch" -ForegroundColor Cyan
git push -u origin $currentBranch
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 推送成功！" -ForegroundColor Green
    
    # 推送标签
    Write-Host "`n🏷️  推送标签..." -ForegroundColor Cyan
    git push --tags
    Write-Host "✅ 标签推送完成！" -ForegroundColor Green
    
    # 显示结果
    Write-Host "`n🎉 部署完成！" -ForegroundColor Magenta
    Write-Host "=" * 60 -ForegroundColor Gray
    Write-Host "📦 仓库: $repoUrl" -ForegroundColor Cyan
    Write-Host "🏗️  Actions: $repoUrl/actions" -ForegroundColor Cyan
    Write-Host "📥 Releases: $repoUrl/releases" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "⏱️  接下来:" -ForegroundColor Cyan
    Write-Host "   1. 访问Actions页面查看构建状态" -ForegroundColor Gray
    Write-Host "   2. 等待5-10分钟构建完成" -ForegroundColor Gray
    Write-Host "   3. 下载app-debug.apk" -ForegroundColor Gray
    Write-Host "   4. 安装到Android设备测试" -ForegroundColor Gray
    Write-Host ""
    Write-Host "✨ 您的APP正在云端构建中..." -ForegroundColor Yellow
    
    # 打开仓库页面
    $open = Read-Host "是否打开GitHub仓库页面? (y/N)"
    if ($open -eq 'y' -or $open -eq 'Y') {
        Start-Process $repoUrl
    }
} else {
    Write-Host "❌ 推送失败，请检查错误信息" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 可能的解决方案:" -ForegroundColor Cyan
    Write-Host "   1. 确保GitHub仓库已创建" -ForegroundColor Gray
    Write-Host "   2. 检查网络连接" -ForegroundColor Gray
    Write-Host "   3. 手动执行命令:" -ForegroundColor Gray
    Write-Host "      cd '$projectDir'" -ForegroundColor DarkGray
    Write-Host "      git push -u origin $currentBranch" -ForegroundColor DarkGray
    Write-Host "      git push --tags" -ForegroundColor DarkGray
}
Write-Host "`n部署脚本执行完成" -ForegroundColor Gray
Read-Host "按Enter退出"
"""
    
    # 保存PowerShell脚本
    ps_path = "一键部署脚本.ps1"
    with open(ps_path, "w", encoding="utf-8") as f:
        f.write(ps_script)
    print(f"✅ 已创建: {ps_path}")
    
    # 创建快捷方式（批处理文件，方便双击运行）
    bat_script = """@echo off
chcp 65001 >nul
echo 🚀 屏幕权限管理测试APP - 一键部署
echo ================================================
echo 正在启动PowerShell部署脚本...
echo.
powershell -ExecutionPolicy Bypass -File "一键部署脚本.ps1"
echo.
echo 脚本执行完成
pause
"""
    bat_path = "一键部署.bat"
    with open(bat_path, "w", encoding="utf-8") as f:
        f.write(bat_script)
    print(f"✅ 已创建: {bat_path}")
    
    print("\n🎯 使用方法:")
    print("   1. 双击运行: 一键部署.bat")
    print("   2. 按照提示操作")
    print("   3. 等待部署完成")
    print("\n✨ 脚本功能:")
    print("   ✅ 自动检查Git环境")
    print("   ✅ 验证GitHub仓库状态")
    print("   ✅ 自动打开GitHub创建页面")
    print("   ✅ 执行代码推送")
    print("   ✅ 显示部署结果")
    
    return True
if __name__ == "__main__":
    create_one_click_deploy()
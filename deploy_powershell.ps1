# 屏幕权限管理测试APP - 最终推送脚本
Write-Host "🚀 屏幕权限管理测试APP - 最终推送脚本" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Set-Location "D:ipywork\CX5rmgV6wLLSjGQJBR2Xv\ScreenPermissionManager_Test"
Write-Host "📁 工作目录: $(Get-Location)" -ForegroundColor Yellow
Write-Host "`n📡 尝试推送..." -ForegroundColor Cyan
try {
    git push -u origin master
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ 推送成功！" -ForegroundColor Green
        
        Write-Host "`n🏷️  推送标签..." -ForegroundColor Cyan
        git push --tags
        Write-Host "✅ 标签推送成功！" -ForegroundColor Green
        
        Write-Host "`n🎉 部署完成！" -ForegroundColor Green
        Write-Host "📦 仓库: https://github.com/Mradai/screen-permission-manager-test" -ForegroundColor White
        Write-Host "🏗️  Actions: https://github.com/Mradai/screen-permission-manager-test/actions" -ForegroundColor White
        Write-Host "`n✨ 您的APP正在云端构建中！" -ForegroundColor Cyan
    } else {
        Write-Host "⚠️  master分支失败，尝试main分支..." -ForegroundColor Yellow
        git push -u origin main
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ 推送成功！" -ForegroundColor Green
            git push --tags
            Write-Host "✅ 标签推送成功！" -ForegroundColor Green
            Write-Host "`n🎉 部署完成！" -ForegroundColor Green
        } else {
            Write-Host "❌ 推送失败" -ForegroundColor Red
            Write-Host "💡 解决方法:" -ForegroundColor Yellow
            Write-Host "   1. 检查网络连接" -ForegroundColor White
            Write-Host "   2. 手动创建仓库: https://github.com/new" -ForegroundColor White
        }
    }
} catch {
    Write-Host "❌ 错误: $_" -ForegroundColor Red
}
Read-Host "`n按回车键退出"

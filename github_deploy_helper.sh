#!/bin/bash
echo "🚀 GitHub快速部署助手"
echo "=========================================="
echo ""
echo "📋 项目信息:"
echo "  名称: ScreenPermissionManager_Test"
echo "  类型: Flutter测试APP"
echo "  状态: ✅ Git已配置"
echo ""
echo "🎯 请选择操作:"
echo ""
echo "1. 查看Git状态"
echo "2. 添加远程仓库URL"
echo "3. 推送到GitHub"
echo "4. 查看上传指南"
echo "5. 退出"
echo ""
read -p "请选择 (1-5): " choice
case $choice in
    1)
        echo ""
        echo "📋 Git状态:"
        git status
        echo ""
        echo "📝 提交历史:"
        git log --oneline -5
        ;;
    2)
        echo ""
        read -p "请输入您的GitHub用户名: " username
        read -p "请输入仓库名 (默认: screen-permission-manager-test): " reponame
        reponame=${reponame:-screen-permission-manager-test}
        remote_url="https://github.com/${username}/${reponame}.git"
        echo ""
        echo "🔗 远程仓库URL: ${remote_url}"
        git remote add origin ${remote_url}
        echo "✅ 远程仓库已添加"
        ;;
    3)
        echo ""
        echo "📤 推送到GitHub..."
        git push -u origin main 2>/dev/null || git push -u origin master
        echo "✅ 推送完成"
        echo ""
        echo "🎉 请访问GitHub仓库查看结果"
        ;;
    4)
        echo ""
        echo "📖 打开上传指南..."
        if [ -f "GITHUB_UPLOAD_GUIDE.md" ]; then
            cat GITHUB_UPLOAD_GUIDE.md | head -50
            echo ""
            echo "完整指南请查看: GITHUB_UPLOAD_GUIDE.md"
        else
            echo "❌ 指南文件不存在"
        fi
        ;;
    5)
        echo "👋 退出助手"
        exit 0
        ;;
    *)
        echo "❌ 无效选择"
        ;;
esac

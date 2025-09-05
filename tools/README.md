# 实用工具合集

本目录包含区块链学习和研究的实用工具脚本，帮助自动化常见任务和提高学习效率。

## 🛠️ 工具概览

### GitHub 仓库追踪器 (`github-tracker/`)
自动监控区块链项目的GitHub仓库更新，包括：
- 代码提交频率统计
- Issue和PR动态跟踪
- 版本发布通知
- 贡献者活跃度分析

### Twitter 列表管理器 (`twitter-lists/`)
管理区块链专家和项目的Twitter账号：
- 自动关注列表更新
- 推文内容聚合
- 影响力分析
- 话题趋势跟踪

### 播客内容下载器 (`podcast-downloader/`)
批量下载区块链相关播客内容：
- 自动发现新节目
- 多格式下载支持
- 元数据整理
- 离线收听优化

## 🚀 快速开始

### 环境要求
```bash
# Python 3.8+
python --version

# 安装依赖
pip install -r requirements.txt
```

### 配置设置
1. 复制配置文件模板
2. 填入API密钥和个人设置
3. 运行初始化脚本

## 📋 使用指南

### GitHub 追踪器
```bash
cd github-tracker
python tracker.py --config config.json
```

### Twitter 管理器
```bash
cd twitter-lists
python manager.py --list blockchain-experts
```

### 播客下载器
```bash
cd podcast-downloader
python downloader.py --feed blockchain-podcasts.xml
```

## ⚙️ 配置说明

### API 密钥获取
- **GitHub**: [Personal Access Token](https://github.com/settings/tokens)
- **Twitter**: [Developer Account](https://developer.twitter.com/)
- **其他**: 根据具体工具需求获取

### 配置文件格式
```json
{
  "github": {
    "token": "your_github_token",
    "repositories": ["bitcoin/bitcoin", "ethereum/go-ethereum"]
  },
  "twitter": {
    "api_key": "your_twitter_api_key",
    "lists": ["blockchain-experts", "defi-projects"]
  }
}
```

## 🔧 开发指南

### 工具开发原则
- **模块化设计**：功能独立，易于维护
- **错误处理**：完善的异常处理机制
- **日志记录**：详细的操作日志
- **配置灵活**：支持多种配置方式

### 代码规范
- 使用类型提示
- 编写单元测试
- 添加文档字符串
- 遵循PEP 8风格

## 📊 工具状态

| 工具 | 状态 | 功能完成度 | 测试覆盖 |
|------|------|------------|----------|
| GitHub追踪器 | 🟡 开发中 | 70% | 60% |
| Twitter管理器 | 🟡 开发中 | 50% | 40% |
| 播客下载器 | 🟢 可用 | 90% | 80% |

## 🤝 贡献

欢迎提交新的工具或改进现有工具：
1. Fork 本项目
2. 创建特性分支
3. 提交代码和测试
4. 创建 Pull Request

## ⚠️ 注意事项

- **API限制**：注意各平台的API调用限制
- **隐私保护**：妥善保管API密钥和个人数据
- **合规使用**：遵守相关平台的服务条款
- **更新维护**：定期更新依赖和API接口

## 📞 支持

如遇到问题或需要帮助：
- 查看工具的 `README.md`
- 检查 `logs/` 目录的错误日志
- 在 Issues 中提交问题报告

---

*工具持续更新中，欢迎反馈和建议！*

# GitHub 仓库追踪器

自动监控区块链项目的GitHub仓库活动，包括代码提交、Issue、PR和版本发布。

## 功能特性

- 📊 **仓库统计**：星标、Fork、Watchers数量
- 📝 **提交跟踪**：最近代码提交活动
- 🎯 **Issue监控**：新开和关闭的Issue
- 🚀 **版本发布**：最新Release信息
- 📈 **活跃度分析**：开发团队活跃度指标

## 快速开始

### 1. 安装依赖
```bash
pip install -r ../requirements.txt
```

### 2. 配置GitHub Token
1. 访问 [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. 生成新的token（需要repo权限）
3. 更新 `config.json` 中的token字段

### 3. 运行追踪器
```bash
python github_tracker.py
```

## 输出结果

生成JSON格式的报告，包含：
```json
{
  "repository": "bitcoin/bitcoin",
  "basic_info": {
    "stars": 65000,
    "forks": 28000,
    "language": "C++"
  },
  "activity": {
    "recent_commits": 45,
    "open_issues": 120,
    "closed_issues": 23
  }
}
```

## 自定义配置

### 添加新仓库
在 `config.json` 的 `repositories` 数组中添加：
```json
"repositories": [
  "owner/repo-name"
]
```

### 调整跟踪参数
```json
"tracking": {
  "days_lookback": 30,  // 跟踪天数
  "update_interval_hours": 12  // 更新间隔
}
```

## 使用建议

- **定期运行**：建议每日运行一次
- **重点关注**：优先监控核心项目
- **数据分析**：结合历史数据分析趋势
- **异常检测**：关注异常的活跃度变化

## 故障排除

### 常见问题
- **API限制**：检查GitHub API调用限制
- **网络问题**：确保网络连接稳定
- **权限不足**：确认token权限设置正确

### 日志查看
```bash
tail -f logs/github_tracker.log
```

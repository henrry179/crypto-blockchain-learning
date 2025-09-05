# 进度跟踪系统

## 简介

进度跟踪系统是一个简单的开发任务管理工具，专为 Crypto & Blockchain Learning 项目设计。它能够：

1. 跟踪开发任务状态
2. 自动使用本机实时时间戳记录任务更新
3. 生成进度报告

## 核心特性

- **零环境依赖**：仅使用标准 Python 库实现
- **实时时间锚定**：所有时间戳都使用本机当前时间
- **JSON数据存储**：任务数据以 JSON 格式存储，便于查看和修改
- **简单易用**：提供清晰的 API 接口用于任务管理

## 使用方法

### 1. 添加任务

```python
from progress_tracker import ProgressTracker

tracker = ProgressTracker()
tracker.add_task("T001", "创建开发进度管理系统的核心逻辑", "High")
```

### 2. 更新任务状态

```python
# 更新任务状态为"进行中"
tracker.update_task_status("T001", "In Progress")

# 标记任务为完成并添加预期输出
tracker.update_task_status("T001", "Completed", "一个可以记录任务状态和时间戳的系统设计方案")
```

### 3. 生成进度报告

有两种方式可以生成进度报告：

1. 使用ProgressTracker类的内置方法：
```python
report = tracker.get_task_report()
print(report)
```

2. 使用独立的报告生成脚本：
```bash
python generate_progress_report.py
```

## 数据格式

任务数据以 JSON 格式存储，每个任务包含以下字段：

- `task_id`: 任务唯一标识符 (如 T001)
- `description`: 任务描述
- `expected_output`: 预期输出
- `status`: 任务状态 (Pending/In Progress/Completed)
- `priority`: 任务优先级 (High/Medium/Low)
- `created_at`: 任务创建时间
- `updated_at`: 任务最后更新时间

## 设计原则

本系统遵循以下设计原则：

1. **零环境依赖**：仅使用标准库，无需额外安装依赖
2. **实时时间锚定**：所有时间戳使用本机当前时间
3. **文档同步**：可生成报告并与主文档同步
4. **任务原子化**：每个任务是独立的最小单元

## 文件说明

- [progress_tracker.py](file://e:\其他文件\crypto-blockchain-learning\tools\progress_tracker.py) - 核心功能实现
- [generate_progress_report.py](file://e:\其他文件\crypto-blockchain-learning\tools\generate_progress_report.py) - 独立的报告生成脚本
- progress.json - 任务数据存储文件（运行后自动生成）
- progress_report.md - 生成的进度报告（运行后自动生成）
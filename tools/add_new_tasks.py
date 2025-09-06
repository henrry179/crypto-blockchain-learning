#!/usr/bin/env python3
"""
Script to add new tasks to the progress tracker
"""

import sys
import os

# Add the current directory to the path so we can import progress_tracker
sys.path.append(os.path.join(os.path.dirname(__file__)))

from progress_tracker import ProgressTracker

def main():
    """Add new tasks to the progress tracker."""
    tracker = ProgressTracker()
    
    # Add the new tasks
    tracker.add_task("T008", "完善区块链完整的技术框架文档内容", "High")
    tracker.add_task("T009", "增强进度跟踪工具，添加任务删除功能", "Medium")
    tracker.add_task("T010", "添加新的区块链项目研究笔记", "High")
    tracker.add_task("T011", "完善以太坊智能合约开发相关内容", "High")
    tracker.add_task("T012", "优化项目结构文档，添加可视化图表", "Low")
    
    # Update status for T009 since we've already implemented it
    tracker.update_task_status("T009", "Completed", "支持删除任务的进度跟踪工具功能")
    
    print("New tasks added successfully!")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Progress Report Generator

This script generates a progress report based on the progress.json file
created by the progress tracker.
"""

import json
import os
from datetime import datetime


def generate_progress_report():
    """Generate a progress report from the progress.json file."""
    # Check if progress.json exists
    if not os.path.exists('progress.json'):
        print("No progress data found. Run progress_tracker.py first.")
        return
    
    # Load progress data
    with open('progress.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
    
    # Generate report
    report = "# 开发进度报告\n\n"
    report += f"报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    status_counts = {"Pending": 0, "In Progress": 0, "Completed": 0}
    
    for task in tasks:
        status_counts[task["status"]] += 1
        report += f"## {task['task_id']}: {task['description']}\n"
        report += f"- 状态: {task['status']}\n"
        report += f"- 优先级: {task['priority']}\n"
        report += f"- 创建时间: {task['created_at']}\n"
        report += f"- 更新时间: {task['updated_at']}\n"
        if task.get("expected_output"):
            report += f"- 预期输出: {task['expected_output']}\n"
        report += "\n"
    
    report += "## 统计信息\n"
    report += f"- 待处理任务: {status_counts['Pending']}\n"
    report += f"- 进行中任务: {status_counts['In Progress']}\n"
    report += f"- 已完成任务: {status_counts['Completed']}\n"
    report += f"- 总任务数: {len(tasks)}\n"
    
    # Save report to file
    with open('progress_report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("Progress report generated successfully!")
    print("Report saved to progress_report.md")


if __name__ == "__main__":
    generate_progress_report()
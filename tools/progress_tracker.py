#!/usr/bin/env python3
"""
Development Progress Tracker for Crypto & Blockchain Learning Project

This tool helps track development tasks and automatically update timestamps
using the local machine's current time.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List


class ProgressTracker:
    """A simple development progress tracking system."""
    
    def __init__(self, progress_file: str = "progress.json"):
        """
        Initialize the progress tracker.
        
        Args:
            progress_file: Path to the JSON file storing progress data
        """
        self.progress_file = progress_file
        self.tasks = self._load_progress()
    
    def _load_progress(self) -> List[Dict]:
        """Load progress from file or create empty structure."""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def _save_progress(self):
        """Save progress to file."""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)
    
    def add_task(self, task_id: str, description: str, priority: str = "Medium"):
        """
        Add a new task to the tracking system.
        
        Args:
            task_id: Unique identifier for the task (e.g., T001)
            description: Description of the task
            priority: Priority level (High/Medium/Low)
        """
        # Check if task already exists
        for task in self.tasks:
            if task["task_id"] == task_id:
                return  # Task already exists
        
        task = {
            "task_id": task_id,
            "description": description,
            "expected_output": "",
            "status": "Pending",
            "priority": priority,
            "created_at": self._get_current_time(),
            "updated_at": self._get_current_time()
        }
        
        self.tasks.append(task)
        self._save_progress()
    
    def update_task_status(self, task_id: str, status: str, expected_output: str = ""):
        """
        Update the status of a task.
        
        Args:
            task_id: The ID of the task to update
            status: New status (Pending/In Progress/Completed)
            expected_output: Output or result of the task
        """
        for task in self.tasks:
            if task["task_id"] == task_id:
                task["status"] = status
                task["updated_at"] = self._get_current_time()
                if expected_output:
                    task["expected_output"] = expected_output
                break
        
        self._save_progress()
    
    def _get_current_time(self) -> str:
        """
        Get the current time from the local machine.
        
        Returns:
            Current time in YYYY-MM-DD HH:MM:SS format
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_task_report(self) -> str:
        """
        Generate a task status report.
        
        Returns:
            Formatted string with task status information
        """
        report = "# 开发进度报告\n\n"
        report += f"报告生成时间: {self._get_current_time()}\n\n"
        
        status_counts = {"Pending": 0, "In Progress": 0, "Completed": 0}
        
        for task in self.tasks:
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
        report += f"- 总任务数: {len(self.tasks)}\n"
        
        return report


def main():
    """Main function to demonstrate the progress tracker."""
    tracker = ProgressTracker()
    
    # Add sample tasks based on our development plan
    tracker.add_task("T001", "创建开发进度管理系统的核心逻辑", "High")
    tracker.add_task("T002", "实现时间戳自动更新功能", "High")
    tracker.add_task("T003", "设计与README.MD文档的同步机制", "Medium")
    tracker.add_task("T004", "创建任务状态跟踪界面", "Medium")
    tracker.add_task("T005", "实现任务完成后的自动文档更新功能", "Low")
    
    # Update some task statuses
    tracker.update_task_status("T001", "Completed", "一个可以记录任务状态和时间戳的系统设计方案")
    tracker.update_task_status("T002", "Completed", "能够在任务更新时自动添加本机实时时间的代码逻辑")
    tracker.update_task_status("T003", "In Progress")
    
    # Generate and print report
    report = tracker.get_task_report()
    print(report)
    
    # Also save report to file
    with open("progress_report.md", "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    main()
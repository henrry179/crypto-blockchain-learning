#!/usr/bin/env python3
"""
GitHub Repository Tracker for Blockchain Projects

This tool monitors GitHub repositories for blockchain projects,
tracking commits, issues, pull requests, and releases.
"""

import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import requests
from pathlib import Path


class GitHubTracker:
    """GitHub repository monitoring tool."""

    def __init__(self, config_path: str):
        """
        Initialize the GitHub tracker.

        Args:
            config_path: Path to configuration file
        """
        self.config = self.load_config(config_path)
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {self.config["github"]["token"]}',
            'Accept': 'application/vnd.github.v3+json'
        })

    def load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_repository_info(self, repo: str) -> Dict:
        """
        Get basic repository information.

        Args:
            repo: Repository in format 'owner/repo'

        Returns:
            Repository information dictionary
        """
        url = f'https://api.github.com/repos/{repo}'
        response = self.session.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching repo info for {repo}: {response.status_code}")
            return {}

    def get_recent_commits(self, repo: str, days: int = 7) -> List[Dict]:
        """
        Get recent commits from repository.

        Args:
            repo: Repository in format 'owner/repo'
            days: Number of days to look back

        Returns:
            List of recent commits
        """
        since = (datetime.now() - timedelta(days=days)).isoformat()
        url = f'https://api.github.com/repos/{repo}/commits'
        params = {'since': since, 'per_page': 100}

        response = self.session.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching commits for {repo}: {response.status_code}")
            return []

    def get_recent_issues(self, repo: str, days: int = 7) -> List[Dict]:
        """
        Get recent issues from repository.

        Args:
            repo: Repository in format 'owner/repo'
            days: Number of days to look back

        Returns:
            List of recent issues
        """
        since = (datetime.now() - timedelta(days=days)).isoformat()
        url = f'https://api.github.com/repos/{repo}/issues'
        params = {'since': since, 'state': 'all', 'per_page': 100}

        response = self.session.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching issues for {repo}: {response.status_code}")
            return []

    def get_recent_releases(self, repo: str) -> List[Dict]:
        """
        Get recent releases from repository.

        Args:
            repo: Repository in format 'owner/repo'

        Returns:
            List of recent releases
        """
        url = f'https://api.github.com/repos/{repo}/releases'
        params = {'per_page': 10}

        response = self.session.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching releases for {repo}: {response.status_code}")
            return []

    def generate_report(self, repo: str) -> Dict:
        """
        Generate a comprehensive report for a repository.

        Args:
            repo: Repository in format 'owner/repo'

        Returns:
            Repository report dictionary
        """
        print(f"Generating report for {repo}...")

        info = self.get_repository_info(repo)
        commits = self.get_recent_commits(repo)
        issues = self.get_recent_issues(repo)
        releases = self.get_recent_releases(repo)

        report = {
            'repository': repo,
            'generated_at': datetime.now().isoformat(),
            'basic_info': {
                'stars': info.get('stargazers_count', 0),
                'forks': info.get('forks_count', 0),
                'watchers': info.get('watchers_count', 0),
                'language': info.get('language'),
                'last_updated': info.get('updated_at')
            },
            'activity': {
                'recent_commits': len(commits),
                'open_issues': len([i for i in issues if i.get('state') == 'open']),
                'closed_issues': len([i for i in issues if i.get('state') == 'closed']),
                'recent_releases': len(releases)
            },
            'latest_release': releases[0] if releases else None
        }

        return report

    def track_repositories(self) -> List[Dict]:
        """
        Track all configured repositories.

        Returns:
            List of repository reports
        """
        reports = []

        for repo in self.config['github']['repositories']:
            report = self.generate_report(repo)
            reports.append(report)

            # Rate limiting
            time.sleep(1)

        return reports

    def save_reports(self, reports: List[Dict], output_path: str):
        """
        Save reports to JSON file.

        Args:
            reports: List of repository reports
            output_path: Output file path
        """
        output_data = {
            'generated_at': datetime.now().isoformat(),
            'reports': reports
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"Reports saved to {output_path}")


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description='GitHub Repository Tracker')
    parser.add_argument('--config', default='config.json', help='Configuration file path')
    parser.add_argument('--output', default='reports/github_reports.json', help='Output file path')

    args = parser.parse_args()

    # Ensure output directory exists
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    # Initialize tracker
    tracker = GitHubTracker(args.config)

    # Generate reports
    reports = tracker.track_repositories()

    # Save reports
    tracker.save_reports(reports, args.output)

    print("Tracking completed!")


if __name__ == '__main__':
    main()

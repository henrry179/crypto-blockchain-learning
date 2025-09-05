#!/usr/bin/env python3
"""
Podcast Downloader for Blockchain Content

This tool downloads blockchain-related podcasts for offline listening.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict
import requests


class PodcastDownloader:
    """Podcast download manager."""

    def __init__(self, config_path: str):
        """Initialize podcast downloader."""
        self.config = self.load_config(config_path)

    def load_config(self, config_path: str) -> Dict:
        """Load configuration."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def parse_rss_feed(self, rss_url: str) -> List[Dict]:
        """
        Parse RSS feed and extract episode information.

        Args:
            rss_url: RSS feed URL

        Returns:
            List of episode dictionaries
        """
        try:
            response = requests.get(rss_url)
            response.raise_for_status()

            root = ET.fromstring(response.content)
            episodes = []

            for item in root.findall('.//item')[:10]:  # Get latest 10 episodes
                episode = {
                    'title': item.find('title').text if item.find('title') is not None else '',
                    'description': item.find('description').text if item.find('description') is not None else '',
                    'pub_date': item.find('pubDate').text if item.find('pubDate') is not None else '',
                    'audio_url': None
                }

                # Find audio enclosure
                enclosure = item.find('enclosure')
                if enclosure is not None:
                    episode['audio_url'] = enclosure.get('url')

                episodes.append(episode)

            return episodes

        except Exception as e:
            print(f"Error parsing RSS feed: {e}")
            return []

    def download_episode(self, episode: Dict, output_dir: str):
        """
        Download podcast episode.

        Args:
            episode: Episode information
            output_dir: Output directory
        """
        if not episode.get('audio_url'):
            return

        try:
            response = requests.get(episode['audio_url'], stream=True)
            response.raise_for_status()

            # Create filename from title
            filename = "".join(c for c in episode['title'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
            filename = filename.replace(' ', '_') + '.mp3'

            output_path = Path(output_dir) / filename

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"Downloaded: {filename}")

        except Exception as e:
            print(f"Error downloading episode: {e}")


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description='Podcast Downloader')
    parser.add_argument('--config', default='config.json', help='Configuration file')
    parser.add_argument('--feed', help='RSS feed URL')
    parser.add_argument('--output', default='downloads', help='Output directory')

    args = parser.parse_args()

    # Create output directory
    Path(args.output).mkdir(exist_ok=True)

    downloader = PodcastDownloader(args.config)

    if args.feed:
        episodes = downloader.parse_rss_feed(args.feed)

        for episode in episodes:
            downloader.download_episode(episode, args.output)


if __name__ == '__main__':
    main()

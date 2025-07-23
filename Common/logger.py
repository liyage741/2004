# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:test_login_page.py
# Author: liyage
# Time:2025年07月22日
import logging
import os
import time
from pathlib import Path
from typing import Optional

from Common.commom_data import CommonData

# 全局变量
COMMON_DATA = CommonData()


class Logger:
    def __init__(self, name: str = "wg.log", level: Optional[str] = None,
                 log_dir: Optional[str] = None):
        self.log_dir = self._resolve_log_dir(log_dir)
        self.log_file = self.log_dir / f"{name}.{time.strftime('%Y-%m-%d')}.log"
        self.level = self._parse_level(level or COMMON_DATA.logLevel)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.level)
        if not self.logger.handlers:
            self._setup_handlers()

    def _resolve_log_dir(self, log_dir: Optional[str] = None) -> Path:
        if log_dir is not None:
            path = Path(log_dir)
        else:
            path = Path(__file__).parent.parent / "logs"
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _parse_level(self, level_str: str) -> int:
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        return level_map.get(level_str.upper(), logging.INFO)

    def _setup_handlers(self) -> None:
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s:%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 文件处理器
        file_handler = logging.FileHandler(
            self.log_file,
            mode='a',
            encoding='utf-8'
        )
        file_handler.setLevel(self.level)
        file_handler.setFormatter(formatter)

        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)
        console_handler.setFormatter(formatter)

        # 添加处理器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger


logger = Logger().get_logger()
if __name__ == "__main__":
    print(f"日志文件路径: {Logger().log_file}")

# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:commom_data.py
# Author: liyage
# Time:2025年07月21日
import yaml
from pathlib import Path
from typing import Dict, Any


class CommonData:
    _instance = None
    _config: Dict[str, Any] = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._load_config()
        return cls._instance

    @classmethod
    def _load_config(cls):
        current_dir = Path(__file__).parent
        config_path = current_dir.parent / "config" / "qingzhou_env.yaml"
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                cls._config = yaml.safe_load(f)
        except FileNotFoundError:
            raise RuntimeError(f"配置文件未找到: {config_path}")
        except yaml.YAMLError as e:
            raise RuntimeError(f"YAML 解析错误: {e}")

    @classmethod
    def get(cls, key: str, default=None) -> Any:
        """获取配置项"""
        return cls._config.get(key, default)

    @property
    def console_url(self) -> str:
        return self.get("console_url")

    @property
    def qingzhou_default_user(self) -> str:
        return self.get("qingzhou_default_user")

    @property
    def qingzhou_default_password(self) -> str:
        return self.get("qingzhou_default_password")

    @property
    def scenarioTenantEnName(self) -> str:
        return self.get("scenarioTenantEnName")

    @property
    def scenarioProjectEnName(self) -> str:
        return self.get("scenarioProjectEnName")

    @property
    def default_gateway_name(self) -> str:
        return self.get("default_gateway_name")

    @property
    def hostHeader(self) -> str:
        return self.get("hostHeader")

    @property
    def logLevel(self) -> str:
        return self.get("logLevel")

    @property
    def appName(self) -> str:
        return self.get("appName")

    @property
    def appName2(self) -> str:
        return self.get("appName2")

    @property
    def appPort(self) -> str:
        return self.get("appPort")

    @property
    def appPort2(self) -> str:
        return self.get("appPort2")

    @property
    def soapAppName(self) -> str:
        return self.get("soapAppName")

    @property
    def soapAppPort(self) -> str:
        return self.get("soapAppPort")

    @property
    def grpcServiceHost(self) -> str:
        return self.get("grpcServiceHost")

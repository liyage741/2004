# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:TestOps
# File_name:gw_enum.py
# Author: liyage
# Time:2025年07月22日
from enum import Enum


class ProtocolType(Enum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    Dubbo = "Dubbo"
    gRPC = "gRPC"
    WebService = "WebService"


class RegisterType(Enum):
    Kubernetes = "Kubernetes"
    Eureka = "Eureka"
    Nacos = "Nacos"
    Zookeeper = "Zookeeper"

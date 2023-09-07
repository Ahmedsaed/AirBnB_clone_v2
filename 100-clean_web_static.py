#!/usr/bin/python3
# Fabric file to clear out-of-date archives
import os
from fabric.api import *

env_hosts = ["100.25.14.86","54.236.115.46"]


def do_clean(number = 0):
    """Clear out-of-date archives"""
    
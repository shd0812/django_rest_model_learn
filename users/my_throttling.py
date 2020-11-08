#! /usr/bin/env python

# -*- coding: utf-8 -*-

# @Time 2020/11/7 20:43
# @Author  cunfu
# @File my_throttling.py

from rest_framework.throttling import SimpleRateThrottle

class UserThrottling(SimpleRateThrottle):
    scope = "luffy"

    def get_cache_key(self, request, view):
        return self.get_ident(request)

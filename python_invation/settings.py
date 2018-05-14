#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'wWX551751'


class Setting():
    """存储游戏《外星人入侵》 的所有设置的类"""
    def __init__(self):
        # 屏幕尺寸和背景颜色
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # 子弹移动速度 尺寸 颜色 数量限制
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人背景颜色
        self.alien_color = 60, 60, 60
        self.alien_speed_factor = 1
        # 外星人撞到屏幕边缘时， 外星人群向下移动的速度
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移， 为-1表示向左移
        self.fleet_direction = 1
        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # 记分
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右； 为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

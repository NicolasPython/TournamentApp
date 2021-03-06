#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.controllers.menu_c import HomeMenuController


class ApplicationController:
    """Main controller, called when the app start"""

    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()

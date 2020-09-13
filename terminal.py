#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhinav

import os
import sys
import emoji

from collections import OrderedDict
from clint.textui import puts, colored
from kreta.advancedScanner import advancedscanner

try:
    input = raw_input  # for python2 compatibility
except NameError:
    pass


def clear():
    """for removing the clutter from the screen when necessary"""
    os.system('cls' if os.name == 'nt' else 'clear')


def printAppBanner():
    clear()
    appBanner = r"""
                    ██╗  ██╗██████╗ ███████╗████████╗ █████╗ 
                    ██║ ██╔╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
                    █████╔╝ ██████╔╝█████╗     ██║   ███████║
                    ██╔═██╗ ██╔══██╗██╔══╝     ██║   ██╔══██║
                    ██║  ██╗██║  ██║███████╗   ██║   ██║  ██║


                                            - By abhinavanand(@ab-anand)
    """
    puts(colored.cyan(appBanner))


def appMenu(invalidChoice=False):
    clear()
    printAppBanner()
    puts(colored.red("\nEnter 'q' to quit"))
    for key, value in menu.items():
        puts(colored.green('{}) {} : '.format(key, value.__doc__)))

    if invalidChoice:
        puts(colored.red("\nInvalid choice! Please try again"))

    choice = input('Action (b/i/q) : ').lower().strip()

    if choice in menu:
        menu[choice]()
    elif choice == 'q':
        clear()
    else:
        appMenu(True)


def basicScanner():
    """performs a plain scanning"""
    pass


def intelligentScanner():
    """performs an intelligent scanning"""

    printAppBanner()
    try:
        puts(colored.magenta("\nEnter input path"))
        inputPath = None
        while inputPath is None or inputPath is "":
            inputPath = input("Input Path: ")
            inputPath = inputPath.strip()

        outputPath = None
        puts(colored.magenta("\n[optional] Do you want to set output path?"))
        choiceForOutputPath = input("Set output path (y/n): ")
        choiceForOutputPath = choiceForOutputPath.lower().strip()
        if choiceForOutputPath == 'y':
            outputPath = input("Output Path: ")
            if outputPath is not "":
                outputPath = outputPath.strip()

        # print(outputPath.lower().strip() is "")

        depth = 5
        puts(colored.magenta("\n[optional] Do you want to directory depth to scan?"))
        choiceForDepth = input("Set directory depth (y/n): ")
        choiceForDepth = choiceForDepth.lower().strip()
        if choiceForDepth == 'y':
            depth = input("Scanning depth: ")
            if depth is not "":
                depth = int(depth)

        printAppBanner()

        try:
            scanner = advancedscanner.AdvancedScanner()
            fileStatus = scanner.readDirectory(inputPath, outputPath=outputPath, depth=depth)

            printAppBanner()

            puts(colored.green("\nFiles moved: {}".format(len(fileStatus["Moved"]))))
            for file in fileStatus["Moved"]:
                print("{}  {}".format(emoji.emojize(":check_mark:"), file))

            puts(colored.red("\nFiles not moved: {}".format(len(fileStatus["NotMoved"]))))
            for file in fileStatus["NotMoved"]:
                print("{} {}".format(emoji.emojize(":cross_mark:"), file))
            print()

        except AssertionError as e:
            puts(colored.red(e))
    except Exception as e:
        puts(colored.red(e))


menu = OrderedDict([
    ('b', basicScanner),
    ('i', intelligentScanner)
])

if __name__ == "__main__":
    try:
        appMenu()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)

"""

     ELMORSY SE

    ------------

    Developer/Author    : abdalla elmorsy

    Supported platform  : all Linux distro and termux(android)

    YouTube             : ELMORSY SE

    Github              : /Ranginang67

    Termux Tested on    : Samsung galaxy J5 prime 8.0

    Linux Tested on     : Ubuntu Gnome 16.04 LTS

    ------------

          ELMORSY SE is a open source, free, and automatic tools.

"""

banner_list = [

    """              ELMORSY SE

       .---.        .-----------

      /     \  __  /    ------

     / /     \(  )/    -----

    //////   ' \/ `   ---

   //// / // :    : ---

  // /   /  /`    '--

 //          //..\\

        ====UU====UU====

        |   '//||\\`   |

        |      ''``    |

ELMORSY ES /AS7HAB ELMGRA /ELMORSY

====================================

    """,

    # """

    # add costum banner here...

    # """,

]

import re

import os

import sys

import platform

import socket

import urllib.request

import json, random

import config.md as md

from time import sleep

import install

if not md.Show().checkAllOK():

    sys.exit(0)

network_status = 0

class MainModule:

    __tools_list = "config/tools.json"

    __home_directory = os.environ["HOME"]

    __tools_tmp = {}

    __users_tmp = {}

    __dell_tmp = {}

    @classmethod

    def getTools(cls,msg,RepoUrl):

        with open(MainModule.__tools_list,"r+") as TS:

            data = json.loads(TS.read())

            try:

                md.Show().Message("normal","{}: {}".format(msg,RepoUrl))

          

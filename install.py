# -*- coding: utf-8 -*-

from os import path, system, getuid

import time, sys

TERMUX      = "/data/data/com.termux/files/usr/bin/"

LINUX       = "/usr/bin/"

ELMORSY SEEXEC = "ELMORSY SE."

COMMAND = {

    "termux":{1:"cd "+TERMUX+"ELMORSY SE",2:"python {}/{}".format(TERMUX,"ELMORSY SE/main.py")},

    "linux":{1:"cd "+LINUX+"ELMORSY SE",2:"python3 {}/{}".format(LINUX,"ELMORSY SE/main.py")}

}

class Install:

    @staticmethod

    def environmentExists(ph):

        if not path.exists(ph):

            return 0

        return 1

    def installLinux(self):

        if getuid():

            sys.exit("Your must be run this tool as superuser")

        execd = open(LINUX+ELMORSY SEEXEC,"w")

        if not self.environmentExists(LINUX+"python3"):

            system("apt-get install python3 -y")

        execd.write(("#!/bin/bash\n"+COMMAND["linux"][1]+"\n"+COMMAND["linux"][2]))

        system("mv ../ELMORSY SE %s && chmod +x %s/%s && chmod 777 -R %s"%(LINUX,LINUX,ELMORSY SEEXEC,LINUX+"/ELMORSY SE"))

        # check if install is success

        if not self.environmentExists(LINUX+ELMORSY SEEXEC) or not self.environmentExists(LINUX+"ELMORSY SE"):

            sys.exit("Install failed.")

        sys.exit("[ ✓ ] Install Success. run: \"ELMORSY SE.\"")

        execd.close()

    def installTermux(self):

        exect = open(TERMUX+ELMORSY SEEXEC,"w")

        if not self.environmentExists(TERMUX+"python3"):

            system("pkg install python -y")

        exect.write(("#!/bin/bash\n"+COMMAN

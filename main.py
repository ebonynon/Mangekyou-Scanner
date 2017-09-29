#!/usr/bin/python

# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------#

# python Mangekyou-Scanner-master

# about:
# ------------
# this is xe-non's 8th program with qt-creator @ ubuntumate
# window in PyQt4

# author:xe-non
# last edited: 19/9/2017

# Licensed under the GNU General Public License Version 3 (GNU GPL v3),
# available at: http://www.gnu.org/licenses/gpl-3.0.txt

# (C) 2017 xe-non

# ----------------------------------------------------------------------------#

from socket import *
import sys
import time
from datetime import datetime
from threading import *
from PyQt4 import QtGui
import gfxui


class App(QtGui.QMainWindow, gfxui.Ui_gfxUI):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.portScan)

    def portScan(self):
        host = str(self.lineEdit.text())
        try:
            tgtIP = gethostbyname(host)
            tgtName = gethostbyaddr(tgtIP)
            self.textEdit.setText("\n[*] Scan Results for: " + tgtName[0])
            self.textEdit.setText("[*] Scan Results for: " + tgtIP)
        except:
            self.textEdit.setText("[-] Cannot resolve '%s': Unknown host" % host)
            return

        self.textEdit.setText("\n[*] Scanning started: %s\n" % time.strftime("%H:%M:%S"))
        start_time = datetime.now()

        setdefaulttimeout(1)

        self.textEdit.setText("Ports are scanning please wait...")

        if ports == "":
            step = 500
            for start_port in range(1, 5001, step):
                end_port = start_port + step
                t = Thread(target=connScan, args=(host, int(start_port), int(end_port)))
                t.start()
        else:
            for port in ports.split(","):
                try:
                    connSkt = socket(AF_INET, SOCK_STREAM)
                    connSkt.connect((host, int(port)))
                    connSkt.send(str.encode('Data\r\n'))
                    results = connSkt.recv(100)
                    screenLock.acquire()
                    self.textEdit.setText("\n[+] Tcp Port %s: open" % port)
                    self.textEdit.setText(results.decode('utf-8'))
                except:
                    screenLock.acquire()
                    self.textEdit.setText("[+] Tcp Port %s: closed" % port + "\n")
                finally:
                    screenLock.release()
                    connSkt.close()

        stop_time = datetime.now()
        total_time_duration = stop_time - start_time
        self.textEdit.setText("\n[*] Scanning Finished: %s" % time.strftime("%H:%M:%S"))
        self.textEdit.setText("[*] Scanned Duration: %s" % total_time_duration)

    # portScan(host)


def main():
    app = QtGui.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()

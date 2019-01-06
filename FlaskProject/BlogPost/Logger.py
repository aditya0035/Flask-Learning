from queue import Queue
import os
from inspect import getframeinfo, stack
from datetime import datetime
from threading import Thread
messageQueue=Queue()
class Logger:
    @staticmethod
    def write(message):
         global messageQueue
         is_logging=bool(os.environ.get("IS_LOGGING",None))
         if(is_logging):
            caller = getframeinfo(stack()[1][0])
            message= f'{datetime.now()}    [{caller.filename}]  {caller.lineno} {message}'
            messageQueue.put(message)
            Thread(target=Logger.__writeToFile).start()
    @staticmethod
    def __writeToFile():
        global messageQueue
        while True:
            message=messageQueue.get()
            messageQueue.task_done()
            with open("logger.txt",'a+') as filepointer:
                filepointer.write(message)
                filepointer.write("\n")

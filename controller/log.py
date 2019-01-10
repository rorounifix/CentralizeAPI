import time;


def log(path, e):

    localtime = time.asctime( time.localtime(time.time()))
    with open("logs/error.logs",'a') as logfile:
        logfile.write('{} at {} => {} \n'.format(path, localtime, str(e)))
        logfile.close()

if __name__ == "__main__":
    log("test", "error")

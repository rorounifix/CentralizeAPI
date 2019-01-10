from controller.getTokenAccess import getTokenAccess
from configparser import ConfigParser
from controller.log import log



def changeConfig():

    try:
        config = ConfigParser()
        config.read('config/config.ini')
        config.set("MAIN","token_access", getTokenAccess())

        with open("config/config.ini", "w") as configfile:
            config.write(configfile)
        return True

    except Exception as e:
        log('changeConfig.py', e)
        return False


if __name__ == "__main__":
    changeConfig()

import os;
import openpyxl;
import configparser;


def define_last_line(last_line):
    config = configparser.ConfigParser()
    config.read('config.cfg') 
    config['DEFAULT'] = {
        'last_line': last_line
    }

    with open('config.cfg', 'w') as config_file:
        config.write(config_file)
        

def define_last_run_crash(last_run_crash):
    config = configparser.ConfigParser()
    config.read('config.cfg') 
    config['CRASH'] = {
        'last_run_crash': last_run_crash
    }

    with open('config.cfg', 'w') as config_file:
        config.write(config_file)


def retrieve_last_line():
    file_path = 'config.cfg'
    file_exists = os.path.isfile(file_path)

    if file_exists:
        config = configparser.ConfigParser()
        config.read('config.cfg')
        print('DEFAULT' in config)
        last_line = config.getint('DEFAULT', 'last_line')
        if 'DEFAULT' in config:
            if last_line > 0 :
                return last_line + 1
            else : 
                return 0
        else:
            return 0
    else :
        return 0

def last_run_crash_check():
    file_path = 'config.cfg'
    file_exists = os.path.isfile(file_path)

    if file_exists:
        config = configparser.ConfigParser()
        config.read('config.cfg')

        last_run_crash = config.getint('CRASH', 'last_run_crash')
        if(last_run_crash) :
            return True
        else : 
            return False
    else :
        return False

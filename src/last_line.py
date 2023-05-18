import os;
import openpyxl;
import configparser;


file_path = './utopya/src/config.cfg'

def define_last_line(last_line):
    config = configparser.ConfigParser()
    config.read(file_path) 
    config['DEFAULT'] = {
        'last_line': last_line
    }

    with open(file_path, 'w') as config_file:
        config.write(config_file)
        

def define_last_run_crash(last_run_crash):
    config = configparser.ConfigParser()
    config.read(file_path) 
    config['CRASH'] = {
        'last_run_crash': last_run_crash
    }

    with open(file_path, 'w') as config_file:
        config.write(config_file)


def retrieve_last_line():
    file_exists = os.path.isfile(file_path)

    if file_exists:
        config = configparser.ConfigParser()
        config.read(file_path)
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
    
    file_exists = os.path.isfile(file_path)
    if file_exists:
        config = configparser.ConfigParser()
        config.read(file_path)

        last_run_crash = config.getboolean('CRASH', 'last_run_crash')
        if(last_run_crash == True) :
            return True
        else : 
            return False
    else :
        return False



def create_config_file():
    file_exists = os.path.isfile(file_path)
    if not file_exists:
        config = configparser.ConfigParser()
        config['CRASH'] = {
            'last_run_crash': False
        }

        config['DEFAULT'] = {
            'last_line': 0
        }

        with open(file_path, 'w') as config_file:
            config.write(config_file)
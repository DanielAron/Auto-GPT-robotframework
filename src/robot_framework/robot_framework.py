from sys import argv, exit, platform
import os
from datetime import datetime
from robot import run, run_cli, rebot_cli

def run_robotframework(file_path):
    print("hia")
    print("file_path")

    # CONFIG BOT
    # proyect_path = os.getcwd()
    # server_path = os.path.dirname(os.path.realpath(__file__))
    # output_path = proyect_path + '/src/bot_logs/'
    keyword = 'gpt robotframework plugin'
    output_path = '/Users/daniel/workspace/rpamaker/liveterminal/autogpt_src/1-Auto-GPT-0.3.0/autogpt/auto_gpt_workspace/'
    d = datetime.strftime(datetime.now(), '%y%m%d%H%M%S%f')
    output_file = 'output-'+d+'.xml'
    log_file = 'log-'+d+'.html'
    report_file = 'report-'+d+'.html'
    common = ['--output', output_path + output_file,
        '--log', output_path + log_file, 
        '--report', output_path + report_file, 
        output_path + '/tasks.robot']

    # common = ['--listener', server_path+'/workspace_listener.py', 
    #     '--output', output_path + output_file,
    #     '--log', output_path + log_file, 
    #     '--report', output_path + report_file, 
    #     server_path + '/tasks.robot']
    # variables = ['--variable', 'id_t:'+str(t_id),
    #     '--variable', 'config:'+str(kwargs)]
    # RUN BOT
    run_cli(['--name', keyword] + common, exit=False)


    return file_path

if __name__ == "__main__":
    run_robotframework('un file_path')

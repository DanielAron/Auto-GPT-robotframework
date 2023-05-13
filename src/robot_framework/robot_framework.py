from sys import argv, exit, platform, version, prefix, base_prefix
import os
from datetime import datetime
from robot import run, run_cli, rebot_cli

def run_robotframework(file='tasks.robot'):
    flag_add_unique_results = os.getenv("FLAG_ADD_UNIQUE_RESULTS", False)
    output_path = os.getenv("AUTO_GPT_WORKSPACE", os.getcwd() + "/autogpt/auto_gpt_workspace/")
    relative_path = os.path.relpath(output_path, os.getcwd())
    keyword = 'gpt robotframework plugin' #ToDo: Take this as parameter. Ask AI to generate an allusive name
    d = datetime.strftime(datetime.now(), '%y%m%d%H%M%S%f')
    if flag_add_unique_results:
        output_file = 'output-'+d+'.xml'
        log_file = 'log-'+d+'.html'
        report_file = 'report-'+d+'.html'
        xunit_file_name = relative_path + '/xunit-'+d+'.xml'
    else:
        output_file = 'output.xml'
        log_file = 'log.html'
        report_file = 'report.html'
        xunit_file_name = relative_path + '/xunit.xml'

    common = ['--output', output_path + output_file,
        '--log', output_path + log_file, 
        '--report', output_path + report_file, 
        output_path + '/' + file]

    # common = ['--listener', server_path+'/workspace_listener.py', 
    #     '--output', output_path + output_file,
    #     '--log', output_path + log_file, 
    #     '--report', output_path + report_file, 
    #     server_path + '/tasks.robot']
    # variables = ['--variable', 'id_t:'+str(t_id),
    #     '--variable', 'config:'+str(kwargs)]

    # RUN BOT
    run_cli(['--name', keyword, '--xunit', xunit_file_name] + common, exit=False)
    xunit_path = os.getcwd() + "/" + xunit_file_name
    output = output_path + output_file
    return open(output).read()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    run_robotframework("open_website.robot")

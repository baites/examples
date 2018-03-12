
import exceptions
import subprocess
import sys
import time

class TimeoutError(Exception):
    pass

def call(command, timeout=5, polltime=0.1):
    """Call a system call by running command in a process."""
    proc = None
    stdout = ''
    stderr = ''
    try:
        # Open a process to run command
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True
        )
        # Set deadline to execute the command
        deadline = time.time() + timeout
        # Loop until command is completed
        # of command reach deadline
        while time.time() < deadline and proc.poll() is None:
            time.sleep(polltime)
        # If the command reach deadline its process is killed
        # After that time exception is raised
        if proc.poll() is None:
            proc.kill()
            raise TimeoutError('Command timeout')
        else:
        # Else check for command status and raise CalledProcessError exception
            if proc.returncode:
                 raise subprocess.CalledProcessError(proc.returncode, command)
            stdout, stderr = proc.communicate()
    except Exception as error:
        # When catching an exception check if process is killed
        if proc.poll() is None:
            proc.kill();
        raise error
   # Return stdout and stderr
    return stdout, stderr

stdout, stderr = call('echo works!')
print stdout, stderr

stdout, stderr = call('sleep 4', timeout=2)
print stdout, stderr

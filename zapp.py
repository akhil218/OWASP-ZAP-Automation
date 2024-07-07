import os
import subprocess
import time

current_dir = os.getcwd()

# Get user input
target_url = input("Enter the target URL: ")
login_url = input("Enter the login URL: ")
email = input("Enter the email: ")
password = input("Enter the password: ")
include_pattern = target_url+".*"

print("Running the script...")

command = [
    "docker", "run", "--rm",
    "-v", f"{current_dir}:/zap/wrk/:rw",
    "-t", "ictu/zap2docker-weekly",
    "zap-full-scan.py",
    "-I", "-j", "-m", "10", "-T", "60",
    "-t", target_url,
    "-r", "testreport.html",
    "--hook=/zap/auth_hook.py",
    "-z",
    f"auth.loginurl={login_url}",
    f"auth.email={email}",
    f"auth.password={password}",
    "auth.submit_field=submit",
    f"auth.include={include_pattern}"
]

start_time = time.time()

# Redirect the output to a file
with open("scan_output.txt", "w") as output_file:
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
        for line in process.stdout:
            output_file.write(line.decode())

end_time = time.time()
runtime = end_time - start_time

print(f"Scanning completed in {runtime} seconds.")

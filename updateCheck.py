import requests
import shutil
import os
import time
from rich.progress import Progress

# Define the URL of the "EtherForge.py" script on GitHub
github_repo = "happy-kitty0821/EtherForge"
script_path = "EtterForge.py"
raw_url = f"https://raw.githubusercontent.com/{github_repo}/main/{script_path}"

# Send a request to retrieve the latest version of the script
response = requests.get(raw_url)

if response.status_code == 200:
    # Retrieve the content of the latest version
    latest_version = response.text
    
    # Check if the local script exists
    if os.path.isfile(script_path):
        # Read the content of the local script
        with open(script_path, 'r') as file:
            current_version = file.read()
        
        # Compare the versions
        if latest_version != current_version:
            # Backup the existing script
            backup_path = "EtterForge_backup.py"
            shutil.copyfile(script_path, backup_path)
            
            # Update the script with the latest version
            with open(script_path, 'w') as file:
                file.write(latest_version)
            
            print("Update successful. The script has been updated to the latest version.")
        else:
            print("No update available. The script is already up to date.")
    else:
        # The local script doesn't exist, download the latest version
        with open(script_path, 'w') as file:
            file.write(latest_version)
        
        print("Script downloaded. You now have the latest version.")
else:
    print("Failed to retrieve the latest version of the script.")

# Display progress bar
with Progress() as progress:
    task = progress.add_task("[cyan]Checking for updates...", total=100)
    
    for i in range(100):
        progress.update(task, advance=1)
    
        # Simulate delay to show progress
        time.sleep(0.01)

print("Update check completed.")

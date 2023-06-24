# for bash as a default shell

**Adding EtherForge to PATH**

1. Open a terminal.

2. Clone the EtherForge repository into the home directory:

   ```bash
   git clone https://github.com/happy-kitty0821/EtherForge.git ~/EtherForge
   ```

3. Grant executable permissions to the EtherForge script:

   ```bash
   chmod +x ~/EtherForge/EtterForge.py
   ```

4. Check the location of the current directory. This will be needed later when adding to the PATH:

   ```bash
   pwd
   ```

   Copy the absolute path of the current directory.

5. Open the `.bashrc` file in a text editor:

   ```bash
   nano ~/.bashrc
   ```

6. Scroll to the end of the file and add the following line:

   ```bash
   export PATH="$PATH:/path/to/EtherForge"
   ```

   Replace `/path/to/EtherForge` with the absolute path of the `EtherForge` directory you copied in step 4.

7. Save the changes and exit the text editor.

8. Update the current session's PATH by running the following command:

   ```bash
   source ~/.bashrc
   ```

9. Close the terminal and reopen it to apply the changes.

10. Test if the script is accessible from anywhere by typing `EtterForge.py`:

    ```bash
    EtterForge.py
    ```

    The EtherForge script should now be executed when typing `EtterForge.py` in the terminal.

Please note that the above instructions assume a typical Linux environment with Bash as the default shell. The steps may vary slightly for different distributions or if you're using a different shell.
#zsh as a Default terminal
If you're using Zsh as the default shell instead of Bash, you can follow these steps to add EtterForge to the PATH:

1. Open a terminal.

2. Clone the EtterForge repository into the home directory:

   ```bash
   git clone https://github.com/happy-kitty0821/EtterForge.git ~/EtterForge
   ```

3. Grant executable permissions to the EtterForge script:

   ```bash
   chmod +x ~/EtterForge/EtterForge.py
   ```

4. Check the location of the current directory. This will be needed later when adding to the PATH:

   ```bash
   pwd
   ```

   Copy the absolute path of the current directory.

5. Open the `.zshrc` file in a text editor:

   ```bash
   nano ~/.zshrc
   ```

6. Scroll to the end of the file and add the following line:

   ```bash
   export PATH="$PATH:/path/to/EtterForge"
   ```

   Replace `/path/to/EtterForge` with the absolute path of the `EtterForge` directory you copied in step 4.

7. Save the changes and exit the text editor.

8. Update the current session's PATH by running the following command:

   ```bash
   source ~/.zshrc
   ```

9. Close the terminal and reopen it to apply the changes.

10. Test if the script is accessible from anywhere by typing `EtterForge.py`:

    ```bash
    EtterForge.py
    ```

    The EtterForge script should now be executed when typing `EtterForge.py` in the terminal.

Please note that the above instructions are specific to Zsh as the default shell. If you're using a different shell, the steps may vary.

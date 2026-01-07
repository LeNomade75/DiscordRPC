# DiscordRPC
## Custom Discord RPC (main folder) :
`main.py` is a process watcher that looks for specific apps being launched and then starts their associated RPC Python script (it's the main script to launch).
### Adding new apps :
- Add your app-specific RPC Config Python scripts to the **Main** folder (see `template.py` for reference).
- Edit the _main.py :   
     PROGRAM_SCRIPTS = {  
    "euphoria.exe": "euphoria.py",  
    `"TheNameOfTheProgramInTaskManager.exe": "TheNameOfYourAssociatedConfigPythonScript.py",  `  
    "deaddays.exe": "deaddays.py"  
}
___
## Start with windows (startup folder):
- Add the `discordrpc.bat` inside your start up folder (find it with `WIN + R` and searching for `shell:startup`)
- Edit the cd command to point to the folder where `_main` is in
___
I may add a GUI later to update the main script and automatically create new RPC Python scripts when creating new RPCs.
___

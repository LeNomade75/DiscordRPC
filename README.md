# DiscordRPC
## Custom Discord RPC (main folder) :
`main.py` is a process watcher that looks for specific apps being launched and then starts their associated RPC Python script.
Add your app-specific Python scripts to the **Main** folder (see `template.py` for reference).
___
## Start with windows (startup folder):
Add the `discordrpc.bat` inside your start up folder (find it with `WIN + R` and searching for `shell:startup`)
edit the cd command to point to the folder where `_main` is in
___
I may add a GUI later to update the main script and automatically create new RPC Python scripts when creating new RPCs.

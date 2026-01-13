import discordrpc
import threading

rpc = discordrpc.RPC(app_id=1460737370231013386)

def start_rpc():
    rpc.run()

threading.Thread(target=start_rpc, daemon=True).start()

rpc.set_activity(
    state="Modeling",
    large_image="blendere",
    large_text="Blender",

)

import time
while True:
    time.sleep(60)  # keep script alive

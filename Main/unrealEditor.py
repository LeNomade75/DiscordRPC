import discordrpc
import threading

rpc = discordrpc.RPC(app_id=1460730285879722055)

def start_rpc():
    rpc.run()

threading.Thread(target=start_rpc, daemon=True).start()

rpc.set_activity(
    state="developping",
    large_image="ues",
    large_text="Unreal Engine",

)

import time
while True:
    time.sleep(60)  # keep script alive

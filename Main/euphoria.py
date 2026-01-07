import discordrpc
import threading

rpc = discordrpc.RPC(app_id=1457541090478526636)

def start_rpc():
    rpc.run()

threading.Thread(target=start_rpc, daemon=True).start()

rpc.set_activity(
    state="playing",
    large_image="euphoria",
    large_text="Euphoria"
)

import time
while True:
    time.sleep(60)  # keep script alive

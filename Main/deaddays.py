import discordrpc
import threading

rpc = discordrpc.RPC(app_id=1458514107102658583)

def start_rpc():
    rpc.run()

threading.Thread(target=start_rpc, daemon=True).start()

rpc.set_activity(
    state="playing",
    large_image="deaddays",
    large_text="DEAD DAYS"
)

import time
while True:
    time.sleep(60)  # keep script alive

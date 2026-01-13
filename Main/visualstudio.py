import discordrpc
import threading

rpc = discordrpc.RPC(app_id=1460716577539362910)

def start_rpc():
    rpc.run()

threading.Thread(target=start_rpc, daemon=True).start()

rpc.set_activity(
    state="coding",
    large_image="visual_studio_icon_2026_svg",
    large_text="Visual Studio 2026"
)

import time
while True:
    time.sleep(60)  # keep script alive

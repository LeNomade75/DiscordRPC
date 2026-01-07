import discordrpc
import threading

rpc = discordrpc.RPC(app_id=#YourDiscordAppID#)

def start_rpc():
    rpc.run()

threading.Thread(target=start_rpc, daemon=True).start()

# ================== ACTIVITY CONFIG ================== look https://senophyx.id/docs/discord-rpc/ for more details

rpc.set_activity(
    # ----- Main text -----
    details="Upper line of the activity",
    state="Lower line of the activity",

    # ----- Activity / status behavior -----
    act_type=Activity.Playing,          # Playing / Streaming / Listening / Watching / Competing
    status_type=StatusDisplay.Name,     # Name / State / Details

    # ----- Large image -----
    large_image="large_image_key",       # MUST exist in app assets
    large_text="Large image tooltip",
    large_url="https://example.com",     # optional

    # ----- Small image -----
    small_image="small_image_key",       # optional
    small_text="Small image tooltip",
    small_url="https://example.com",     # optional

    # ----- Clickable text URLs -----
    state_url="https://example.com",     # optional
    details_url="https://example.com",   # optional

    # ----- Timestamps -----
    ts_start=Utils.timestamp_now(),      # start time (now)
    ts_end=None,                         # or Utils.timestamp_now() + seconds

    # ----- Party / session -----
    party_id="party_123",
    party_size=[1, 5],                   # [current, max]

    # ----- Secrets (advanced / optional) -----
    join_secret="join_secret_here",
    spectate_secret="spectate_secret_here",
    match_secret="match_secret_here",

    # ----- Buttons (max 2) -----
    buttons=[
        button.Button(label="Website", url="https://example.com"),
        button.Button(label="GitHub", url="https://github.com")
    ]
)


import time
while True:
    time.sleep(60)
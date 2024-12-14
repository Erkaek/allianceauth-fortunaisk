import requests

def notify_winner_discord(user, amount):
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
    payload = {
        "content": f"🎉 Congratulations {user.username}! You won {amount} ISK in the FortunaISK lottery!"
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        print("Failed to send Discord notification")

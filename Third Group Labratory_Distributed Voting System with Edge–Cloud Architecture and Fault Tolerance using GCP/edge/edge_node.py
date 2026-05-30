from supabase import create_client
from dotenv import load_dotenv
import os
import uuid
import random
import time

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

EDGE_ID = f"edge_{random.randint(1000,9999)}"

def generate_vote():

    return {
        "vote_id": str(uuid.uuid4()),
        "user_id": str(uuid.uuid4()),
        "poll_id": "poll_1",
        "choice": random.choice(["A", "B", "C"]),
        "edge_id": EDGE_ID,
        "timestamp": time.time()
    }

def send_vote(vote):

    retries = 3

    for attempt in range(retries):

        try:

            supabase.table(
                "pending_votes"
            ).insert(vote).execute()

            print(
                f"[{EDGE_ID}] Sent:",
                vote["choice"]
            )

            return True

        except Exception as e:

            print(
                f"Retry {attempt+1}:",
                e
            )

            time.sleep(2)

    return False

while True:

    vote = generate_vote()

    send_vote(vote)

    time.sleep(
        random.uniform(1,3)
    )
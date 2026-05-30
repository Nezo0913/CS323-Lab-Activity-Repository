from supabase import create_client
from dotenv import load_dotenv
import os
import time

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

processed_count = 0

while True:

    try:

        response = (
            supabase.table("pending_votes")
            .select("*")
            .eq("processed", False)
            .limit(20)
            .execute()
        )

        votes = response.data

        if not votes:

            print("No pending votes")
            time.sleep(2)
            continue

        for vote in votes:

            processed_vote = {
                "vote_id": vote["vote_id"],
                "user_id": vote["user_id"],
                "poll_id": vote["poll_id"],
                "choice": vote["choice"],
                "edge_id": vote["edge_id"],
                "timestamp": vote["timestamp"]
            }

            (
                supabase.table("processed_votes")
                .upsert(processed_vote)
                .execute()
            )

            (
                supabase.table("pending_votes")
                .update({"processed": True})
                .eq("id", vote["id"])
                .execute()
            )

            latency = (
                time.time()
                - vote["timestamp"]
            )

            processed_count += 1

            print(
                f"Processed "
                f"{processed_count} "
                f"Latency={latency:.2f}s"
            )

    except Exception as e:

        print(
            "Worker Error:",
            e
        )

    time.sleep(2)
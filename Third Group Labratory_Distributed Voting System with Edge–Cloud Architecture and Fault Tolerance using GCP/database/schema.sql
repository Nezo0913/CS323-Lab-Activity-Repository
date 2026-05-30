CREATE TABLE pending_votes (
    id BIGSERIAL PRIMARY KEY,
    vote_id TEXT UNIQUE NOT NULL,
    user_id TEXT NOT NULL,
    poll_id TEXT NOT NULL,
    choice TEXT NOT NULL,
    edge_id TEXT NOT NULL,
    timestamp DOUBLE PRECISION NOT NULL,
    processed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE processed_votes (
    vote_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    poll_id TEXT NOT NULL,
    choice TEXT NOT NULL,
    edge_id TEXT NOT NULL,
    timestamp DOUBLE PRECISION NOT NULL,
    processed_at TIMESTAMP DEFAULT NOW()
);
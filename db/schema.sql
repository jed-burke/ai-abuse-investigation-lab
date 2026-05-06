DROP TABLE IF EXISTS ai_usage_logs;
DROP TABLE IF EXISTS account_profiles;

CREATE TABLE account_profiles (
    account_id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    plan_type TEXT NOT NULL,
    org_name TEXT NOT NULL,
    trust_tier TEXT NOT NULL,
    prior_enforcement_count INTEGER NOT NULL
);

CREATE TABLE ai_usage_logs (
    event_id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    event_ts TEXT NOT NULL,
    account_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    session_id TEXT NOT NULL,
    ip_address TEXT NOT NULL,
    user_agent TEXT NOT NULL,
    model TEXT NOT NULL,
    prompt_category TEXT NOT NULL,
    prompt_text TEXT NOT NULL,
    response_outcome TEXT NOT NULL,
    moderation_label TEXT NOT NULL,
    moderation_score REAL NOT NULL,
    policy_signal TEXT NOT NULL,
    risk_score INTEGER NOT NULL,
    is_synthetic_abuse INTEGER NOT NULL,
    analyst_note TEXT NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account_profiles(account_id)
);

CREATE INDEX idx_ai_usage_logs_case_ts ON ai_usage_logs(case_id, event_ts);
CREATE INDEX idx_ai_usage_logs_account ON ai_usage_logs(account_id);
CREATE INDEX idx_ai_usage_logs_session ON ai_usage_logs(session_id);
CREATE INDEX idx_ai_usage_logs_policy_signal ON ai_usage_logs(policy_signal);


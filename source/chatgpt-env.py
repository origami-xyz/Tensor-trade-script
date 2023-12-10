trading_env = TradingEnvironment(
    exchange=exchange,
    feature_pipeline=feature_pipeline,
    action_scheme="managed-risk",
    reward_scheme=RiskAdjustedReturns(),
    window_size=15,
    max_allowed_loss=0.05
)

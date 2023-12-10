strategy = StableBaselinesTradingStrategy(env=trading_env, model="ppo")
strategy.train(n_episodes=1000)

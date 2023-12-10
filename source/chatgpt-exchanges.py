# Define an exchange
exchange = Exchange("exchange", service=OHLCV)  # OHLCV is your chosen data service

# Define a feature pipeline
feature_pipeline = FeaturePipeline(
    steps=[
        FractionalDifference(difference_order=0.6),
        MinMaxNormalizer(),
        TechnicalAnalysis(),
        ExponentialMovingAverage(),
        SimpleMovingAverage()
    ]
)

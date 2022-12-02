from corva import Api, Cache, Logger, ScheduledDataTimeEvent, scheduled


from src.app import konstantin_scheduled_data_time_app

@scheduled
def lambda_handler(event: ScheduledDataTimeEvent, api: Api, cache: Cache):
    """Insert your logic here"""
    Logger.info("This is a log line for my schedule app")
    return konstantin_scheduled_data_time_app(event, api, cache)

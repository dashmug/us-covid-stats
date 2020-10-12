import logging

from us_covid_stats.etl.handler import refresh_data_from_sources

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print(refresh_data_from_sources(None, None))

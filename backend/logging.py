from azure.monitor.opentelemetry import configure_azure_monitor
import logging
from opentelemetry.instrumentation.logging import LoggingInstrumentor
import os
from dotenv import load_dotenv
load_dotenv()
configure_azure_monitor(
    connection_string=os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
)
LoggingInstrumentor().instrument(set_logging_format=True)
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger("app_logger")
logger.setLevel(logging.INFO)
from azure.monitor.opentelemetry import configure_azure_monitor
import logging
from opentelemetry.instrumentation.logging import LoggingInstrumentor
configure_azure_monitor(
    connection_string="InstrumentationKey=7abaa987-fa18-4aed-a339-67422ecc0416;IngestionEndpoint=https://centralindia-0.in.applicationinsights.azure.com/;LiveEndpoint=https://centralindia.livediagnostics.monitor.azure.com/;ApplicationId=ec470a25-1e53-43aa-b4cc-c3c5436768a4"
)
LoggingInstrumentor().instrument(set_logging_format=True)
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger("app_logger")
logger.setLevel(logging.INFO)
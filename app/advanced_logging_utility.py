import logging
import logging.config
import os
import json

class AdvancedLoggingUtility:
    @staticmethod
    def configure_logging():
        os.makedirs('logs', exist_ok=True)
        logging_conf_path = 'advanced_logging.conf'  # Assumes a different or extended configuration
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Advanced logging configured.")
    
    @staticmethod
    def info(message, **kwargs):
        logging.info(AdvancedLoggingUtility._format_message(message, **kwargs))
    
    @staticmethod
    def warning(message, **kwargs):
        logging.warning(AdvancedLoggingUtility._format_message(message, **kwargs))
    
    @staticmethod
    def error(message, **kwargs):
        logging.error(AdvancedLoggingUtility._format_message(message, **kwargs))
    
    @staticmethod
    def _format_message(message, **kwargs):
        """Formats a log message as a structured JSON string if additional context is provided."""
        if kwargs:
            log_entry = {'message': message, 'context': kwargs}
            return json.dumps(log_entry, ensure_ascii=False)
        return message


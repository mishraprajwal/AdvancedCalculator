import logging
import logging.config
import os
import json

class AdvancedLoggingUtility:
    @staticmethod
    def configure_logging():
        # Ensure the 'logs' directory exists for file logging
        os.makedirs('logs', exist_ok=True)
        
        # Specify the path to the logging configuration file
        logging_conf_path = 'advanced_logging.conf'
        
        # Check if the advanced logging configuration file exists
        if os.path.exists(logging_conf_path):
            # Configure logging according to the config file
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            # If the configuration file does not exist, use the basic configuration setup
            AdvancedLoggingUtility.configure_basic()
        
        # Log a message indicating that logging has been configured
        logging.info("Advanced logging configured.")
    
    @staticmethod
    def configure_basic():
        """Set up a basic logging configuration as a fallback."""
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.StreamHandler(),
                                logging.FileHandler("logs/default.log")
                            ])
        logging.info("Basic logging configuration is set up.")
    
    @staticmethod
    def info(message, **kwargs):
        """Log an info level message."""
        logging.info(AdvancedLoggingUtility._format_message(message, **kwargs))
    
    @staticmethod
    def warning(message, **kwargs):
        """Log a warning level message."""
        logging.warning(AdvancedLoggingUtility._format_message(message, **kwargs))
    
    @staticmethod
    def error(message, **kwargs):
        """Log an error level message."""
        logging.error(AdvancedLoggingUtility._format_message(message, **kwargs))
    
    @staticmethod
    def _format_message(message, **kwargs):
        """Formats a log message as a structured JSON string if additional context is provided."""
        if kwargs:
            log_entry = {'message': message, 'context': kwargs}
            return json.dumps(log_entry, ensure_ascii=False)
        return message

# app/__init__.py
import os
import sys
import pkgutil
import importlib
from dotenv import load_dotenv
from app.command import CommandHandler, Command
from app.advanced_logging_utility import AdvancedLoggingUtility  # Ensure this is correctly imported

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'advanced_logging.conf'  # Adjusted for consistency
        if os.path.exists(logging_conf_path):
            AdvancedLoggingUtility.configure_logging()  # Utilize AdvancedLoggingUtility for setup
        else:
            AdvancedLoggingUtility.configure_basic()  # Assume a basic setup method exists for fallback
        AdvancedLoggingUtility.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        AdvancedLoggingUtility.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            AdvancedLoggingUtility.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    AdvancedLoggingUtility.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                AdvancedLoggingUtility.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        AdvancedLoggingUtility.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    AdvancedLoggingUtility.info("Application exit.")
                    sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:
                    AdvancedLoggingUtility.error(f"Unknown command: {cmd_input}")
                    sys.exit(1)  # Use a non-zero exit code to indicate failure or incorrect command.
        except KeyboardInterrupt:
            AdvancedLoggingUtility.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            AdvancedLoggingUtility.info("Application shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()

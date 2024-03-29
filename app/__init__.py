import os
import sys
import pkgutil
import importlib
from dotenv import load_dotenv
from app.command import CommandHandler, Command
from app.advanced_logging_utility import AdvancedLoggingUtility

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'advanced_logging.conf'
        if os.path.exists(logging_conf_path):
            AdvancedLoggingUtility.configure_logging()
        else:
            AdvancedLoggingUtility.configure_basic()
        AdvancedLoggingUtility.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        AdvancedLoggingUtility.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        calculation_path = os.path.join(plugins_package.replace('.', '/'), 'calculations')
        history_path = os.path.join(plugins_package.replace('.', '/'), 'history')
        other_plugins_path = plugins_package.replace('.', '/')
        
        self.load_plugin_commands(calculation_path, f'{plugins_package}.calculations')
        self.load_plugin_commands(history_path, f'{plugins_package}.history')
        
        self.load_plugin_commands(other_plugins_path,f'{plugins_package}')

                    
    def load_plugin_commands(self, path, package):
        if not os.path.exists(path):
            AdvancedLoggingUtility.warning(f"Directory '{path}' not found.")
            return
        for _, plugin_name, _ in pkgutil.iter_modules([path]):
            try:
                plugin_module = importlib.import_module(f'{package}.{plugin_name}')
                command_instance = getattr(plugin_module, f'{plugin_name.capitalize()}Command')()
                self.command_handler.register_command(plugin_name, command_instance)
                AdvancedLoggingUtility.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
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
                    sys.exit(0)
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:
                    AdvancedLoggingUtility.error(f"Unknown command: {cmd_input}")
                    print(f"Unknown command: {cmd_input}")
                except Exception as e:
                    AdvancedLoggingUtility.error(f"Error during command execution: {e}")
                    print(f"Error during command execution: {e}")
        except KeyboardInterrupt:
            AdvancedLoggingUtility.info("Application interrupted and exiting gracefully.")
            sys.exit(0)
        finally:
            AdvancedLoggingUtility.info("Application shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()
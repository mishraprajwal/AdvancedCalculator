from app.command.base_command import BaseCommand

class LoadCommand(BaseCommand):
    def execute(self, *args):
        if len(args) > 0:
            print("The load command does not accept any arguments.")
        else:
            if self.history_instance.load_history():
                print("Calculation history successfully loaded.")
            else:
                print("Failed to load calculation history.")

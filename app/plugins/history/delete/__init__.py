from app.command.base_command import BaseCommand

class DeleteCommand(BaseCommand):
    def execute(self, *args):
        if len(args) != 1:
            print("The delete command requires exactly one argument: the index of the record to delete.")
        else:
            try:
                index = int(args[0])
                if self.history_instance.delete_history(index):
                    print(f"Successfully deleted record at index {index}.")
                else:
                    print(f"Failed to delete record at index {index}.")
            except ValueError:
                print("Error: Index must be an integer.")

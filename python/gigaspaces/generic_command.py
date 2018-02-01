from datetime import datetime

class GenericCommand:
    @classmethod
    def parse_command(cls,text):
        normalized_text = text.lower()
        if normalized_text=='ping':
            return PingCommand()
        elif normalized_text=='time':
            return TimeCommand()
        else:
            return UnknownCommand()

    def response(self):
        return ""

class PingCommand(GenericCommand):
    def response(self):
        return "pong"

class TimeCommand(GenericCommand):
    def response(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class UnknownCommand(GenericCommand):
    def response(self):
        return 'unrecognized command'

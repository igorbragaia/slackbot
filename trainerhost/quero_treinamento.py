import time
from trainerhost.constants import Constants
from db.operations import *


class QueroTreinamento:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self, slack_client, parser):
        self.slack_client = slack_client
        self.parser = parser

    def run(self, string_array, channel):
        string_to_match = self.call_strings_from_db()  # call from db
        response = ""
        for key_str in string_array:
            best_string = ""  # function(key_str, string_to_match)
            if best_string.lower() == key_str.lower() or best_string == "":
                self.add_string_to_quero_treinamento_db(key_str)
                response = "Querer treinamento de " + key_str + " com sucesso!"
            else:
                self.slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text="Pode ser treinamento de " + best_string + "? [Y/n]"
                )
                while True:
                    command, channel = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                    if command:
                        response = self.loop_to_quero_treinamento_response(command.lower(), key_str,
                                                                           best_string)
                        break
                    time.sleep(self.parser.RTM_READ_DELAY)

        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )

    def call_strings_from_db(self):
        return ["ruby, C, C#, ruby on rails, python, sql, excel"]

    def add_string_to_quero_treinamento_db(self, new_str):
        print("String " + new_str + " should be added to the quero_treinamento_db")
        pass

    def loop_to_quero_treinamento_response(self, command, key_str, best_string):
        response = ""
        if command == "y":
            response = best_string
            self.add_string_to_quero_treinamento_db(best_string)
        else:
            response = key_str
            self.add_string_to_quero_treinamento_db(response)

        return "Querer treinamento de " + response + " com sucesso!"

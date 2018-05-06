import time
from trainerhost.constants import Constants
from db.operations import *
from IA.stringMatching import stringMatch


class QueroTreinamento:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self, slack_client, parser):
        self.slack_client = slack_client
        self.parser = parser

    def run(self, string_array, channel):
        print("Got IA values")
        string_to_match = self.call_strings_from_db()  # call from db

        for key_str in string_array:
            best_string = stringMatch(key_str, list(string_to_match))  # function(key_str, string_to_match)
            if best_string.lower() == key_str.lower() or best_string == "":
                response_str = key_str
            else:
                self.slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text="Pode ser treinamento de " + best_string + "? [Y/n]"
                )
                while True:
                    command, channel = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                    if command:
                        response_str = self.loop_to_quero_treinamento_response(command.lower(), key_str,
                                                                               best_string)
                        break
                    time.sleep(Constants.RTM_READ_DELAY)

            response = "Querer treinar " + response_str + " com sucesso!"
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=response
            )
            print("Call from db")
            self.add_string_to_quero_treinamento_db(response_str)
            print("Added values to db")

    def call_strings_from_db(self):
        return get_unique_requested_trainings()

    def add_string_to_quero_treinamento_db(self, new_str):
        insert_requested_trainings("test", "nlo", new_str)
        pass

    def loop_to_quero_treinamento_response(self, command, key_str, best_string):
        response = ""
        if command == "y":
            response = best_string
        else:
            response = key_str

        return response

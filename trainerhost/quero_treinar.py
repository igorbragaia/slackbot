import time
from trainerhost.constants import Constants
from db.operations import *
from IA.stringMatching import string_match


class QueroTreinar:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self, slack_client, parser):
        self.slack_client = slack_client
        self.parser = parser

    def run(self, string_array, channel, team, id_slack):
        print("Got IA values")
        string_to_match = self.call_strings_from_db()  # call from db
        # string_to_match = []
        print("Call from db")

        for key_str in string_array:
            best_string = string_match(key_str, list(string_to_match))  # function(key_str, string_to_match)
            if best_string.lower() == key_str.lower() or best_string == "":
                response_str = key_str
            else:
                self.slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text="Pode ser treinar " + best_string + "? [Y/n]"
                )
                while True:
                    command, channel, user_id = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                    if command:
                        response_str = self.loop_to_quero_treinar_response(command.lower(), key_str,
                                                                           best_string)
                        break
                    time.sleep(Constants.RTM_READ_DELAY)

            response = "Desejo de treinamento de " + response_str + " registrado com sucesso!"
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=response
            )

            insert_offered_trainings(id_slack, team, response_str)

            print("Added values to db")

    def call_strings_from_db(self):
        return ["espanhol, lideranca, culinaria, vendas, typescript, ingles, elixir, ux, "
                "excel, angular, vue, pitch, react"]


    def loop_to_quero_treinar_response(self, command, key_str, best_string):
        if command == "y":
            response = best_string
        else:
            response = key_str

        return response

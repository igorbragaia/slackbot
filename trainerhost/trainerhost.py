from os import environ
import time
from slackclient import SlackClient
from trainerhost.parse_bot_commands import Parser
from trainerhost.constants import Constants
from trainerhost.quero_treinar import QueroTreinar
from IA.nlp import NLP


class TrainerHost:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self):
        # instantiate Slack client
        self.slack_client = SlackClient(environ['SLACK_BOT_TOKEN'])
        # starterbot's user ID in Slack: value is assigned after the bot starts up
        self.starterbot_id = None

        if self.slack_client.rtm_connect(with_team_state=False):
            print("Starter Bot connected and running!")
            # Read bot's user ID by calling Web API method `auth.test`
            self.starterbot_id = self.slack_client.api_call("auth.test")["user_id"]
            self.parser = Parser(self.starterbot_id)
            self.quero_treinar = QueroTreinar(self.slack_client, self.parser)

            while True:
                command, channel = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                if command:
                    self.handle_command(command, channel)
                time.sleep(self.RTM_READ_DELAY)
        else:
            print("Connection failed. Exception traceback printed above.")

    def handle_command(self, command, channel):
        """
            Executes bot command if the command is known
        """

        # This is where you start to implement more commands!
        if command.startswith("quero_treinar"):
            text_minus_first_word = [command.split(' ', 1)[1]]
            nlp_response = NLP.get_key_phrases(text_minus_first_word)
            self.quero_treinar.quero_treinar(nlp_response[0], channel)
        elif command.startswith("quero_treinamento"):
            text_minus_first_word = [command.split(' ', 1)[1]]
            nlp_response = NLP.get_key_phrases(text_minus_first_word)
            self.quero_treinamento(nlp_response[0], channel)
        else:
            # Default response is help text for the user
            default_response = "Comando Invalido. Tente <quero_treinar> ou <quero_treinamento>."
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=default_response
            )

    def quero_treinamento(self, string_array, channel):
        pass

    def add_string_to_quero_treinamento_db(self, new_str):
        print("String " + new_str + " should be added to the quero_treinamento_db")
        pass

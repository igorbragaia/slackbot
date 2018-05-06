import os
import time
from slackclient import SlackClient
from trainerhost.parse_bot_commands import Parser
from trainerhost.constants import Constants
from trainerhost.quero_treinar import QueroTreinar
from trainerhost.quero_treinamento import QueroTreinamento
from IA.nlp import NLP


class TrainerHost:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self):
        # instantiate Slack client
        self.slack_client = SlackClient('xoxb-358908890179-GlArK9QbFmMEGxJueOKRoBaf')
        # starterbot's user ID in Slack: value is assigned after the bot starts up
        self.starterbot_id = None

        if self.slack_client.rtm_connect(with_team_state=False):
            print("Starter Bot connected and running!")
            # Read bot's user ID by calling Web API method `auth.test`
            self.starterbot_id = self.slack_client.api_call("auth.test")["user_id"]
            self.parser = Parser(self.starterbot_id)
            self.quero_treinar = QueroTreinar(self.slack_client, self.parser)
            self.quero_treinamento = QueroTreinamento(self.slack_client, self.parser)

            while True:
                command, channel = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                if command:
                    print("The user id is ", self.slack_client)
                    self.handle_command(command, channel)
                time.sleep(self.RTM_READ_DELAY)
        else:
            print("Connection failed. Exception traceback printed above.")

    def handle_command(self, command, channel):
        """
            Executes bot command if the command is known
        """

        # This is where you start to implement more commands!
        if command.startswith("quero_treinar") or command.startswith("quero_treinamento"):
            text_minus_first_word = [command.split(' ', 1)[1]]
            nlp_response = NLP.get_key_phrases(text_minus_first_word)

            if command.startswith("quero_treinar"):
                self.quero_treinar.run(nlp_response[0], channel)
            else:
                self.quero_treinamento.run(nlp_response[0], channel)
        else:
            # Default response is help text for the user
            default_response = "Comando Invalido. Tente <quero_treinar> ou <quero_treinamento>."
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=default_response
            )

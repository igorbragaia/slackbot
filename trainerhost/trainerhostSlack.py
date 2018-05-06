import time
from slackclient import SlackClient
from trainerhost.parse_bot_commands import Parser
from trainerhost.constants import Constants
from trainerhost.quero_treinar import QueroTreinar
from trainerhost.quero_treinamento import QueroTreinamento
from trainerhost.quero_remover import QueroRemover
from trainerhost.quero_ver import QueroVer
from trainerhost.quero_help import QueroHelp
from IA.nlp import NLP
from IA.keys import Keys
from db.operations import *


class TrainerHost:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self):
        # instantiate Slack client
        self.slack_client = SlackClient(Keys.slack_key)
        # starterbot's user ID in Slack: value is assigned after the bot starts up
        self.starterbot_id = None

        if self.slack_client.rtm_connect(with_team_state=False):
            print("Starter Bot connected and running!")
            # Read bot's user ID by calling Web API method `auth.test`
            self.starterbot_id = self.slack_client.api_call("auth.test")["user_id"]
            self.parser = Parser(self.starterbot_id)
            self.quero_treinar = QueroTreinar(self.slack_client, self.parser)
            self.quero_treinamento = QueroTreinamento(self.slack_client, self.parser)
            self.quero_remover = QueroRemover(self.slack_client, self.parser)
            self.quero_ver = QueroVer(self.slack_client, self.parser)
            self.quero_help = QueroHelp(self.slack_client, self.parser)

            while True:
                command, channel, user_id = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                if command:
                    self.handle_command(command, channel, get_user(user_id))
                time.sleep(self.RTM_READ_DELAY)
        else:
            print("Connection failed. Exception traceback printed above.")

    def handle_command(self, command, channel, found_user):
        """
            Executes bot command if the command is known
        """

        # This is where you start to implement more commands!
        if command.startswith("treinar") or command.startswith("treinamento") or \
                command.startswith("remover"):
            text_minus_first_word = [command.split(' ', 1)[1]]
            nlp_response = NLP.get_key_phrases(text_minus_first_word)

            if not found_user:
                print("Nao conheco esse usuario ", self.slack_client.api_call("auth.test")["user_id"].strip())
                insert_user(self.slack_client.api_call("auth.test")["user_id"].strip(), "Dev")
            else:
                print("Eu jah te conheco!", self.slack_client.api_call("auth.test")["user_id"].strip())

            if command.startswith("treinar"):
                self.quero_treinar.run(nlp_response[0], channel)
            elif command.startswith("remover"):
                self.quero_remover.run(nlp_response[0], channel)
            else:
                self.quero_treinamento.run(nlp_response[0], channel)
        else:
            if command.startswith("ver"):
                self.quero_ver.run(channel)
            elif command.startswith("help"):
                self.quero_help.run(channel)
            else:
                # Default response is help text for the user
                response = "Comando Invalido. Tente <treinar> ou <treinamento>."
                self.slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text=response
                )

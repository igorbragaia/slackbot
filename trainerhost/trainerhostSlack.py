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
                    print(user_id, " sent a command")
                    self.handle_command(command, channel, user_id)
                time.sleep(self.RTM_READ_DELAY)
        else:
            print("Connection failed. Exception traceback printed above.")

    def handle_command(self, command, channel, user_id):
        """
            Executes bot command if the command is known
        """
        team = get_user(user_id)
        print(user_id)
        if team is None:
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text="Ola usuario! Nao lhe conheco, mas quero ser seu amigo! Me conte mais sobre voce: Qual o seu setor? (dev/parcerias/rh/vendas)"
            )
            while True:
                team, channel, user_id = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                print("No loop")
                if team:
                    print("Command: ", team)
                    if team == "dev" or team == "parcerias" or team == "rh" or team == "vendas":
                        print("Sai do loop")
                        break
                    else:
                        self.slack_client.api_call(
                            "chat.postMessage",
                            channel=channel,
                            text="Desculpa, nao reconheci seu setor. Lembrando que ele deve ser dev/parcerias/rh/vendas"
                        )
                time.sleep(Constants.RTM_READ_DELAY)
            print("Vai inserir o usuario ", user_id, " do time ", team, " agora")
            insert_user(user_id, team)
            print("Usuario inserido")

        print(command)

        # This is where you start to implement more commands!
        if command.startswith("treinar") or command.startswith("treinamento") or \
                command.startswith("remover"):
            text_minus_first_word = [command.split(' ', 1)[1]]
            nlp_response = NLP.get_key_phrases(text_minus_first_word)

            if not get_user(user_id):
                # insert_user(self.slack_client.api_call("auth.test")["user_id"].strip(), "Eric", "Dev")
                self.slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text="Ola usuario! Nao lhe conheco, mas quero ser seu amigo! Me conte mais sobre voce: Qual o seu setor? (dev/parcerias/rh/vendas)"
                )
                while True:
                    command, channel, user_id = self.parser.parse_bot_commands(self.slack_client.rtm_read())
                    print("No loop")
                    if command:
                        print("Command: ", command)
                        if command == "dev" or command == "parcerias" or command == "rh" or command == "vendas":
                            team = command
                            print("Sai do loop")
                            break
                        else:
                            self.slack_client.api_call(
                                "chat.postMessage",
                                channel=channel,
                                text="Desculpa, nao reconheci seu setor. Lembrando que ele deve ser dev/parcerias/rh/vendas"
                            )
                    time.sleep(Constants.RTM_READ_DELAY)
                print("Vai inserir o usuario agora")
                insert_user(user_id, team)

            if command.startswith("treinar"):
                self.quero_treinar.run(nlp_response[0], channel, team, user_id)
            elif command.startswith("remover"):
                self.quero_remover.run(nlp_response[0], channel, team, user_id)
            else:
                self.quero_treinamento.run(nlp_response[0], channel, team, user_id)
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

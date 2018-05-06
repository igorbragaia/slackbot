from os import environ
import time
import re
from slackclient import SlackClient
#from pprint import pprint
#from IA.nlp import NLP


class TrainerHost:
    # constants
    RTM_READ_DELAY = 1  # 1 second delay between reading from RTM
    MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

    def __init__(self):
        # instantiate Slack client
        self.slack_client = SlackClient(environ['SLACK_BOT_TOKEN'])
        # starterbot's user ID in Slack: value is assigned after the bot starts up
        self.starterbot_id = None

        if self.slack_client.rtm_connect(with_team_state=False):
            print("Starter Bot connected and running!")
            # Read bot's user ID by calling Web API method `auth.test`
            self.starterbot_id = self.slack_client.api_call("auth.test")["user_id"]
            while True:
                command, channel = self.parse_bot_commands(self.slack_client.rtm_read())
                if command:
                    self.handle_command(command, channel)
                time.sleep(self.RTM_READ_DELAY)
        else:
            print("Connection failed. Exception traceback printed above.")

    def parse_bot_commands(self, slack_events):
        """
            Parses a list of events coming from the Slack RTM API to find bot commands.
            If a bot command is found, this function returns a tuple of command and channel.
            If its not found, then this function returns None, None.
        """
        for event in slack_events:
            if event["type"] == "message" and not "subtype" in event:
                user_id, message = self.parse_direct_mention(event["text"])
                if user_id == self.starterbot_id:
                    return message, event["channel"]
        return None, None

    def parse_direct_mention(self, message_text):
        """
            Finds a direct mention (a mention that is at the beginning) in message text
            and returns the user ID which was mentioned. If there is no direct mention, returns None
        """
        matches = re.search(self.MENTION_REGEX, message_text)
        # the first group contains the username, the second group contains the remaining message
        return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

    def handle_command(self, command, channel):
        """
            Executes bot command if the command is known
        """
        # Default response is help text for the user
        default_response = "Comando Invalido. Tente <quero_treinar> ou <quero_treinamento>."

        # Finds and executes the given command, filling in response
        response = None

        # This is where you start to implement more commands!
        if command.startswith("quero_treinar"):
            text_minus_first_word = [command.split(' ', 1)[1]]
            nlp_response = NLP.get_key_phrases(text_minus_first_word)
            self.quero_treinar(nlp_response[0], channel)
        elif command.startswith("quero_treinamento"):
            text_minus_first_word = [command.split(' ', 1)[1]]
            nlp_response = NLP.get_key_phrases(text_minus_first_word)
            self.quero_treinamento(nlp_response[0], channel)

    def quero_treinar(self, string_array, channel):
        string_to_match = ["ruby, C, C#, ruby on rails, python, sql, excel"]  # call from db
        response = ""
        for key_str in string_array:
            best_string = ""  # function(key_str, string_to_match)
            if best_string.lower() == key_str.lower() or best_string == "":
                self.add_string_to_quero_treinar_db(key_str)
                response = "Querer treinar " + key_str + " com sucesso!"
            else:
                # Sends the response back to the channel
                self.slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text="Pode ser treinar " + best_string + "? [Y/n]"
                )
                while True:
                    command, channel = self.parse_bot_commands(self.slack_client.rtm_read())
                    if command:
                        response = self.loop_to_quero_treinar_response(command.lower(), channel,
                                                            key_str, best_string)
                        break
                    time.sleep(self.RTM_READ_DELAY)

        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )

    def add_string_to_quero_treinar_db(self, new_str):
        print("String " + new_str + " should be added to the quero_treinar_db")
        pass

    def loop_to_quero_treinar_response(self, command, channel, key_str, best_string):
        response = ""
        if command == "y":
            response = best_string
            self.add_string_to_quero_treinar_db(best_string)
        else:
            response = key_str
            self.add_string_to_quero_treinar_db(response)

        return "Querer treinar " + response + " com sucesso!"

    def quero_treinamento(self, string_array, channel):
        pass

    def add_string_to_quero_treinamento_db(self, new_str):
        print("String " + new_str + " should be added to the quero_treinamento_db")
        pass

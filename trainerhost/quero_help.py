from trainerhost.constants import Constants


class QueroHelp:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self, slack_client, parser):
        self.slack_client = slack_client
        self.parser = parser

    def run(self, channel):

        response = "Removeu  com sucesso!"
        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )

from trainerhost.constants import Constants
from db.operations import *


class QueroVer:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self, slack_client, parser):
        self.slack_client = slack_client
        self.parser = parser

    def run(self, channel):
        unique_requested = get_unique_requested_trainings()
        unique_offered = get_unique_offered_trainings_with_quantity()

        print("unique_offered: ")
        print(unique_offered)
        print("unique_requested: ")
        print(unique_requested)

        response = "Dados: "
        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )
        print("Data has been saw")

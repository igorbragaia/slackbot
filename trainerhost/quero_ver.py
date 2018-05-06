from trainerhost.constants import Constants
from db.operations import *


class QueroVer:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self, slack_client, parser):
        self.slack_client = slack_client
        self.parser = parser

    def run(self, channel):
        unique_requested = get_unique_requested_trainings_with_quantity()
        unique_offered = get_unique_offered_trainings_with_quantity()

        response = "Offered Courses: \n"
        unique_offered = sorted(unique_offered)

        for key, values in unique_offered.items():
            response += "  " + str(key) + ": " + str(values) + "\n"

        response += "\nRequested Courses: \n"
        unique_requested = sorted(unique_requested)
        for key, values in unique_requested.items():
            response += "  " + str(key) + ": " + str(values) + "\n"

        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )

from trainerhost.constants import Constants


class QueroHelp:
    RTM_READ_DELAY = Constants.RTM_READ_DELAY

    def __init__(self, slack_client, parser):
        self.slack_client = slack_client
        self.parser = parser

    def run(self, channel):

        response = "Use \"@quero_help treinamento\" seguindo pelo o que você quer aprender\n"
        response += "Use \"@quero_help treinar\" seguido pelo o que você consegue ou deseja lecionar\n"
        response += "Use \"@quero_help ver\" para ver os cursos mais desejados e os que já tem professor\n"
        response += "Use \"@quero_help remover\" seguido pelo curso concluído para remover do database\n"
        response += "Use \"@quero_help help\" para ver o menu com todos os comandos disponíveis para o bot\n\n"


        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )

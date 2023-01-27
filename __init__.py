from mycroft import MycroftSkill, intent_file_handler


class Discroftslash(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('discroftslash.intent')
    def handle_discroftslash(self, message):
        self.speak_dialog('discroftslash')


def create_skill():
    return Discroftslash()


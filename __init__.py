from mycroft import MycroftSkill, intent_file_handler


class Desinfetante(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('desinfetante.intent')
    def handle_desinfetante(self, message):
        self.speak_dialog('desinfetante')


def create_skill():
    return Desinfetante()


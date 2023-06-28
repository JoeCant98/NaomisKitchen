from naomi import plugin
import random

class smartKitchenPlugin(plugin.SpeechHandlerPlugin):

    def intents(self):
        return {
            'SearchIntent': {
                'locale': {
                    'en-US': {
                        'keywords': {
                            'NumberKeyword': [
                                "One",
                                "Two",
                                "Three",
                                "Four",
                                "Five"
                                ]},
                        'regex': {
                            'Item': [
                                " add {Number} (?P<Item>)",
                                ]},
                        'templates': [
                            'add {Number} {Item}'
                            ]}
                        },
                'action': self.handle
                }
            }

    def handle(self, intent, mic):
        NUMBERS = {
            'ONE' :    1,
            'TWO' :    2,
            'THREE' :  3,
            'FOUR' :   4,
            'FIVE' :   5
        }
        ERROR = ''
        NUMBER ='ONE'
        try:
            NUMBER = intent['matches']['NumberKeyword'][0]
            # print (" Number is: " + NUMBER)      # For debug
        except KeyError:
            ERROR = "Could not understand input. Please try again!"
        # try:
        #     NumberInt = NUMBERS[NUMBER]
        # except KeyError:  
        #     ERROR = "Number input out of range"

        if ERROR != '':
            mic.say(self.gettext("ERROR: %s!" % ERROR))

        else:
            mic.say(self.gettext("Adding {Number} {item} to ingredients list"))
            # Add item * number to ingredients
            # If unsuccessful, output error. Else:
            response = random.choice([
                self.gettext("{NUMBER} {Item} have been added you absolute legend"),
                self.gettext("{Number} {Item} added. Can I help with anything else? I have no teeth!"),
                self.gettext("I have added {Number} {Item} you sexy beast"),
                self.gettext("I've added {Number} {Item} you filthy animal")
            ])
            mic.say(response)
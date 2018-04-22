# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from bs4 import BeautifulSoup

__author__ = 'bhaveshAn'

LOGGER = getLogger(__name__)


class BusinessNews(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(BusinessNews, self).__init__(name="BusinessNews")
        
        # Initialize working variables used within the skill.
        self.count = 0

    def initialize(self):
        intent = IntentBuilder("BusinessNewsIntent").require("BusinessNewsKeyword").build()
        self.register_intent(intent, self.handle_intent) 
    
    def handle_intent(self, message):
        fixed_url = 'https://www.cnbc.com/economy/'
        response = requests.get(fixed_url)
        news_string = ''
        soup = BeautifulSoup(response.text, "html.parser")
        for new in soup.findAll('li', {'class': 'headline'}):
        news_string = news_string + str(new.find('a').text)
        self.speak(news_string)


def create_skill():
    return BusinessNews()

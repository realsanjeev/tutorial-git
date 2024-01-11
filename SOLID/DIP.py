from typing import final
from abc import ABC, abstractmethod
from LSP import (Duck,
                Crow,
                SimpleConversation,
                AbstractConversation)

class AbstractChannel(ABC):
    @abstractmethod
    def get_channel_message(self) ->str:
        pass

class SMSChannel(AbstractChannel):
    def get_channel_message(self) -> str:
        return "(via SMS)"

class AbstractCommunicator(ABC):
    def get_channel(self) -> AbstractChannel:
        pass

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(),
              self.get_channel().get_channel_message(),
              sep = '\n')

class SimpleCommunicator(AbstractCommunicator):  
    def __init__(self, channel : AbstractChannel):
        self._channel = channel
   
    def get_channel(self) -> str:
        return self._channel

if __name__=="__main__":
    duck1 = Duck("L")
    duck2 = Duck("P")
    crow1 = Crow("T")
    crow2 = Crow("A")
    channel = SMSChannel()
    communicator = SimpleCommunicator(channel=channel)
    conversation = SimpleConversation(duck1, duck2)
    communicator.communicate(conversation)

from abc import abstractmethod


class StateBase(object):

    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def on_leave(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def handle_input(self, user_input, state_stack):
        pass


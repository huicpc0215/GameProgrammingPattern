class StateHandler(object):

    def __init__(self, force_change_state_function):
        self.cur_state = None
        self.state_stack = list()
        self.force_change_state_function = force_change_state_function

    def handle_input(self, user_input):
        if self.cur_state is None:
            self.cur_state = self.force_change_state_function(user_input)
        else:
            next_state = self.cur_state.handle_input(user_input, self.state_stack)
            if next_state is not None:
                self.cur_state.on_leave()
                self.cur_state = next_state
                self.cur_state.on_enter()

    def update(self):
        if self.cur_state is not None:
            self.cur_state.update()

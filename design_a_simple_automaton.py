class State(object):
    def __init__(self, is_accept):
        self._is_accept = is_accept

    def is_accept(self):
        return self._is_accept

    def get_next_move(self, command):
        return self._next_moves[command]

    def set_next_moves(self, next_moves):
        self._next_moves = next_moves

class Automaton(object):

    def __init__(self):
        q1, q2, q3 = State(False), State(True), State(False)
        q1.set_next_moves({'0': q1, '1': q2})
        q2.set_next_moves({'0': q3, '1': q2})
        q3.set_next_moves({'0': q2, '1': q2})
        self.state = q1

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        for command in commands:
            self.state = self.state.get_next_move(command)
        return self.state.is_accept()

my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.

## ============================================================
##  HANGMAN MINIGAME for Ren'Py
## ============================================================

init python:

    import string
    import random

    class HangmanState(object):
        """Holds all the runtime state for one round of hangman."""

        MAX_WRONG = 4 

        def __init__(self, word_list, category=""):
            self.category = category
            self.word = random.choice(word_list).upper()
            self.guessed = set()
            self.wrong_letters = []
            self.finished = False
            self.won = False

        @property
        def wrong_count(self):
            return len(self.wrong_letters)

        @property
        def remaining(self):
            return HangmanState.MAX_WRONG - self.wrong_count

        def display_word(self):
            """Returns the word with unguessed letters replaced by underscores."""
            chars = []
            for letter in self.word:
                if letter in self.guessed or not letter.isalpha():
                    chars.append(letter)
                else:
                    chars.append("_")
            return " ".join(chars)

        def is_solved(self):
            return all((not letter.isalpha()) or (letter in self.guessed) for letter in self.word)

        def guess(self, letter):
            letter = letter.upper()
            if self.finished or letter in self.guessed or letter in self.wrong_letters:
                return

            if letter in self.word:
                self.guessed.add(letter)
                if self.is_solved():
                    self.finished = True
                    self.won = True
            else:
                self.wrong_letters.append(letter)
                if self.wrong_count >= HangmanState.MAX_WRONG:
                    self.finished = True
                    self.won = False


    # ASCII gallows art, one stage per wrong guess (0 to 6 wrong guesses)
    HANGMAN_STAGES = [
        r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    ]


label hangman_minigame(word_list=["LILY"], category="What I love"):

    python:
        hangman_state = HangmanState(word_list, category=category)
        hangman_result = None

    call screen hangman_screen(hangman_state)

    python:
        hangman_result = "win" if hangman_state.won else "lose"

    return


screen hangman_screen(state):

    modal True
    zorder 100

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        background "#ffffff00"

        vbox:
            spacing 20
            xalign 0.5

            if state.category:
                text "Category: [state.category]" size 52 color "#cc3333" xalign 0.5

            text state.display_word() size 96 color "#8b0000" xalign 0.5 font "gui/fonts/cmunorm.ttf"

            text "[HANGMAN_STAGES[state.wrong_count]]" font "gui/fonts/cmunorm.ttf" size 32 color "#b30000" xalign 0.5

            text "Wrong guesses left: [state.remaining]" size 40 color "#993333" xalign 0.5

            if state.wrong_letters:
                text "Missed: [' '.join(state.wrong_letters)]" size 36 color "#661111" xalign 0.5

            # letter buttons, laid out in rows
            grid 13 2:
                xalign 0.5
                spacing 4
                for letter in string.ascii_uppercase:
                    textbutton letter:
                        sensitive (letter not in state.guessed) and (letter not in state.wrong_letters) and (not state.finished)
                        text_size 40
                        text_color "#000000"
                        text_insensitive_color "#00000055"
                        xsize 90
                        ysize 90
                        action [Function(state.guess, letter), Function(renpy.restart_interaction)]

            if state.finished:
                if state.won:
                    text "You got it! The word was [state.word]." size 52 color "#8b0000" xalign 0.5
                else:
                    text "Out of guesses! The word was [state.word]." size 52 color "#b30000" xalign 0.5

                textbutton "Continue":
                    xalign 0.5
                    action Return()
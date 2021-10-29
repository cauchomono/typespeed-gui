from tkinter import *
from time import sleep
from random import choice

class TypeTest:

    def __init__(self,words_list):
        self.words_list = words_list
        self.time = 60
        self.correct_words = 0
        self.correct_letters = 0
        self.words_per_minute = 0
        self.word ="Here are the words to be written"

        self.bg_color = "white"
        self.pad_x = 15
        self.font_label = ("Arial", 13)
        self.font_word_label = ("Arial", 20)

        self.window = Tk()
        self.window.title("Type Speed Test")
        self.window.geometry("800x600")
        self.window.config(bg=self.bg_color)
        self.upper_frame()
        self.middle_frame()
        self.downer_frame()


        self.window.mainloop()

    def upper_frame(self):
        self.frame_1 = Frame(self.window,width=800,height=200 )
        self.frame_1.grid(row=0, column=0, columnspan=3)
        self.frame_1.config(bg="white")
        self.words_lbl =Label(self.frame_1, text=f"High Scores:", bg=self.bg_color, font=self.font_label).grid(row=0, column=0, padx=self.pad_x)
        self.words_lbl =Label(self.frame_1, text=f"Words per Minute: {self.words_per_minute}", bg=self.bg_color, font=self.font_label).grid(row=0, column=3, padx=self.pad_x)
        self.correct_words_lbl = Label(self.frame_1, text=f"Correct Words: {self.correct_words}",bg=self.bg_color, font=self.font_label).grid(row=0, column=1, padx=self.pad_x)
        self.correct_letters_lbl = Label(self.frame_1, text=f"Correct Letters: {self.correct_letters}",bg=self.bg_color, font=self.font_label).grid(row=0, column=2, padx=self.pad_x)
        self.timer_update()

    def timer_update(self):
        self.time_lbl = Label(self.frame_1, text=f"Time left: {self.time}", bg=self.bg_color,
                              font=self.font_label).grid(row=0, column=4, padx=self.pad_x)

    def middle_frame(self):
        self.frame_2 = Frame(self.window,width=800,height=200)
        self.frame_2.grid(row=1, column=0, columnspan=3)
        self.frame_2.config(bg="white")
        self.update_word()
        self.word_entry= Entry(self.frame_2).grid(row=1)


    def downer_frame(self):
        self.frame_3 = Frame(self.window, width=800, height=200)
        self.frame_3.grid(row=2, column=0, columnspan=3)
        self.frame_3.config(bg="white")

        Button(text="Start", command=self.init_game).grid()


    def game_timer(self):
        self.time = 60
        self.time -= 1
        self.window.after(1000, self.game_timer)
        self.timer_update()
        self.window.update()




    def word_generator(self):
        self.word = choice(self.words_list)
        self.word_label.destroy()

    def update_word(self):

        self.word_label = Label(self.frame_2, text=self.word, bg=self.bg_color, font=self.font_word_label)
        self.word_label.grid(row =0,pady=50)



    def init_game(self):

        self.word_generator()
        self.update_word()
        print(self.word)

    def words_judge(self):
        pass

    def word_counter(self):
        pass

    def letter_counter(self):
        pass

    def score(self):
        pass

    def reset_scores(self):
        pass


    def play(self):
        pass

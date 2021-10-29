from tkinter import *
from time import sleep
from random import choice
import csv
from tkinter import messagebox

class TypeTest:

    def __init__(self,words_list):
        self.words_list = words_list
        self.correct_words_HS = 0
        self.correct_letters_HS = 0
        self.words_per_minute_HS = 0
        self.obtain_high_scores()
        self.time = 5
        self.correct_words = 0
        self.correct_letters = 0
        self.words_per_minute = 0
        self.word ="Here are the words to be written"
        self.user_word = ""

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
        self.words_lbl =Label(self.frame_1, text=f"Words per Minute: {self.words_per_minute_HS}", bg=self.bg_color, font=self.font_label).grid(row=0, column=3, padx=self.pad_x)
        self.correct_words_lbl = Label(self.frame_1, text=f"Correct Words: {self.correct_words_HS}",bg=self.bg_color, font=self.font_label).grid(row=0, column=1, padx=self.pad_x)
        self.correct_letters_lbl = Label(self.frame_1, text=f"Correct Letters: {self.correct_letters_HS}",bg=self.bg_color, font=self.font_label).grid(row=0, column=2, padx=self.pad_x)
        self.timer_update()

    def timer_update(self):
        self.time_lbl = Label(self.frame_1, text=f"Time left: {self.time}", bg=self.bg_color,
                              font=self.font_label).grid(row=0, column=4, padx=self.pad_x)

    def middle_frame(self):
        self.frame_2 = Canvas(self.window,width=800,height=200)
        self.frame_2.grid(row=1, column=0, columnspan=3)
        self.frame_2.config(bg="white")
        self.word_label = Label(self.frame_2, text=self.word, bg=self.bg_color, font=self.font_word_label)
        self.word_label.grid(row=0, pady=50)
        self.word_entry= Entry(self.frame_2)
        self.word_entry.grid(row=1)

    def downer_frame(self):
        self.frame_3 = Frame(self.window, width=800, height=200)
        self.frame_3.grid(row=2, column=0, columnspan=3)
        self.frame_3.config(bg="white")

        Button(text="Start", command=self.init_game).grid()


    def game_timer(self):
        self.time -= 1
        self.window.update()
        self.timer_update()
        if self.time == 0:
            return False
        self.window.after(1000, self.game_timer)


    def user_words_collector(self,event):
        self.user_word = self.word_entry
        self.words_judge()
        self.word_generator()
        print(self.correct_words)



    def word_generator(self):
        self.word_label.destroy()
        self.word = choice(self.words_list)
        self.word_label = Label(self.frame_2, text=self.word, bg=self.bg_color, font=self.font_word_label)
        self.word_label.grid(row=0, pady=50)
        self.word_entry.delete(0, 'end')




    def init_game(self):
        self.word_generator()
        if True:
            self.window.bind("<space>",self.user_words_collector)
            self.window.bind("<Return>", self.user_words_collector)


    def words_judge(self):
        self.user_word = self.word_entry.get()
        if self.word == self.user_word:
            self.correct_words += 1
            self.correct_letters += len(self.word)


    def final_scores(self):
        message_scores = f"Correct Words{self.correct_words}\n" \
                         f"Correct letters {self.correct_letters}\n" \
                         f"Words per Minute{self.words_per_minute}" \
                         f"Words per Minute(5 letter per word average)"

        messagebox.showinfo(title="Your Score",message=message_scores)

    def save_score(self):
        pass

    def reset_scores(self):
        pass

    def obtain_high_scores(self):
        high_score_list=[]
        with open("high_scores.txt") as hs:
            high_scores_csv=csv.reader(hs)
            for row in high_scores_csv:
                high_score_list.append(row)
        self.correct_words_HS = high_score_list[1][0]
        self.correct_letters_HS = high_score_list[1][1]
        self.words_per_minute_HS = high_score_list[1][2]










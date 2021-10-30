from tkinter import *
from random import choice
import csv
from tkinter import messagebox

class TypeTest:

    def __init__(self,words_list):
        self.words_list = words_list
        self.obtain_high_scores()

        self.time = 60
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
        self.window.geometry("1000x600")
        self.window.config(bg=self.bg_color)
        self.upper_frame()
        self.middle_frame()
        self.downer_frame()


        self.window.mainloop()

    def upper_frame(self):
        self.frame_1 = Frame(self.window,width=800,height=200,pady=20,padx=10 )
        self.frame_1.grid(row=0, column=0, columnspan=3)
        self.frame_1.config(bg="white")
        restart_high_score_btn = Button(self.frame_1,text="Restart HighScore",command=self.reset_scores).grid(row=0,column=0)

        self.words_lbl =Label(self.frame_1, text=f"High Scores:", bg=self.bg_color, font=self.font_label)
        self.words_lbl.grid(row=0, column=1, padx=self.pad_x)

        self.correct_words_lbl = Label(self.frame_1, text=f"Correct Words: {self.correct_words_HS}", bg=self.bg_color,
                                       font=self.font_label)
        self.correct_words_lbl.grid(row=0, column=2, padx=self.pad_x)

        self.correct_letters_lbl = Label(self.frame_1, text=f"Correct Letters: {self.correct_letters_HS}",
                                         bg=self.bg_color, font=self.font_label)
        self.correct_letters_lbl.grid(row=0, column=3, padx=self.pad_x)

        self.words_lbl =Label(self.frame_1, text=f"Words per Minute: {self.words_per_minute_HS}", bg=self.bg_color, font=self.font_label)
        self.words_lbl.grid(row=0, column=4, padx=self.pad_x)

        self.time_lbl = Label(self.frame_1, text=f"Time left: {self.time}", bg=self.bg_color,
                              font=self.font_label)
        self.time_lbl.grid(row=0, column=5, padx=self.pad_x)

    def timer_update(self):
        self.time_lbl.config(text=f"Time left: {self.time}")

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

        self.start_button = Button(self.frame_3,text="Start", command=self.init_game)
        self.start_button.grid(row=0, column=0,pady=20)


    def game_timer(self):
        self.time -= 1
        self.window.update()
        self.timer_update()
        if self.time == 0:
            return False
        self.window.after(1000, self.game_timer)


    def user_words_collector(self,event):
        self.user_word = self.word_entry.lower()
        self.words_judge()
        self.word_generator()


    def word_generator(self):
        self.word_label.destroy()
        self.word = choice(self.words_list)
        self.word_label = Label(self.frame_2, text=self.word, bg=self.bg_color, font=self.font_word_label)
        self.word_label.grid(row=0, pady=50)
        self.word_entry.delete(0, 'end')


    def init_game(self):
        if self.time > 0:
            self.word_generator()
            self.game_timer()
            self.window.bind("<space>",self.user_words_collector)
            self.window.bind("<Return>", self.user_words_collector)
            self.window.after(self.time*1000,self.finish_game)
            self.start_button.grid_remove()




    def words_judge(self):
        self.user_word = self.word_entry.get().lower()
        if self.word == self.user_word:
            self.correct_words += 1
            self.correct_letters += len(self.word)
        self.words_per_minute = float("{0:.2f}".format(self.correct_letters/5))

    def finish_game(self):
        self.final_scores()
        self.save_hig_scores()
        Button(self.frame_3, text="Restart", command=self.restart_game).grid(row=0, column=1)
        self.update_lbl()


    def update_lbl(self):
        self.correct_words_lbl.config(text=f"Correct Words: {self.correct_words_HS}")
        self.correct_letters_lbl.config(text=f"Correct Letters: {self.correct_letters_HS}")
        self.words_lbl.config(text=f"Words per Minute: {self.words_per_minute_HS}")

    def restart_game(self):
        self.time = 60
        self.correct_words = 0
        self.correct_letters = 0
        self.words_per_minute = 0
        self.update_lbl()
        self.init_game()

    def final_scores(self):
        message_scores = f"Correct Words: {self.correct_words}\n" \
                         f"Correct letters: {self.correct_letters}\n" \
                         f"Words per Minute: {self.words_per_minute}\n" \
                         f"Note: Words per Minute are 5 letter per word average"

        messagebox.showinfo(title="Your Score",message=message_scores)


    def save_hig_scores(self):
        if self.correct_words > self.correct_words_HS:
            self.correct_words_HS = self.correct_words

        if self.correct_letters > self.correct_letters_HS:
            self.correct_letters_HS = self.correct_letters

        if self.words_per_minute > self.words_per_minute_HS:
            self.words_per_minute_HS = self.words_per_minute

        with open("high_scores.txt","w") as hs:
            scores=[self.correct_words_HS,self.correct_letters_HS,self.words_per_minute_HS]
            high_scores_csv = csv.writer(hs)
            high_scores_csv.writerow(self.correct_letters_titles)
            high_scores_csv.writerow(scores)


    def reset_scores(self):
        with open("high_scores.txt","w") as hs:
            high_scores_csv = csv.writer(hs)
            high_scores_csv.writerow(self.correct_letters_titles)
            high_scores_csv.writerow([0,0,0])
        self.obtain_high_scores()
        self.update_lbl()



    def obtain_high_scores(self):
        high_score_list=[]
        with open("high_scores.txt") as hs:
            high_scores_csv=csv.reader(hs)
            for row in high_scores_csv:
                high_score_list.append(row)
        self.correct_letters_titles = high_score_list[0]
        self.correct_words_HS = int(high_score_list[2][0])
        self.correct_letters_HS = int(high_score_list[2][1])
        self.words_per_minute_HS = float(high_score_list[2][2])










import tkinter as tk

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Program")
        self.qaid = 0
        self.map = {}
        self.qpa = [
            ["What is the musical term for a group of notes played together?", "Chord", "Harmony", "Melody", "Rhythm"],
            ["Who is often referred to as the King of Pop?", "Michael Jackson", "Elvis Presley", "Madonna", "None of the above"],
            ["Which music streaming service was founded in 2006?", "Spotify", "Apple Music", "Prime Music", "Youtube Music"],
            ["Which female artist released the album 'Folklore' in 2020?", "Taylor Swift", "Ariana Grande", "Cardi B", "Clairo"],
            ["What is the stage name of the American singer Abel Tesfaye?", "The Weeknd", "Eminem", "Quavo", "Chance"],
            ["In music, what does the term 'fortissimo' (ff) indicate?", "Play very loudly", "Play very softly", "Be silent", "Play in a falsetto"],
            ["Who is known for playing the electric guitar with his teeth?", "Jimi Hendrix", "John Lennon", "Eric Clapton", "None of the above"],
            ["Which genre of music originated in Jamaica?", "Reggae", "Jazz", "Pop", "R&B"],
            ["What is the name of the Korean boy band with songs like 'Dynamite'?", "BTS", "EXO", "BLACKPINK", "NCT"],
            ["Who won the MTV Video Music Award for Artist of the Year in 2020?", "Taylor Swift", "Billie Eilish", "Ariana Grande", "Lady Gaga"]
        ]

        self.bg = tk.StringVar(value="Choice1")

        self.panel = tk.LabelFrame(root, text="Question", padx=20, pady=20, background="#FFD700")
        self.panel.pack(padx=10, pady=10)
        self.lblmess = tk.Label(self.panel, text="", font=("Arial", 14), background="#FFD700")
        self.lblmess.pack(padx=10, pady=10)
        
        self.choice_frame = tk.Frame(self.panel, background="#FFD700")
        self.choice_frame.pack(padx=10, pady=10)

        self.choice1 = tk.Radiobutton(self.choice_frame, text="", variable=self.bg, value="Choice1", font=("Arial", 12), background="#FFD700")
        self.choice1.pack(side=tk.LEFT, padx=10)
        self.choice2 = tk.Radiobutton(self.choice_frame, text="", variable=self.bg, value="Choice2", font=("Arial", 12), background="#FFD700")
        self.choice2.pack(side=tk.LEFT, padx=10)
        self.choice3 = tk.Radiobutton(self.choice_frame, text="", variable=self.bg, value="Choice3", font=("Arial", 12), background="#FFD700")
        self.choice3.pack(side=tk.LEFT, padx=10)
        self.choice4 = tk.Radiobutton(self.choice_frame, text="", variable=self.bg, value="Choice4", font=("Arial", 12), background="#FFD700")
        self.choice4.pack(side=tk.LEFT, padx=10)

        self.btnext = tk.Button(self.panel, text="Next", command=self.next_question, font=("Arial", 12), background="#FFD700")
        self.btnext.pack(padx=10, pady=10)
        self.update_question()

    def update_question(self):
        question, choice1, choice2, choice3, choice4 = self.qpa[self.qaid]
        self.lblmess.config(text=question)
        self.choice1.config(text=choice1)
        self.choice2.config(text=choice2)
        self.choice3.config(text=choice3)
        self.choice4.config(text=choice4)

    def next_question(self):
        selected_choice = self.bg.get()
        if selected_choice == "Choice1":
            selected_text = self.choice1.cget("text")
        elif selected_choice == "Choice2":
            selected_text = self.choice2.cget("text")
        elif selected_choice == "Choice3":
            selected_text = self.choice3.cget("text")
        elif selected_choice == "Choice4":
            selected_text = self.choice4.cget("text")
        else:
            selected_text = "Not answered"

        self.map[self.qaid] = selected_text

        if self.qaid < 9:
            self.qaid += 1
            self.update_question()
        else:
            self.show_answers()

    def show_answers(self):
        self.panel.destroy()

        result_panel = tk.LabelFrame(self.root, text="Quiz Result", padx=20, pady=20, background="#FFD700")
        result_panel.pack(padx=10, pady=10)

        left_frame = tk.Frame(result_panel, background="#FFD700")
        left_frame.pack(side=tk.LEFT, padx=10)
        right_frame = tk.Frame(result_panel, background="#FFD700")
        right_frame.pack(side=tk.LEFT, padx=10)

        score = 0
        for qid in range(5):
            question, correct_answer, _, _, _ = self.qpa[qid]
            user_answer = self.map.get(qid, "Not answered")
            tk.Label(left_frame, text=f"Q{qid+1}: {question}", font=("Arial", 12), background="#FFD700").pack(anchor=tk.W)
            tk.Label(left_frame, text=f"Your Answer: {user_answer}", font=("Arial", 10), background="#FFD700").pack(anchor=tk.W)
            tk.Label(left_frame, text=f"Correct Answer: {correct_answer}", font=("Arial", 10), background="#FFD700").pack(anchor=tk.W)
            tk.Label(left_frame, text="", background="#FFD700").pack(anchor=tk.W)
            if user_answer == correct_answer:
                score += 1

        for qid in range(5, 10):
            question, correct_answer, _, _, _ = self.qpa[qid]
            user_answer = self.map.get(qid, "Not answered")
            tk.Label(right_frame, text=f"Q{qid+1}: {question}", font=("Arial", 12), background="#FFD700").pack(anchor=tk.W)
            tk.Label(right_frame, text=f"Your Answer: {user_answer}", font=("Arial", 10), background="#FFD700").pack(anchor=tk.W)
            tk.Label(right_frame, text=f"Correct Answer: {correct_answer}", font=("Arial", 10), background="#FFD700").pack(anchor=tk.W)
            tk.Label(right_frame, text="", background="#FFD700").pack(anchor=tk.W)
            if user_answer == correct_answer:
                score += 1

        tk.Label(result_panel, text=f"Your Score: {score}/10", font=("Arial", 14), background="#FFD700").pack(anchor=tk.W)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="#FFD700")
    app = Quiz(root)
    root.mainloop()

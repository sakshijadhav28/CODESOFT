import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import ImageTk, Image
from Recommender import recommend

def recommend_movies(event=None):  
    movie_name = entry.get()
    recommendations = recommend(movie_name)
    
    text.delete('1.0', tk.END)
    for i, movie in enumerate(recommendations, start=1):
        text.insert(tk.END, f"{i}. {movie}\n")

root = tk.Tk()
root.title("Movie Recommendation System")  
root.configure(bg='Gray94')  

label = tk.Label(root, text="Enter the title of your favourite movie:",font=('Times', 18, 'bold'), bg='Gray94', fg='#333333')
label.pack()

entry = tk.Entry(root, width=30,font=('Helvetica', '18'))  
entry.pack(pady=15)

button = tk.Button(root, text="Recommend Movies", command=recommend_movies,font=('Roboto', 14), bg='azure4', fg='black')
button.pack(pady=20)

text = scrolledtext.ScrolledText(root,bg='Gray94')
text.pack()

root.bind('<Return>', recommend_movies)  # bind Enter key 
root.mainloop()

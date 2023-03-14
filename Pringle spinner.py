import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

videoplayer = TkinterVideo(master=root, scaled=True)

videoplayer.load(r"C:/Users/Omega/Documents/GitHub/spinner/Pingle.mov")
videoplayer.pack(expand=True, fill="both")
videoplayer.play()


root.mainloop()

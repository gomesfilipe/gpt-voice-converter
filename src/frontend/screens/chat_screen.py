from typing import List
from src.frontend.helpers.message import Message
from src.frontend.screens.screen import Screen
import tkinter as tk
from src.audio_text_converters.pyttsx3_audio_text_converter import Pyttsx3AudioTextConverter
from src.enums.side import Side
import os

class ChatScreen(Screen):
  def __init__(self):
    self.__messages: List[Message] = [
      Message('ola tudo bem1', 'audio.mp3', 30, Side.LEFT),
      Message('ola tudo bem2', 'audio.mp3', 30, Side.RIGHT),
      Message('ola tudo bem3', 'audio.mp3', 30, Side.LEFT),
      Message('ola tudo bem4', 'audio.mp3', 30, Side.RIGHT),
      Message('ola tudo bem4', 'audio.mp3', 30, Side.RIGHT),
    ]

    self.__converter = Pyttsx3AudioTextConverter()
    self.__size = 20

  def render(self) -> None:
    self.__screen = tk.Tk()
    self.__screen .title('Chat de Voz com IA')

    self.__robot_icon = tk.PhotoImage(file = os.path.join('assets', 'robot.png'), width = self.__size, height = self.__size)
    self.__avatar_icon = tk.PhotoImage(file = os.path.join('assets', 'avatar.png'), width = self.__size, height = self.__size)
    self.__play_icon = tk.PhotoImage(file = os.path.join('assets', 'play.png'), width = self.__size, height = self.__size)

    self.__canvas = tk.Canvas(self.__screen)
    self.__scrollbar = tk.Scrollbar(self.__screen, orient="vertical", command=self.__canvas.yview)
    self.__canvas.configure(yscrollcommand=self.__scrollbar.set)

    self.__canvas.grid(row=0, column=0, sticky="nsew")
    self.__scrollbar.grid(row=0, column=1, sticky="ns")

    self.__main_frame = tk.Frame(self.__canvas)
    self.__canvas.create_window((0, 0), window=self.__main_frame, anchor="nw")
    button_frame = tk.Frame(self.__screen)
    # self.__canvas.create_window((0, 0), window=button_frame, anchor="s")
    # self.__main_frame.pack()

    for message in self.__messages:
      self.add_message(message)
    

    button = tk.Button(
      button_frame,
      text = 'oi',
      command = lambda message = message: self.on_click_play_audio(message),
      # image = self.__play_icon,
    )

    button.pack( padx = 10)

    self.__screen.grid_rowconfigure(0, weight=1)
    self.__screen.grid_columnconfigure(0, weight=1)
    self.__screen.mainloop()

  def on_click_speak_button(self) -> None:
    pass

  def on_click_play_audio(self, message: Message) -> None:
    self.add_message(message)
    print(message)
  
  def add_message(self, message: Message) -> None: 
    author_icon = self.__robot_icon if message.side == Side.LEFT else self.__avatar_icon
  
    message_frame = tk.Frame(self.__main_frame)
    message_frame.pack(padx = 20, pady = 20)

    icon_label = tk.Label(message_frame, image = author_icon)
    icon_label.pack(side = tk.LEFT, padx = 10)

    label_message = tk.Label(message_frame, text = message.content, font = ('Arial', 14))
    label_message.pack(side = tk.LEFT, padx = 10)

    button = tk.Button(
      message_frame,
      text = message.content,
      command = lambda message = message: self.on_click_play_audio(message),
      image = self.__play_icon,
    )

    button.pack(side = tk.RIGHT, padx = 10)
    self.__canvas.configure(scrollregion=self.__canvas.bbox("all"))

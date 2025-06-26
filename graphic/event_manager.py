import pygame as pr

class EventManager():
    def __init__(self):
        self.listeners = []
        self.events = []

    def trigger(self, event):
        self.events.append(event)
        for listener in self.listeners:
            listener(event)

    def listen(self, callback):
        self.listeners.append(callback)


event_manager = EventManager()

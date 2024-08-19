from utils import *
from creatures import PC

class Objective:
    def __init__(self, description, is_completed=False):
        self.description = description
        self.is_completed = is_completed

    def complete(self):
        self.is_completed = True


class Quest:
    def __init__(self, title, description, objectives, rewards):
        self.title = title
        self.description = description
        self.objectives = objectives  # List of objectives
        self.rewards = rewards  # Rewards for completing the quest
        self.status = "Not Started"  # Can be "Not Started", "In Progress", or "Completed"

    def start(self):
        self.status = "In Progress"

    def complete(self, completer: PC):
        if all(obj.is_completed for obj in self.objectives):
            self.status = "Completed"
            for reward in self.rewards:
                completer.money += reward

    def is_completed(self):
        return self.status == "Completed" and all(obj.is_completed for obj in self.objectives)


class QuestManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest: Quest):
        self.quests.append(quest)

    def start_quest(self, quest_title):
        for quest in self.quests:
            if quest.title == quest_title:
                quest.start()
                type_text(f"%*ORANGE*%Quest '{quest.title}' started: {quest.description}%*RESET*%")
                return
        type_text(f"Quest '{quest_title}' not found.")

    def complete_quest(self, quest_title):
        for quest in self.quests:
            if quest.title == quest_title and quest.is_completed():
                quest.complete()
                type_text(f"%*ORANGE*%Quest '{quest.title}' completed! Rewards: {quest.rewards} money%*RESET*%")
                return

    def show_quests(self):
        for quest in self.quests:
            status = quest.status
            type_text(f"%*ORANGE*%Quest '{quest.title}': {status}%*RESET*%")
            for obj in quest.objectives:
                obj_status = "Completed" if obj.is_completed else "Not Completed"
                type_text(f"%*ORANGE*%  - {obj.description}: {obj_status}%*RESET*%")

    def update_objective(self, objective_description):
        for quest in self.quests:
            for obj in quest.objectives:
                if obj.description == objective_description:
                    obj.complete()
                    type_text(f"%*ORANGE*%Objective '{obj.description}' completed!%*RESET*%")
                    return


class MalwareClass:

    def __init__(self, name, extension, cve_score, target_os):
        self.name = name
        self.extension = extension
        self.cve_score = cve_score
        self.target_os = target_os

    def update_cve_score(self, cve_score):
        self.cve_score = cve_score

    def attack(self):
        print("This is the attack method")
from malware import MalwareClass

 class RansomwareClass(MalwareClass):
     def __init__(self, name, extension, cve_score, target_os, encryption, ransom_amount):
         super().__init__(name, extension, cve_score, target_os)
         self.encryption = encryption
         self.ransom_amount = ransom_amount
from typing import List
from models import Patient,InsertPatient,UpdatePatient

#``````````````````````````````````````````Query``````````````````````````````````````````
class GetPatientsInterface:
    def getPatients(self)->List[Patient]:
        raise NotImplementedError("This method should be overridden.")
class GetPatientDataInterface:
    def getPatientData(self,id:int)->Patient:
        raise NotImplementedError("This method should be overridden.")
    
#``````````````````````````````````````````Mutation``````````````````````````````````````````
class InsertPatientInterface:
    def insertPatient(self,patient:InsertPatient)->str:
        raise NotImplementedError("This method should be overridden.")

class UpdatePatientInterface:
    def updatePatient(self, patient:UpdatePatient)->str:
        raise NotImplementedError("This method should be overridden.")

class DeletePatientInterface:
    def deletePatient(self, id:int)->str:
        raise NotImplementedError("This method should be overridden.")
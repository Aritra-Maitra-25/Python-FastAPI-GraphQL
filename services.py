import strawberry
from strawberry.asgi import GraphQL
from resolvers import GetPatientsResolver,GetPatientDataResolver,InsertPatientResolver,UpdatePatientResolver,DeletePatientResolver
from interfaces import GetPatientsInterface,GetPatientDataInterface,InsertPatientInterface,UpdatePatientInterface,DeletePatientInterface
from typing import List
from models import Patient,InsertPatient, Response, UpdatePatient


@strawberry.type
class Query:
    @strawberry.field
    def getPatients(self) -> List[Patient]:
        getPatientsResolver: GetPatientsInterface = GetPatientsResolver()
        patients=getPatientsResolver.getPatients()
        return patients
    
    @strawberry.field
    def getPatientData(self, id: int) -> Patient:
        getPatientDataResolver: GetPatientDataInterface = GetPatientDataResolver()
        patient = getPatientDataResolver.getPatientData(id=id)
        return patient
    
@strawberry.type
class Mutation:
    @strawberry.field
    def insertPatients(self,patient:InsertPatient)->Response:
        insertPatientResolver:InsertPatientInterface=InsertPatientResolver()
        message=insertPatientResolver.insertPatient(patient=patient)
        return Response(message=message)
    
    @strawberry.field
    def updatePatient(self, patient: UpdatePatient) -> Response:
        updatePatientResolver: UpdatePatientInterface = UpdatePatientResolver()
        message = updatePatientResolver.updatePatient(patient=patient)
        return Response(message=message)
    
    @strawberry.field
    def deletePatient(self, id: int) -> Response:
        deletePatientResolver: DeletePatientInterface = DeletePatientResolver()
        message = deletePatientResolver.deletePatient(id=id)
        return Response(message=message)
    

import config
from models import Patient,InsertPatient,UpdatePatient
import logging
from typing import List
from interfaces import GetPatientsInterface,InsertPatientInterface,GetPatientDataInterface,UpdatePatientInterface,DeletePatientInterface

#``````````````````````````````````````````Query``````````````````````````````````````````

class GetPatientsResolver(GetPatientsInterface):
    def getPatients(self)->List[Patient]:
        cursor=config.DBConnect()
        try:
            cursor.execute("SELECT id, name, age, phone, email, address FROM public.patients")
            result=cursor.fetchall()
          # patients = [Patient(id=row[0], name=row[1], age=row[2] , phone=row[3], email=row[4], address=row[5]) for row in result]
            patients = [Patient(*row) for row in result]
        except Exception as e:
            logging.error(f"Error fetching patients: {e}")
            return []
        finally:
            cursor.close()
        return patients
    
class GetPatientDataResolver(GetPatientDataInterface):
    def getPatientData(self,id:int)->Patient:
        cursor=config.DBConnect()
        result=None
        try:
            cursor.execute ("""
                Select p.id,p."name",p.age,p.phone,p.email,p.address from public.patients p where p.id =%s
                            """,(id,))
            result=cursor.fetchone()
        except Exception as e:
            logging.error(f"Error fetching patients: {e}")
        finally:
            cursor.close()
        if not result:
            raise Exception(f"Patient with id {id} not found.") 
        return Patient(*result)
    
#``````````````````````````````````````````Mutation``````````````````````````````````````````

class InsertPatientResolver(InsertPatientInterface):
    def insertPatient(self, patient:InsertPatient)->str:
        cursor=config.DBConnect()
        try:
            cursor.execute("""
            INSERT INTO public.patients(id,"name",age,phone,email,address)
            values(%s,%s,%s,%s,%s,%s)
            """,(patient.id,patient.name,patient.age,patient.phone,patient.email,patient.address))
            cursor.connection.commit()
        except Exception as e:
            logging.error(f"Error inserting patients: {e}")
            cursor.connection.rollback()
            return "Error inserting patient"
        finally:
            cursor.close()
        return "Patient inserted successfully"
    
class UpdatePatientResolver(UpdatePatientInterface):
    def updatePatient(self,patient:UpdatePatient)->str:
        cursor=config.DBConnect()
        try:
            update_fields=[]
            update_values = []

            if  patient.name is not None:
                update_fields.append('"name"=%s')
                update_values.append(patient.name)
            if  patient.age is not None:
                update_fields.append('"age"=%s')
                update_values.append(patient.age)
            if  patient.email is not None:
                update_fields.append('"email"=%s')
                update_values.append(patient.email)
            if  patient.phone is not None:
                update_fields.append('"phone"=%s')
                update_values.append(patient.phone)
            if patient.address is not None:
                update_fields.append('"address"=%s')
                update_values.append(patient.address)

            if not update_fields:
                return "No fields to update"
            
            update_fields_str= ",".join(update_fields)
            update_values.append(patient.id)

            query=f"""
            UPDATE public.patients
            SET {update_fields_str}
            WHERE id=%s
            """

            cursor.execute(query,update_values)
            cursor.connection.commit()
        except Exception as e:
            logging.error(f"Error updating patient: {e}")
            cursor.connection.rollback()
            return "Error updating patient"
        finally:
            cursor.close()
        return "Patient updated successfully"
    
class DeletePatientResolver(DeletePatientInterface):
    def deletePatient(self, id: int) -> str:
        cursor=config.DBConnect()
        try:
            cursor.execute("""
                DELETE FROM public.patients
                WHERE id=%s;
                       """,(id,))
            cursor.connection.commit()
        except Exception as e:
            logging.error(f"Error deleting patient: {e}")
            cursor.connection.rollback()
            return "Error deleting patient"
        finally:
            cursor.close()
        return "Patient Successfully Deleted!"
    
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://face-attendence-b1f23-default-rtdb.firebaseio.com/"})

ref = db.reference('Students')

data = {
    "D1212":
        {
            "name": "Dawood",
            "major": "SEO",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2024-04-11 00:53:34"

        },
    "22221":
        {
            "name": "Eisha",
            "major": "Doctor",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2024-04-11 00:53:34"
             },
    "321654":
        {
            "name": "Hassan",
            "major": "Engineer",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-04-11 00:53:34"
        },
    "85271":
        {
            "name": "Rose",
            "major": "Doctor",
            "starting_year": 2017,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-07-11 00:50:36"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "SpaceX",
            "starting_year": 2024,
            "total_attendance": 2,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-04-11 00:53:34"
        },
    "17981798":
        {
            "name": "Ali Suleman",
            "major": "Cyber",
            "starting_year": 2024,
            "total_attendance": 3,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-04-11 00:53:34"
        }


}
#for specific directory

for key, value in data.items():
    ref.child(key).set(value)
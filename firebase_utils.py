from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase app once
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate("serviceAccountKey.json")  # Adjust path if needed
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://faceattend-2f396-default-rtdb.firebaseio.com/"  # Replace with your DB URL
    })

def mark_attendance(name):
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "name": name,
            "timestamp": now
        }
        ref = db.reference("Attendance")
        ref.push(data)
        print(f"[DEBUG] Attendance marked for {name} at {now}")
    except Exception as e:
        print(f"[ERROR] Failed to mark attendance for {name}: {e}")

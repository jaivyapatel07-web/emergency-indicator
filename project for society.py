"importrequests"

def send_emergency_alert(contacts, message):
    """
    Sends an emergency SMS alert to a list of phone numbers.
    
    Note: You will need to sign up for a free SMS gateway API (like Twilio, Vonage, or Textbelt).
    """
    print(f" Initializing Broadcast: '{message}'\n" + "-"*40)
    
    for contact in contacts:
        name = contact.get("name")
        phone = contact.get("phone")
        
        # Example using a placeholder public SMS gateway (Textbelt)
        # Replace this URL and payload with your actual SMS provider's documentation
        payload = {
            'number': phone,
            'message': f"EMERGENCY ALERT: {message}",
            'key': 'textbelt'  # Replace with your actual API key
        }
        try:
            # Simulating the network request
            print(f"Sending message to {name} ({phone})...")
            # response = requests.post('https://textbelt.com', data=payload)
            # response_data = response.json()
            
            # Simulated success for this demo
            print(f" Alert successfully sent to {name}!")
            
        except Exception as e:
            
            print(f" Failed to send alert to {name}: {e}")

# --- Example Usage ---
community_contacts = [
    {"name": "Alice Smith", "phone": "+15550199"},

    {"name": "Bob Jones", "phone": "+15550188"},

    {"name": "Charlie Brown", "phone": "+15550177"}
]

critical_message = "Flash flood warning for Sector 4. Please move to higher ground immediately."

send_emergency_alert(community_contacts, critical_message)


class ResourceMatcher:
    def __init__(self):
        self.donors = []

    def register_donor(self, name, blood_type, location, contact):

        donor = {"name": name, "blood_type": blood_type, "location": location, "contact": contact}
        
        self.donors.append(donor)
        
        print(f" Thank you {name}! Registered as a {blood_type} donor.")

    def find_match(self, required_blood_type, patient_location):
        
        print(f"\n Searching for {required_blood_type} donors in {patient_location}...")
        matches = []
        
        for donor in self.donors:
            if donor["blood_type"] == required_blood_type and donor["location"].lower() == patient_location.lower():
                matches.append(donor)
        
        if not matches:
            print(" No direct matches found in this area. Expanding search or alert networks is advised.")
            return
        
        print(f" Found {len(matches)} matching donor(s):")
        
        for match in matches:
            print(f" Name: {match['name']} | Contact: {match['contact']}")

# --- Example Usage ---
matcher = ResourceMatcher()

# Registering community donors
matcher.register_donor("Ron weast", "O+", "Downtown", "+15550122")

matcher.register_donor("John carter", "A-", "Uptown", "+15550133")

matcher.register_donor("Susan potter", "O+", "Downtown", "+15550144")

# Patient emergency request
matcher.find_match(required_blood_type="O+", patient_location="Downtown")
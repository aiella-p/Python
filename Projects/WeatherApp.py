import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt 

class WeatherApp(QWidget): # QWidget is the base class of all user interface objects in Qt. It 
#provides properties, functions and signals to create, manage and customize widgets.
 def __init__(self): # we need constractor and no arguments besides 'self'
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self) # we are adding city_label to our weather_app object
# In case the arguments sends to the parents we will call the parent 'super' class then call 
# the constractor        
        self.city_input = QLineEdit(self) # for text box...
        self.get_weather_button = QPushButton(" Get Weather", self)  
        self.temperature_label = QLabel(self)      
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

 def initUI(self):
     self.setWindowTitle("Weather App") 
     vbox = QVBoxLayout()   
     vbox.addWidget(self.city_label)
     vbox.addWidget(self.city_input)
     vbox.addWidget(self.get_weather_button)
     vbox.addWidget(self.temperature_label)
     vbox.addWidget(self.emoji_label)
     vbox.addWidget(self.description_label)
     
     self.setLayout(vbox)

     self.city_label.setAlignment(Qt.AlignCenter)
     self.city_input.setAlignment(Qt.AlignCenter)
     #self.get_weather_button.setAlignment(Qt.AlignCenter)
     self.temperature_label.setAlignment(Qt.AlignCenter)
     self.emoji_label.setAlignment(Qt.AlignCenter)
     self.description_label.setAlignment(Qt.AlignCenter)

     self.city_label.setObjectName("city_label")
     self.city_input.setObjectName("city_input")
     self.get_weather_button.setObjectName("get_weather_button")
     self.temperature_label.setObjectName("temperature_label")
     self.emoji_label.setObjectName("emoji_label")
     self.description_label.setObjectName("description_label")

     self.setStyleSheet("""
              QLabel, QPushButton{
                 font-family: calibri;       
               }      
              QLabel#city_label{
                 font-size: 40px;
                 font-style: Italic;                 
                }          
                QLineEdit#city_input{
                 font-size: 40px;
                 }          
                 QPushButton#get_weather_button{
                  font-size: 30px; 
                  font-weight: bold;       
                 }        
                 QLabel#temperature_label{
                  font-size: 75px;       
                 }       
                 QLabel#emoji_label{
                  font-size: 100px;       
                  font-family: segoe UI emoji;
                 }
                 QLabel#description_label{
                   font-size: 40px;      
                         }
     """)
     self.get_weather_button.clicked.connect(self.get_weather)
     
 def get_weather(self):
   api_key='f1b4f7b3253f512e1d3f0894cc14290b'
   city= self.city_input.text()
   url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    #print(data)
    if data["cod"] == 200:
        self.display_weather(data) 

   except requests.exceptions.HTTPError as http_error:
     match response.status_code:
       case 400:
         self.display_error("Bad request\n Please check your input")
  
       case 401:
         self.display_error("UnAuthorised, Invalid API Key")

       case 403:
         self.display_error("Access denied\n Forbidden")

       case 404:
         self.display_error("not found\n city not found")

       case 500:
         self.display_error("Internal server error\n Please try again")

       case 502:
         self.display_error("Bad gateway\n Invalid response from server")

       case 503:
         self.display_error("Service Unavaialable\n Server is down")

       case 504:
         self.display_error("Gateway Timeout\n No response from the server")  

       case _: 
         self.display_error(f"HTTP Error occuried\n{http_error}")  
   except requests.exceptions.ConnectionError:
       self.display_error("Connection error, check internet !")
   except requests.exceptions.Timeout:
       self.display_error("Timeout error")
     
   except requests.exceptions.TooManyRedirects:
     self.display_error("Too many redirect error - check url")
    
   except requests.exceptions.RequestException as req_error:
     self.display_error(f"Request error:\n{req_error}")


 def display_error(self,message):
   self.temperature_label.setStyleSheet("font-size: 30px;")
   self.temperature_label.setText(message)
   self.emoji_label.clear()
   self.description_label.clear()

 def display_weather(self,data):
   self.temperature_label.setStyleSheet("font-size: 50px;")
   print(data)
   temp_k = data["main"]["temp"]
   temp_c = temp_k - 273.15
   temp_f = (temp_k *9/5) - 459.67
   weather_id = data["weather"][0]["id"] 
   # create a local variable weather_id to access the 'data' object then access the key
   # by name 'weather', the value of key weather is 'list', so, the list has only one 
   #item in it....so, the index of operator is[0], then we access the key as 'id' is a three
   # digit number (803...)
   weather_description = data["weather"][0]["description"]
   print(temp_c)    
   print(temp_k)
   print(temp_f)
   print(data)

   self.temperature_label.setText(f"{temp_f:.0f}°F")
   self.emoji_label.setText(self.get_weather_emoji(weather_id))
   self.description_label.setText(weather_description)

 @staticmethod
 def get_weather_emoji(weather_id):
     
     if 200 <= weather_id <= 232:
       return "⛈️"
     elif 300 <= weather_id <= 321:
       return "⛅"
     elif 500 <= weather_id <= 531:
       return "⛈️"
     elif 600 <= weather_id <= 622:
       return "❄️"
     elif 701 <= weather_id <= 741:
       return "🌫️"
     elif weather_id == 762:
       return "🌋"
     elif weather_id == 771:
       return "🍃🍃"
     elif weather_id == 781:
       return "🌪️"
     elif weather_id == 800:
       return "☀️"
     elif 801 <= weather_id <= 804:
       return "☁️"
     else:
       return ""
if __name__ == "__main__": # if we are running python file directly we are running WeatherApp object otherwise wo donot !!

  app = QApplication(sys.argv)
  weather_app=WeatherApp() # we will create a weather_app constrator based on class WeatherApp
  weather_app.show() # we are calling show() 
  sys.exit(app.exec_()) # this method handles events of application such as closing window...!!
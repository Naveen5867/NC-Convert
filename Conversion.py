from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.uix.spinner import Spinner


# Length dictionary

length = {

    "m": 1,
    "cm": 100,
    "mm": 1000,
    "km": 0.001,
    "ft" : 3.280839895,
    "in" : 39.3700787402,
    "mile" : 0.0006213712,
    "yd" : 1.0936132983

}
volume = {
        "m cube" : 1,
        "ml" : 1000000,
        "litre" : 1000,
        "gallon" : 219.9692482991,
        "inch cube" : 61023.744094732,
        "ft cube" : 35.3146667215,
        "mm cube" : 1000000000
}
area = {
        "m square" : 1,
        "cm square" : 10000,
        "mm square" : 1000000,
        "ft square" : 10.7639104167,
        "acre" : 0.0002471054,
        "km square" : 0.000001,
        "hectare" : 0.0001 
}
mass = {
        "kg" : 1,
        "g" : 1000,
        "mg" : 1000000,
        "pound" : 2.2046226218,
        "ounce" : 35.2739619496,
        "ton" : 0.001 
}
speed = {
        "m/s" : 1,
        "km/h" : 18/5,
        "mph" : 2.2369362921,               
        "mi/s": 0.000621371,
        "ft/s" : 3.280839895,
        "km/s" : 0.001,
        "ft/h" : 11811.023622047,
        "in/s" : 39.3700787402,
        "in/h" : 141732.28346457,
        "knot" : 1.9438444924
}
time = {
        "sec" : 1,
        "min" : 1/60,
        "hr" : 1/3600,
        "milsec" : 1000,
        "day" : 0.0000115741,
        "week" : 0.0000016534
}
data = {
        "byte" : 1,
        "mb" : 0.000001,
        "kb" : 0.001,
        "gb" : 0.000000001,
        "tb" : 0.000000000001,
        "bit" : 0.125
}
temprature = {}
all_quantities = {
        'length' : length,
        'volume' : volume,
        'data' : data,
        'speed' : speed,
        'area' : area,
        'mass' : mass,
        'time' : time,
        'temprature' : temprature
}

# Conversion function

def convert(value, from_unit, to_unit, quantity):

    r = value * quantity[to_unit] / quantity[from_unit]
    return r

def C_F(c):
    return(9/5 * c) + 32
def C_K(c):
    return c + 273.15
def F_C(f):
    return 5/9 *( f - 32)
def F_K(f):
    return 5/9 *( f - 32) + 273.15
def K_C(k):
    return k - 273.15
def K_F(k):
    return ((k - 273.15) * 9/5 ) + 32
    
    
class ConverterApp(App):

    def build(self):

        layout = BoxLayout(
            orientation='vertical',
            padding=[30,20,30,20]
            spacing=50
        )
    

        # Title

        title = Label(
            text='Unit Converter 😄🔥',
            font_size=60
        )

        layout.add_widget(title)


        # Value input

        self.value_input = TextInput(
            hint_text='Enter value',
            multiline=False
        )
        
        layout.add_widget(self.value_input)

        self.quantity = Spinner(
            text = 'Choose quantity:    ',
            values = ('mass','length','volume','area','data','speed','time','temprature'),
            size_hint = (1,None),
            height = 100
        )
        
        layout.add_widget(self.quantity)
        
        # From unit input

        self.from_input = Spinner(
                text = 'Choose from unit:  ',
                values = (),
            
         )
        
        layout.add_widget(self.from_input)
   
        self.to_input = Spinner(
           text = 'Choose to unit:    ',
           values = (),
       )
        layout.add_widget(self.to_input)
        self.quantity.bind(text=self.update_units)
        # Convert button

        button = Button(
            text='Convert',
            size_hint=(1, 0.3)
        )

        button.bind(on_press=self.do_conversion)
    
        layout.add_widget(button)


        # Result label

        self.result = Label(
            text='Result appears here',
            font_size=40
        )

        layout.add_widget(self.result)
    
        return layout

    def update_units(self,spinner,text):

            if self.quantity.text == 'temprature':
                units = ('C','F','K')
            else:
                units = tuple(

            all_quantities[text].keys()

            )

            self.from_input.values = units

            self.to_input.values = units
            
            
    def do_conversion(self, instance):

        try:

            value = float(self.value_input.text)

            from_unit = self.from_input.text

            to_unit = self.to_input.text
            
            quantity = all_quantities[self.quantity.text]
            
            if self.quantity.text == 'temprature':
                
                if from_unit == 'C':
                        if to_unit == 'F':
                             answer = C_F(value)
                        else:
                             answer = C_K(value)
                elif from_unit == 'K':
                              if to_unit == 'C':
                                  answer = K_C(value)
                              else:
                                  answer = K_F(value)
                elif from_unit == 'F':
                        if to_unit == 'C':
                            answer = F_C(value)
                        else:
                                answer = F_K(value) 
            elif from_unit == to_unit:
                answer = value
      
            else:
                
                answer = convert(
                    value,
                    from_unit,
                    to_unit,
                    quantity
                )

                   
            self.result.text = str(answer)
            
            with open('history.txt','a') as f:
                f.write(
                f"{value}{from_unit}—>{answer}{to_unit}\n"
                )

        except:

            self.result.text = "Invalid Input 😭"


ConverterApp().run()
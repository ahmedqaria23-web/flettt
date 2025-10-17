from flet import *
from flet_flashlight import Flashlight
from flet_permission_handler import PermissionHandler, PermissionType



def main(page:Page):
    page.title = "abdalluh"
    
    page.scroll ="auto"
    page.window.top = 1
    page.window.left = 1000
    page.window.width = 500
    page.window.height = 800
    page.bgcolor = "blue"
    
    flashlight = Flashlight()
    page.overlay.append(flashlight)
    
    ph=PermissionHandler()
    page.overlay.append(ph)
    
    
    #setting bar
    def open_app_setting(e):
        ph.open_app_settings(e)
    
    
    page.add(
        
        
        AppBar(
            title= Text('flash abdalluh '),
        
            color= "white",
            bgcolor= "red",
            actions= [
                IconButton(Icons.SETTINGS,on_click= open_app_setting)
            ]
            ),
        
        
        
        
        
        Row([
            Text("\n\n\n on and of flash " , size=35 ,color= "black")
            
        ] ,alignment=MainAxisAlignment.CENTER
            ),
        
        Row([
            Image(src="app/image_processing.jpg" , width=300 ,height=200)
            
            
        ],alignment=MainAxisAlignment.CENTER),
        
        Row([
            ElevatedButton(
                "ON",
                width=100,
                icon=Icons.PLAY_ARROW  ,
                style=ButtonStyle(
                    bgcolor=" black",
                    padding=20,
                   color= "white",
                    shape= ContinuousRectangleBorder(radius=100)
                      
                ) , 
                on_click=lambda _: flashlight.turn_on()   
                
            ),
            
             ElevatedButton(
                "Off",
                width=100,
                icon=Icons.PLAY_DISABLED_SHARP  ,
                style=ButtonStyle(
                    bgcolor=" black",
                    padding=20,
                   color= "white",
                    shape= ContinuousRectangleBorder(radius=100)
                      
                ) , 
                on_click=lambda _: flashlight.turn_off()
                
            )
            
            
        ]  ,alignment=MainAxisAlignment.CENTER),
        
        
        Row([
            Text("\n\n\n Abdalluh Ahemd App" , size=20 ,color= "black")
            
        ] ,alignment=MainAxisAlignment.CENTER
            )
        
            
        
    )


    page.update()

app(main)    

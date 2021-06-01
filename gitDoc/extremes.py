glyphWidth = 290
capHeight = 288

thickness = 12
middleLine = 0.519
roundness = 0.395
# propNumb for handleX and handle Y
propNumb = 1.9
# diagonalExtra = 4.61




def left_margin(path):
    
    with savedState():
        # set a color
        fill(0)
        # do a transformation
        # draw something
        rect(0, 0, glyphWidth, capHeight)
    
    path.moveTo((0, 0))
    path.lineTo((thickness, 0))
    path.lineTo((thickness, capHeight))
    path.lineTo((0, capHeight))
    path.closePath()
    
def draw_G():
    path = BezierPath()
    left_margin(path)
    
    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 3) * roundness
    handleY = (capHeight ) * roundness / 2 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY     
    
    
    # 1     
    path.moveTo((glyphWidth/ 2, 0))

    path.qCurveTo( 
        (glyphWidth/2 - handleX, 0),
        (thickness, capHeight/2- handleY),
        (thickness, capHeight/2 + handleY),                
        (glyphWidth/ 2 - handleX, capHeight),
        (glyphWidth/2, capHeight)
)
    
    path.lineTo((0, capHeight ))
    path.lineTo((0, 0 ))
    path.lineTo((glyphWidth / 2, 0))

    path.closePath()
    # 1 end   
    
    # 2 ----------------------------------------------
    # 2a start ---------------------------------------
    path.moveTo((glyphWidth/ 2, 0))

    path.qCurveTo(
   
        (glyphWidth/2 + handleX, 0), 
        (onx, capHeight/2 - handleY),
        (onx, capHeight/2 )
        
          
        )
    path.lineTo((3*thickness, capHeight/2 ))
    path.lineTo((3*thickness, capHeight/2 -thickness ))
    path.lineTo((onx-thickness, capHeight/2 -thickness ))
    path.qCurveTo(
        
        
        # (onx-thickness, ony - 2*handleY/propNumb),
        (onx-thickness, capHeight/2 -handleY),
        (glyphWidth/2 + handleX/propNumb, thickness),
        (glyphWidth/2 - handleX/propNumb, thickness),
        
        (thickness*2, capHeight/2 - handleY/propNumb),
        
         # 2a end ---------------------------------------------
         # 2b start ---------------------------------------------
        (thickness*2, capHeight/2+ handleY/propNumb),

        
        (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),               
        (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
        
               
        (onx-thickness, capHeight/2 + handleY), 
        
    )

    path.lineTo((onx, capHeight/2+ handleY ))
    
    path.qCurveTo(
        
        (glyphWidth/2 + handleX, capHeight),
        (glyphWidth/2 , capHeight)
        
               
        )

    
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth,0))
    
    
    path.closePath()
    
    
    stroke(0)
    fill(1)
    drawPath(path)
    return path

       
            
    



    
def draw_Z():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    
    #left part 
    
    path.moveTo((thickness, thickness))
    path.lineTo((glyphWidth-thickness*(1+propNumb), capHeight-thickness))
    path.lineTo((thickness, capHeight-thickness))
    path.closePath()
    # right part
    path.moveTo((glyphWidth, 0))    
    path.lineTo((glyphWidth - thickness, 0))
    path.lineTo((glyphWidth-thickness, thickness))
    path.lineTo((thickness*(1+propNumb),thickness))
    path.lineTo((glyphWidth-thickness, capHeight -thickness))
    path.lineTo((glyphWidth- thickness, capHeight))
    path.lineTo((glyphWidth, capHeight))
    path.closePath()
    
       
    return path


def draw_N():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    path.closePath()
    
    path.moveTo((glyphWidth-2*thickness-thickness/propNumb,0))
    path.lineTo((2*thickness, capHeight -propNumb*thickness))
    path.lineTo((2*thickness, 0))
    path.closePath()
    
    path.moveTo((2*thickness+thickness/propNumb, capHeight))
    path.lineTo((glyphWidth-2*thickness, capHeight))
    path.lineTo((glyphWidth-2*thickness, propNumb*thickness))
    path.closePath()
    
    return path

def draw_M():
    path = BezierPath()
    left_margin(path)
    fill(1)
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    path.closePath()
    
    path.moveTo((2*thickness+thickness/propNumb, capHeight))
    path.lineTo((glyphWidth-2*thickness-thickness/propNumb, capHeight))
    path.lineTo((glyphWidth/2, propNumb*thickness))
    path.closePath()

    
    path.moveTo((glyphWidth-2*thickness-thickness/propNumb,0))
    path.lineTo((2*thickness, capHeight -propNumb*thickness))
    path.lineTo((2*thickness, 0))
    path.closePath()
    
    return path

def draw_U():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 3) * roundness
    handleY = (capHeight ) * roundness / 2 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY     
    
    path.moveTo((glyphWidth/ 2, 0))
    path.qCurveTo(
        
        
        (glyphWidth/2 + handleX, 0),
        (onx, capHeight/2 - handleY),
        (onx, capHeight/2)
               
        )
    
    path.lineTo((onx, capHeight ))
    path.lineTo((glyphWidth, capHeight ))
    path.lineTo((glyphWidth, 0 ))
    path.lineTo((glyphWidth / 2, 0))
    path.closePath()
    
    path.moveTo((glyphWidth/ 2, 0))

    path.qCurveTo( 
        (glyphWidth/2 - handleX, 0),
        (thickness, capHeight/2 - handleY),
        (thickness, capHeight/2 ),                
        
)
    
    path.lineTo((thickness, capHeight ))
    path.lineTo((0, 0 ))
    path.lineTo((glyphWidth / 2, 0))
    
    
    path.closePath()
    
    
    
    # INSIDE COUNTER 
    
    path.moveTo((glyphWidth/2, thickness))
    
    path.qCurveTo(
        
       (glyphWidth/2 + handleX/propNumb, thickness),
        (onx-thickness, capHeight/2 - handleY/propNumb),
        (onx-thickness, capHeight ),
        # (onx-thickness, capHeight/2 + handleY/propNumb),                
        # (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
        # (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),
        # (thickness*2, capHeight/2 + handleY/propNumb),
        

        )
    path.lineTo((onx-thickness,capHeight))
    path.lineTo((thickness*2,capHeight))
    
    path.qCurveTo(
        
        (thickness*2, capHeight/2 - handleY/propNumb),
        (glyphWidth/2 - handleX/propNumb, thickness),
        (glyphWidth/2 , thickness),

        )
    
    path.closePath()
    

    return path




def draw_S():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 5) * roundness
    handleY = (capHeight ) * roundness / 1 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY     
    
        
    
    path.moveTo((glyphWidth/ 2, 0))
    path.qCurveTo(
        (glyphWidth/2 + handleX, 0), 
        (onx, capHeight/4 - handleY/propNumb),
        (onx, capHeight/4 + handleY),
        
        (thickness*2, capHeight*3/4 - handleY/propNumb),
        (thickness*2, capHeight*3/4 + handleY/propNumb),
        
        (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),               
        (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
          
        (onx-thickness, capHeight/2 + handleY),        
    )
    path.lineTo((onx, capHeight/2+ handleY ))
    path.qCurveTo( 
        (glyphWidth/2 + handleX, capHeight),
        (glyphWidth/2 , capHeight)     
        )
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth,0))
    path.closePath()
    
    path.moveTo((glyphWidth/2,0))
    path.qCurveTo(
        (glyphWidth/2 - handleX, 0),
        (thickness, capHeight/2 - handleY),

        )
    path.lineTo((2*thickness, capHeight/2 - handleY))
    path.qCurveTo(
        # (glyphWidth/ 2 - handleX/propNumb, thickness),
        # (2*thickness, capHeight*1/4 - handleY/propNumb),
        (glyphWidth/ 2 - handleX/propNumb, thickness),
        (glyphWidth/ 2 + handleX/propNumb, thickness),
        (glyphWidth-2*thickness, capHeight*1/4 - handleY/propNumb),
        (glyphWidth-2*thickness, capHeight*1/4 + handleY/propNumb),
        (thickness, capHeight*3/4 - handleY),
        (thickness, capHeight*3/4 + handleY/propNumb),
        (glyphWidth/2 - handleX, capHeight),
        (glyphWidth/2 , capHeight)
        
        )
    path.lineTo((thickness , capHeight))
    path.lineTo((thickness , 0))
    path.closePath()

    
    
    return path







def draw_H():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    path.closePath()
    
    path.moveTo((glyphWidth - thickness*2, 0))  
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine - thickness / 2))
    path.lineTo(( thickness*2, capHeight * middleLine - thickness / 2))
    path.lineTo((thickness*2 , 0))
    path.closePath()
    
    path.moveTo((glyphWidth - thickness*2, capHeight))  
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine + thickness / 2))
    path.lineTo(( thickness*2, capHeight * middleLine + thickness / 2))
    path.lineTo((thickness*2 , capHeight))
    path.closePath()
    return path
    
def draw_I():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((thickness*2, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((thickness*2, capHeight))
    path.closePath()
        
    return path


def draw_L():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((thickness*2, capHeight))
    path.lineTo((thickness*2, thickness))
    path.lineTo((glyphWidth-thickness, thickness))
    path.closePath()
        
    return path

def draw_T():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((glyphWidth /2 + thickness/2, 0))    

    path.lineTo((glyphWidth /2 + thickness/2, capHeight-thickness))
    path.lineTo((glyphWidth-thickness, capHeight-thickness))
    path.lineTo((glyphWidth-thickness, capHeight))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth, 0))
   
    path.closePath()
    
    path.moveTo((glyphWidth /2 - thickness/2, 0)) 
    path.lineTo((glyphWidth /2 - thickness/2, capHeight - thickness))
    path.lineTo((thickness, capHeight - thickness))
    path.lineTo((thickness, 0))
    path.closePath()
        
    return path


def draw_E():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight - thickness))
    path.lineTo((thickness * 2, capHeight - thickness))
    path.lineTo((thickness * 2, capHeight * middleLine + thickness / 2))
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine + thickness / 2))
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine - thickness / 2))
    path.lineTo((thickness * 2, capHeight * middleLine - thickness / 2))
    path.lineTo((thickness * 2, thickness))
    path.lineTo((glyphWidth - thickness, thickness))
    path.closePath()
    
    return path

def draw_F():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((thickness*2, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight - thickness))
    path.lineTo((thickness * 2, capHeight - thickness))
    path.lineTo((thickness * 2, capHeight * middleLine + thickness / 2))
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine + thickness / 2))
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine - thickness / 2))
    path.lineTo((thickness * 2, capHeight * middleLine - thickness / 2))
    path.lineTo((thickness * 2, 0))
    path.closePath()
    
    return path


def draw_O():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 3) * roundness
    handleY = (capHeight ) * roundness / 2 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY     
    
    path.moveTo((glyphWidth/ 2, 0))

    path.qCurveTo(
        
        
        (glyphWidth/2 + handleX, 0),
        (onx, capHeight/2 - handleY),
        (onx, capHeight/2 + handleY),                
        (glyphWidth/ 2 + handleX, capHeight),
        (glyphWidth/2, capHeight)        
        )
    
    path.lineTo((glyphWidth, capHeight ))
    path.lineTo((glyphWidth, 0 ))
    path.lineTo((glyphWidth / 2, 0))
    
    
    path.closePath()
    
    path.moveTo((glyphWidth/ 2, 0))

    path.qCurveTo( 
        (glyphWidth/2 - handleX, 0),
        (thickness, capHeight/2 - handleY),
        (thickness, capHeight/2 + handleY),                
        (glyphWidth/ 2 - handleX, capHeight),
        (glyphWidth/2, capHeight)
)
    
    path.lineTo((0, capHeight ))
    path.lineTo((0, 0 ))
    path.lineTo((glyphWidth / 2, 0))
    
    
    path.closePath()
    
    
    
    # INSIDE COUNTER 
    
    path.moveTo((glyphWidth/2, thickness))
    
    path.qCurveTo(
        
        (glyphWidth/2 + handleX/propNumb, thickness),
        (onx-thickness, capHeight/2 - handleY/propNumb),
        (onx-thickness, capHeight/2 + handleY/propNumb),                
        (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
        (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),
        (thickness*2, capHeight/2 + handleY/propNumb),
        (thickness*2, capHeight/2 - handleY/propNumb),
        (glyphWidth/2 - handleX/propNumb, thickness),
        (glyphWidth/2 , thickness),

        )
    
    path.closePath()
    

    


    
    
    return path






def draw_C():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 3) * roundness
    handleY = (capHeight ) * roundness / 2 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY     
    
        
    path.moveTo((glyphWidth/ 2, 0))

    path.qCurveTo( 
        (glyphWidth/2 - handleX, 0),
        (thickness, capHeight/2- handleY),
        (thickness, capHeight/2 + handleY),                
        (glyphWidth/ 2 - handleX, capHeight),
        (glyphWidth/2, capHeight)
)
    
    path.lineTo((0, capHeight ))
    path.lineTo((0, 0 ))
    path.lineTo((glyphWidth / 2, 0))
    
    
    path.closePath()
    
    path.moveTo((glyphWidth/ 2, 0))

    path.qCurveTo(
        
        
        (glyphWidth/2 + handleX, 0), 
        (onx, capHeight/2 - handleY),
          
        )
    path.lineTo((onx-thickness, capHeight/2 - handleY ))
    path.qCurveTo(
        
        
        # (onx-thickness, ony - 2*handleY/propNumb),
        (glyphWidth/2 + handleX/propNumb, thickness),
        (glyphWidth/2 - handleX/propNumb, thickness),
        
        (thickness*2, capHeight/2 - handleY/propNumb),
        (thickness*2, capHeight/2+ handleY/propNumb),

        
        (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),               
        (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
        
               
        (onx-thickness, capHeight/2 + handleY), 
        
    )

    path.lineTo((onx, capHeight/2+ handleY ))
    
    path.qCurveTo(
        
        (glyphWidth/2 + handleX, capHeight),
        (glyphWidth/2 , capHeight)
        
               
        )

    
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth,0))
    
    
    path.closePath()
    

    
    points2 = [
        
        (onx-thickness, ony - handleY ),
        
        
        
        # (onx-thickness, ony - 2*handleY/propNumb),
        (glyphWidth/2 + handleX/propNumb, thickness),
        (glyphWidth/2 - handleX/propNumb, thickness),
        
        (thickness*2, ony - handleY/propNumb),
        (thickness*2, ony + handleY/propNumb),

        
        (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),               
        (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
        
               
        (onx-thickness, ony + 2*handleY/propNumb),
        
        
            ]


    
    
    
    
    stroke(None)
     
    return path








def draw_D():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 3) * roundness
    handleY = (capHeight ) * roundness / 2 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY     
    
    path.moveTo((thickness * 2, 0))
    path.lineTo((thickness*3, 0 ))
    path.qCurveTo(
        
        # here maybe the point where the curve begins could be independent from multiplying thickness
        
        (thickness * 3 + handleX, 0),
        (onx, capHeight/2 - handleY),
        (onx, capHeight/2 + handleY),                
        (thickness * 3 + handleX, capHeight),
        (thickness * 3, capHeight)
        
        )
    
    path.lineTo((glyphWidth, capHeight ))
    path.lineTo((glyphWidth, 0 ))
    path.lineTo((thickness * 2, 0))
    
    
    path.closePath()
    
    # INSIDE COUNTER 
    path.moveTo((thickness * 2, thickness))
    path.lineTo((thickness * 3 , thickness))
    path.qCurveTo(
        (thickness * 3 + handleX/propNumb, thickness),
        (onx-thickness, capHeight/2 - handleY/propNumb),
        (onx-thickness, capHeight/2 + handleY/propNumb),                
        (thickness * 3 + handleX/propNumb, capHeight-thickness),
        (thickness * 3, capHeight-thickness)
        )
    path.lineTo((thickness * 2, capHeight-thickness))
    
    path.closePath()
   

    
   
            
    return path


    
    
    


    
    
    


def draw_P():
    
    path = BezierPath()
    
    left_margin(path)
    fill(1)

    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 3) * roundness
    handleY = (capHeight - middleY) * roundness / 2 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY + (capHeight - middleY) / 2    
    
    path.moveTo((thickness * 2, 0))
    path.lineTo((thickness * 2, capHeight * middleLine - thickness / 2))
    path.lineTo((thickness * 3, capHeight * middleLine - thickness / 2))
    
    path.qCurveTo(
        (thickness * 3 + handleX, middleY),
        (onx, ony - handleY),
        (onx, ony + handleY),                
        (thickness * 3 + handleX, capHeight),
        (thickness * 3, capHeight)
        )
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth, 0))
    path.closePath()
    
    path.moveTo((thickness * 2, capHeight * middleLine + thickness / 2))
    path.lineTo((thickness * 3, capHeight * middleLine + thickness / 2))
    path.qCurveTo(
        (thickness * 3 + handleX/propNumb, middleY+thickness),
        (onx-thickness, ony - handleY/propNumb),
        (onx-thickness, ony + handleY/propNumb),                
        (thickness * 3 + handleX/propNumb, capHeight-thickness),
        (thickness * 2, capHeight-thickness)
        )
    path.closePath()
    return path    

def draw_B():
    
    path = BezierPath()
    left_margin(path)
    fill(1)

    # calculate the middle Y position
    middleY = (capHeight * middleLine) - thickness / 2
    # calculate the max lenght of the handles
    handleX = (glyphWidth - thickness * 3) * roundness
    handleY = (capHeight - middleY) * roundness / 2 
    # calculate the extreme point on the right
    onx = glyphWidth - thickness
    ony = middleY + (capHeight - middleY) / 2   
    ony2 = 0 + (capHeight - middleY) / 2 
    
    
    path.moveTo((thickness * 2, 0))
    path.lineTo((thickness*3,0))
    
    path.qCurveTo(
        
        (thickness * 3 + handleX, 0),
        (onx, ony2 - handleY),
        (onx, ony2 + handleY), 
        (thickness * 4 + handleX/2, capHeight*middleLine),
        )
    path.qCurveTo(
        (thickness * 4 + handleX/2, capHeight*middleLine),
        (onx, ony - handleY),
        (onx, ony + handleY),                
        (thickness * 3 + handleX, capHeight),
        (thickness * 3, capHeight)
        )
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth, 0))

    path.closePath()
    # SMALL COUNTERS 
    
    path.moveTo((thickness * 2, capHeight * middleLine + thickness / 2))
    path.lineTo((thickness * 3, capHeight * middleLine + thickness / 2))
    
    path.qCurveTo(
        (thickness * 3 + handleX/propNumb, middleY+thickness),
        (onx-thickness, ony - handleY/propNumb),
        (onx-thickness, ony + handleY/propNumb),                
        (thickness * 3 + handleX/propNumb, capHeight-thickness),
        (thickness * 2, capHeight-thickness)
        )
    
    path.closePath()
        # SMALL BOTTOM 
    path.moveTo((thickness * 2, thickness))
    path.lineTo((thickness * 3, thickness))
    path.qCurveTo(
        (thickness * 3 + handleX/propNumb, thickness),
        (onx-thickness, ony2 - handleY/propNumb),
        (onx-thickness, ony2 + handleY/propNumb),                
        (thickness * 3 + handleX/propNumb, (capHeight * middleLine)- thickness / 2),
        (thickness * 2, (capHeight * middleLine)- thickness / 2)
        )
        
    path.closePath()
    return path


def draw_A():
    
    middleY = (capHeight * middleLine) - thickness / 2
    path = BezierPath()
    left_margin(path)
    fill(1)
    

    
    path.moveTo((thickness, 0))   
    path.lineTo((glyphWidth/2-thickness, capHeight))
    path.lineTo((0, capHeight))
    path.closePath()
    
    path.moveTo((glyphWidth-thickness, 0))
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth/2+thickness, capHeight))
    path.closePath()
    
    
    diffxLeft = (glyphWidth/2-thickness) - thickness
    diffyLeft = capHeight 
    
    diffxRight = (glyphWidth/2+thickness) - (glyphWidth-thickness)
    diffyRight = capHeight
    
    path.closePath()
    
    path.moveTo((thickness + diffxLeft * middleLine + thickness, diffyLeft * middleLine ))
    path.lineTo((glyphWidth-thickness + diffxRight * middleLine - thickness, diffyRight * middleLine))
    
    path.lineTo((glyphWidth - thickness * 2, 0))
    path.lineTo((thickness * 2, 0))
    
    path.closePath()
    
    thicknessFactor = thickness / capHeight
    
    path.moveTo((glyphWidth / 2, capHeight))
    path.lineTo((glyphWidth-thickness + diffxRight * (middleLine+thicknessFactor) - thickness, diffyRight * (middleLine+thicknessFactor)))
    path.lineTo((thickness + diffxLeft * (middleLine+thicknessFactor) + thickness, diffyLeft * (middleLine+thicknessFactor)))
    path.closePath()



    return path


def draw_M():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    path.closePath()
    
    path.moveTo((2*thickness+thickness/propNumb, capHeight))
    path.lineTo((glyphWidth-2*thickness-thickness/propNumb, capHeight))
    path.lineTo((glyphWidth/2, 2*thickness))
    path.closePath()

    
    path.moveTo((glyphWidth-2*thickness,0))
    path.lineTo((glyphWidth-2*thickness, capHeight -propNumb*thickness))
    path.lineTo((glyphWidth/2 + thickness/2, thickness))
    path.lineTo((glyphWidth/2 - thickness/2, thickness))
    path.lineTo((2*thickness, capHeight -propNumb*thickness))
    path.lineTo((2*thickness, 0))
    path.closePath()
    
        
    return path

def draw_V():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    
    
    path.moveTo((thickness+thickness*propNumb, capHeight))
    path.lineTo((glyphWidth-thickness -thickness*propNumb, capHeight))
    path.lineTo((glyphWidth/2, thickness*propNumb))
    path.closePath()

    
    path.moveTo((glyphWidth,0))
    path.lineTo((glyphWidth,capHeight))
    path.lineTo((glyphWidth-thickness, capHeight))
    path.lineTo((glyphWidth/2 + thickness/2, 0))
    path.closePath()
    path.moveTo((glyphWidth/2 - thickness/2, 0))
    path.lineTo((thickness, capHeight ))
    path.lineTo((thickness, 0))
    path.closePath()
    
    return path

def draw_W():
    path = BezierPath()
    left_margin(path)
    fill(1)
    
    # leftpart
    path.moveTo((glyphWidth/4 - thickness/2, 0))    
    path.lineTo((thickness, 0))
    path.lineTo((thickness, capHeight))
    path.closePath()
    
    # rightblock
    path.moveTo((glyphWidth-(glyphWidth/4 - thickness/2), 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    path.closePath()
    
    # bottom part
    path.moveTo((glyphWidth/4 + thickness, 0))
    path.lineTo((glyphWidth*3/4 - thickness, 0))
    path.lineTo((glyphWidth/2, capHeight-2*thickness-propNumb*thickness))
    path.closePath()

    # top part
    
    path.moveTo((glyphWidth-2*thickness,capHeight))
    path.lineTo((glyphWidth-(1/4*glyphWidth + thickness*1/4), propNumb*thickness))
    path.lineTo((glyphWidth/2 + thickness/2, capHeight-thickness))
    path.lineTo((glyphWidth/2 - thickness/2, capHeight-thickness))
    path.lineTo((1/4*glyphWidth + thickness*1/4, propNumb*thickness))
    path.lineTo((2*thickness, capHeight))
    path.closePath()
    
        
    return path
    


# def draw_W2():
#     path = BezierPath()
#     left_margin(path)
    
    
    
#     path.moveTo((thickness+thickness*propNumb, capHeight))
#     path.lineTo((glyphWidth-thickness -thickness*propNumb, capHeight))
#     path.lineTo((glyphWidth/2, thickness*propNumb))
#     path.closePath()

    
#     path.moveTo((glyphWidth,0))
#     path.lineTo((glyphWidth,capHeight))
#     path.lineTo((glyphWidth-thickness, capHeight))
#     path.lineTo((glyphWidth- glyphWidth/4 + thickness/2, 0))
#     path.closePath()
    
#     path.moveTo((glyphWidth/4 - thickness/2, 0))
#     path.lineTo((thickness, capHeight ))
#     path.lineTo((thickness, 0))
#     path.closePath()
    
        
#     return path





settings = [
    #thickness, middleLine, roundness, propNumb
    # (12, 0.519, 0.395, 1.9)
    # (66, 0.519, 1.795, 1.9),
    # (66, 0.3,   3.795, .5)
    # (6,  0.489, 0.319, 1.36),
    # (6,  0.489, 0.319, -1.36),
        # (-7, 0.217, 0.94, 1.4),
    # (-8, 0.527, 0.524, 270),
    # (30,  0.52, -2.319, 0.36)
    # (60,  0.52, -3.319, 0.36)
    
    # thickness, middleLine, roundness, propNumb
    # combinations of t:r:m:p
    
    # (1,  0.1,    0.01,  0.1),
    # (1,  1,      0.01,  0.1),
    # (1,  0.1,    4,     0.1),
    # (1,  1,      4,     0.1),
    
    # (94,  0.1,   0.01,  0.1),
    # (94,  1,     0.01,  0.1),
    # (94,  0.1,   4,     0.1),
    # (94,  1,     4,     0.1),
    
    # (1,   0.1,   0.01,  200),
    # (1,   1,     0.01,  200),
    # (1,   0.1,   4,     200),
    # (1,   1,     4,     200),
    
    # (94,  0.1,   0.01,  200),
    # (94,  1,     0.01,  200),
    # (94,  0.1,   4,     200),
    (94,  1,     4,     200)
    
    # (94,  0.517, 0.319, 1.36)

    
  
]

settings.append(settings[0])

frames = 1

lines = [
    (draw_C, draw_A, draw_B, draw_G, draw_E, draw_M, draw_V),    
    (draw_V, draw_F, draw_M, draw_N, draw_L, draw_A, draw_N),
    (draw_I, draw_P, draw_T, draw_H, draw_Z, draw_A, draw_T),
    (draw_T, draw_W, draw_O, draw_N, draw_L, draw_S, draw_U)
]


startThickness, startMiddleLine, startRoundness, startPropNumb = settings[0]

for nextThickness, nextMiddleLine, nextRoundness, nextPropNumb in settings[1:]:

    for i in range(frames):
        factor = i / frames
    
        thickness = startThickness + (nextThickness-startThickness) * factor
        middleLine = startMiddleLine + (nextMiddleLine-startMiddleLine) * factor
        roundness = startRoundness + (nextRoundness-startRoundness) * factor
        propNumb = startPropNumb + (nextPropNumb-startPropNumb) * factor
    
    
        if propNumb == 0:
            propNumb = 0.000001

        newPage(glyphWidth * 7, capHeight * len(lines))
        translate(0, height()-capHeight)

        for line in lines:
            with savedState():
               for func in line:
                    path = func()
                    drawPath(path)
                    translate(glyphWidth)
            translate(0, -capHeight)


    startThickness = nextThickness
    startMiddleLine = nextMiddleLine
    startRoundness = nextRoundness
    startPropNumb = nextPropNumb


# saveImage("twon12.gif")



scaleFactor = 2

clipBox = BezierPath()
clipBox.rect(10, 10, 500, 500)

f = CurrentFont()

namespace = globals()

for name in sorted(namespace.keys()):
    if name.startswith("draw_"):
        glyphName = name[5:]
        print(glyphName)
        
        func = namespace[name]
        path = func()
        path.scale(scaleFactor)
        
        clippedPath = path 

        g = f[glyphName]
        g.clear()
        clippedPath.drawToPen(g.getPen())
        g.width = glyphWidth * scaleFactor

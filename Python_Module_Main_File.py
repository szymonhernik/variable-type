
glyphWidth = 290
capHeight = 288

thickness = 66
middleLine = -0.001 
roundness = 1.775
# Create propNumb different for handleX and handle Y
propNumb = 1.9 
diagonalExtra = 4.61





def left_margin(path):
    
    with savedState():
        # set a color
        fill(1)
        # do a transformation
        # draw something
        rect(0, 0, glyphWidth, capHeight)
    
    path.moveTo((0, 0))
    path.lineTo((thickness, 0))
    path.lineTo((thickness, capHeight))
    path.lineTo((0, capHeight))
    path.closePath()
    
def draw_Z():
    path = BezierPath()
    left_margin(path)
    
    
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
    
       
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)


def draw_N():
    path = BezierPath()
    left_margin(path)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    
    path.moveTo((glyphWidth-2*thickness-thickness/propNumb,0))
    path.lineTo((2*thickness, capHeight -propNumb*thickness))
    path.lineTo((2*thickness, 0))
    path.closePath()
    
    path.moveTo((2*thickness+thickness/propNumb, capHeight))
    path.lineTo((glyphWidth-2*thickness, capHeight))
    path.lineTo((glyphWidth-2*thickness, propNumb*thickness))
    path.closePath()
    
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)

def draw_M():
    path = BezierPath()
    left_margin(path)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    
    path.moveTo((2*thickness+thickness/propNumb, capHeight))
    path.lineTo((glyphWidth-2*thickness-thickness/propNumb, capHeight))
    path.lineTo((glyphWidth/2, propNumb*thickness))
    path.closePath()

    
    path.moveTo((glyphWidth-2*thickness-thickness/propNumb,0))
    path.lineTo((2*thickness, capHeight -propNumb*thickness))
    path.lineTo((2*thickness, 0))
    path.closePath()
    
        
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)

def draw_U():
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
    
    
    stroke(0)
    fill(0)
    drawPath(path)
    
    points2 = [
        (glyphWidth/2 + handleX/propNumb, thickness),
        (onx-thickness, capHeight/2 - handleY/propNumb),
        # (onx-thickness, capHeight/2 + handleY/propNumb),                
        # (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
        # (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),
        # (thickness*2, capHeight/2 + handleY/propNumb),
        (thickness*2, capHeight/2 - handleY/propNumb),
        (glyphWidth/2 - handleX/propNumb, thickness),
        (glyphWidth/2 , thickness),
    ]


    points = [
        
        
        
        (glyphWidth/ 2, 0),
        (glyphWidth/2 + handleX, 0),
        (onx, ony - handleY),
        (onx, ony + handleY),                
        (glyphWidth/ 2 + handleX, capHeight),
        (glyphWidth/2, capHeight)
    ]
    points3 = [
        
        
        
        (glyphWidth/ 2, 0),
        (glyphWidth/2 - handleX, 0),
        (0, ony - handleY),
        (0, ony + handleY),                
        (glyphWidth/ 2 - handleX, capHeight),
        (glyphWidth/2, capHeight)
    ]
    
    
    # stroke(None)
    
    # fill(0, 1, 0)
    # dotSize = 10
    # for x, y in points:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
    # fill(0, 0, 1)
    # dotSize = 10
    # for x, y in points3:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
        
    # fill(1, 0, 1)
    # dotSize = 10
    # for x, y in points2:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)

    
    
   
            
    translate(glyphWidth)




def draw_S():
    path = BezierPath()
    left_margin(path)
    
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
    
    
    stroke(0)
    fill(0)
    drawPath(path)
    
    points2 = [
        
        (glyphWidth/2 - handleX, 0),
        (thickness, capHeight/2 - handleY),
        (2*thickness, capHeight*1/4 - handleY/propNumb),
        (glyphWidth/ 2 - handleX/propNumb, thickness),
        (glyphWidth/ 2 + handleX/propNumb, thickness),
        (glyphWidth-2*thickness, capHeight*1/4 - handleY/propNumb),
        (glyphWidth-2*thickness, capHeight*1/4 + handleY/propNumb),
        (thickness, capHeight*3/4 - handleY/propNumb),
        (thickness, capHeight*3/4 + handleY/propNumb),
        (glyphWidth/2 - handleX, capHeight)
        
        
            ]


    points = [
        (glyphWidth/ 2, 0),
        (glyphWidth/2 + handleX, 0),
        (onx, ony - handleY)  ,
        (onx, ony + 2*handleY/propNumb ),
        (glyphWidth/ 2 + handleX, capHeight),
        (glyphWidth/2, capHeight) ,
        (glyphWidth, capHeight),
        (glyphWidth, 0)
        
        
    ]
    
    points3 = [
        (onx, ony )
        
        ]
    
    
    
    
    stroke(None)
    
    fill(0, 1, 0)
    dotSize = 10
    # for x, y in points2:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
           
    # fill(1, 0, 1)
    # dotSize = 10
    # for x, y in points2:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)

    
    
   
            
    translate(glyphWidth)







def draw_H():
    path = BezierPath()
    left_margin(path)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    
    path.moveTo((glyphWidth - thickness*2, 0))  
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine - thickness / 2))
    path.lineTo(( thickness*2, capHeight * middleLine - thickness / 2))
    path.lineTo((thickness*2 , 0))
    
    path.moveTo((glyphWidth - thickness*2, capHeight))  
    path.lineTo((glyphWidth - thickness*2, capHeight * middleLine + thickness / 2))
    path.lineTo(( thickness*2, capHeight * middleLine + thickness / 2))
    path.lineTo((thickness*2 , capHeight))
    
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)
    
def draw_I():
    path = BezierPath()
    left_margin(path)
    
    path.moveTo((thickness*2, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((thickness*2, capHeight))
    path.closePath()
        
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)

def draw_L():
    path = BezierPath()
    left_margin(path)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((thickness*2, capHeight))
    path.lineTo((thickness*2, thickness))
    path.lineTo((glyphWidth-thickness, thickness))
    path.closePath()
        
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)

def draw_T():
    path = BezierPath()
    left_margin(path)
    
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
        
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)


def draw_E():
    path = BezierPath()
    left_margin(path)
    
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
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)

def draw_F():
    path = BezierPath()
    left_margin(path)
    
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
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)


def draw_O():
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
    
    
    stroke(0)
    fill(0)
    drawPath(path)
    
    points2 = [
        (glyphWidth/2 - handleX/propNumb, thickness),
        (glyphWidth/2 + handleX/propNumb, thickness),
        (onx-thickness, ony - handleY/propNumb),
        (onx-thickness, ony + handleY/propNumb),                
        (glyphWidth/ 2 + handleX/propNumb, capHeight-thickness),
        (glyphWidth/ 2 - handleX/propNumb, capHeight-thickness),
        (thickness*2, ony - handleY/propNumb),
        (thickness*2, ony + handleY/propNumb),
    ]


    points = [
        
        
        
        (glyphWidth/ 2, 0),
        (glyphWidth/2 + handleX, 0),
        (onx, ony - handleY),
        (onx, ony + handleY),                
        (glyphWidth/ 2 + handleX, capHeight),
        (glyphWidth/2, capHeight)
    ]
    points3 = [
        
        
        
        (glyphWidth/ 2, 0),
        (glyphWidth/2 - handleX, 0),
        (0, ony - handleY),
        (0, ony + handleY),                
        (glyphWidth/ 2 - handleX, capHeight),
        (glyphWidth/2, capHeight)
    ]
    
    
    # stroke(None)
    
    # fill(0, 1, 0)
    # dotSize = 10
    # for x, y in points:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
    # fill(0, 0, 1)
    # dotSize = 10
    # for x, y in points3:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
        
    # fill(1, 0, 1)
    # dotSize = 10
    # for x, y in points2:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)

    
    
   
            
    translate(glyphWidth)






def draw_C():
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
    
    
    stroke(0)
    fill(0)
    drawPath(path)
    
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


    points = [
        (glyphWidth/ 2, 0),
        (glyphWidth/2 + handleX, 0),
        (onx, ony - handleY)  ,
        (onx, ony + 2*handleY/propNumb ),
        (glyphWidth/ 2 + handleX, capHeight),
        (glyphWidth/2, capHeight) ,
        (glyphWidth, capHeight),
        (glyphWidth, 0)
        
        
    ]
    
    points3 = [
        (onx, ony )
        
        ]
    
    
    
    
    stroke(None)
    
    # fill(0, 1, 0)
    # dotSize = 10
    # for x, y in points3:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
           
    # fill(1, 0, 1)
    # dotSize = 10
    # for x, y in points2:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)

    
    
   
            
    translate(glyphWidth)








def draw_D():
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
    
    
    stroke(0)
    fill(0)
    drawPath(path)

    # INSIDE COUNTER points
    points = [
        (thickness * 2, thickness),
        (thickness * 3 , thickness),
        (thickness * 3 + handleX, thickness),
        (onx-thickness, middleY - handleY),
        (onx-thickness, middleY + handleY),                
        (thickness * 3 + handleX, capHeight-thickness),
        (thickness * 3, capHeight-thickness),
        (thickness * 2, capHeight-thickness)
        
    ]
    points2 = [
        (thickness * 2, 0),
        (thickness * 2 + handleX, 0),
        (onx, ony - handleY),
        (onx, ony + handleY),                
        (thickness * 2 + handleX, capHeight),
        (thickness * 2, capHeight)
    ]
    points3 = [
        (thickness*2, 0 ),
        (thickness*3, 0 ),
        (thickness * 3 + handleX, 0),
        (onx, ony - handleY),
        (onx, ony + handleY),                
        (thickness * 3 + handleX, capHeight),
        (thickness * 3, capHeight),    
        (thickness * 2, capHeight)   
        ]
    
    
    stroke(None)
    
    fill(0, 1, 0)
    dotSize = 10
    # for x, y in points:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
    
    
   
            
    translate(glyphWidth)


    
    
    


    
    
    


def draw_P():
    
    path = BezierPath()
    
    left_margin(path)

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
    
        
    stroke(0)
    fill(0)
    drawPath(path)
   
            
    translate(glyphWidth)
    
def draw_B():
    
    path = BezierPath()
    left_margin(path)

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
    stroke(0)
    fill(0)
    drawPath(path)
    
    points3 = [
        (thickness * 2, 0),
        (thickness * 2 + handleX, 0),
        (onx, ony2 - handleY),
        (onx, ony2 + handleY),
     
        (thickness * 3 + handleX/2, capHeight/2),
        (onx, ony - handleY),
        (onx, ony + handleY),                
        (thickness * 2 + handleX, capHeight),
        (thickness * 2, capHeight)
    ]
    
    points2 = [
        (thickness * 2 + handleX/propNumb, thickness),
        (onx-thickness, ony2 - handleY/propNumb),
        (onx-thickness, ony2 + handleY/propNumb),                
        (thickness * 2 + handleX/propNumb, (capHeight * middleLine)),
        (thickness * 2, (capHeight * middleLine))
    ]
    points = [
        (thickness * 2 + handleX/propNumb, middleY+thickness),
        (onx-thickness, ony - handleY/propNumb),
        (onx-thickness, ony + handleY/propNumb),                
        (thickness * 2 + handleX/propNumb, capHeight-thickness),
        (thickness * 2, capHeight-thickness)
    ]
    
    
    stroke(None)
    
    fill(0, 1, 0)
    dotSize = 10
    # for x, y in points2:
        
    #     oval(x-dotSize, y-dotSize, dotSize*2, dotSize*2)
    
  
        
    translate(glyphWidth)


def draw_A():
    
    middleY = (capHeight * middleLine) - thickness / 2
    path = BezierPath()
    left_margin(path)
    

    
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
    
    path.moveTo((thickness + diffxLeft * middleLine + thickness, diffyLeft * middleLine ))
    path.lineTo((glyphWidth-thickness + diffxRight * middleLine - thickness, diffyRight * middleLine))
    
    path.lineTo((glyphWidth - thickness * 2, 0))
    path.lineTo((thickness * 2, 0))
    
    
    thicknessFactor = thickness / capHeight
    
    path.moveTo((glyphWidth / 2, capHeight))
    path.lineTo((glyphWidth-thickness + diffxRight * (middleLine+thicknessFactor) - thickness, diffyRight * (middleLine+thicknessFactor)))
    path.lineTo((thickness + diffxLeft * (middleLine+thicknessFactor) + thickness, diffyLeft * (middleLine+thicknessFactor)))
    path.closePath()

    
    
    
    #path.lineTo((glyphWidth-thickness*2, capHeight))
    #path.lineTo((glyphWidth-thickness, 0))
    #path.lineTo((glyphWidth, 0))
    #path.lineTo((glyphWidth, capHeight))
    #path.lineTo((0, capHeight))
    #path.lineTo((0, 0))
    
    #path.moveTo((thickness*2, 0))
    #path.lineTo((glyphWidth/2, middleY))
    
    path.closePath()
    
    stroke(0)
    
    fill(0)
    drawPath(path)
    translate(glyphWidth)

# def draw_M():
    
#     middleY = (capHeight * middleLine) - thickness / 2
#     path = BezierPath()
#     left_margin(path)
    

    
    
    
#     path.moveTo((glyphWidth-thickness, 0))
#     path.lineTo((glyphWidth, 0))
#     path.lineTo((glyphWidth, capHeight))
#     path.lineTo((glyphWidth-thickness, capHeight))
#     path.closePath()
    
    
#     diffxLeft = (glyphWidth/2-thickness) - thickness
#     diffyLeft = capHeight 
    
#     diffxRight = (glyphWidth/2+thickness) - (glyphWidth-thickness)
#     diffyRight = capHeight
    
#     path.moveTo((thickness * 2, 0))
#     path.lineTo((thickness*2,(capHeight-2*thickness)))
#     path.lineTo((thickness + diffxLeft * middleLine + thickness, diffyLeft * middleLine ))
#     path.lineTo((glyphWidth-thickness + diffxRight * middleLine - thickness, diffyRight * middleLine))
#     path.lineTo((glyphWidth-thickness*2,(capHeight-2*thickness)))
    
#     path.lineTo((glyphWidth - thickness * 2, 0))
    
    
    
#     thicknessFactor = thickness / capHeight
    
#     path.moveTo((thickness*2, capHeight))
#     path.lineTo((glyphWidth-thickness + diffxRight * (middleLine+thicknessFactor) - thickness, diffyRight * (middleLine+thicknessFactor)))
#     path.lineTo((thickness + diffxLeft * (middleLine+thicknessFactor) + thickness, diffyLeft * (middleLine+thicknessFactor)))
#     path.closePath()

    
    
    
#     path.lineTo((glyphWidth-thickness*2, capHeight))
#     path.lineTo((glyphWidth-thickness, 0))
#     path.lineTo((glyphWidth, 0))
#     path.lineTo((glyphWidth, capHeight))
#     path.lineTo((0, capHeight))
#     path.lineTo((0, 0))
    
#     path.moveTo((thickness*2, 0))
#     path.lineTo((glyphWidth/2, middleY))
    
#     path.closePath()
    
#     stroke(0)
    
#     fill(0)
#     drawPath(path)
#     translate(glyphWidth)    

def draw_M():
    path = BezierPath()
    left_margin(path)
    
    path.moveTo((glyphWidth - thickness, 0))    
    path.lineTo((glyphWidth, 0))
    path.lineTo((glyphWidth, capHeight))
    path.lineTo((glyphWidth - thickness, capHeight))
    
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
    
        
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)

def draw_V():
    path = BezierPath()
    left_margin(path)
    
    
    
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
    
        
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)

def draw_W():
    path = BezierPath()
    left_margin(path)
    
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
    
        
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)
    


def draw_W2():
    path = BezierPath()
    left_margin(path)
    
    
    
    path.moveTo((thickness+thickness*propNumb, capHeight))
    path.lineTo((glyphWidth-thickness -thickness*propNumb, capHeight))
    path.lineTo((glyphWidth/2, thickness*propNumb))
    path.closePath()

    
    path.moveTo((glyphWidth,0))
    path.lineTo((glyphWidth,capHeight))
    path.lineTo((glyphWidth-thickness, capHeight))
    path.lineTo((glyphWidth- glyphWidth/4 + thickness/2, 0))
    path.closePath()
    
    path.moveTo((glyphWidth/4 - thickness/2, 0))
    path.lineTo((thickness, capHeight ))
    path.lineTo((thickness, 0))
    path.closePath()
    
        
    
    stroke(0)
    fill(0)
    drawPath(path)
    translate(glyphWidth)





settings = [
    #thickness, middleLine, roundness, propNumb
    (12, 0.519, 0.395, 1.9),
    (66, 0.519, 1.795, 1.9),
    (66, 0.3,   3.795, .5),
    (6,  0.489, 0.319, 1.36),
    (6,  0.489, 0.319, -1.36),
    (34,  0.517, 0.319, 1.36),
    (-7, 0.217, 0.94, 1.4),
    (-8, 0.527, 0.524, 270),
    (30,  0.52, -2.319, 0.36)
    # (60,  0.52, -3.319, 0.36)
    
  
]

settings.append(settings[0])

frames = 20

lines = [
    (draw_C, draw_A, draw_B, draw_D, draw_E, draw_M, draw_V),
    
    
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
                    func()
            translate(0, -capHeight)


    startThickness = nextThickness
    startMiddleLine = nextMiddleLine
    startRoundness = nextRoundness
    startPropNumb = nextPropNumb


saveImage("twon12.gif")





# Letter-Studio-Python-Process
# Gif and more of chosen combinations.

## Animated combinations of letters

![Letters animation Python Scripting .gif format](all3.gif)

## Single Letters

```python
for i in range(frames):
  factor = i / frames
        
  thickness = startThickness + (nextThickness-startThickness) * factor
  middleLine = startMiddleLine + (nextMiddleLine-startMiddleLine) * factor
  roundness = startRoundness + (nextRoundness-startRoundness) * factor
  propNumb = startPropNumb + (nextPropNumb-startPropNumb) * factor
        
        
  if propNumb == 0:
  propNumb = 0.000001
    
  newPage(glyphWidth , capHeight/4 * len(lines))
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

```


<img src="S8.gif" alt="Single letter animation py script" width="250" float="left">
<img src="gif14_b.gif" alt="Single letter animation py script" width="250">
<img src="C.gif" alt="Single letter animation py script" width="250">


## Presentation of the letters which don't include circular shapes. That demonstrates how it does look without letters overlapping much and without the contrast added by the way the circularly shaped latters behave. 

![](twon14.gif)


## One other animated combination

![](twon7.gif)


### Archive of chosen combinations

![](/chosen/2.jpg)
![](/chosen/3.jpg)
![](/chosen/4.jpg)
![](/chosen/5.jpg)
![](/chosen/6.jpg)
![](/chosen/7.jpg)
![](/chosen/8.jpg)
![](/chosen/9.jpg)
![](/chosen/10.jpg)
![](/chosen/11.jpg)
![](/chosen/12.jpg)
![](/chosen/13.jpg)
![](/chosen/14.jpg)
![](/chosen/15.jpg)
![](/chosen/16.jpg)
![](/chosen/17.jpg)
![](/chosen/18.jpg)
![](/chosen/19.jpg)
![](/chosen/20.jpg)
![](/chosen/21.jpg)
![](/chosen/22.jpg)
![](/chosen/23.jpg)
![](/chosen/24.jpg)
![](/chosen/25.jpg)
![](/chosen/26.jpg)
![](/chosen/twon12.jpg)

## Test with changing the size of the page

![](twonl-test-changing-pageSize.gif)


## Test with changing the width and height of the glyphs

![](twonl-test-changing-glyph-width-and-height.gif)




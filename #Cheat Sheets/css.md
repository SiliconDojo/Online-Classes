# CSS Cheat Sheet


## Bounding Boxes

This creates a DIV Box that contains a picture.  On the picture a 10px by 10px Bounding Box is drawn that starts 5px from the top, and 5px from the left.

```
<div style="position:relative; border:5px solid black; height:200px; width:200px;">
<img src="./picture.jpg">
<div style="position:absolute; border:3px solid red; height:10px; width:10px; top:5px; left:5px;"></div>
</div>
```

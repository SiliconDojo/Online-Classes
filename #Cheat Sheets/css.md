# CSS Cheat Sheet


## Bounding Boxes

This creates a DIV Box that contains a picture.  On the picture a 10px by 10px Bounding Box is drawn that starts 5px from the top, and 5px from the left.

```
<div style="position:relative; border:5px solid black; height:200px; width:200px;">
<img src="./picture.jpg">
<div style="position:absolute; border:3px solid red; height:10px; width:10px; top:5px; left:5px;"></div>
</div>
```

## Caption DIV Box

This creates a caption on the DIV Box 5px from the bottom and 5px from the left. This can be used to caption images.

```
<div style="position:relative; border:5px solid black; height:200px; width:200px;">
<div style="position:absolute; bottom:5px; left:5px;">
    <p>hello world</p>
</div>
</div>
```

## Inline Responsive DIV - display:inline-block

This makes the DIV boxes be displayed inline, and they regroup as the page is resized

```
<div style="border:5px solid red;">
<div style="display:inline-block;border:5px solid black; height:200px; width:200px;"></div>
<div style="display:inline-block;border:5px solid black; height:200px; width:200px;"></div>
<div style="display:inline-block;border:5px solid black; height:200px; width:200px;"></div>
<div style="display:inline-block;border:5px solid black; height:200px; width:200px;"></div>
<div style="display:inline-block;border:5px solid black; height:200px; width:200px;"></div>
<div style="display:inline-block;border:5px solid black; height:200px; width:200px;"></div>
</div>
```

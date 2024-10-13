# CSS Cheat Sheet


## Bounding Boxes

This creates a DIV Box that contains a picture.  On the picture a 150px by 150px Bounding Box is drawn that starts 200px from the top, and 210px from the left.

<img width="650" alt="Screenshot 2024-10-13 at 10 33 17 AM" src="https://github.com/user-attachments/assets/713d3410-5a61-4929-9a03-0af3d77e6c7c">


```
<div style="position:relative;">
    <img src="./picture.jpg">
    <div style="position:absolute; border:3px solid red; height:150px; width:150px; top:200px; left:210px;"></div>
</div>
```

## Caption DIV Box

This creates a caption on the DIV Box 400px from the top and 10px from the left. This can be used to caption images.

<img width="646" alt="Screenshot 2024-10-13 at 10 43 09 AM" src="https://github.com/user-attachments/assets/df1e29d0-f1fd-41cc-9746-1e2ec305f102">

```
div style="position:relative;">
    <img src="./picture.jpg">
    <div style="position:absolute; background-color:lightgray;top:400px; left:10px;">
        <p>
            This is a cute puppy
        </p>
    </div>
</div>
```

## Inline Responsive DIV - display:inline-block

This makes the DIV boxes be displayed inline, and they regroup as the page is resized

<img width="400" alt="Screenshot 2024-10-13 at 10 21 49 AM" src="https://github.com/user-attachments/assets/4294aee7-ce44-4020-a7b8-e58a7b015c3b">


<img width="200" alt="Screenshot 2024-10-13 at 10 21 37 AM" src="https://github.com/user-attachments/assets/6ae55bdf-a229-4680-ae2d-8174f4960589">

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

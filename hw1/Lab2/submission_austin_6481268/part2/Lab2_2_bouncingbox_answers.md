# Lab2_2_answers
> Austin Jetrin Maddison 6481268

### Q1
My attempt of describing the `drawBox()`. 
```js
function drawBox() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(box.x + box.width / 2, box.y + box.height / 2);
    ctx.rotate(box.angle);
    ctx.translate(-box.width / 2, -box.height / 2);
    ctx.fillStyle = '#3498db';
    ctx.fillRect(0, 0, box.width, box.height);
    ctx.restore();
}
```

1. Clear the buffer before rendering the next frame, if not previous frames will trail.
```js
ctx.clearRect(0, 0, canvas.width, canvas.height);
```
2. Seems like it saves the current state of the of the context. So when you are done performing an operation on the context that is undergone transformations you can restore it back to what it was when you saved using  `ctx.restore()`.
```js
ctx.save();
```
3. This translates the orgin matching the position of the center of the box.
```js
ctx.translate(box.x + box.width / 2, box.y + box.height / 2);
```
4. Rotates the context about its pivot.
```js
ctx.rotate(box.angle);
```
5. Since the rotation is not pivoting from center of the box we have to offset the context to give the impression that it is. 
```js
ctx.translate(-box.width / 2, -box.height / 2);
```
6. The fill style hints the context what color should be used when a fill operation is performed on the context. 
```js
ctx.fillStyle = '#3498db';
```
7. This fills the now transformed context in the contexts co-ord space. Notice that 0, 0 is the top left corner of the rect while the corresponding end points are the dimensions of the box. 

Notice that its not drawn using the canvas co-ordinate space, which would be tedious. We use a context as a so called 'model-space' to describe the box in its own context.   
```js
ctx.fillRect(0, 0, box.width, box.height);
```
8. Restore the context to its original state uncontaminate future operations to the context.
```js
ctx.restore();
```
---
### Q2
[Lab2_2_bouncingbox.html](hw1\Lab2\part2\Lab2_2_bouncingbox.html)

---
### Q3

First I give the box a color variable. I also declare a variable to track the box's rotation. If the `rotated_so_far >=  30` degree (but is compared using radians) a random color is assigned to it and the tracking variable is reset. `getRandomColor()` is borrowd from `Lab1_1bouncingball.html`.

```js

let box = {
    // ...
    color: "3498db",
    // ...
}

let rotated_so_far = 0
// ...
function updateBox() {
    // ...
    box.angle += box.rotationSpeed;
    rotated_so_far += box.rotationSpeed;
    // ... so on
    
    if(rotated_so_far >= 30/180 * Math.PI)
    {
        rotated_so_far = 0
        box.color = getRandomColor()
    }
}
```
---
### Q4
[bouncingbox3.html](hw1\Lab2\part2\bouncingbox3.html)

# Lab2_1_answers
> Austin Jetrin Maddison 6481268

### Q1
Modify code to increment and decrement ball radius.
```js
let x = canvas.width / 2; 
let y = canvas.height / 2;
let dx = 2; 
let dy = -2; 
let radius = 10; 
let color = '#ff0000';
const radius_increment_rate = 5;
const radius_decrement_rate = 5;

function drawBall() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); 
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2); 
    ctx.fillStyle = color;
    ctx.fill();
    ctx.closePath();
}

function updatePosition() {
    x += dx;
    y += dy;
    
    if (x + radius > canvas.width || x - radius < 0) {
        dx = -dx; 
        color = getRandomColor(); 
        radius -= radius_decrement_rate;
    }
    if (y + radius > canvas.height || y - radius < 0) {
        dy = -dy;
        
        dr = radius_increment_rate
        radius += dr;
        y += dr * dy
        x += dr * dx
    }
}
```


### Q2
#### Explaination:

I first make radius into a mutable variable.
```js
let radius = 10; 
```

I set increment and decrement constants for the ball radius when a collition occurs.
```js
const radius_increment_rate = 5;
const radius_decrement_rate = 5;
```

For the x-axis collision handler I decrement the radius.
```js
if (x + radius > canvas.width || x - radius < 0) {
    dx = -dx; 
    color = getRandomColor(); 
    radius -= radius_decrement_rate;
} 
```

For the y-axis collision handler I increment the radius. However this causes a feedback loop of collisions. So I apply an offset into the bounce direction propotional to the radius change.
```js
if (y + radius > canvas.height || y - radius < 0) {
    dy = -dy;
    
    dr = radius_increment_rate
    radius += dr;
    y += dr * dy
    x += dr * dx
} 
```

### Q2



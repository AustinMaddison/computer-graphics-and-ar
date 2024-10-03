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

---
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
---
### Q3
[bouncingball3.html](hw1\Lab2\part2\bouncingball3.html)

---
### Q4

I first turn the ball related logic and variables to a Ball class.
``` js
class Ball {
             class Ball {
            constructor(x, y, dx, dy) {
                this.x = x;
                this.y = y;
                this.dx = dx
                this.dy = dy; 
                this.radius = 10; 
                this.color = '#ff0000';
                this.radius_increment_rate = 5;
                this.radius_decrement_rate = 5
              }

            drawBall() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2); 
                ctx.fillStyle = this.color;
                ctx.fill();
                ctx.closePath();
            }

            updatePosition() {
                this.x += this.dx;
                this.y += this.dy;
                
                if (this.x + this.radius > canvas.width || this.x - this.radius < 0) {
                    this.dx = -this.dx; 
                    this.color = this.getRandomColor(); 
                    this.radius -= this.radius_decrement_rate;
                }
                if (this.y + this.radius > canvas.height || this.y - this.radius < 0) {
                    this.dy = -this.dy;
                    
                    let dr = this.radius_increment_rate
                    this.radius += dr;
                    this.y += dr * this.dy
                    this.x += dr * this.dx
                }
            }

            getRandomColor() {
                // Function to generate a random color (optional for color change on bounce)
                const letters = '0123456789ABCDEF';
                let color = '#';
                for (let i = 0; i < 6; i++) {
                    color += letters[Math.floor(Math.random() * 16)];
                }
                return color;
            }

            update() {
                this.updatePosition();
                this.drawBall();
            }
        
        }
```

Notice that I added 
1. `update()` to update and render the ball. 
2. moved `ctx.clearRect(0, 0, canvas.width, canvas.height);` out because it would clear the buffer before rendering all balls.

I then create an array of 3 Balls
```js
const Balls = [
        new Ball(canvas.width/2, canvas.height/2, 2, 2),
        new Ball(canvas.width/2, canvas.height/2, 2, -2),
        new Ball(canvas.width/2, canvas.height/2, -2, 2),
    ]
```

In the main loop I clear the buffer and then update each of the Balls in the array.

```js
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); 
    Balls.forEach(ball => ball.update());
    requestAnimationFrame(animate); // Schedule next animation frame
}
```
---


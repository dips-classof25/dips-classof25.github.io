let bubbles = [];
let color, canvas;

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    createStars();
}

function createStars() {
    for(let i = 0; i < 70; i++){
        let x = random(width);
        let y = random(height);
        let r = random(2,15);
        let distance = random(25, 100);
        bubbles[i] = new Star(x, y, r, distance, 255);
    }
}

function setup() {
    canvas = createCanvas(windowWidth, windowHeight);
    canvas.position(0, 0);
    canvas.style('z-index', '1');

    frameRate(30);
    createStars();
}


function mouseMoved() {
    for(let i = 0; i < bubbles.length; i++) {
        bubbles[i].parallax(mouseX, mouseY);
    }
}

//function mousePressed() {
    //for(let i = 0; i < bubbles.length; i++){
        //bubbles[i].clicked(mouseX, mouseY);
    //}
//}

function draw() {
    background('#000055');

    for(let i = 0; i < bubbles.length; i++){
        bubbles[i].hovered(mouseX, mouseY);
        bubbles[i].show(mouseX, mouseY);
        bubbles[i].flicker();
    }
}

///

class Star {
    constructor(x, y, r, distance, fill) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.startr = r;
        this.fill = fill;
        this.firstX = x;
        this.firstY = y;
        this.distance = distance;
    }


    //clicked (x,y) {
        //let d = dist (x, y, this.x, this.y);
        //if(d < this.r){
            //this.r = this.r + 10;
        //}
    //}

    hovered (x,y) {
        let d = dist (x, y, this.x, this.y);
        if(d < this.r){
            rectMode(CENTER);
            ellipse(this.x, this.y, 20,20);
        }
    }

    flicker (){
        this.x = this.x + random(-0.1,0.1);
        this.y = this.y + random(-0.1,0.1);
        this.r = this.startr + random(-0.4,0.4);
    }

    parallax (x, y) {
        let
            halfWidth = width,
            halfHeight = height,
            isNegative = x - halfWidth > 0 ? -1 : 1,
            isNegativeY = y - halfHeight > 0 ? -1 : 1,

            mapDistance = Math.abs(x - halfWidth) / halfWidth * this.distance,
            mapDistanceY = Math.abs(y - halfHeight) / halfHeight * this.distance;

        this.x = this.firstX + mapDistance * isNegative;
        this.y = this.firstY + mapDistanceY * isNegativeY;
    }

    show (x, y) {
        noStroke();
        fill(this.fill);
        ellipse (this.x, this.y, this.r, this.r);

        let d = dist(mouseX, mouseY, this.x, this.y);
        if (d<150){
            stroke(255, 150);
            ellipse(x, y, 2, 2);
            line(mouseX,mouseY, this.x, this.y);
        }
    }
}

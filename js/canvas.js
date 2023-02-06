// "https://images.uesp.net/3/3c/MW-map-Vvardenfell.jpg"
// import {drawPath, gameToPixels} from "draw";

const image_dims = (2668, 3095)  // width, height
const game_dimensions = (-220000, 170000, -115000, 223000);  // (xmin, xmax, ymin, ymax)

function gameToPixels(coord) {
    x = coord[0];
    y = coord[1];
    xmin = game_dimensions[0];
    xmax = game_dimensions[1];
    ymin = game_dimensions[2];
    ymax = game_dimensions[3];
    x -= xmin;
    y -= ymin;
    x /= (xmax - xmin);
    y /= (ymax - ymin);
    // flip y, coordinates are backwards in game compared to a canvas tag.
    y = 1 - y;
    return ((Math.round(x*image_dims[0]), Math.round(y*image_dims[1])))
}

function drawPath(path, ctx) {
    ctx.beginPath();
    for (i = 0; i < path.length; i++) {
        // row = path[i][0];
        // col = path[i][1];
        pixels = gameToPixels(path[i]);
        row = pixels[0];
        col = pixels[1];
        console.log(row, col)
        if (i == 0) {
            ctx.moveTo(row, col);
        } else {
            ctx.lineTo(row, col);
        }
    }
    ctx.strokeStyle = "#fa34a3";
    ctx.stroke();
}


console.log("This is working");

canvas = document.querySelector("canvas");
canvas.width = 2668 
canvas.height = 3095
ctx = canvas.getContext("2d");

img = new Image;
img.src = "MW-map-Vvardenfell.jpg"

console.log(img.width)

img.onload = function() {
    ctx.drawImage(img, 0, 0);
    path = [(-19480, -17336), (147456, 38912), (147533, 39900), (148556, 39971), (148951, 40770), (149833, 40340), (150724, 40176), (151984, 38159), (152724, 38313), (153457, 38075), (163029, 33910)];
    // path = path.map(gameToPixels);
    drawPath(path, ctx);
}
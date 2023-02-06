// "https://images.uesp.net/3/3c/MW-map-Vvardenfell.jpg"

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
}


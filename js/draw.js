
const image_dims = (2668, 3095)  // width, height
const game_dimensions = (-220000, 170000, -115000, 223000);  // (xmin, xmax), (ymin, ymax)

function gameToPixels(coord) {
    x, y = coord;
    xmin, xmax, ymin, ymax = game_dimensions;
    x -= xmin;
    y -= ymin;
    x /= (xmax - xmin);
    y /= (ymax - ymin);
    // flip y, coordinates are backwards in game compared to a canvas tag.
    y = 1 - y;
    return (Math.round(x*image_dims[0]), Math.round(y*image_dims[1]))
}

function drawPath(path, ctx) {
    ctx.beginPath();
    for (i = 0; i < path.length; i++) {
        row, col = path[i]
        if (i == 0) {
            ctx.moveTo(row, col);
        } else {
            ctx.lineTo(row, col);
        }
    }
    ctx.strokeStyle = "#fa34a3";
    ctx.stroke();
}
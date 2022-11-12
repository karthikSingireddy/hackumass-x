function draw(ctx, canvas) {
  console.log('hamp')
  ctx.fill = "#FFFF00";
  ctx.fillRect(canvas.current.width/2, canvas.current.height/2, 5, 5);
}

export default {
  draw
}
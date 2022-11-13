function draw(ctx, canvas) {
  ctx.fillStyle = "#000000";
  let x = 90;
  ctx.fillRect(x,10,120,2);
  ctx.fillRect(x,10,2,120);
  ctx.fillRect(x,130,120,2);
  ctx.fillRect(120+x,10,2,122);
}

export default {
  draw
}
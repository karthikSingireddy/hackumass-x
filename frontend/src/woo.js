function draw(ctx, canvas) {
  ctx.fillStyle = "#000000";
  ctx.fillRect(20, 20, 250, 2);
  ctx.fillRect(270, 20, 2, 120);
  ctx.fillRect(130, 140, 142, 2);
  ctx.fillRect(130, 120, 2, 20);
  ctx.fillRect(20, 120, 110, 2);
  ctx.fillRect(20, 20, 2, 100);
}

export default {
  draw
}
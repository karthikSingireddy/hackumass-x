function draw(ctx, canvas) {
  console.log('hamp')
  ctx.fillStyle = "#FFFFFF";
  ctx.fillRect(60, 10, 180, 2);
  //ctx.fillRect(20, 20, 2, 100);
  //ctx.fillRect(130, 140, 142, 2);
  //ctx.fillRect(130, 120, 2, 20);
  //ctx.fillRect(20, 120, 110, 2);
  ctx.fillRect(60, 10, 2, 120);
  ctx.fillRect(240, 10, 2, 120);
  ctx.fillRect(60, 130, 30, 2);
  ctx.fillRect(212, 130, 30, 2);
  ctx.fillRect(90, 122, 2, 10);
  ctx.fillRect(212, 122, 2, 10);
  ctx.fillRect(90, 120, 124, 2);
}

export default {
  draw
}
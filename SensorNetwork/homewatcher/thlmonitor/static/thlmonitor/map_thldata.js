window.onload = function() {
    draw_ground_floor();
    draw_first_floor();
}
function draw_ground_floor() {
    const ground = document.getElementById("ground_floor");
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;
    gctx.strokeStyle = `rgba(127, 127, 127, 0.1)`;
    for (let i = 60; i <= W; i+=60) {
        gctx.moveTo(i, 0)
        gctx.lineTo(i, H);
        gctx.stroke();
    }
    for (let i = 80; i <= H; i+=80) {
        gctx.moveTo(0, i)
        gctx.lineTo(W, i);
        gctx.stroke();
    }
}

function draw_first_floor() {
    const ground = document.getElementById("first_floor");
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;
    gctx.strokeStyle = `rgba(127, 127, 127, 0.1)`;
    for (let i = 60; i <= W; i+=60) {
        gctx.moveTo(i, 0)
        gctx.lineTo(i, H);
        gctx.stroke();
    }
    for (let i = 80; i <= H; i+=80) {
        gctx.moveTo(0, i)
        gctx.lineTo(W, i);
        gctx.stroke();
    }
}
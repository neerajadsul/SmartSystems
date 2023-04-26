window.onload = function() {
    draw_ground_floor();
    draw_first_floor();
    draw_ground_floor_rooms();
    draw_first_floor_rooms();
}

const Xd = 60;
const Yd = 80;
function draw_ground_floor() {
    const ground = document.getElementById("ground_floor");
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;
    gctx.strokeStyle = `rgba(127, 127, 127, 0.1)`;
    gctx.setLineDash([5, 15]);
    for (let i = Xd; i <= W; i+=Xd) {
        gctx.moveTo(i, 0)
        gctx.lineTo(i, H);
        gctx.stroke();
    }
    for (let i = Yd; i <= H; i+=Yd) {
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
    gctx.setLineDash([5, 15]);
    for (let i = Xd; i <= W; i+=Xd) {
        gctx.moveTo(i, 0)
        gctx.lineTo(i, H);
        gctx.stroke();
    }
    for (let i = Yd; i <= H; i+=Yd) {
        gctx.moveTo(0, i)
        gctx.lineTo(W, i);
        gctx.stroke();
    }
}

function draw_ground_floor_rooms() {
    const ground = document.getElementById("ground_floor_rooms");
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;
      // Draw Kitchen Boundary
    gctx.strokeStyle = `rgb(10, 10, 10)`;
    gctx.moveTo(0, 3*Yd);
    gctx.lineTo(W, 3*Yd);
    gctx.stroke();
    gctx.moveTo(2*Xd, 3*Yd);
    gctx.lineTo(2*Xd, H);
    gctx.stroke();
    gctx.moveTo(1*Xd, 3*Yd);
    gctx.lineTo(1*Xd, H);
    gctx.stroke();
    gctx.moveTo(0, 4*Yd);
    gctx.lineTo(1*Xd, 4*Yd);
    gctx.stroke();
    gctx.moveTo(0, 5*Yd);
    gctx.lineTo(1*Xd, 5*Yd);
    gctx.stroke();
    gctx.moveTo(0, 2*Yd);
    gctx.lineTo(1*Xd, 2*Yd);
    gctx.stroke();
    gctx.moveTo(Xd, 2*Yd);
    gctx.lineTo(Xd, 3*Yd);
    gctx.stroke();
}

function draw_first_floor_rooms() {
    const ground = document.getElementById("first_floor_rooms");
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;
      // Draw Kitchen Boundary
    gctx.strokeStyle = `rgb(10, 10, 10)`;
    // Central separator line
    gctx.moveTo(3*Xd, 0);
    gctx.lineTo(3*Xd, H);
    gctx.stroke();
    // Main Bedroom
    gctx.moveTo(3*Xd, 3*Yd);
    gctx.lineTo(6*Xd, 3*Yd);
    gctx.stroke();
    // Storage and shower
    gctx.moveTo(4.25*Xd, 3*Yd);
    gctx.lineTo(4.25*Xd,4.25*Yd);
    gctx.stroke();
    gctx.moveTo(3*Xd, 4.25*Yd);
    gctx.lineTo(W, 4.25*Yd);
    gctx.stroke();
    // Neeraj Office
    gctx.moveTo(0, 5*Yd);
    gctx.lineTo(3*Xd, 5*Yd);
    gctx.stroke();
    // Family Bath
    gctx.moveTo(2*Xd, 2.25*Yd);
    gctx.lineTo(2*Xd, 5*Yd);
    gctx.stroke();
    gctx.moveTo(0, 2.25*Yd);
    gctx.lineTo(3*Xd, 2.25*Yd);
    gctx.stroke();
    gctx.moveTo(0, 4*Yd);
    gctx.lineTo(2*Xd, 4*Yd);
    gctx.stroke();
}
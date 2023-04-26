window.onload = function() {
    draw_ground_floor();
    draw_first_floor();
    draw_ground_floor_rooms();
    draw_first_floor_rooms();
}
function draw_ground_floor() {
    const ground = document.getElementById("ground_floor");
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;
    gctx.strokeStyle = `rgba(127, 127, 127, 0.1)`;
    gctx.setLineDash([5, 15]);
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
    gctx.setLineDash([5, 15]);
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

function draw_ground_floor_rooms() {
    const ground = document.getElementById("ground_floor_rooms");
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;
      // Draw Kitchen Boundary
    gctx.strokeStyle = `rgb(10, 10, 10)`;
    gctx.moveTo(0, 3*80);
    gctx.lineTo(W, 3*80);
    gctx.stroke();
    gctx.moveTo(2*60, 3*80);
    gctx.lineTo(2*60, H);
    gctx.stroke();
    gctx.moveTo(1*60, 3*80);
    gctx.lineTo(1*60, H);
    gctx.stroke();
    gctx.moveTo(0, 4*80);
    gctx.lineTo(1*60, 4*80);
    gctx.stroke();
    gctx.moveTo(0, 5*80);
    gctx.lineTo(1*60, 5*80);
    gctx.stroke();
    gctx.moveTo(0, 2*80);
    gctx.lineTo(1*60, 2*80);
    gctx.stroke();
    gctx.moveTo(60, 2*80);
    gctx.lineTo(60, 3*80);
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
    gctx.moveTo(3*60, 0);
    gctx.lineTo(3*60, H);
    gctx.stroke();
    // Main Bedroom
    gctx.moveTo(3*60, 3*80);
    gctx.lineTo(6*60, 3*80);
    gctx.stroke();
    // Storage and shower
    gctx.moveTo(4.25*60, 3*80);
    gctx.lineTo(4.25*60,4.25*80);
    gctx.stroke();
    gctx.moveTo(3*60, 4.25*80);
    gctx.lineTo(W, 4.25*80);
    gctx.stroke();
    // Neeraj Office
    gctx.moveTo(0, 5*80);
    gctx.lineTo(3*60, 5*80);
    gctx.stroke();
    // Family Bath
    gctx.moveTo(2*60, 2.25*80);
    gctx.lineTo(2*60, 5*80);
    gctx.stroke();
    gctx.moveTo(0, 2.25*80);
    gctx.lineTo(3*60, 2.25*80);
    gctx.stroke();
    gctx.moveTo(0, 4*80);
    gctx.lineTo(2*60, 4*80);
    gctx.stroke();
}
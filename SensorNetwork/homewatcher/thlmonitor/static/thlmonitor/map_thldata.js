window.onload = function() {
    draw_ground_floor();
    draw_first_floor();
    draw_ground_floor_rooms();
    draw_first_floor_rooms();

    const thl =JSON.parse(document.getElementById("thl-data").textContent);
    console.log(thl);
    thl.forEach(elm => {
        display_measurements(elm.loc, elm.row, elm.col, elm.T, elm.RH, elm.lux);
    });
    // show_grid_coordinates("ground");
    // show_grid_coordinates("first");

    const ground_floor = document.getElementById("ground_floor");

    ground_floor.addEventListener(
        "click", function ( ev) {
            let rect = ground_floor.getBoundingClientRect();
            let x = ev.clientX - rect.left
            let y = ev.clientY - rect.top;
            console.log(x, y);
        }

    );

    const first_floor = document.getElementById("first_floor");

    first_floor.addEventListener(
        "click", function ( ev) {
            let rect = first_floor.getBoundingClientRect();
            let x = ev.clientX - rect.left
            let y = ev.clientY - rect.top;
            console.log(x, y);
        }

    );

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

const col_dict = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7
};

const findKey = (obj, val) => {
   const res = {};
   Object.keys(obj).map(key => {
      res[obj[key]] = key;
   });
   // if the value is not present in the object
   // return false
   return res[val] || false;
};

function display_measurements(floor, row, col, T, RH , LUX) {
    if (floor==="ground") {
        floor = "ground_floor_rooms";
    } else if(floor==="first") {
        floor = "first_floor_rooms";
    }
    const ground = document.getElementById(floor);
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;

    gctx.font = "16px Arial";
    console.log(T.toString());
    // gctx.strokeText(T.toString(), row*Xd, col_dict[col]*Yd);
    gctx.strokeText("T:"+ T.toString(), col_dict[col]*Xd-Xd/2-20, row*Yd-Yd/2);
    gctx.strokeText("H:" + RH.toString(), col_dict[col]*Xd-Xd/2-20, row*Yd-Yd/2+16);
    gctx.strokeText("L:" + LUX.toString(), col_dict[col]*Xd-Xd/2-20, row*Yd-Yd/2+32);
    console.log(row, col_dict[col]);

}

function show_grid_coordinates(floor) {
    let MAX_COL = "E";
    let MAX_ROW = 6;
    if (floor==="ground") {
        floor = "ground_floor_rooms";
        MAX_COL = "E";
        MAX_ROW = 6;
    } else if(floor==="first") {
        floor = "first_floor_rooms";
        MAX_COL = "F";
        MAX_ROW = 7;
    }
    const ground = document.getElementById(floor);
    const gctx = ground.getContext("2d");
    const W = ground.width;
    const H = ground.height;

    gctx.font = "16px Arial";

    for (let i = 1; i <= MAX_ROW; i++) {
        for (let j = 1; j <= col_dict[MAX_COL]; j++) {
            var msg = i.toString() + findKey(col_dict, j);
            console.log(msg);
            gctx.strokeText(msg, j*Xd-Xd/2, i*Yd-Yd/2);
        }
    }
}



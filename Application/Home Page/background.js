const canvas = document.getElementById("stars");
const ctx =  canvas.getContext("2d");   
var screen;

var params = {speed : 10 , count : 350 ,life :5};
var starArr;

setup();
update();
window.onresize = function(){
    setup();
}

function Star(){
    this.x = Math.random()* canvas.width;
    this.y = Math.random()* canvas.height;
    this.z = Math.random()* canvas.width;
    
    this.move  = function(){
        this.z -= params.speed;
        if(this.z<=0){
            this.z = canvas.width;
        }
    }
    
    this.show = function(){
        let x,y,radius,opacity;
        radius = canvas.width/this.z;
        x = (this.x - screen.c[0]) * radius;
        x = x + screen.c[0]; 
        y = (this.y - screen.c[1]) * radius;
        y = y + screen.c[1];
        
        opacity =radius > params.life ? (2 - radius/params.life)*1.5 : 1;
        ctx.beginPath();
        ctx.fillStyle = "rgba(255,255,255,"+opacity+")";
        ctx.arc(x,y,radius,0,Math.PI*2);
        ctx.fill(); 
    }
}
function setup(){
    screen = {
        w : window.innerWidth-9.5,
        h : window.innerHeight,
        c : [window.outerWidth*0.5,window.outerHeight*0.5],
    }
    window.cancelAnimationFrame(update);
    canvas.width = screen.w;
    canvas.height = screen.h;

    starArr=[];
    for(var i=0;i<params.count;i++){
        starArr[i] = new Star();
    }
}

function update(){
    ctx.fillStyle = '#222e79';
    ctx.fillRect(0,0,canvas.width,canvas.height);
    starArr.forEach(function(s) {
        s.show();
        s.move();  
    });
    
    window.requestAnimationFrame(update);
}

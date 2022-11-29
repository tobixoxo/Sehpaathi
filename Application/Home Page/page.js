let options = {
    strings: ['Machine Learning', 'Deep Learning' ,'Natural Language Processing'],
    typeSpeed: 100,
    backSpeed: 80,
    loop : true,
}
let typed  = new Typed('.typing',options);


function lines(){
    let x = document.querySelector('.home');
    let i=0;    
    let count = 50;
    while(i<count){
        let shinning = document.createElement('i');
        shinning.id = 'lines';
        let w= Math.floor(Math.random()*window.innerWidth);
        let h = Math.floor(Math.random()*100);
        let duration = Math.random()*1;

        shinning.style.left= w + 'px';
        shinning.style.width = 1 + 'px';
        shinning.style.height= h + 'px';
        shinning.style.animationDuration = duration + 's';

        x.appendChild(shinning);
        i++;
    }
}

$(window).scroll( function(){

    if(this.scrollY > 20){

        $(".navbar").addClass("sticky");
    }
    else{

        $('.navbar').removeClass("sticky");
    }

    if(this.scrollY > 500){

        $('.scroll-up-btn').addClass('show');
    }
    else{
        $('.scroll-up-btn').removeClass('show');
    }
});

document.querySelector('.scroll-up-btn').addEventListener('click',function(){

    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
    
})
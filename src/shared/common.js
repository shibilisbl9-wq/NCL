/* Wraps every .sheet in a page. ?mode=print adds 3 mm bleed, 10 mm slug and crop marks. */
(function(){
  var q=new URLSearchParams(location.search), print=q.get('mode')==='print';
  var B=print?(+q.get('bleed')||3):0, SL=print?10:0;   // mm
  document.documentElement.style.setProperty('--b',B+'mm');
  document.documentElement.style.setProperty('--slug',SL+'mm');
  var sheets=[].slice.call(document.querySelectorAll('.sheet'));
  if(!sheets.length) return;
  var W=+sheets[0].dataset.w, H=+sheets[0].dataset.h;
  var PW=W+2*(B+SL), PH=H+2*(B+SL);
  var st=document.createElement('style');
  st.textContent='@page{size:'+PW+'mm '+PH+'mm;margin:0}html,body{margin:0}';
  document.head.appendChild(st);
  sheets.forEach(function(sh){
    var w=+sh.dataset.w, h=+sh.dataset.h;
    var page=document.createElement('div'); page.className='page';
    page.style.width=PW+'mm'; page.style.height=PH+'mm';
    var bb=document.createElement('div'); bb.className='bleedbox';
    bb.style.left=SL+'mm'; bb.style.top=SL+'mm'; bb.style.width=(w+2*B)+'mm'; bb.style.height=(h+2*B)+'mm';
    sh.parentNode.insertBefore(page,sh); page.appendChild(bb); bb.appendChild(sh);
    sh.style.left=B+'mm'; sh.style.top=B+'mm'; sh.style.width=w+'mm'; sh.style.height=h+'mm';
    if(print){
      var ns='http://www.w3.org/2000/svg', svg=document.createElementNS(ns,'svg');
      svg.setAttribute('class','marks'); svg.setAttribute('width',PW+'mm'); svg.setAttribute('height',PH+'mm');
      svg.setAttribute('viewBox','0 0 '+PW+' '+PH);
      var x0=SL+B, y0=SL+B, x1=x0+w, y1=y0+h, gap=B+1.5, len=5, d='';
      [[x0,y0,-1,-1],[x1,y0,1,-1],[x0,y1,-1,1],[x1,y1,1,1]].forEach(function(c){
        var x=c[0],y=c[1],sx=c[2],sy=c[3];
        d+='M'+(x+sx*gap)+' '+y+'L'+(x+sx*(gap+len))+' '+y+'M'+x+' '+(y+sy*gap)+'L'+x+' '+(y+sy*(gap+len));
      });
      var p=document.createElementNS(ns,'path'); p.setAttribute('d',d); p.setAttribute('stroke','#000'); p.setAttribute('stroke-width','0.12'); p.setAttribute('fill','none');
      svg.appendChild(p);
      var t=document.createElementNS(ns,'text'); t.setAttribute('x',x0); t.setAttribute('y',PH-3); t.setAttribute('font-size','2.2'); t.setAttribute('font-family','Montserrat'); t.setAttribute('fill','#000');
      t.textContent=(document.title||'')+'  |  trim '+w+' x '+h+' mm  |  bleed 3 mm';
      svg.appendChild(t);
      page.appendChild(svg);
    }
  });
})();

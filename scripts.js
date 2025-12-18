document.addEventListener('DOMContentLoaded', ()=>{
  // Scroll reveal semplice
  const revealEls = document.querySelectorAll('.reveal')
  const onScroll = ()=>{
    const h = window.innerHeight
    revealEls.forEach(el=>{
      const r = el.getBoundingClientRect()
      if(r.top < h - 80){ el.classList.add('visible') }
    })
  }
  onScroll()
  window.addEventListener('scroll', onScroll, {passive:true})

  // Micro-interaction: evidenzia card al click (accessibilità)
  document.querySelectorAll('.card').forEach(card=>{
    card.addEventListener('click', ()=>{card.animate([{transform:'translateY(-6px)'},{transform:'translateY(0)'}],{duration:300,easing:'cubic-bezier(.2,.9,.3,1)'} )})
  })
})

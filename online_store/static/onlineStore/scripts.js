document.addEventListener('DOMContentLoaded',function() {
    const logo= document.querySelectorAll('.logo h1')
    const article= document.querySelectorAll('.article p')
    const description= document.querySelector('.description')
    const title= document.querySelectorAll('.title')
    const image= document.querySelector('.article img')
    const h1= document.querySelector('.big h1')
    const more_infos= document.querySelector('.more_infos')

    // menu deroulant
    const links= document.querySelector('.links')
    const menu_list= document.querySelector('.menu_list') //  selection de "menu_list"
    menu_list.onclick = function(){    // on ajoute a menu_list un ajouteur d'un evenement ".onclick" ensuite on definie une fonction pour reagir dondc tout les scripts suivant n'agisse que si l'evenement se produit 
        menu_list.classList.toggle("active")  // ".classList.toggle("nom_selecteur_css") ajoute la classe  specifie comme argument si elle est presente sinon elle l'enleve"
        links.classList.toggle('responsive')
    }
    
    window.addEventListener('load',function() {
        const TL = gsap.timeline()   
        .staggerFrom(logo, 0.6, {x:-200,opacity:0,ease:"power2.out"},0.1)
        .from(article, 1.5, {x:100, opacity:0,ease:"power2.out"}, 0)
        .from(description, 1, {x:200, opacity:0,ease:"power2.out"}, 0)
        .from(title , 1, {x:-100, opacity:0, ease:"power2.out"}, 0)
        .from(image, 1 , {y:-300, opacity:0,ease:"bounce"}, 0 )
        .from(h1, 1.5 , {x:-300, opacity:0,ease:"power2.out"}, 0 )
        .from(more_infos, 1.5 , {x:-300, opacity:0,ease:"power2.out"}, 0 )
    })
})


document.addEventListener('DOMContentLoaded',function(){
    const btn= document.querySelector('.form_btn')
    const form= document.querySelector('.form')
    btn.onclick= function(){
        form.classList.toggle('active_form')
    }
})